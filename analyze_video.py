import cv2
import numpy as np
from scipy.fftpack import fft
from scipy.signal import find_peaks

def extrair_linha_fluido(video_path):
    cap = cv2.VideoCapture(video_path)
    y_positions = []
    frames = []
    timestamps = []

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        altura = frame.shape[0]
        largura = frame.shape[1]
        meio = largura // 2

        # Cortar uma linha vertical no centro
        linha_vertical = frame[:, meio-2:meio+2]

        # Converter para escala de cinza
        gray = cv2.cvtColor(linha_vertical, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        # Detectar borda superior (supõe-se que o líquido seja escuro)
        min_y = np.argmax(np.mean(blur, axis=1) < 100)  # pixel escuro = fluido

        y_positions.append(min_y)
        frames.append(frame)
        timestamps.append(frame_count / fps)

        frame_count += 1

    cap.release()
    return y_positions, frames, timestamps


def calcular_amplitude(y_positions, janela=10):
    """Mede variação local da linha do fluido"""
    amplitudes = []
    for i in range(len(y_positions)):
        ini = max(0, i - janela)
        fim = min(len(y_positions), i + janela)
        local = y_positions[ini:fim]
        amp = max(local) - min(local)
        amplitudes.append(amp)
    return amplitudes


def calcular_frequencia(y_positions, fps=30):
    """Usa FFT para encontrar frequência dominante"""
    n = len(y_positions)
    yf = fft(y_positions)
    freqs = np.fft.fftfreq(n, 1 / fps)

    idx = np.where(freqs > 0)
    magnitudes = np.abs(yf[idx])
    freqs_pos = freqs[idx]

    if len(magnitudes) == 0:
        return 0

    dominante = freqs_pos[np.argmax(magnitudes)]
    return dominante


def calcular_tempo_estabilizacao(y_positions, timestamps, limite=5):
    """Detecta quando a amplitude cai abaixo do limite"""
    amplitudes = calcular_amplitude(y_positions)
    for i in range(len(amplitudes)):
        janela = amplitudes[i:i + 10]
        if len(janela) == 10 and max(janela) < limite:
            return timestamps[i]
    return timestamps[-1]


def detectar_inclinacoes(frames):
    """Detecta inclinação da superfície do fluido usando HoughLines"""
    angulos = []
    for frame in frames:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150)
        lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=10)

        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line[0]
                angulo = np.degrees(np.arctan2((y2 - y1), (x2 - x1)))
                angulos.append(angulo)
                break  # pega só a primeira linha por frame
        else:
            angulos.append(0)

    return angulos

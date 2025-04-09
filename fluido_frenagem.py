import cv2
import numpy as np

# Configurações
width, height = 640, 480
duration_sec = 10
fps = 30
total_frames = duration_sec * fps

# Criar vídeo
video_path = "fluid_simulation_inclinacao.mp4"
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(video_path, fourcc, fps, (width, height))

# Parâmetros da onda
amplitude_inicial = 40
frequencia = 2  # Hz
frenagem_apos = 5  # segundos

# Inclinação máxima da linha (em pixels de diferença entre as extremidades)
inclinacao_max_px = 100  # aproximadamente uns 10-15 graus

for i in range(total_frames):
    t = i / fps
    frame = np.ones((height, width, 3), dtype=np.uint8) * 255

    if t < frenagem_apos:
        amplitude = amplitude_inicial
        inclinacao = inclinacao_max_px * np.sin(np.pi * t / frenagem_apos)  # vai até o pico e volta
    else:
        decaimento = np.exp(-1.5 * (t - frenagem_apos))
        amplitude = amplitude_inicial * decaimento
        inclinacao = inclinacao_max_px * decaimento  # inclinação decai com o movimento

    y_center = int(height // 2 + amplitude * np.sin(2 * np.pi * frequencia * t))
    
    # Calcular início e fim da linha com inclinação
    x1, x2 = 0, width
    y1 = int(y_center - inclinacao / 2)
    y2 = int(y_center + inclinacao / 2)

    cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
    out.write(frame)

out.release()
print(f"✅ Vídeo com inclinação gerado em: {video_path}")

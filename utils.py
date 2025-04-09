import numpy as np
import pandas as pd
from scipy.ndimage import uniform_filter1d


def suavizar_dados(dados, tamanho_janela=5):
    """Aplica média móvel para suavizar oscilações"""
    return uniform_filter1d(dados, size=tamanho_janela)


def exportar_csv(timestamps, y_positions, amplitudes, angulos):
    """Prepara os dados analisados para exportação em CSV"""
    df = pd.DataFrame({
        "tempo_s": timestamps,
        "posicao_y": y_positions,
        "amplitude": amplitudes,
        "angulo": angulos
    })
    return df


def normalizar_lista(valores):
    """Normaliza os valores entre 0 e 1"""
    min_val = np.min(valores)
    max_val = np.max(valores)
    return [(v - min_val) / (max_val - min_val) for v in valores]

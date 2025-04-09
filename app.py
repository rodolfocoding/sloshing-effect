import streamlit as st
import matplotlib.pyplot as plt
import tempfile


from analyze_video import (
    extrair_linha_fluido,
    calcular_amplitude,
    calcular_frequencia,
    calcular_tempo_estabilizacao,
    detectar_inclinacoes
)

from utils import suavizar_dados, exportar_csv


st.set_page_config(page_title="Análise de fluido em movimento", layout="wide")
st.title("🚗💧 Análise dinâmica de fluido em recipiente em movimento")

st.markdown(
    """
    Este app analisa o comportamento de um fluido (ex: água em uma garrafa) com base em um vídeo.
    
    Suba um vídeo filmando o recipiente durante o movimento e veja:
    - Amplitude das oscilações do nível do líquido
    - Frequência das ondas
    - Tempo de estabilização após frenagem
    - Inclinação da superfície (indicando força G)

    ---
    """
)

uploaded_file = st.file_uploader("📹 Envie um vídeo .mp4", type=["mp4"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_video_path = tmp_file.name

    with st.spinner("🔍 Processando vídeo..."):
        y_positions, frames, timestamps = extrair_linha_fluido(tmp_video_path)
        amplitudes = calcular_amplitude(y_positions)
        frequencia = calcular_frequencia(y_positions)
        tempo_estabilizacao = calcular_tempo_estabilizacao(y_positions, timestamps)
        angulos = detectar_inclinacoes(frames)
        # Suavização
        y_positions_suav = suavizar_dados(y_positions)
        amplitudes_suav = suavizar_dados(amplitudes)
        angulos_suav = suavizar_dados(angulos)

    # Resultados numéricos
    st.subheader("📊 Resultados:")
    col1, col2, col3 = st.columns(3)
    col1.metric("Frequência das ondas", f"{frequencia:.2f} Hz")
    col2.metric("Tempo para estabilizar", f"{tempo_estabilizacao:.2f} s")
    col3.metric("Inclinação média", f"{sum(angulos_suav)/len(angulos_suav):.2f}°")

    # Gráficos
    st.subheader("📈 Gráficos")

    fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

    axs[0].plot(timestamps, y_positions_suav, color='blue')
    axs[0].set_ylabel("Nível do fluido (Y)")
    axs[0].set_title("Oscilação do fluido")

    axs[1].plot(timestamps, amplitudes_suav, color='orange')
    axs[1].set_ylabel("Amplitude")
    axs[1].set_title("Amplitude das oscilações")

    axs[2].plot(timestamps, angulos_suav, color='green')
    axs[2].set_ylabel("Inclinação (°)")
    axs[2].set_xlabel("Tempo (s)")
    axs[2].set_title("Inclinação da superfície (força G)")

    st.pyplot(fig)

    # Exportação
    st.subheader("📤 Exportar resultados")
    df = exportar_csv(timestamps, y_positions_suav, amplitudes_suav, angulos_suav)
    csv = df.to_csv(index=False)
    st.download_button(
        label="💾 Baixar CSV",
        data=csv,
        file_name="analise_fluido.csv",
        mime="text/csv",
    )

    st.info("🚀 Análise concluída!")

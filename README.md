# 🚗💧 Análise de sloshing (movimento de fluidos)

Este projeto analisa o comportamento de fluidos em movimento dentro de recipientes, um fenômeno conhecido como **efeito sloshing**. É especialmente útil para estudar como líquidos se comportam em veículos em movimento, como água em uma garrafa durante uma frenagem.

![Exemplo de Sloshing](https://i.imgur.com/7McgsdF.gif)

## 📋 O que este aplicativo faz?

O aplicativo permite:

- Analisar vídeos de fluidos em movimento
- Medir a **amplitude das ondas** formadas no líquido
- Calcular a **frequência das oscilações**
- Determinar o **tempo de estabilização** após uma perturbação
- Medir a **inclinação da superfície** do líquido (relacionada à força G)
- Exportar os resultados para análise posterior

## 🚀 Como usar

### Requisitos

Antes de começar, você precisa ter o Python instalado no seu computador. Em seguida, instale as dependências:

```bash
pip install -r requirements.txt
```

### Executando o aplicativo

1. Abra um terminal na pasta do projeto
2. Execute o comando:

```bash
streamlit run app.py
```

3. O aplicativo abrirá automaticamente no seu navegador

### Passo a passo para análise

1. **Prepare seu vídeo**: Grave um vídeo de um recipiente com líquido durante um movimento (como uma frenagem)
2. **Faça upload do vídeo**: Clique no botão de upload e selecione seu arquivo MP4
3. **Aguarde o processamento**: O sistema analisará automaticamente o vídeo
4. **Veja os resultados**: Serão exibidos os valores numéricos e gráficos
5. **Exporte os dados**: Clique em "Baixar CSV" para salvar os resultados no seu computador

## 📊 Entendendo os resultados

### Métricas principais

- **Frequência das Ondas (Hz)**: Quantas oscilações o fluido faz por segundo
- **Tempo para Estabilizar (s)**: Quanto tempo leva para o fluido parar de oscilar significativamente
- **Inclinação média (°)**: Ângulo médio da superfície do líquido durante o movimento

### Gráficos

O aplicativo gera três gráficos:

1. **Oscilação do Fluido**: Mostra a posição do nível do fluido ao longo do tempo
2. **Amplitude das Oscilações**: Indica a intensidade das ondas em cada momento
3. **Inclinação da Superfície**: Representa a inclinação do fluido (relacionada à força G)

## 💾 Exportação de dados

Os dados podem ser exportados em formato CSV para análise em outros programas como Excel ou Python. Basta clicar no botão "Baixar CSV" e escolher onde salvar o arquivo no seu computador.

O arquivo CSV contém as seguintes colunas:

- `tempo_s`: Tempo em segundos
- `posicao_y`: Posição vertical do nível do fluido
- `amplitude`: Amplitude das oscilações
- `angulo`: Inclinação da superfície do fluido

## 🔧 Informações técnicas

Este projeto utiliza:

- **OpenCV**: Para processamento de vídeo e detecção de bordas
- **Streamlit**: Para a interface gráfica interativa
- **Numpy/Scipy**: Para cálculos e processamento de sinais
- **Matplotlib**: Para geração de gráficos
- **Pandas**: Para manipulação de dados

## ❓ Solução de problemas

- **O vídeo não é reconhecido**: Certifique-se de que está no formato MP4
- **A detecção do fluido não funciona**: Tente gravar com melhor iluminação e contraste entre o fluido e o fundo
- **Resultados imprecisos**: A qualidade da análise depende da clareza do vídeo e do contraste entre o fluido e o recipiente

## 📝 Notas adicionais

- Para melhores resultados, grave o vídeo com boa iluminação
- Mantenha a câmera estável durante a gravação
- Use um recipiente transparente para melhor visualização do fluido
- O contraste entre o fluido e o fundo é importante para a detecção

## 🎬 Gerando vídeos de simulação

O projeto inclui um script para gerar vídeos de simulação do efeito sloshing. Isso é útil para testes ou quando você não tem um vídeo real disponível.

### Como gerar um vídeo de simulação:

1. Abra um terminal na pasta do projeto
2. Execute o comando:

```bash
python fluido_frenagem.py
```

3. O script irá gerar um arquivo de vídeo chamado `fluid_simulation_inclinacao.mp4` na pasta do projeto

### Personalizando a simulação:

Você pode editar o arquivo `fluido_frenagem.py` para ajustar os parâmetros da simulação:

- `duration_sec`: Duração do vídeo em segundos
- `fps`: Quadros por segundo
- `amplitude_inicial`: Tamanho inicial das ondas
- `frequencia`: Frequência das oscilações em Hz
- `frenagem_apos`: Momento (em segundos) em que ocorre a frenagem
- `inclinacao_max_px`: Inclinação máxima da superfície do fluido

Após modificar os parâmetros, execute novamente o script para gerar um novo vídeo com as configurações personalizadas.

---

Desenvolvido para análise de dinâmica de fluidos em movimento.

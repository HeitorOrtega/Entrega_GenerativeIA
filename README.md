# 🏍️ Projeto de Detecção de Motos com Visão Computacional

## Resumo do Projeto

Este projeto implementa um protótipo funcional de detecção e rastreamento de motos em tempo real usando técnicas de visão computacional. O objetivo é demonstrar a capacidade de identificar e contar veículos, simulando uma solução de monitoramento para o desafio proposto.

A solução utiliza um modelo de aprendizado profundo (YOLOv5) para analisar um fluxo de vídeo, exibir as detecções visualmente e persistir os dados quantitativos para análise futura.

## Tecnologias Utilizadas

* **Python**: Linguagem de programação principal.
* **Google Colab**: Ambiente de desenvolvimento.
* **YOLOv5**: Algoritmo de Visão Computacional para detecção de objetos.
* **PyTorch**: Framework de machine learning usado pelo YOLO.
* **OpenCV**: Biblioteca para processamento e análise de vídeo.
* **Pandas**: Para tratamento e persistência dos dados em formato `.csv`.

## Instruções de Uso

Para rodar o projeto, siga os passos abaixo no Google Colab:

1. **Carregar o Vídeo**: Suba o seu arquivo `video_sprint3.mp4` para a raiz do Colab.

   * Certifique-se de que o caminho esteja correto:

     ```python
     video_file = "/video_sprint3.mp4"
     ```
2. **Instalar Bibliotecas**: Execute a célula para instalar as bibliotecas necessárias (`torch`, `ultralytics`, `opencv-python`, `pandas`).
3. **Executar o Script**: Rode a célula com o script principal.
   O processamento ocorrerá entre `start_time_sec = 6` e `end_time_sec = 9`.
   Ao final, será gerado um arquivo CSV com os logs:

   ```python
   csv_file = "/content/historico_deteccoes.csv"
   ```

## Resultados

O projeto gera dois resultados principais:

1. **Output Visual em Tempo Real**: O script exibe o vídeo com as motos detectadas, destacadas por caixas delimitadoras e pontuações de confiança.
2. **Persistência de Dados**: O arquivo `historico_deteccoes.csv` é gerado em `/content/`, contendo um log de detecções com `timestamp`, `num_motos_detectadas` e `confianca_media`.

---

Heitor Ortega Silva – RM 557825

Marcos Lourenço – RM 556496

Pedro Saraiva – RM 555160

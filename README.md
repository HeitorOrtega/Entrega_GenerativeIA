# 🏍️ Projeto Mottu – Detecção e Monitoramento de Motos com Visão Computacional

# Link Video: https://youtu.be/5Ap9HddAV2o

## 📘 Resumo do Projeto

Este projeto implementa uma solução funcional de **monitoramento de frotas** para o desafio da **Mottu**, integrando **Visão Computacional (Python/YOLO)** e **Dashboard Interativo (Flask + React)**.  
O sistema realiza a **detecção de motos em vídeo**, armazena os resultados em um arquivo `.csv`, e exibe visualmente a **distribuição e o status das motos** em um **grid visual no dashboard**.

---

## 🧠 Objetivo

A proposta tem como foco demonstrar um fluxo **ponta a ponta** de monitoramento inteligente:

1. **Captura e processamento de dados** via Visão Computacional.  
2. **Persistência de informações** (quantidade de motos e confiança da detecção).  
3. **Visualização final** no dashboard da Mottu, simulando o pátio com status individuais de cada moto.

---

## 🧰 Tecnologias Utilizadas

| Camada | Tecnologia | Função |
|--------|-------------|--------|
| 💻 Backend | **Python (Flask)** | Fornece uma API que lê e retorna os dados do CSV |
| 📹 Processamento | **YOLOv5 + OpenCV + PyTorch** | Detecta motos em vídeo e gera logs de detecção |
| 📊 Análise | **Pandas + Numpy** | Tratamento e consolidação das detecções |
| 📈 Visualização | **Matplotlib (Google Colab)** | Gera o grid visual do pátio |
| 🌐 Dashboard | **React (Front-end)** | Exibe o resumo de motos e o gráfico de evolução |
| ☁️ Ambiente | **Google Colab + VS Code** | Ambientes de execução dos componentes |

---

## 🚀 Estrutura do Projeto

📦 Projeto-Mottu

┣ 📂 backend/

┃ ┗ 📜 app.py # API Flask

┣ 📂 dados/
┃ ┗ 📜 historico_deteccoes.csv # Logs de detecção gerados pelo Colab

┣ 📂 dashboard/

┃ ┗ 📜 DashboardMottu.jsx # Dashboard React (visualização)

┣ 📜 README.md

┗ 📜 grid_visual_colab.ipynb # Script Colab para visualização do pátio

---

## ⚙️ Instruções de Execução

### 🧩 1. Etapa de Visão Computacional (no Google Colab)

1. Abra o arquivo **`grid_visual_colab.ipynb`** no Google Colab.  
2. Faça o upload do vídeo `video_sprint3.mp4` e execute o script de detecção YOLOv5.  
3. Aguarde o processamento (entre 6 e 9 segundos de vídeo).  
4. Um arquivo CSV será gerado automaticamente:

   ```bash
   /content/historico_deteccoes.csv
   ```
#### O notebook exibirá automaticamente o grid visual do pátio, com cores representando o status das motos:

🟩 Em uso

🟨 Parada

🟥 Em manutenção

⬜ Vazia

#### O último registro do CSV também mostrará:

📅 Timestamp da última detecção

🏍️ Quantidade de motos detectadas

🎯 Confiança média da detecção

---

## 🖥️ 2. Etapa de Backend (no VS Code)

- Navegue até a pasta backend

Certifique-se de ter o Flask instalado:
   
pip install flask pandas


Execute a API:
```bash
uvicorn app:app --reload
```

O servidor será iniciado em:
```bash
http://127.0.0.1:5000
```

Para verificar os dados processados, acesse:
```
http://127.0.0.1:8000/api/mottu/status
```

🔹 Essa rota lê o arquivo historico_deteccoes.csv e retorna as informações em formato JSON para o front-end.


## 🗺️ Demonstração Visual do Pátio

O grid visual mostra o estado das motos em um pátio simulado de 30 vagas.

Cada célula representa uma vaga:

🟩 Em uso → Moto circulando ou em deslocamento

🟨 Parada → Moto estacionada e disponível

🟥 Manutenção → Moto em reparo ou revisão

⬜ Vazia → Vaga livre

O título do gráfico mostra o horário da última detecção, total de motos detectadas e a confiança média do modelo.

## 🧑‍💻 Desenvolvedores

Heitor Ortega Silva	557825	
Marcos Lourenço	556496	
Pedro Saraiva	555160	



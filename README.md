# Conversor RGB para HSV

Este projeto é uma aplicação web interativa construída com Python e Streamlit, desenvolvida como atividade para a disciplina de Computação Gráfica. O objetivo principal é realizar a conversão manual de uma imagem do espaço de cores RGB (lido nativamente como BGR pelo OpenCV) para HSV.

## 🚀 Funcionalidades

* **Upload de Imagens:** Interface simples para o envio de imagens (JPG, PNG) usando o File Uploader do Streamlit.
* **Conversão Matemática Otimizada:** Implementação manual do cálculo de Matiz (Hue), Saturação (Saturation) e Valor (Value) através de máscaras booleanas no NumPy.
* **Visualização:** Renderização instantânea da matriz HSV processada diretamente na tela.

## 🛠️ Tecnologias Utilizadas

* **Python**
* **Streamlit** (Interface Gráfica Web)
* **OpenCV** (Leitura de bytes, redimensionamento e exibição)
* **NumPy** (Processamento rápido de arrays e cálculo das matrizes H, S e V)

## ⚙️ Como executar o projeto

1. **Abra o terminal na pasta do projeto.**
2. **Ative o seu ambiente virtual:**
   * No Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   * No Linux/Mac:
     ```bash
     source venv/bin/activate
     ```
3. **Instale as dependências (caso ainda não tenha feito):**
   ```bash
   pip install streamlit opencv-python numpy
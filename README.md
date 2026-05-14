# Conversor e Editor RGB para HSV

Este projeto é uma aplicação desktop de Computação Gráfica desenvolvida em Python. O software permite carregar uma imagem no formato RGB, realizar a conversão para o espaço de cores HSV utilizando processamento matricial, exibi-la via renderização por texturas em OpenGL e manipular os canais Matiz, Saturação e Valor de forma interativa.

## Funcionalidades

* **Processamento Vetorizado:** Conversão de cores RGB para HSV através de operações matriciais com a biblioteca `NumPy`.
* **Renderização em OpenGL:** Mapeamento de texturas 2D sobre polígonos (`GL_QUADS`) com configuração de projeção ortogonal.
* **Manipulação em Tempo Real:** Controles interativos desenvolvidos com `PyQt5` para aplicação de transformações (offsets) nos canais H, S e V da imagem.

## Estrutura do Projeto

O código está modularizado para separar as responsabilidades lógicas e visuais:

* `main.py`: Ponto de entrada da aplicação. Inicializa o loop de eventos `QApplication` do PyQt5 e executa a janela principal.
* `janela.py`: Contém a interface gráfica principal (`QMainWindow`). Gerencia os componentes visuais (botões, sliders), a leitura de arquivos de imagem via `OpenCV`, o algoritmo de conversão RGB para HSV e o recálculo dos parâmetros da imagem baseados nas entradas do usuário.
* `tela.py`: Responsável pela renderização gráfica. Define a classe `TelaOpenGL` (herdada de `QOpenGLWidget`), que gerencia o contexto OpenGL, a definição da projeção 2D (`glOrtho`) e o carregamento e mapeamento das texturas na placa de vídeo.

## Tecnologias e Dependências

Para a execução do projeto, instale as seguintes dependências no seu ambiente virtual (`venv`):

```bash
pip install PyQt5 PyOpenGL opencv-python numpy
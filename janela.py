import cv2
import numpy as np
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import (
    QMainWindow,
    QPushButton,
    QFileDialog,
    QTextEdit,
    QLabel,
    QSlider
)

from tela import TelaOpenGL


class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo = 100
        self.esquerda = 100
        self.largura = 900   
        self.altura = 700
        self.titulo = "Conversor RGB -> HSV"

        self.img_original = None
        self.hsv_base = None 
        
        # lado esquerdo
        self.telaEsq = TelaOpenGL(self)
        self.telaEsq.setGeometry(40, 40, 400, 400)

        # botão upload
        botaoUpload = QPushButton('Carregar Imagem', self)
        botaoUpload.move(40, 460) 
        botaoUpload.resize(180, 50)
        botaoUpload.setStyleSheet('QPushButton {background-color: #58585c; font: bold; font-size: 14px}')
        botaoUpload.clicked.connect(self.FazerUpload)

        # botão converter
        botaoConversao = QPushButton('Converter pra HSV', self)
        botaoConversao.move(260, 460) # Ao lado do upload
        botaoConversao.resize(180, 50)
        botaoConversao.setStyleSheet('QPushButton {background-color: #58585c; font: bold; font-size: 14px}')
        botaoConversao.clicked.connect(self.Converter)

        # Explicação dos parâmetros
        self.caixa_texto = QTextEdit(self)
        self.caixa_texto.setGeometry(40, 530, 400, 130)
        self.caixa_texto.setReadOnly(True) 
        self.caixa_texto.setText(
            "Sobre o Algoritmo (Parâmetros 0, 2 e 4):\n\n"
            "O espaço HSV é um círculo de 360°. O cálculo do Matiz (Hue) divide esse círculo "
            "com base na cor predominante do pixel (R, G ou B). Os parâmetros são offsets "
            "multiplicados por 60°:\n"
            "- 0: Offset para Vermelho dominante (inicia em 0°).\n"
            "- 2: Offset para Verde dominante (inicia em 120°, pois 2x60=120).\n"
            "- 4: Offset para Azul dominante (inicia em 240°, pois 4x60=240)."
        )

       # lado direito
        self.telaDir = TelaOpenGL(self)
        self.telaDir.setGeometry(460, 40, 400, 400)

        # Slider Matiz (H)
        self.label_h = QLabel("Matiz (Hue):", self)
        self.label_h.move(460, 460)
        self.slider_h = QSlider(Qt.Horizontal, self)
        self.slider_h.setGeometry(460, 480, 400, 20)
        self.slider_h.setRange(-180, 180) 
        self.slider_h.setValue(0) 
        self.slider_h.valueChanged.connect(self.AplicarManipulacao)
        
        # Slider Saturação (S)
        self.label_s = QLabel("Saturação (Saturation):", self)
        self.label_s.move(460, 520)
        self.slider_s = QSlider(Qt.Horizontal, self)
        self.slider_s.setGeometry(460, 540, 400, 20)
        self.slider_s.setRange(-255, 255)
        self.slider_s.setValue(0)
        self.slider_s.valueChanged.connect(self.AplicarManipulacao)
        
        # Slider Valor/Brilho (V)
        self.label_v = QLabel("Valor (Value / Brilho):", self)
        self.label_v.move(460, 580)
        self.slider_v = QSlider(Qt.Horizontal, self)
        self.slider_v.setGeometry(460, 600, 400, 20)
        self.slider_v.setRange(-255, 255) 
        self.slider_v.setValue(0)
        self.slider_v.valueChanged.connect(self.AplicarManipulacao)

        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(
            self.esquerda,
            self.topo,
            self.largura,
            self.altura
        )

        self.setWindowTitle(self.titulo)
        self.show()
        
    def AplicarManipulacao(self):
        if self.hsv_base is None:
            return

        h_val = self.slider_h.value()
        s_val = self.slider_s.value()
        v_val = self.slider_v.value()

        H, S, V = cv2.split(self.hsv_base)

        H_novo = np.int16(H) + (h_val // 2)
        H_novo = np.mod(H_novo, 180).astype(np.uint8)

        S_novo = np.clip(np.int16(S) + s_val, 0, 255).astype(np.uint8)
        V_novo = np.clip(np.int16(V) + v_val, 0, 255).astype(np.uint8)

        img_hsv_modificada = cv2.merge([H_novo, S_novo, V_novo])
        
        self.telaDir.receberImagem(img_hsv_modificada)

    def FazerUpload(self):
        caminho_arquivo, _ = QFileDialog.getOpenFileName(
            self,
            "Escolha sua imagem",
            "",
            "Imagens (*.png *.jpg *.jpeg)"
        )

        if caminho_arquivo:
            img = cv2.imread(caminho_arquivo)

            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            img = cv2.resize(img, (400, 400))

            self.img_original = img

            self.telaEsq.receberImagem(self.img_original)

    def Converter(self):
        normalizada = self.img_original / 255.0

        B = normalizada[:, :, 0] # azul
        G = normalizada[:, :, 1] # verde
        R = normalizada[:, :, 2] # vermelho
        
        # econtrar max e min
        Cmax = np.max(normalizada, axis=2) 
        Cmin = np.min(normalizada, axis=2) 
        Delta = Cmax - Cmin
        
        # o V
        V = Cmax
        
        # encontrar S
        S = np.where(Cmax == 0, 0, Delta / Cmax)
        
        # encontrar Hue
        linhas, colunas = Cmax.shape
        H = np.zeros((linhas, colunas))
        
        mascara_R = (Cmax == R) & (Delta != 0)
        mascara_G = (Cmax == G) & (Delta != 0)
        mascara_B = (Cmax == B) & (Delta != 0)

        H[mascara_R] = 60 * (((G[mascara_R] - B[mascara_R]) / Delta[mascara_R]) + 0)
        H[mascara_G] = 60 * (((B[mascara_G] - R[mascara_G]) / Delta[mascara_G]) + 2)
        H[mascara_B] = 60 * (((R[mascara_B] - G[mascara_B]) / Delta[mascara_B]) + 4)
        H[H < 0] += 360
        
        # Junta as 3 matrizes de volta em uma imagem 3D final
        V *= 255
        S *= 255
        H /= 2
        img_hsv = np.dstack((H, S, V))

        img_hsv = img_hsv.astype(np.uint8)
        
        self.hsv_base = img_hsv.copy()
        
        self.slider_h.setValue(0)
        self.slider_s.setValue(0)
        self.slider_v.setValue(0)

        self.AplicarManipulacao()

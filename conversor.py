import cv2
import numpy as np
import streamlit as st

st.title("RGB 2 HSV")

imagem = st.file_uploader("Insira a imagem que você quer converter")

click = st.button("Converter para HSV")

if click:
    # converte a imagem pra bits
    file_bytes = np.asarray(bytearray(imagem.read()), dtype=np.uint8)
    # lê a imagem
    img = cv2.imdecode(file_bytes, 1)

    new_width = 640
    new_height = 480
    new_size = (new_width, new_height)

    # redimensiona a imagem pra melhor processamento
    resize = cv2.resize(img, new_size)

    # converte a imagem pra csv
    normalizada = resize / 255.0

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

    # Converte o tipo de dado de volta para inteiros de 8 bits
    img_hsv = img_hsv.astype(np.uint8)

    st.image(img_hsv, caption="Monke",)

    
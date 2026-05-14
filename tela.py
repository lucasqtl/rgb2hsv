from PyQt5.QtWidgets import QOpenGLWidget
from OpenGL.GL import *

class TelaOpenGL(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.imagem = None

    def receberImagem(self, matriz_imagem):
        self.imagem = matriz_imagem
        self.update()

    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_TEXTURE_2D)

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        glOrtho(0, w, h, 0, -1, 1)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT)

        if self.imagem is not None:
            altura, largura, _ = self.imagem.shape

            img_bytes = self.imagem.tobytes()

            textura_id = glGenTextures(1)
            glBindTexture(GL_TEXTURE_2D, textura_id)

            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

            glTexImage2D(
                GL_TEXTURE_2D,
                0,
                GL_RGB,
                largura,
                altura,
                0,
                GL_RGB,
                GL_UNSIGNED_BYTE,
                img_bytes
            )

            glBegin(GL_QUADS)

            glTexCoord2f(0.0, 0.0)
            glVertex2f(0.0, 0.0)

            glTexCoord2f(1.0, 0.0)
            glVertex2f(largura, 0.0)

            glTexCoord2f(1.0, 1.0)
            glVertex2f(largura, altura)

            glTexCoord2f(0.0, 1.0)
            glVertex2f(0.0, altura)

            glEnd()
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from tkinter import filedialog 
import tkinter as tk

def main():
    pygame.init()
    display = (1000, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, display[0], 0, display[1])
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Loop principal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Desenhar/Limpar a tela
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Botão de upload
        glColor3f(1.0, 1.0, 1.0) 

        glBegin(GL_QUADS)
        glVertex2f(50.0, 30.0)
        glVertex2f(200.0, 30.0)
        glVertex2f(200.0, 80.0)
        glVertex2f(50.0, 80.0)
        glEnd()

        # Botão de Conversão
        glColor3f(1.0, 1.0, 1.0) 

        glBegin(GL_QUADS)
        glVertex2f(250.0, 30.0)
        glVertex2f(400.0, 30.0)
        glVertex2f(400.0, 80.0)
        glVertex2f(250.0, 80.0)
        glEnd()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()

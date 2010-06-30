# -*- coding: UTF-8 -*-
# Autor: Hugo Henriques Maia Vieira

from   sys import argv
from   OpenGL.GL import *
from   OpenGL.GLU import *
from   OpenGL.GLUT import *

from faces import Faces

ARQUIVO = "h.txt"

class Interface:

    def __init__(self):
        self.faces = Faces()
        self.faces.ler_dados(open(ARQUIVO))
        self.zoom = 80
        self.aspecto = 0
        self.angulo = 0

    def init(self):
        glClearColor(1, 1, 1, 1)

    # Função usada para especificar o volume de visualização
    def EspecificaParametrosVisualizacao(self):

    	glMatrixMode(GL_PROJECTION)
    	glLoadIdentity()

    	gluPerspective(self.zoom,self.aspecto,0.5,500)

    	glMatrixMode(GL_MODELVIEW)
    	glLoadIdentity()

    	gluLookAt(0,0,50,
    	          0,0,0,
    	          0,1,0)

    def gerencia_mouse(self, button, state, x, y):
        if (button == GLUT_LEFT_BUTTON):
        	if (state == GLUT_DOWN): # Zoom-in
        		if (self.zoom >= 10): self.zoom -= 5

        if (button == GLUT_RIGHT_BUTTON):
        	if (state == GLUT_DOWN): # Zoom-out
        		if (self.zoom <= 130): self.zoom += 5

        self.EspecificaParametrosVisualizacao()
        glutPostRedisplay()

    def gerencia_teclado(self, tecla, x, y):
        if tecla == GLUT_KEY_LEFT: # direita
    		self.angulo += 2
        if tecla == GLUT_KEY_RIGHT: # esquerda
    		self.angulo -= 2


        self.EspecificaParametrosVisualizacao()
        glutPostRedisplay()

    def display(self):
    	glClear(GL_COLOR_BUFFER_BIT)
    	glColor3f(0.0, 0.0, 1.0)

        glRotatef(self.angulo, 0, 1, 0);
        self.faces.desenha()

    	glutSwapBuffers()

    def reshape(self, largura, altura):
        if ( altura == 0 ): altura = 1
    	# Especifica o tamanho da viewport
        glViewport(0 , 0, largura, altura)
    	# Calcula a correção de aspecto
        self.aspecto = largura/altura

    	self.EspecificaParametrosVisualizacao()

    def main(self):
        glutInit(argv)

        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    	glutInitWindowSize(600,600)
    	glutCreateWindow("Faces 3D")
        glutDisplayFunc(self.display)
        glutReshapeFunc(self.reshape)
        glutSpecialFunc(self.gerencia_teclado)
    	glutMouseFunc(self.gerencia_mouse)
        self.init()
        glutMainLoop()

if __name__ == "__main__":
    interface = Interface()
    interface.main()


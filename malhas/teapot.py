# -*- coding: UTF-8 -*-
# Autor: Hugo Henriques Maia Vieira
# Licença: creative commons by-nc-sa


from   OpenGL.GL import *
from   OpenGL.GLU import *
from   OpenGL.GLUT import *
from sys import argv

class Interface:

    def __init__(self):
        self.angulo = 45
        self.aspecto = 0
        self.rotacao = 0
        self.inclinacao = 0

    def init(self):
        glClearColor(1, 1, 1, 1)

    # Função usada para especificar o volume de visualização
    def EspecificaParametrosVisualizacao(self):

    	glMatrixMode(GL_PROJECTION)
    	glLoadIdentity()

    	gluPerspective(self.angulo,self.aspecto,0.1,500)

    	glMatrixMode(GL_MODELVIEW)
    	glLoadIdentity()

    	gluLookAt(self.rotacao,self.inclinacao,250, 0,0,0, -1,0,0)

    def gerencia_mouse(self, button, state, x, y):
        if (button == GLUT_LEFT_BUTTON):
        	if (state == GLUT_DOWN): # Zoom-in
        		if (self.angulo >= 10): self.angulo -= 5

        if (button == GLUT_RIGHT_BUTTON):
        	if (state == GLUT_DOWN): # Zoom-out
        		if (self.angulo <= 130): self.angulo += 5

        self.EspecificaParametrosVisualizacao()
        glutPostRedisplay()

    def gerencia_teclado(self, tecla, x, y):
        if tecla == 101: # cima
            self.inclinacao -= 5
        if tecla == 103: # baixo
            self.inclinacao += 5
        if tecla == 102: # direita
    		self.rotacao -= 5
        if tecla == 100: # esquerda
    		self.rotacao += 5

        self.EspecificaParametrosVisualizacao()
        glutPostRedisplay()


    def display(self):
    	glClear(GL_COLOR_BUFFER_BIT)
    	glColor3f(0.0, 0.0, 1.0)

    	glutWireTeapot(50.0)

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

        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    	glutInitWindowSize(350,300)
    	glutCreateWindow("Visualizacao 3D")
        glutDisplayFunc(self.display)
        glutReshapeFunc(self.reshape)
        glutSpecialFunc(self.gerencia_teclado)
    	glutMouseFunc(self.gerencia_mouse)
        self.init()
        glutMainLoop()

if __name__ == "__main__":
    interface = Interface()
    interface.main()


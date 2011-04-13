# -*- coding: UTF-8 -*-
# Autor: Hugo Henriques Maia Vieira

from   sys import argv
from   OpenGL.GL import *
from   OpenGL.GLU import *
from   OpenGL.GLUT import *

from malhas import Bezier, Splines, Catmull

BEZIER, SPLINES, CATMULL, LIMPAR = range(4)
ARQUIVO = "dados.teste"

X=0
Y=1
Z=2

class Interface:

    def __init__(self):
        self.malha = None
        self.zoom = 50
        self.aspecto = 0
        self.angulo = 0

    def init(self):
        glClearColor(1, 1, 1, 1)

    # Função usada para especificar o volume de visualização
    def EspecificaParametrosVisualizacao(self):

    	glMatrixMode(GL_PROJECTION)
    	glLoadIdentity()

    	gluPerspective(self.zoom,self.aspecto,0.5,900)

    	glMatrixMode(GL_MODELVIEW)
    	glLoadIdentity()

        if self.malha:
        	gluLookAt(0,0,500,
        	          self.malha.centro[X],self.malha.centro[Y],self.malha.centro[Z],
        	          0,1,0)
        else:
        	gluLookAt(0,0,500,
        	          0,0,0,
        	          0,1,0)

    def gerencia_mouse(self, button, state, x, y):
        if (button == GLUT_LEFT_BUTTON):
        	if (state == GLUT_DOWN): # Zoom-in
        		if (self.zoom >= 10): self.zoom -= 5

        if (button == GLUT_RIGHT_BUTTON):
        	if (state == GLUT_DOWN): # Zoom-out
        		if (self.zoom <= 250): self.zoom += 5

        self.EspecificaParametrosVisualizacao()
        glutPostRedisplay()

    def gerencia_teclado(self, tecla, x, y):
        if tecla == GLUT_KEY_LEFT: # direita
    		self.angulo -= 2
        if tecla == GLUT_KEY_RIGHT: # esquerda
    		self.angulo += 2

        self.EspecificaParametrosVisualizacao()
        glutPostRedisplay()

    def display(self):
    	glClear(GL_COLOR_BUFFER_BIT)
    	glColor3f(0.0, 0.0, 1.0)

        glRotatef(self.angulo, 0, 1, 0);
        if self.malha: self.malha.desenha()

    	glutSwapBuffers()

    def reshape(self, largura, altura):
        if ( altura == 0 ): altura = 1
    	# Especifica o tamanho da viewport
        glViewport(0 , 0, largura, altura)
    	# Calcula a correção de aspecto
        self.aspecto = largura/altura

    	self.EspecificaParametrosVisualizacao()

    def menu_principal(self, opcao):
        if opcao == BEZIER:
            self.malha = Bezier(ARQUIVO)
            self.malha.calcular_pontos_da_curva()
            self.malha.desenha()
            glutPostRedisplay()
        if opcao == SPLINES:
            self.malha = Splines(ARQUIVO)
            self.malha.calcular_pontos_da_curva()
            self.malha.desenha()
            glutPostRedisplay()
        if opcao == CATMULL:
            self.malha = Catmull(ARQUIVO)
            self.malha.calcular_pontos_da_curva()
            self.malha.desenha()
            glutPostRedisplay()
        if opcao == LIMPAR:
            if self.malha:
                self.malha.limpar()
                self.malha = None
        return 0

    def cria_menu(self):

        menu = glutCreateMenu(self.menu_principal)
        glutAddMenuEntry("Bezier", BEZIER)
        glutAddMenuEntry("Splines", SPLINES)
        glutAddMenuEntry("Catmull", CATMULL)
        glutAddMenuEntry("Limpar", LIMPAR)

        glutAttachMenu(GLUT_MIDDLE_BUTTON)

    def main(self):
        glutInit(argv)

        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    	glutInitWindowSize(600,600)
    	glutCreateWindow("Visualizacao 3D")
        glutDisplayFunc(self.display)
        glutReshapeFunc(self.reshape)
        glutSpecialFunc(self.gerencia_teclado)
    	glutMouseFunc(self.gerencia_mouse)
        self.init()
        self.cria_menu()
        glutMainLoop()

if __name__ == "__main__":
    interface = Interface()
    interface.main()


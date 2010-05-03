# -*- coding: UTF-8 -*-
# Autor: Hugo Henriques Maia Vieira
# Licença: creative commons by-nc-sa


from   OpenGL.GL import *
from   OpenGL.GLU import *
from   OpenGL.GLUT import *
from sys import argv

from malhas import Bezier

BEZIER, SPLINES, CATMULL = range(3)
ARQUIVO = "dados.teste"

class Interface:

    def __init__(self):
        self.malha = None
        self.limite_x = 300
        self.limite_y = 300

    def init(self):
        glClearColor(1, 1, 1, 1)

    def plano_cartesiano(self):
        glColor3f(0, 0, 0)
        glLineWidth(1)

        glBegin(GL_LINES)
        glVertex2f(-self.limite_x, 0)
        glVertex2f(self.limite_x, 0)
        glVertex2f(0, -self.limite_y)
        glVertex2f(0, self.limite_y)
        glEnd()

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT)

        glLoadIdentity()
        gluOrtho2D(-self.limite_x,self.limite_x,-self.limite_y,self.limite_y)

        self.plano_cartesiano()
        if self.malha != None:
            self.malha.desenha()
        glFlush()

    def reshape(self, largura, altura):
        glViewport(0 , 0, largura, altura)
        self.limite_x = largura/2
        self.limite_y = altura/2


    def menu_principal(self, opcao):
        if opcao == BEZIER:
            self.malha = Bezier(ARQUIVO)
            self.malha.calcular_pontos_da_curva()
            self.malha.desenha()
            glutPostRedisplay()
        if opcao == SPLINES:
            pass
        if opcao == CATMULL:
            pass
        return 0

    def cria_menu(self):

        menu = glutCreateMenu(self.menu_principal)
        glutAddMenuEntry("Bezier", BEZIER)
        glutAddMenuEntry("Splines", SPLINES)
        glutAddMenuEntry("Catmull-rom", CATMULL)

        glutAttachMenu(GLUT_MIDDLE_BUTTON)

    def main(self):
        glutInit(argv)

        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
        glutInitWindowSize(self.limite_x*2,self.limite_y*2)
        glutCreateWindow("Malhas")

        glutDisplayFunc(self.display)
        glutReshapeFunc(self.reshape)
        self.init()
        self.cria_menu()
        glutMainLoop()

if __name__ == "__main__":
    interface = Interface()
    interface.main()


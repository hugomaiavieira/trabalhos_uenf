# -*- coding: UTF-8 -*-
# Autor: Hugo Henriques Maia Vieira

from   sys import argv
from   OpenGL.GL import *
from   OpenGL.GLU import *
from   OpenGL.GLUT import *

from numpy import array
from curvas import Hermite, Bezier, Splines, Catmull

NADA, LIMPAR, DESENHAR_HERMITE, MANIPULAR_HERMITE, DESENHAR_BEZIER, MANIPULAR_BEZIER, DESENHAR_SPLINES, MANIPULAR_SPLINES, DESENHAR_CATMULL, MANIPULAR_CATMULL = range(10)

class Interface:

    def __init__(self):
        self.curva = None
        self.limite_x = 300
        self.limite_y = 300
        self.tarefa = NADA
        self.elemento_selecionado = None

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
        if self.curva : self.curva.desenha("curva")
        glFlush()

    def reshape(self, largura, altura):
        glViewport(0 , 0, largura, altura)
        self.limite_x = largura/2
        self.limite_y = altura/2


    def gerencia_mouse(self, button, state, x, y):
        # As duas linhas seguintes servem para ajeitar as coordenadas recebidas
        # pelo clique do mouse de acordo com as coordenadas de tela.
        # As coordenadas de mouse numa tela de 200x200, vão de (0,0) no canto
        # superior esquerdo, até (199,199) no canto inferior direito.
        x = x - self.limite_x
        y = self.limite_y - y

        if self.tarefa == DESENHAR_HERMITE:
            if(button == GLUT_LEFT_BUTTON):
                if(state == GLUT_DOWN):
                    if len(self.curva.pontos) < 1:
                        self.curva.adicionar_ponto(array([x,y]))
                        self.curva.desenha()
                    else:
                        self.curva.adicionar_ponto(array([x,y]))
                        self.curva.adicionar_tangentes()
                        self.curva.calcular_pontos_da_curva()
                        self.curva.desenha("curva")
                        self.tarefa = MANIPULAR_HERMITE

        if (self.tarefa == DESENHAR_BEZIER) or (self.tarefa == DESENHAR_SPLINES) or (self.tarefa == DESENHAR_CATMULL):
            if(button == GLUT_LEFT_BUTTON):
                if(state == GLUT_DOWN):
                    if len(self.curva.pontos) < 3:
                        self.curva.adicionar_ponto(array([x,y]))
                        self.curva.desenha()
                    else:
                        self.curva.adicionar_ponto(array([x,y]))
                        self.curva.calcular_pontos_da_curva()
                        self.curva.desenha("curva")
                        self.tarefa = MANIPULAR_BEZIER


        elif (self.tarefa == MANIPULAR_BEZIER) or (self.tarefa == MANIPULAR_SPLINES) or (self.tarefa == MANIPULAR_CATMULL) or (self.tarefa == MANIPULAR_HERMITE):
            if(button == GLUT_LEFT_BUTTON):
                if(state == GLUT_DOWN):
                    self.elemento_selecionado = self.curva.ponto_proximo(x,y)
                elif(state == GLUT_UP):
                    self.elemento_selecionado = None

    def gerencia_motion(self, x, y):
        # As duas linhas seguintes servem para ajeitar as coordenadas recebidas
        # pelo clique do mouse de acordo com as coordenadas de tela.
        # As coordenadas de mouse numa tela de 200x200, vão de (0,0) no canto
        # superior esquerdo, até (199,199) no canto inferior direito.
        x = x - self.limite_x
        y = self.limite_y - y

        if (self.tarefa == MANIPULAR_BEZIER) or (self.tarefa == MANIPULAR_SPLINES) or (self.tarefa == MANIPULAR_CATMULL) or (self.tarefa == MANIPULAR_HERMITE):
            if self.elemento_selecionado != None:
                self.curva.mover_ponto(self.elemento_selecionado, x, y)
                self.curva.desenha("curva")
            glutPostRedisplay()

    def menu_principal(self, opcao):
        if opcao == LIMPAR:
            self.tarefa = None
            self.curva.limpar()
            glutPostRedisplay()
        if opcao == DESENHAR_HERMITE:
            self.curva = Hermite()
            self.curva.limpar()
            self.tarefa = DESENHAR_HERMITE
            glutPostRedisplay()
        if opcao == DESENHAR_BEZIER:
            self.curva = Bezier()
            self.curva.limpar()
            self.tarefa = DESENHAR_BEZIER
            glutPostRedisplay()
        if opcao == DESENHAR_SPLINES:
            self.curva = Splines()
            self.curva.limpar()
            self.tarefa = DESENHAR_SPLINES
            glutPostRedisplay()
        if opcao == DESENHAR_CATMULL:
            self.curva = Catmull()
            self.curva.limpar()
            self.tarefa = DESENHAR_CATMULL
            glutPostRedisplay()
        return 0

    def cria_menu(self):

        menu = glutCreateMenu(self.menu_principal)
        glutAddMenuEntry("Limpar", LIMPAR)
        glutAddMenuEntry("Hermite", DESENHAR_HERMITE)
        glutAddMenuEntry("Bezier", DESENHAR_BEZIER)
        glutAddMenuEntry("Splines", DESENHAR_SPLINES)
        glutAddMenuEntry("Catmull-rom", DESENHAR_CATMULL)

        glutAttachMenu(GLUT_MIDDLE_BUTTON)

    def main(self):
        glutInit(argv)

        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
        glutInitWindowSize(self.limite_x*2,self.limite_y*2)
        glutCreateWindow("Curvas")

        glutDisplayFunc(self.display)
        glutReshapeFunc(self.reshape)
        glutMouseFunc(self.gerencia_mouse)
        glutMotionFunc(self.gerencia_motion)
        self.init()
        self.cria_menu()
        glutMainLoop()

if __name__ == "__main__":
    interface = Interface()
    interface.main()


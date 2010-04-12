# Autor: Hugo Henriques Maia Vieira
# Licença: creative commons by-nc-sa

# -*- coding: UTF-8 -*-

from   sys import argv
from   OpenGL.GL import *
from   OpenGL.GLU import *
from   OpenGL.GLUT import *

from numpy import array
from transformacoes import Objeto

NENHUMA, DESENHAR, TRANSLADAR, REDIMENSIONAR, ROTACIONAR, CISALHAR, REFLETIR_H, REFLETIR_V, REFLETIR_O, HERMITE = range(10)

class Interface:

    def __init__(self):
        self.objeto = Objeto()
        self.limite_x = 300
        self.limite_y = 300
        self.tarefa = DESENHAR
        self.indice_vertice_selecionado = None
        self.eixo_cisalhar = None

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
        self.objeto.desenha("poligono")
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

        if self.tarefa == DESENHAR:
            if(button == GLUT_LEFT_BUTTON):
                if(state == GLUT_UP):
                    self.objeto.vertices.append(array([x, y]))
                    self.objeto.desenha("pontos")
            if(button == GLUT_RIGHT_BUTTON):
                if(state == GLUT_DOWN):
                    self.objeto.desenha("poligono")
                    self.objeto.centro()
                    self.tarefa = NENHUMA

        elif self.tarefa == TRANSLADAR:
            if(button == GLUT_LEFT_BUTTON):
                if(state == GLUT_DOWN):
                    self.objeto.transladar(x,y)
                    glutPostRedisplay()

        elif self.tarefa == ROTACIONAR:
            if(button == GLUT_LEFT_BUTTON):
                if(state == GLUT_DOWN):
                    self.indice_vertice_selecionado = self.objeto.vertice_proximo(x,y)
                elif(state == GLUT_UP):
                    self.indice_vertice_selecionado = None

        elif self.tarefa == REDIMENSIONAR:
            if(button == GLUT_LEFT_BUTTON):
                if(state == GLUT_DOWN):
                    self.indice_vertice_selecionado = self.objeto.vertice_proximo(x,y)
                elif(state == GLUT_UP):
                    self.indice_vertice_selecionado = None

        elif self.tarefa == CISALHAR:
            if(button == GLUT_LEFT_BUTTON):
                if(state == GLUT_DOWN):
                    self.eixo_cisalhar = "x"
                    self.indice_vertice_selecionado = self.objeto.vertice_proximo(x,y)
                elif(state == GLUT_UP):
                    self.indice_vertice_selecionado = None
            if(button == GLUT_RIGHT_BUTTON):
                if(state == GLUT_DOWN):
                    self.eixo_cisalhar = "y"
                    self.indice_vertice_selecionado = self.objeto.vertice_proximo(x,y)
                elif(state == GLUT_UP):
                    self.indice_vertice_selecionado = None

    def gerencia_motion(self, x, y):
        # As duas linhas seguintes servem para ajeitar as coordenadas recebidas
        # pelo clique do mouse de acordo com as coordenadas de tela.
        # As coordenadas de mouse numa tela de 200x200, vão de (0,0) no canto
        # superior esquerdo, até (199,199) no canto inferior direito.
        x = x - self.limite_x
        y = self.limite_y - y

        if self.tarefa == TRANSLADAR:
            self.objeto.transladar(x,y)
            glutPostRedisplay()

        elif self.tarefa == ROTACIONAR:
            if self.indice_vertice_selecionado != None:
                vertice_rotacao = self.objeto.vertices[self.indice_vertice_selecionado]
                ponto = array([x,y])
                angulo = self.objeto.angulo_vertice_ponto(vertice_rotacao,ponto)
                self.objeto.rotacionar(angulo)
                glutPostRedisplay()

        elif self.tarefa == REDIMENSIONAR:
            if self.indice_vertice_selecionado != None:
                vertice_redimencao = self.objeto.vertices[self.indice_vertice_selecionado]
                ponto = array([x,y])
                proporcao = self.objeto.proporcao_fixa_vertice_ponto(vertice_redimencao,ponto)
                self.objeto.redimensionar(proporcao)
                glutPostRedisplay()

        elif self.tarefa == CISALHAR:
            if self.indice_vertice_selecionado != None:
                vertice_cisalhamento = self.objeto.vertices[self.indice_vertice_selecionado]
                ponto = array([x,y])
#                proporcao = self.objeto.proporcao_fixa_vertice_ponto(ponto,vertice_cisalhamento)
                self.objeto.cisalhar(vertice_cisalhamento, ponto, self.eixo_cisalhar)
                glutPostRedisplay()

    def menu_principal(self, opcao):
        if opcao == DESENHAR:
            self.tarefa = DESENHAR
            self.objeto.vertices = []
            glutPostRedisplay()
        return 0

    def menu_transformacoes(self, opcao):
        if opcao == TRANSLADAR:
            self.tarefa = TRANSLADAR
        elif opcao == REDIMENSIONAR:
            self.tarefa = REDIMENSIONAR
        elif opcao == ROTACIONAR:
            self.tarefa = ROTACIONAR
        elif opcao == CISALHAR:
            self.tarefa = CISALHAR

    def menu_refletir(self, opcao):
        if opcao == REFLETIR_H:
            self.objeto.refletir("x")
            self.tarefa = REFLETIR_H
            glutPostRedisplay()
        elif opcao == REFLETIR_V:
            self.objeto.refletir("y")
            self.tarefa = REFLETIR_V
            glutPostRedisplay()
        elif opcao == REFLETIR_O:
            self.objeto.refletir("o")
            self.tarefa = REFLETIR_O
            glutPostRedisplay()

    def cria_menu(self):

        submenu_refletir = glutCreateMenu(self.menu_refletir)
        glutAddMenuEntry("Horizontalmente", REFLETIR_H)
        glutAddMenuEntry("Verticalmente", REFLETIR_V)
        glutAddMenuEntry("Centralmente", REFLETIR_O)

        submenu_transformacoes = glutCreateMenu(self.menu_transformacoes)
        glutAddMenuEntry("Transladar", TRANSLADAR)
        glutAddMenuEntry("Redimensionar", REDIMENSIONAR)
        glutAddMenuEntry("Rotacionar", ROTACIONAR)
        glutAddMenuEntry("Cisalhar", CISALHAR)
        glutAddSubMenu("Refletir", submenu_refletir)

        menu = glutCreateMenu(self.menu_principal)
        glutAddMenuEntry("Desenhar", DESENHAR)
        glutAddSubMenu("Transformacoes", submenu_transformacoes)

        glutAttachMenu(GLUT_MIDDLE_BUTTON)

    def main(self):
        glutInit(argv)

        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
        glutInitWindowSize(self.limite_x*2,self.limite_y*2)
        glutCreateWindow("Transformacoes")

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


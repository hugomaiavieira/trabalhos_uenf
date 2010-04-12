# Autor: Hugo Henriques Maia Vieira
# Licença: creative commons by-nc-sa

# -*- coding: UTF-8 -*-

from OpenGL.GL import *
from numpy import array, matrix, sin, cos, hypot, arccos, inner, cross

X = 0
Y = 1

class Objeto:

    def __init__(self,vertices=[]):
        self.vertices = vertices

    def desenha(self, parametro):
        if parametro == "pontos":
            parametro = GL_LINE_STRIP
        elif parametro == "poligono":
            parametro = GL_LINE_LOOP

        glColor3f(0.2,0.5,0.8)
        glLineWidth(3)
        glBegin(parametro)
        for vertice in self.vertices:
            glVertex2f(vertice[X],vertice[Y])
        glEnd()
        glFlush()

    def centro(self):
        if self.vertices:
            centro = array([0,0])
            for vertice in self.vertices:
                centro = centro + vertice
            centro = centro / float(self.vertices.__len__())
            return centro
        else:
            return None

    def vertice_proximo(self, x, y):
        raio = 4
        ponto = array([x,y])
        i=0
        while i < self.vertices.__len__():
            vertice = self.vertices[i]
            vetor_distancia = ponto - vertice
            modulo_distancia = hypot(vetor_distancia[X],vetor_distancia[Y])
            if modulo_distancia <= raio:
                return i
            i+=1
        return None

    def angulo_vertice_ponto(self, vertice, ponto):
        if (vertice != None) and (ponto != None):
            modulo_vertice = hypot(vertice[X],vertice[Y])
            modulo_ponto = hypot(ponto[X],ponto[Y])
            coseno = inner(vertice, ponto)/(modulo_vertice * modulo_ponto)
            angulo = arccos(coseno)
            if cross(vertice,ponto) > 0:
                return angulo
            else:
                return -angulo
        else:
            return 0

    def transladar(self, x, y):
        vetor_translacao = array([x, y]) - self.centro()

        i=0
        while i < self.vertices.__len__():
            self.vertices[i] += vetor_translacao
            i+=1

    def proporcao_fixa_vertice_ponto(self, vertice, ponto):
        ponto = ponto - self.centro()
        vertice = vertice - self.centro()
        modulo_ponto = hypot(ponto[X], ponto[Y])
        modulo_vertice = hypot(vertice[X], vertice[Y])

        proporcao = modulo_ponto / modulo_vertice
        return proporcao


    def redimensionar(self, proporcao):
        centro_original = self.centro()
        self.transladar(0,0)

        matriz_escala = matrix([[proporcao, 0],
                                [0, proporcao]])

        i=0
        while i < self.vertices.__len__():
            self.vertices[i] = self.vertices[i] * matriz_escala
            # As duas linhas seguintes são para converter a matriz resultante
            # da multiplicação acima para o formato de array padrão.
            self.vertices[i] = array(self.vertices[i])
            self.vertices[i] = array(self.vertices[i][0])
            i+=1

        self.transladar(centro_original[X], centro_original[Y])

    def refletir(self, parametro):
        if (parametro == "vertical") or (parametro == "y"):
            vetor_reflexao = array([-1, 1])
        elif (parametro == "horizontal") or (parametro == "x"):
            vetor_reflexao = array([1, -1])
        elif (parametro == "origem") or (parametro == "o"):
            vetor_reflexao = array([-1, -1])

        i=0
        while i < self.vertices.__len__():
            self.vertices[i] *= vetor_reflexao
            i+=1

    def rotacionar(self, angulo):
        centro_original = self.centro()
        self.transladar(0,0)

        matriz_rotacao = matrix([[cos(angulo), sin(angulo)],
                                 [-sin(angulo), cos(angulo)]])

        i=0
        while i < self.vertices.__len__():
            self.vertices[i] = self.vertices[i] * matriz_rotacao
            # As duas linhas seguintes são para converter a matriz resultante
            # da multiplicação acima para o formato de array padrão.
            self.vertices[i] = array(self.vertices[i])
            self.vertices[i] = array(self.vertices[i][0])
            i+=1

        self.transladar(centro_original[X], centro_original[Y])

    def cisalhar(self, vertice, ponto, eixo):
        if eixo == "y":
            proporcao = 0.06
            if ponto[Y] < vertice[Y]:
                proporcao = -proporcao
            matriz_cisalhamento = matrix([[1, proporcao],
                                         [0, 1]])
        elif eixo == "x":
            proporcao = 0.06
            if ponto[X] < vertice[X]:
                proporcao = -proporcao
            matriz_cisalhamento = matrix([[1, 0],
                                         [proporcao, 1]])

        i=0
        while i < self.vertices.__len__():
            self.vertices[i] = self.vertices[i] * matriz_cisalhamento
            # As duas linhas seguintes são para converter a matriz resultante
            # da multiplicação acima para o formato de array padrão.
            self.vertices[i] = array(self.vertices[i])
            self.vertices[i] = array(self.vertices[i][0])
            i+=1


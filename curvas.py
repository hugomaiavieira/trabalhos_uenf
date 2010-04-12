# -*- coding: UTF-8 -*-
# Autor: Hugo Henriques Maia Vieira
# Licença: creative commons by-nc-sa


from OpenGL.GL import *
from numpy import array, matrix, hypot, transpose

X = 0
Y = 1

class Erro(Exception): pass

class Curva:

    def __init__(self,pontos=[]):
        self.pontos = pontos

    def adicionar_ponto(self, ponto):
        self.pontos.append(ponto)

    def ponto_proximo(self, x, y):
        raio = 4
        ponto_clicado = array([x,y])
        i=0
        while i < len(self.pontos):
            ponto = self.pontos[i]
            vetor_distancia = ponto_clicado - ponto
            modulo_distancia = hypot(vetor_distancia[X],vetor_distancia[Y])
            if modulo_distancia <= raio:
                return i
            i+=1
        return None

    def mover_ponto(self, indice, x, y):
        self.pontos[indice] = array([x,y])
        self.calcular_pontos_da_curva()


class Hermite(Curva):

    def __init__(self, pontos=[]):
        Curva.__init__(self, pontos)
        self.tangentes = []
        self.pontos_da_curva = []
        self.matriz = matrix([[2, -2, 1, 1],
                              [-3, 3, -2, -1],
                              [0, 0, 1, 0],
                              [1, 0, 0, 0]])


    def tangente_proxima(self, x, y):
        raio = 4
        ponto_clicado = array([x,y])
        i=0
        while i < len(self.tangentes):
            tangente = self.tangentes[i]
            vetor_distancia = ponto_clicado - tangente
            modulo_distancia = hypot(vetor_distancia[X],vetor_distancia[Y])
            if modulo_distancia <= raio:
                return i
            i+=1
        return None

    def elemento_proximo(self, x, y):
        indice_ponto = self.ponto_proximo(x,y)
        if indice_ponto != None:
            return {"ponto": indice_ponto}

        indice_tangente = self.tangente_proxima(x,y)
        if indice_tangente != None:
            return {"tangente": indice_tangente}

        return None

    def mover_tangente(self, indice, x, y):
        self.tangentes[indice] = array([x,y])
        self.calcular_pontos_da_curva()

    def calcular_tangentes_iniciais(self):
        if len(self.pontos) >= 2:
            i=0
            for ponto in self.pontos:
                if i%2 == 0:
                    self.tangentes.append(ponto + array([0,100]))
                else:
                    self.tangentes.append(ponto + array([0,-100]))
                i+=1
        else:
            raise Erro, "deve-se ter no minimo dois pontos para calcular as tangentes"

    def calcular_pontos_da_curva(self, passo=0.03):
        self.pontos_da_curva = []
        i=0
        while i < len(self.pontos)-1:
            vetor_pontos_tangentes = array([self.pontos[i],
                                           self.pontos[i+1],
                                           self.tangentes[i],
                                           self.tangentes[i+1]])
            t=0
            while t <= 1:
                vetor_t = array([pow(t,3), pow(t,2), t, 1])
                ponto_da_curva = vetor_t * self.matriz * vetor_pontos_tangentes
                self.pontos_da_curva.append(ponto_da_curva)
                t+=passo
            i+=1

    def montar_curva(self, passo=""):
        self.calcular_tangentes_iniciais()
        if passo:
            self.calcular_pontos_da_curva(passo)
        else:
            self.calcular_pontos_da_curva()

    def limpar(self):
        self.pontos=[]
        self.tangentes=[]
        self.pontos_da_curva=[]

    def desenha(self, fase=""):
        # Desenha pontos
        glColor3f(1,0,0)
        glPointSize(3)
        glBegin(GL_POINTS)
        for ponto in self.pontos:
            glVertex2f(ponto[X],ponto[Y])
        glEnd()
        glFlush()

        if fase == "curvas":
            # Desenha tangentes
            i=0
            glColor3f(0,0,1)
            glBegin(GL_LINES)
            while i < len(self.pontos):
                glVertex2f(self.pontos[i][X],self.pontos[i][Y])
                glVertex2f(self.tangentes[i][X],self.tangentes[i][Y])
                i+=1
            glEnd()
            glFlush()

            # Desenha curvas
            i=0
            glColor3f(1,0,0)
            glBegin(GL_LINE_STRIP)
            while i < len(self.pontos_da_curva):
                glVertex2f(self.pontos_da_curva[i].item(X),self.pontos_da_curva[i].item(Y))
                glVertex2f(self.pontos_da_curva[i].item(X),self.pontos_da_curva[i].item(Y))
                i+=1
            glEnd()
            glFlush()


class Bezier(Curva):

    def __init__(self, pontos=[]):
        Curva.__init__(self, pontos)
        self.pontos_da_curva = []
        self.matriz = matrix([[-1, 3, -3, 1],
                              [3, -6, 3, 0],
                              [-3, 3, 0, 0],
                              [1, 0, 0, 0]])

    def calcular_pontos_da_curva(self, passo=0.03):
        self.pontos_da_curva = []
        vetor_pontos = array([self.pontos[0],
                              self.pontos[1],
                              self.pontos[2],
                              self.pontos[3]])
        t=0
        while t <= 1:
            vetor_t = array([pow(t,3), pow(t,2), t, 1])
            ponto_da_curva = vetor_t * self.matriz * vetor_pontos
            self.pontos_da_curva.append(ponto_da_curva)
            t+=passo

    def limpar(self):
        i=0
        tamanho = len(self.pontos)
        while i < tamanho:
            self.pontos.pop()
            i+=1
        self.pontos_da_curva = []

    def desenha(self, fase=""):
        # Desenha pontos
        glColor3f(1,0,0)
        glPointSize(3)
        glBegin(GL_POINTS)
        for ponto in self.pontos:
            glVertex2f(ponto[X],ponto[Y])
        glEnd()
        glFlush()

        if fase == "curvas":
            parametro = GL_LINE_LOOP # Desenha poligono
        else:
            parametro = GL_LINE_STRIP # Desenha apenas linhas

        glColor3f(0.2,0.5,0.8)
        glColor3f(0,0,1)
        glBegin(parametro)
        for ponto in self.pontos:
            glVertex2f(ponto[X],ponto[Y])
        glEnd()
        glFlush()

        if fase == "curvas":
            # Desenha curvas
            glColor3f(1,0,0)
            glBegin(GL_LINE_STRIP)
            for ponto in self.pontos_da_curva:
                glVertex2f(ponto.item(X), ponto.item(Y))
            glEnd()
            glFlush()

class Splines(Bezier):

    def __init__(self, pontos=[]):
        Curva.__init__(self, pontos)
        self.pontos_da_curva = []
        self.matriz = matrix([[-1, 3, -3, 1],
                                [3, -6, 3, 0],
                                [-3, 0, 3, 0],
                                [1, 4, 1, 0]])

    def calcular_pontos_da_curva(self, passo=0.03):
        self.pontos_da_curva = []
        vetor_pontos = array([self.pontos[0],
                              self.pontos[1],
                              self.pontos[2],
                              self.pontos[3]])
        t=0
        while t <= 1:
            vetor_t = array([pow(t,3), pow(t,2), t, 1])
            ponto_da_curva = (vetor_t * self.matriz * vetor_pontos) / 6
            self.pontos_da_curva.append(ponto_da_curva)
            t+=passo

class Catmull(Bezier):

    def __init__(self, pontos=[]):
        Curva.__init__(self, pontos)
        self.pontos_da_curva = []
        self.matriz = matrix([[-1, 3, -3, 1],
                                [2, -5, 4, -1],
                                [-1, 0, 1, 0],
                                [0, 2, 0, 0]])

    def calcular_pontos_da_curva(self, passo=0.03):
        self.pontos_da_curva = []
        vetor_pontos = array([self.pontos[0],
                              self.pontos[1],
                              self.pontos[2],
                              self.pontos[3]])
        t=0
        while t <= 1:
            vetor_t = array([pow(t,3), pow(t,2), t, 1])
            ponto_da_curva = (vetor_t * self.matriz * vetor_pontos) / 2
            self.pontos_da_curva.append(ponto_da_curva)
            t+=passo


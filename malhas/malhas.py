from OpenGL.GL import *
from numpy import array, matrix, transpose, dot

X=0
Y=1
Z=2

def frange(start, end=None, inc=1.0):
    "A range function, that does accept float increments..."

    if end == None:
        end = start + 0.0
        start = 0.0

    L = []
    while 1:
        next = start + len(L) * inc
        if inc > 0 and next >= end:
            break
        elif inc < 0 and next <= end:
            break
        L.append(next)
    return L

class Malha(object):

    def __init__(self, arquivo):
        arquivo = open(arquivo)
        self.pontos = Malha.ler_dados(arquivo)
        self.curva_s_t = []

    @classmethod
    def ler_dados(self, arquivo):
        arquivo = arquivo.read().splitlines()
        if "" in arquivo: arquivo.remove("")
        dados = []
        for linha in arquivo:
            aux = []
            linha = linha.split()
            for item in linha:
                item = item.split(",")
                aux.append(map(int,item))
            dados.append(aux)
        return dados

    def matriz_pontos(self, eixo):
        matriz = []
        for linha in self.pontos:
            aux = []
            for ponto in linha:
                aux.append(ponto[eixo])
            matriz.append(aux)
        return matrix(matriz)

    def calcular_pontos_da_curva(self):
        self.curva_s_t = []
        curva_t = []
        for s in frange(0,1,0.1):
            for t in frange(0,1,0.1):
                vetor_s = matrix([pow(s,3), pow(s,2), s, 1])
                vetor_t = matrix([pow(t,3), pow(t,2), t, 1])

                ponto_x = (vetor_s * self.matriz * self.matriz_pontos(X) * self.matriz.transpose() * vetor_t.transpose())
                ponto_y = (vetor_s * self.matriz * self.matriz_pontos(Y) * self.matriz.transpose() * vetor_t.transpose())
                ponto_z = (vetor_s * self.matriz * self.matriz_pontos(Z) * self.matriz.transpose() * vetor_t.transpose())

                curva_t.append(array([float(ponto_x), float(ponto_y), float(ponto_z)]))
            self.curva_s_t.append(curva_t)

    def desenha(self):
        # Desenha pontos
        glColor3f(1,0,0)
        glPointSize(3)
        glBegin(GL_POINTS)
        for linha in self.pontos:
            for ponto in linha:
                glVertex2f(ponto[X],ponto[Y])
        glEnd()

        glColor3f(0.2,0.4,0.6)
        for linha in self.pontos:
            for ponto in linha:
                glBegin(GL_LINES)
                glVertex2f(ponto[X],ponto[Y])
                glVertex2f(ponto[X],0)
                glEnd()

        glColor3f(0,0,1)
        for linha in self.curva_s_t:
            glBegin(GL_POINTS)
            for ponto in linha:
                glVertex2f(ponto.item(X), ponto.item(Y))
            glEnd()
        glFlush()


class Bezier(Malha):

    def __init__(self, arquivo):
        Malha.__init__(self, arquivo)
        self.matriz = matrix([[-1, 3, -3, 1],
                              [3, -6, 3, 0],
                              [-3, 3, 0, 0],
                              [1, 0, 0, 0]])


# -*- coding: UTF-8 -*-
# Autor: Hugo Henriques Maia Vieira
# Licença: creative commons by-nc-sa

from OpenGL.GL import *
from re import match
from numpy import array
from lib import distance

X=0
Y=1
Z=2

class Barreira(object):

    def __init__(self, vertices=[]):
        self.vertices = vertices


class Particula(object):

    def __init__(self, massa=0, posicao=[0,0,0], velocidade=[0,0,0], forca_sofrida=[0,0,0]):
        self.massa = massa
        self.posicao = posicao
        self.velocidade = velocidade
        self.forca_sofrida = forca_sofrida

    def variar_forca(self, aceleracao):
        """
        forca = massa * aceleracao

        """
        self.forca_sofrida += self.massa * aceleracao

    def variar_velocidade(self, delta_t):
        """
        forca = massa * aceleracao
        aceleracao = forca / massa

        aceleracao = velocidade / delta_t
        velocidade = delta_t * aceleracao

        velocidade = delta_t * (forca / massa)
        """
        self.velocidade += delta_t * (self.forca_sofrida / self.massa )

    def variar_posicao(self, delta_t):
        """
        v = s / delta_t
        s = delta_t * v
        """
        self.posicao += delta_t * self.velocidade

    def distancia_para_a_barreira(self, barreira):
        distiancia = distance(barreira.vertices, self.posicao)
        return distancia

    def animar(self, aceleracao, delta_t):
        self.variar_forca(aceleracao)
        self.variar_velocidade(delta_t)
        self.variar_posicao(delta_t)

    def desenhar(self):
        glColor3f(0.2,0.6,0.3)
        glPointSize(5)
        glBegin(GL_POINTS)
        glVertex3f(self.posicao[X], self.posicao[Y], self.posicao[Z])
        glEnd()


class SistemaParticulas(object):

    def __init__(self, particulas=[], t0=0, delta_t=0, gravidade=0):
        self.particulas = particulas
        self.t0 = t0
        self.delta_t = delta_t
        self.gravidade = gravidade

    def ler_dados(self, _arquivo):
        linha = _arquivo.readline()
        while linha:
            if match(r'#dados_gerais', linha):
                linha = _arquivo.readline()
                while not match(r'^#', linha):
                    g = match(r'^gravidade (?P<gravidade>[-]?[0-9]+([.][0-9]+)?)', linha)
                    t = match(r'^delta_t (?P<delta_t>[0-9]+([.][0-9]+)?)', linha)
                    if g: self.gravidade = array([0,float(g.groupdict()['gravidade']),0])
                    if t: self.delta_t = float(t.groupdict()['delta_t'])
                    linha = _arquivo.readline()
            if match(r'#particula', linha):
                particula = Particula()
                linha = _arquivo.readline()
                while not match(r'^#', linha) and linha:
                    m = match(r'^massa (?P<massa>[0-9]+([.][0-9]+)?)', linha)
                    p = match(r'^posicao (?P<x>-?[0-9]+([.][0-9]+)?) (?P<y>-?[0-9]+([.][0-9]+)?) (?P<z>-?[0-9]+([.][0-9]+)?)', linha)
                    v = match(r'^velocidade (?P<x>-?[0-9]+([.][0-9]+)?) (?P<y>-?[0-9]+([.][0-9]+)?) (?P<z>-?[0-9]+([.][0-9]+)?)', linha)
                    f = match(r'^forca_sofrida (?P<x>-?[0-9]+([.][0-9]+)?) (?P<y>-?[0-9]+([.][0-9]+)?) (?P<z>-?[0-9]+([.][0-9]+)?)', linha)
                    if m: particula.massa = float(m.groupdict()['massa'])
                    if p: particula.posicao = array([float(p.groupdict()['x']), float(p.groupdict()['y']), float(p.groupdict()['z'])])
                    if v: particula.velocidade = array([float(v.groupdict()['x']), float(v.groupdict()['y']), float(v.groupdict()['z'])])
                    if f: particula.forca_sofrida = array([float(f.groupdict()['x']), float(f.groupdict()['y']), float(f.groupdict()['z'])])
                    linha = _arquivo.readline()
                self.particulas.append(particula)

    def animar(self):
        for particula in self.particulas:
            particula.animar(self.gravidade, self.delta_t)

    def desenhar(self):
        for particula in self.particulas:
            particula.desenhar()


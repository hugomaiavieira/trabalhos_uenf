# -*- coding: UTF-8 -*-
# Autor: Hugo Henriques Maia Vieira
# Licença: creative commons by-nc-sa

from OpenGL.GL import *
from re import match
from random import random

X=0
Y=1
Z=2

class Faces (object):

    def __init__(self):
        self.vertices = []
        self.faces = []

    def ler_dados(self, arquivo):
        linha = arquivo.readline()
        while linha:
            if match(r'^#[V|v]ertice', linha):
                linha = arquivo.readline()
                while match(r'^-?[0-9]', linha):
                    vertice = linha.split()
                    vertice = map(float,vertice)
                    self.vertices.append(vertice)
                    linha = arquivo.readline()
            if match(r'^#[F|f]aces', linha):
                linha = arquivo.readline()
                while match(r'^-?[0-9]', linha):
                    face = linha.split()
                    face = map(int,face)
                    self.faces.append(face)
                    linha = arquivo.readline()
            else:
                linha = arquivo.readline()

    def desenha(self):
        # Desenha vertices
        glColor3f(1,0,0)
        glPointSize(3)
        glBegin(GL_POINTS)
        for vertice in self.vertices:
            glVertex3f(vertice[X], vertice[Y], vertice[Z])
        glEnd()

        # Desenha faces
        for face in self.faces:
            r=random(); g=random(); b=random() # Cores aleatórias para faces
            glColor3f(r,g,b)
            glBegin(GL_POLYGON)
            for indice in face:
                vertice =  self.vertices[indice-1]
                glVertex3f(vertice[X], vertice[Y], vertice[Z])
            glEnd()

        glFlush()


# -*- coding: UTF-8 -*-
# Autor: Hugo Henriques Maia Vieira

from OpenGL.GL import *
from re import match
from random import random
from numpy import array, cross
from vector_lib import versor, vector_by

X=R=0
Y=G=1
Z=B=2

class Face(object):

    def __init__(self, vertices):
        self.vertices = vertices
        self.cor = "[R,G,B]"
        self.normal = [0,0,0]

        self.definir_cor()
        self.definir_normal()
        print self.normal

    def definir_cor(self):
        r=random(); g=random(); b=random() # Cores aleatórias para face
        self.cor = [r,g,b]

    def definir_normal(self):
        vetor1 = vector_by(self.vertices[0], self.vertices[1])
        vetor2 = vector_by(self.vertices[1], self.vertices[2])
        normal = cross(vetor1, vetor2)
        self.normal = versor(normal)

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
                    self.vertices.append(array(vertice))
                    linha = arquivo.readline()
            if match(r'^#[F|f]aces', linha):
                linha = arquivo.readline()
                while match(r'^-?[0-9]', linha):
                    indices = map(int, linha.split())
                    vertices = []
                    for indice in indices:
                        vertices.append(self.vertices[indice-1])
                    self.faces.append(Face(vertices))
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
            glColor3f(face.cor[R], face.cor[G], face.cor[B])
            glBegin(GL_POLYGON)
            glNormal3f(face.normal[X], face.normal[Y], face.normal[Z])
            for vertice in face.vertices:
                glVertex3f(vertice[X], vertice[Y], vertice[Z])
            glEnd()

        glFlush()


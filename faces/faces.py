# -*- coding: UTF-8 -*-
# Autor: Hugo Henriques Maia Vieira
# Licença: creative commons by-nc-sa

from re import match
from numpy import array

class Faces (object):

    def __init__(self):
        self.vertices = []
        self.faces = []

    def ler_dados(self, arquivo):
        linha = arquivo.readline()
        while linha:
            print linha
            if match(r'^#[V|v]ertice', linha):
                linha = arquivo.readline()
                while match(r'^[0-9]', linha):
                    vertice = linha.split()
                    vertice = map(float,vertice)
                    self.vertices.append(vertice)
                    linha = arquivo.readline()
            if match(r'^#[F|f]aces', linha):
                linha = arquivo.readline()
                while match(r'^[0-9]', linha):
                    face = linha.split()
                    face = map(float,face)
                    self.faces.append(face)
                    linha = arquivo.readline()
            else:
                linha = arquivo.readline()


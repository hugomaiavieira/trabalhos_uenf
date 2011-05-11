# encoding: utf-8

from random import choice
from functions import no_zero_range

ORIGEM, DESTINO, PESO = (0, 1, 2)

class PMediana(object):

    def __init__(self, arquivo):
        """
        Formato do arquivo:
            Número de vértices, número de arestas, p (número de medianas).
            Vértices inicial, vértice final, custo da aresta.
        """
        arquivo = open(arquivo)
        linha1 = arquivo.readline()
        self.n_vertices, irrelevante, self.n_medianas = map(int, linha1.split())

        linhas_arquivo = arquivo.readlines()
        self.definir_arestas(linhas_arquivo)

        self.vertices = self.todos_vertices()

        self.definir_matriz_adjacencias()
        self.definir_medianas()

    def definir_arestas(self, linhas):
        """
        Define self.arestas = { ORIGEM1: { DESTINO1: PESO1, DESTINO2: PESO2 } }
        """
        self.arestas = {}
        for linha in linhas:
            aresta = map(int, linha.split())
            if aresta[ORIGEM] in self.arestas.keys():
                self.arestas[aresta[ORIGEM]][aresta[DESTINO]] = aresta[PESO]
            else:
                self.arestas[aresta[ORIGEM]] = {aresta[DESTINO]: aresta[PESO]}

    def definir_matriz_adjacencias(self):
        """
        Define a matriz de adjacencias do grafo.
        """
        self.matriz = [[]]
        for i in no_zero_range(self.n_vertices):
            self.matriz.append([])
            for j in no_zero_range(self.n_vertices):
                if i == j:
                    self.matriz[i].append(0)
                elif i != 0 and j != 0:
                    self.matriz[i].append(self.peso_entre(i, j))
        self.matriz = self.matriz[1:] # Remover linha 0,0

    def peso_entre(self, origem, destino):
        """
        Retorna o peso da ligação entre os nós origem e destino ou vice-versa.
        Caso não exista ligação entre os nós retorna um número grande para o
        algorítimo não considerar o caminho que não existe.
        """
        if (origem in self.arestas.keys()) and (destino in self.arestas[origem].keys()):
            return self.arestas[origem][destino]

        origem, destino = destino, origem
        # Replay! Now from a diferent angle! Hhauahiaua
        if (origem in self.arestas.keys()) and (destino in self.arestas[origem].keys()):
            return self.arestas[origem][destino]

        return 5000

    def todos_vertices(self):
        origens = set(self.arestas.keys())
        destinos = set()
        for origem in origens:
            destinos = destinos.union(set(self.arestas[origem].keys()))

        return list(origens.union(destinos))


    def definir_medianas(self):
        """
        Define aleatóriamente as medianas.
        """
        self.medianas = []
        while len(self.medianas) != self.n_medianas:
            vertice = choice(self.vertices)
            if not vertice in self.medianas:
                self.medianas.append(vertice)

    def floyd(self):
        """
        Modifica self.matriz para ficar com a distancia mínima para chegar de
        um nó a outro.
        """
        for k in range(self.n_vertices):
            for i in range(self.n_vertices):
                for j in range(self.n_vertices):
                    distancia = self.matriz[i][k] + self.matriz[k][j]
                    if self.matriz[i][j] > distancia:
                        self.matriz[i][j] = distancia

    def definir_grafo(self):
        self.grafo = {}
        for vertice in self.vertices:
            menor_distancia = 50000
            for mediana in self.medianas:
                if not vertice in self.medianas:
                    distancia_vertice_mediana = self.matriz[vertice-1][mediana-1]
                    if distancia_vertice_mediana < menor_distancia:
                        self.grafo[vertice] = mediana
                        menor_distancia = distancia_vertice_mediana

    def distancia_total(self):
        soma = 0
        for vertice, mediana in self.grafo.items():
            soma += self.matriz[vertice-1][mediana-1]
        return soma


if __name__ == '__main__':
    p = PMediana('pmed1.txt')
    p.floyd()
    p.definir_grafo()
    print p.medianas
    print p.distancia_total()


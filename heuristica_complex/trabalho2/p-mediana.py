# encoding: utf-8

from time import time
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

        self.arestas = {}
        linhas_arquivo = arquivo.readlines()
        self.definir_arestas(linhas_arquivo)

        self.vertices = self.todos_vertices()

        self.matriz_adjacencias = [[]]
        self.definir_matriz_adjacencias()
        self.floyd()

        self.medianas = []
        self.grafo = {}
        self.solucao = None


    def definir_arestas(self, linhas):
        """
        Define self.arestas = { ORIGEM1: { DESTINO1: PESO1, DESTINO2: PESO2 } }
        """
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
        for i in no_zero_range(self.n_vertices):
            self.matriz_adjacencias.append([])
            for j in no_zero_range(self.n_vertices):
                if i == j:
                    self.matriz_adjacencias[i].append(0)
                elif i != 0 and j != 0:
                    self.matriz_adjacencias[i].append(self.peso_entre(i, j))
        self.matriz_adjacencias = self.matriz_adjacencias[1:] # Remover linha 0,0

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

    def floyd(self):
        """
        Modifica self.matriz_adjacencias para ficar com a distancia mínima para
        chegar de um nó a outro.
        """
        for k in range(self.n_vertices):
            for i in range(self.n_vertices):
                for j in range(self.n_vertices):
                    distancia = self.matriz_adjacencias[i][k] + self.matriz_adjacencias[k][j]
                    if self.matriz_adjacencias[i][j] > distancia:
                        self.matriz_adjacencias[i][j] = distancia

    def todos_vertices(self):
        """Retorna todos os vértices do grafo."""
        origens = set(self.arestas.keys())
        destinos = set()
        for origem in origens:
            destinos = destinos.union(set(self.arestas[origem].keys()))

        return list(origens.union(destinos))

    def definir_grafo(self, medianas):
        """Retrona um grafo {vertice: mediana} de acordo com as medianas
        informadas.
        """
        grafo = {}
        for vertice in self.vertices:
            menor_distancia = 50000
            for mediana in medianas:
                if not vertice in medianas:
                    distancia_vertice_mediana = self.matriz_adjacencias[vertice-1][mediana-1]
                    if distancia_vertice_mediana < menor_distancia:
                        grafo[vertice] = mediana
                        menor_distancia = distancia_vertice_mediana
        return grafo

    def distancia_total(self, grafo):
        """Retorna a distancia total entre os vertices e duas medianas"""
        soma = 0
        for vertice, mediana in grafo.items():
            soma += self.matriz_adjacencias[vertice-1][mediana-1]
        return soma

    def solucao_contrutiva(self):
        """Cria uma solução aleatória válida para o problema."""
        medianas = []
        # Define aleatóriamente as medianas.
        while len(medianas) != self.n_medianas:
            vertice = choice(self.vertices)
            if not vertice in medianas:
                medianas.append(vertice)
        grafo = self.definir_grafo(medianas)
        distancia = self.distancia_total(grafo)
        self.medianas, self.solucao = medianas, distancia

    def busca_local(self, iteracoes):
        """"Meta-heuristica para encontrar a solução ótima."""
        for i in range(iteracoes):
            velha_mediana = choice(self.medianas)
            nova_mediana = choice(list(set(self.vertices).difference(set(self.medianas))))
            medianas = list(set(self.medianas).difference(set([velha_mediana])).union(set([nova_mediana])))
            grafo = self.definir_grafo(medianas)
            distancia = self.distancia_total(grafo)
            if distancia < self.solucao:
                self.medianas = medianas
                self.solucao = distancia

    def busca_tabu(self, iteracoes):
        """"Meta-heuristica para encontrar a solução ótima."""
        ultimos_movimentos = ['x', 'x', 'x', 'x', 'x'] # irrelevante. nunca acontece do movimento estar nessa lista.
        frequencias = {}
        for i in range(iteracoes):
            velha_mediana = choice(self.medianas)
            nova_mediana = choice(list(set(self.vertices).difference(set(self.medianas))))
            movimento = "%s,%s" % (velha_mediana, nova_mediana)
            frequencia = frequencias.get(movimento)

            if frequencia == None:
                frequencias[movimento] = 0

            if (frequencia < 2) and not (movimento in ultimos_movimentos):
                medianas = list(set(self.medianas).difference(set([velha_mediana])).union(set([nova_mediana])))
                grafo = self.definir_grafo(medianas)
                distancia = self.distancia_total(grafo)
                if distancia < self.solucao:
                    self.medianas = medianas
                    self.solucao = distancia
                ultimos_movimentos.pop(0)
                ultimos_movimentos.append(movimento)
            frequencias[movimento] += 1


if __name__ == '__main__':
    inicio=time()
    p = PMediana('pmed1.txt')
    fim=time()
    tempo = fim - inicio
    print "Rodar o floyd\t\t tempo: %s" % tempo


    inicio=time()
    p.solucao_contrutiva()
    p.busca_local(1000)
    fim=time()
    tempo = fim - inicio
    print "busca local: %s\t tempo: %s" % (p.solucao, tempo)

    inicio=time()
    p.solucao_contrutiva()
    p.busca_tabu(1000)
    fim=time()
    tempo = fim - inicio
    print "busca tabu: %s\t tempo: %s" % (p.solucao, tempo)


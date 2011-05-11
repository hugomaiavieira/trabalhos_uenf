from random import randrange

def sequencia_aleatoria(n):
    lista = []
    for i in range(n):
        lista.append(randrange(100))
    return lista

def probabilidade(lista):
    probabilidades = []
    for i in range(len(lista)):
        probabilidades.append(1/float(i+1))
    return probabilidades

def sequencia_descrecente(sequencia):
    for i in range(len(sequencia)):
        if sequencia[i] < sequencia[i+1]: return False
    return True


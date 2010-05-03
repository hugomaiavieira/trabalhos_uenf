from sys import argv

class Malhas(object):

    def __init__(arquivo):
        pass

def ler_dados(arquivo):
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


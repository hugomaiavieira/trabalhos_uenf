# coding: utf-8

import sys

class LZW:

    def __init__(self):
        self.proximo_codigo = 0
        self.dicionario = {}
        # Inicia o dicionário com os 256 caracteres ASCII possíveis
        for i in range(256):
            self.add_ao_dicionario(chr(i))

    def add_ao_dicionario(self, str):
        self.dicionario[str] = self.proximo_codigo
        self.proximo_codigo = self.proximo_codigo + 1

    def encode(self, str):
        saida = []
        buffer = ''
        for char in str:
            # enquanto a cadeia atual existir no dicionário, continuamos acresncentando caracteres a ela
            if self.dicionario.has_key(buffer + char):
                buffer += char
            else:
                # ao encontrar a maior cadeia presente é emitido o código dessa
                # cadeia e é criada uma nova cadeia, acrescentando o último
                # caractere lido.
                codigo = self.dicionario[buffer]
                self.add_ao_dicionario(buffer + char)
                buffer = char
                saida.append(codigo)
        if buffer:
            saida.append(self.dicionario[buffer])
        return saida


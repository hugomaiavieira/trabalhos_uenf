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
            if self.dicionario.has_key(buffer + char):
                buffer += char
            else:
                codigo = self.dicionario[buffer]
                self.add_ao_dicionario(buffer + char)
                print "%s - %s" % (buffer + char, self.dicionario[buffer + char])
                saida.append([buffer, codigo])
                buffer = char
        if buffer:
            saida.append([buffer, self.dicionario[buffer]])
        return saida


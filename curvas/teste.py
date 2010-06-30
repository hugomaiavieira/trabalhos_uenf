# -*- coding: UTF-8 -*-
# Autor: Hugo Henriques Maia Vieira

import unittest

from curvas import Curva
from numpy import array, allclose

X=0
Y=1

class TesteCurvas(unittest.TestCase):

    def teste_adicionar_ponto(self):
        curva = Curva()
        ponto = array([2,2])
        curva.adicionar_ponto(ponto)
        self.assertEqual(len(curva.pontos), 1)
        self.assertTrue(allclose(curva.pontos[0], ponto))

    def teste_limpar(self):
        curva = Curva([array([2, 2]), array([5, 2])])
        curva.limpar()
        self.assertEqual(curva.pontos, [])
        self.assertEqual(curva.pontos_da_curva, [])

if __name__ == "__main__":
    unittest.main()


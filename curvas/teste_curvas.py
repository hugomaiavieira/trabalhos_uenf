# -*- coding: UTF-8 -*-
# Autor: Hugo Henriques Maia Vieira
# Licença: creative commons by-nc-sa

import unittest

from curvas import Curva, Hermite, Erro
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


class TesteHermite(unittest.TestCase):

    def teste_adicionar_ponto(self):
        curva = Hermite()
        ponto = array([7,9])
        curva.adicionar_ponto(ponto)
        self.assertEqual(len(curva.pontos), 1)
        self.assertTrue(allclose(curva.pontos[0], ponto))

    def teste_calcular_tangentes_iniciais_para_curva_com_2_pontos(self):
        curva = Hermite([array([2, 2]), array([5, 2])])
        curva.calcular_tangentes_iniciais()
        self.assertTrue(allclose(curva.tangentes[0], array([2,102])))
        self.assertTrue(allclose(curva.tangentes[1], array([5,-98])))

    def teste_calcular_pontos_da_curva_para_curva_com_2_pontos(self):
        curva = Hermite([array([2, 2]), array([5, 2])])
        curva.calcular_tangentes_iniciais()
        curva.calcular_pontos_da_curva(passo=0.2)
        self.assertTrue(allclose(array([2,2]), curva.pontos_da_curva[0]))          # t=0
        self.assertTrue(allclose(array([2.408,18.192]), curva.pontos_da_curva[1])) # t=0.2
        self.assertTrue(allclose(array([3.416,25.904]), curva.pontos_da_curva[3])) # t=0.6
        self.assertTrue(allclose(array([5,2]), curva.pontos_da_curva[5]))          # t=1

    def teste_deve_ter_no_minimo_2_pontos_para_calcular_as_tangentes(self):
        curva = Hermite([])
        self.assertRaises(Erro, curva.calcular_tangentes_iniciais)
        curva = Hermite([array([1,2])])
        self.assertRaises(Erro, curva.calcular_tangentes_iniciais)

    def teste_montar_curva(self):
        curva = Hermite([array([2, 2]), array([5, 2])])
        curva.montar_curva(passo=0.2)
        self.assertTrue(allclose(curva.tangentes[0], array([2,102])))
        self.assertTrue(allclose(curva.tangentes[1], array([5,-98])))
        self.assertTrue(allclose(array([2,2]), curva.pontos_da_curva[0]))          # t=0
        self.assertTrue(allclose(array([2.408,18.192]), curva.pontos_da_curva[1])) # t=0.2
        self.assertTrue(allclose(array([3.416,25.904]), curva.pontos_da_curva[3])) # t=0.6
        self.assertTrue(allclose(array([5,2]), curva.pontos_da_curva[5]))          # t=1

    def teste_limpar(self):
        curva = Hermite([array([2, 2]), array([5, 2])])
        curva.montar_curva()
        curva.limpar()
        self.assertEqual(curva.pontos, [])
        self.assertEqual(curva.tangentes, [])
        self.assertEqual(curva.pontos_da_curva, [])

if __name__ == "__main__":
    unittest.main()


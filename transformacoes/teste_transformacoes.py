# Autor: Hugo Henriques Maia Vieira
# Licença: creative commons by-nc-sa

# coding: UTF-8

import unittest
from transformacoes import Objeto

from numpy import array
from numpy import allclose

X = 0
Y = 1

class TesteTransformacoes(unittest.TestCase):

    def setUp(self):
        self.objeto = Objeto([array([2, 2]), array([4, 4]), array([3, 6])])

    def teste_vertices(self):
        self.assertEqual(self.objeto.vertices.__len__(),3)
        self.assertTrue(allclose(self.objeto.vertices[0], array([2, 2])))
        self.assertFalse(allclose(self.objeto.vertices[1], array([2, 2])))

    def teste_centro_inteiro(self):
        self.assertTrue(allclose(self.objeto.centro(), array([3,4])))

    def teste_centro_real(self):
        self.objeto.vertices.append(array([6,9]))
        self.assertTrue(allclose(self.objeto.centro(), array([3.75,5.25])))

    def teste_centro_objeto_sem_vertices(self):
        objeto = Objeto()
        self.assertEqual(objeto.centro(), None)

    def teste_trasladar(self):
        self.objeto.transladar(0,0)
        self.assertTrue(allclose(self.objeto.vertices[0], array([-1, -2])))
        self.assertTrue(allclose(self.objeto.vertices[1], array([1, 0])))
        self.assertTrue(allclose(self.objeto.vertices[2], array([0, 2])))

    def teste_proporcao_fixa_vertice_ponto_para_aumentar(self):
        ponto = array([1,1])
        vertice_redimencao = self.objeto.vertices[0]
        proporcao = self.objeto.proporcao_fixa_vertice_ponto(vertice_redimencao, ponto)
        self.assertEqual(proporcao, 1.6124515496597098)

    def teste_proporcao_fixa_vertice_ponto_para_diminuir(self):
        ponto = array([2.5,3])
        vertice_redimencao = self.objeto.vertices[0]
        proporcao = self.objeto.proporcao_fixa_vertice_ponto(vertice_redimencao, ponto)
        self.assertEqual(proporcao, 0.5)

    def teste_redimensionar(self):
        self.objeto.redimensionar(1.6124515496597098)
        self.assertTrue(allclose(self.objeto.vertices[0], array([1.38754845, 0.7750969])))
        self.assertTrue(allclose(self.objeto.vertices[1], array([4.61245155, 4.0])))
        self.assertTrue(allclose(self.objeto.vertices[2], array([3.0, 7.2249031])))

    def teste_angulo_vertice_ponto(self):
        self.objeto = Objeto([array([1,0])])
        ponto = array([0,1])
        self.assertAlmostEqual(self.objeto.angulo_vertice_ponto(self.objeto.vertices[0],ponto), 1.5707963267948966)
        ponto = array([1,1])
        self.assertAlmostEqual(self.objeto.angulo_vertice_ponto(self.objeto.vertices[0],ponto), 0.78539816339744828)

    def teste_rotacionar(self):
        self.objeto.rotacionar(0.52359877559829882)
        self.assertAlmostEqual(self.objeto.vertices[0][X], 3.13, 2)
        self.assertAlmostEqual(self.objeto.vertices[0][Y], 1.77, 2)
        self.assertAlmostEqual(self.objeto.vertices[1][X], 3.87, 2)
        self.assertAlmostEqual(self.objeto.vertices[1][Y], 4.5)
        self.assertAlmostEqual(self.objeto.vertices[2][X], 2.0)
        self.assertAlmostEqual(self.objeto.vertices[2][Y], 5.73, 2)

    def teste_refletir_horizontal(self):
        self.objeto.refletir("x")
        self.assertTrue(allclose(self.objeto.vertices[0], array([2, -2])))
        self.assertTrue(allclose(self.objeto.vertices[1], array([4, -4])))
        self.assertTrue(allclose(self.objeto.vertices[2], array([3, -6])))

    def teste_refletir_vertical(self):
        self.objeto.refletir("vertical")
        self.assertTrue(allclose(self.objeto.vertices[0], array([-2, 2])))
        self.assertTrue(allclose(self.objeto.vertices[1], array([-4, 4])))
        self.assertTrue(allclose(self.objeto.vertices[2], array([-3, 6])))

    def teste_refletir_origem(self):
        self.objeto.refletir("origem")
        self.assertTrue(allclose(self.objeto.vertices[0], array([-2, -2])))
        self.assertTrue(allclose(self.objeto.vertices[1], array([-4, -4])))
        self.assertTrue(allclose(self.objeto.vertices[2], array([-3, -6])))

    def teste_vertice_proximo(self):
        self.objeto = Objeto([array([20, 20]), array([40, 40]), array([30, 60])])
        self.assertEqual(self.objeto.vertice_proximo(23,22), 0)
        self.assertEqual(self.objeto.vertice_proximo(37,38), 1)
        self.assertEqual(self.objeto.vertice_proximo(44,44), None)

#    def teste_cisalhar(slef):
#        self.objeto.cisalhar(5)
#        self.assertTrue(self.objeto.vertice([]))

if __name__ == "__main__":
    unittest.main()


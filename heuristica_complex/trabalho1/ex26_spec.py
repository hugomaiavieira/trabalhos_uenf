import unittest
from should_dsl import *
from ex_26 import *

class Ex26Spec(unittest.TestCase):

    def deve_retornar_uma_sequencia_aleatoria_de_n_elementos(self):
        sequencia = sequencia_aleatoria(8)
#        sequencia(8) |should| be_kind_of('list')
        sequencia |should| have(8).elementos

        sequencia = sequencia_aleatoria(50)
#        sequencia(50) |should| be_kind_of('list')
        sequencia |should| have(50).elementos


    def deve_verificar_que_a_probabilidade_de_ai_ser_maior_que_todos_os_seus_predecessores_na_sequencia(self):
        lista = sequencia_aleatoria(10)
#        True |should| be(False)


    def deve_verificar_se_as_probabilidades_vao_sempre_diminuindo(self):
        sequencia = sequencia_aleatoria(10)
        sequencia_descrecente(sequencia) |should| equal_to(True)

        sequencia = sequencia_aleatoria(50)
        sequencia_descrecente(sequencia) |should| equal_to(True)

        sequencia_descrecente([0.9, 0.8, 0.6, 1]) |should| equal_to(False)


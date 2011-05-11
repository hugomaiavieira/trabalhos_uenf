import unittest
from should_dsl import *

from ex_25 import *

class Ex25Spec(unittest.TestCase):

    def deve_calcular_a_potencia_de_um_dado_numero(self):
        dois_elevado_a(0) |should| equal_to(1)
        dois_elevado_a(1) |should| equal_to(2)
        dois_elevado_a(2) |should| equal_to(4)
        dois_elevado_a(4) |should| equal_to(16)
        dois_elevado_a(5) |should| equal_to(32)

    def deve_calcular_a_multiplicacao_entre_dois_numeros(self):
        multiplicar(0,4) |should| equal_to(0)
        multiplicar(3,5) |should| equal_to(15)
        multiplicar(9,2) |should| equal_to(18)

    def deve_calcular_o_somatorio_sem_usar_multipica(self):
        horner_bitwise([9,6,2,1,3], 2) |should| equal_to(897)


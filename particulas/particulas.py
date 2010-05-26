class Particula(object):
    def __init__(self, massa=0, posicao=[0,0,0], velocidade=[0,0,0], forca_sofrida=[0,0,0]):
        self.massa = massa
        self.posicao = posicao
        self.velocidade = velocidade
        self.forca_sofrida = forca_sofrida


class SistemaParticulas(object):
    def __init__(self, particulas=[], t0=0, delta_t=0, gravidade=0):
        self.particulas = particulas
        self.t0 = t0
        self.delta_t = delta_t
        self.gravidade = gravidades


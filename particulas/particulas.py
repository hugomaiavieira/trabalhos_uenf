from re import match

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
        self.gravidade = gravidade

    def ler_dados(self, _arquivo):
        arquivo = open(_arquivo)
        linha = arquivo.readline()
        while linha:
            if match(r'#dados_gerais', linha):
                linha = arquivo.readline()
                while not match(r'^#', linha):
                    g = match(r'^[Gg]ravidade (?P<gravidade>[-]?[0-9]+([.][0-9]+)?)', linha)
                    t = match(r'^[Dd]delta[ _]t (?P<delta_t>[0-9]+([.][0-9]+)?)', linha)
                    if g: self.gravidade = float(g.groupdict()['gravidade'])
                    if t: self.delta_t = float(t.groupdict()['delta_t'])
                    linha = arquivo.readline()
            if match(r'#particula', linha):
                particula = Particula()
                linha = arquivo.readline()
                while not match(r'^#', linha):
                    m = match(r'^[Mm]assa (?P<massa>[0-9]+([.][0-9]+)?)', linha)
                    p = match(r'^[Pp]osicao (?P<x>[0-9]+([.][0-9]+)?) (?P<y>[0-9]+([.][0-9]+)?) (?P<z>[0-9]+([.][0-9]+)?)', linha)
                    v = match(r'^[Vv]elociadae (?P<x>[0-9]+([.][0-9]+)?) (?P<y>[0-9]+([.][0-9]+)?) (?P<z>[0-9]+([.][0-9]+)?)', linha)
                    f = match(r'^[Ff]orca[ _]sofrida (?P<x>[0-9]+([.][0-9]+)?) (?P<y>[0-9]+([.][0-9]+)?) (?P<z>[0-9]+([.][0-9]+)?)', linha)
                    if m: particula.massa = float(m.groupdict()['massa'])
                    if p: particula.posicao = [float(p.groupdict()['x']), float(p.groupdict()['y']), float(p.groupdict()['z'])]
                    if v: particula.velocidade = [float(v.groupdict()['x']), float(v.groupdict()['y']), float(v.groupdict()['z'])]
                    if f: particula.forca_sofrida = [float(f.groupdict()['x']), float(f.groupdict()['y']), float(f.groupdict()['z'])]
                    linha = arquivo.readline()
                self.particulas.append(particula)


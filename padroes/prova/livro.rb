#encoding: utf-8
class Livro

  attr_reader :titulo, :fila_reserva, :tipo

  def initialize tipo, titulo
    @fila_reserva = []
    @tipo = tipo
    @titulo = titulo
  end

  def calcular_suspensao dias_emprestado
    dias = dias_emprestado - self.dias_de_emprestimo
    dias > 0 ? self.dias_de_suspensao * dias : 0
  end

  def dias_de_suspensao
    { :comum => 3, :disponibilidade_limitada => 5, :periodico => 7 }[self.tipo]
  end

  def dias_de_emprestimo
    { :comum => 7, :disponibilidade_limitada => 3, :periodico => 1 }[self.tipo]
  end

  def add_interessados interessado
    self.fila_reserva << interessado unless self.fila_reserva.include? interessado
  end

  def remover_interessados interessado
    self.fila_reserva.delete(interessado)
  end

  def informar_disponibilidade
    self.fila_reserva.each_with_index do |interessado, posicao|
      interessado.atualizar(self.titulo, posicao+1)
    end
  end

end


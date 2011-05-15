#encoding: utf-8
class Usuario

  attr_reader :biblioteca, :nome
  attr_accessor :dias_de_suspensao

  def initialize nome, biblioteca
    @nome = nome
    @biblioteca = biblioteca
    @dias_de_suspensao = 0
  end

  def pegar_livro livro
    biblioteca.pegar_livro livro
  end

  def devolver_livro livro, dias_emprestado
    dias_de_suspensao = biblioteca.devolver_livro livro, dias_emprestado
  end

  def reservar_livro livro
    biblioteca.reservar_livro livro, self
  end

  def atualizar livro, posicao
    puts "#{nome}: Oba! Alguém entregou o #{livro}! Sou o #{posicao}º da fila."
  end

end


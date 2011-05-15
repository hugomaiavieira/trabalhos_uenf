#encoding: utf-8
class Biblioteca

  attr_reader :livros_emprestados

  def initialize livros
    @livros = livros
    @livros_emprestados = []
    @livros_reservados = []
  end

  def pegar_livro livro
    unless self.livros_emprestados.include? livro
      self.livros_emprestados << livro
      puts "Você pegou o item #{livro.titulo}. Pode ficar #{livro.dias_de_emprestimo} dia com ele."
    else
      puts "#{livro.titulo} está emprestado. Se quiser, pode fazer uma reservá-lo."
    end
  end

  def devolver_livro livro, dias_emprestado
    if self.livros_emprestados.include? livro
      self.livros_emprestados.delete(livro)
      livro.informar_disponibilidade
      dias_de_suspensao = livro.calcular_suspensao(dias_emprestado)
      if dias_de_suspensao > 0
        puts "Se deu mal jovem! Está suspenso por #{dias_de_suspensao} dias."
      end
      puts "Entregou o livro na moral, sem suspensão =)"
      return dias_de_suspensao
    end
  end

  def reservar_livro livro, interessado
    if self.livros_emprestados.include? livro
      livro.add_interessados interessado
    else
      puts "#{livro.titulo} está disponível meu jovem. Pode pegá-lo emprestado."
    end
  end

end


require './biblioteca.rb'
require './livro.rb'
require './usuario.rb'

linux = Livro.new(:periodico, 'Linux magazine')
ruby = Livro.new(:comum, 'Ruby metaprogramming')
padroes = Livro.new(:disponibilidade_limitada, 'GOF Design Patterns')
livros = [linux, ruby, padroes]

biblioteca = Biblioteca.new livros

hugo = Usuario.new 'Hugo', biblioteca
rodrigo = Usuario.new 'Rodrigo', biblioteca
dudu = Usuario.new 'Dudu', biblioteca

hugo.pegar_livro linux
rodrigo.pegar_livro linux
rodrigo.reservar_livro linux

hugo.devolver_livro linux, 5
rodrigo.pegar_livro linux
hugo.pegar_livro linux

hugo.pegar_livro ruby
rodrigo.reservar_livro ruby
dudu.reservar_livro ruby

hugo.devolver_livro ruby, 5


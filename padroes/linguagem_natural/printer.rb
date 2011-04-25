class Printer

  def printObject attribute, klass
    object = eval(klass.capitalize).new
    puts "#{klass} - #{attribute}: #{object.send(attribute)}"
  end

end


class Cliente
  attr_accessor :nome

  def initialize
    @nome = "Ronaldo"
  end
end


class Pessoa
  attr_accessor :telefone

  def initialize
    @telefone = "2722-3196"
  end
end


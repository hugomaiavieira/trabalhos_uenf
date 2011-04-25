require './interpreter.rb'
require './printer.rb'

puts "\nXML"
puts '-' * 80
xml = Interpreter.new './data/exemplo.xml'
xml.execute
puts '=' * 80

puts "\nHTML"
puts '-' * 80
xml = Interpreter.new './data/exemplo.html'
xml.execute
puts '=' * 80

puts "\nTEXT"
puts '-' * 80
xml = Interpreter.new './data/exemplo.txt'
xml.execute
puts '=' * 80

puts "\nOTHER TEXT"
puts '-' * 80
xml = Interpreter.new './data/exemplo.txt'
xml.execute
puts '=' * 80


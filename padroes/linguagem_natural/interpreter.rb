module Executor
  attr_accessor :document

  def initialize doc
    @document = doc
  end

  def execute
    lines = document.readlines
    lines.each do |line|
      elements = parse_line(line)
      if elements
        object = eval(elements[:class]).new
        object.send(elements[:method], *elements[:params])
      end
    end
    nil
  end

  def parse_line line
    raise NotImplementedError
  end
end

class XmlExecutor
  include Executor

  def parse_line line
    if line =~ /<command run="(.*)">(.*?)<\/command>/
      klass, method = $1.split('#')
      params = $2.scan(/\((.*?)\)/).flatten
      return nil if klass == nil or method == nil
      return { :class => klass, :method => method, :params => params}
    end
  end
end

class HtmlExecutor
  include Executor

  def parse_line line
    if line =~ /<span command="(.*)">(.*?)<\/span>/
      klass, method = $1.split('#')
      params = $2.scan(/\((.*?)\)/).flatten
      return nil if klass == nil or method == nil
      return { :class => klass, :method => method, :params => params}
    end
  end
end

class TextExecutor
  include Executor

  def parse_line line
    if line =~ /\/\/.*([A-Z]\w*#[a-z]\w*)$/
      klass, method = $1.split('#')
      params = line.scan(/\((.*?)\)/).flatten
      return nil if klass == nil or method == nil
      return { :class => klass, :method => method, :params => params}
    end
  end
end

class Interpreter
  attr_reader :executor

  def initialize doc
    doc = open(doc)
    extent = File.extname(doc.path)
    case extent
      when '.xml'
        @executor = XmlExecutor.new(doc)
      when '.html'
        @executor = HtmlExecutor.new(doc)
    else
      @executor = TextExecutor.new(doc)
    end
  end

  def execute
    executor.execute
  end
end


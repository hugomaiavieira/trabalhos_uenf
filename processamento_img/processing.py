# encoding: utf-8

from PIL import Image

R, G, B = (0, 1, 2)

class ImageProcessor(object):

    def __init__(self, imagem):
        self.imagem = Image.open(imagem)

    def grayScale(self):
        width, height = self.imagem.size
        pixels = self.imagem.load()
        for x in range(width):
            for y in range(height):
                pixel = pixels[x,y]
                cinza = (pixel[R] + pixel[G] + pixel[B]) / 3
                pixels[x,y] = (cinza, cinza, cinza)
        return self.imagem

    def binarize(self, limiar):
        width, height = self.imagem.size
        pixels = self.imagem.load()
        for x in range(width):
            for y in range(height):
                pixel = pixels[x,y]
                canal = ( pixel[R] + pixel[G] + pixel[B] ) / 3
                if canal < limiar:
                    pixels[x,y] = (0, 0, 0) # Preto
                else:
                    pixels[x,y] = (255, 255, 255) # Branco
        return self.imagem

    def scale(self, new_width, new_height):
        nova = Image.new('RGB', (new_width, new_height))
        width, height = self.imagem.size
        proporcao_x = width / float(new_width)
        proporcao_y = height / float(new_height)
        pixels_original = self.imagem.load()
        pixels_nova = nova.load()
        for x in range(new_width):
            for y in range(new_height):
                valor = pixels_original[x * proporcao_x, y * proporcao_y]
                pixels_nova[x, y] = valor
        return nova


processor = ImageProcessor('lena.jpg')
processor.grayScale()
#processor.binarize(100)
processor.imagem.show()
#imagem_scale = processor.scale(150, 150)
#imagem_scale = processor.scale(600, 600)
#imagem_scale.show()


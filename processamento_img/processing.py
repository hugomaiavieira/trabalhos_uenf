# encoding: utf-8

from PIL import Image

R, G, B = (0, 1, 2)

SOBEL_X = [[-1,0,1],
           [-2,0,2],
           [-1,0,1]]

SOBEL_Y = [[-1,-2,-1],
           [0,0,0],
           [1,2,1]]

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

    def sobel_filter(self):
          from functions import no_zero_range
          width, height = self.imagem.size
          nova = Image.new('RGB', (width, height))
          self.grayScale()
          pixels_original = self.imagem.load()
          pixels_nova = nova.load()
          for x in no_zero_range(width-2):
            for y in no_zero_range(height-2):
              pixel_x = (SOBEL_X[0][0] * pixels_original[x-1,y-1][R]) + (SOBEL_X[0][1] * pixels_original[x,y-1][R]) + (SOBEL_X[0][2] * pixels_original[x+1,y-1][R]) + \
                        (SOBEL_X[1][0] * pixels_original[x-1,y][R])   + (SOBEL_X[1][1] * pixels_original[x,y][R])   + (SOBEL_X[1][2] * pixels_original[x+1,y][R]) + \
                        (SOBEL_X[2][0] * pixels_original[x-1,y+1][R]) + (SOBEL_X[2][1] * pixels_original[x,y+1][R]) + (SOBEL_X[2][2] * pixels_original[x+1,y+1][R])

              pixel_y = (SOBEL_Y[0][0] * pixels_original[x-1,y-1][R]) + (SOBEL_Y[0][1] * pixels_original[x,y-1][R]) + (SOBEL_Y[0][2] * pixels_original[x+1,y-1][R]) + \
                        (SOBEL_Y[1][0] * pixels_original[x-1,y][R])   + (SOBEL_Y[1][1] * pixels_original[x,y][R])   + (SOBEL_Y[1][2] * pixels_original[x+1,y][R]) + \
                        (SOBEL_Y[2][0] * pixels_original[x-1,y+1][R]) + (SOBEL_Y[2][1] * pixels_original[x,y+1][R]) + (SOBEL_Y[2][2] * pixels_original[x+1,y+1][R])
              soma = abs(pixel_x) + abs(pixel_y)
              if soma > 255: soma = 255
              pixels_nova[x,y] = (soma, soma, soma)
          return nova

processor = ImageProcessor('lena.jpg')
#processor.grayScale()
#processor.binarize(100)
#processor.imagem.show()
#imagem_scale = processor.scale(150, 150)
#imagem_scale = processor.scale(600, 600)
#imagem_scale.show()
imagem_sobel = processor.sobel_filter()
imagem_sobel.show()


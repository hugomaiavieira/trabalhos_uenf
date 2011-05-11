def horner_bitwise(lista, k):
    resultado = 0
    for i in range(0, len(lista)):
        ki = multiplicar(k, i)
        resultado += multiplicar(dois_elevado_a(ki), lista[i])
    return resultado

def multiplicar(num1, num2):
    resultado = 0
    maior, menor = (num1, num2) if num1 >= num2 else (num2, num1)
    for i in range(menor):
        resultado += maior
    return resultado

def dois_elevado_a(n):
    return 1 << n


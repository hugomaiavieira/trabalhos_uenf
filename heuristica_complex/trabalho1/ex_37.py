#!/usr/bin/python
# coding: utf-8

from time import time
import sys

def fibonacci_nao_recursivo(n, k):
    if 0 <= n < (k - 1):
        return 0
    elif n == k - 1:
        return 1
    else:
        f = range(n+2)
        for i in range(k-1):
            f[i] = 0
        f[k-1]=1
        for i in range(k,n+1):
            soma=0
            for j in range(1,k+1):
                soma += f[i-j]
            f[i] = soma
        return f[n]

def fibonacci_recursivo(n, k):
    if 0 <= n < (k - 1):
        return 0
    elif n == (k - 1):
        return 1
    else: # n >= k
        soma = 0
        for i in range(1,k+1):
          soma += fibonacci_recursivo(n-i, k)
        return soma

if __name__ == "__main__":

    n, k = (int(sys.argv[1]), int(sys.argv[2]))

    print "não recursivo"

    inicio=time()
    fibonacci = fibonacci_nao_recursivo(n, k)
    fim=time()

    tempo = fim - inicio
    print "resultado: %d" % (fibonacci)
    print "tempo: %.20f" % (tempo)

    print "\nrecursivo"

    inicio=time()
    fibonacci = fibonacci_recursivo(n, k)
    fim=time()

    tempo = fim - inicio
    print "resultado: %d" % (fibonacci)
    print "tempo: %.20f" % (tempo)


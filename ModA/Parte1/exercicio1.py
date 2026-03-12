import math
import statistics
import numpy as np
#a)
def multiplosSeis(a):
    for n in range(a, a**2 + 1):
        if n % 6 == 0:
            print(n)
print("Teste multiplosSeis")
multiplosSeis(6)
print("FIM TESTE")

#b)
def mmc(a,b):
    print(math.lcm(a, b))

print("Teste mmc")
mmc(2,21)
print("FIM TESTE")

#c)

def primeirosNtermos(u,r,N):
    print(np.arange(u, u + N * r, r))

print("Teste primeirosNtermos")
primeirosNtermos(3,4,10)
print("FIM TESTE")

#d)

def formulaResolvente(a,b,c):
    resultado = np.roots([a,b,c])
    print(f"as raizes sao: {resultado}")

print("Teste formulaResolvente")
formulaResolvente(2,4,-2)
print("FIM TESTE")

#e)

def analiseVetor(v):
    try:
        moda = statistics.mode(v)
    except statistics.StatisticsError:
        moda = "Não existe uma moda única"

    print(f"Vetor: {v}")
    print(f"Mínimo: {np.min(v)}")
    print(f"Máximo: {np.max(v)}")
    print(f"Média:  {np.mean(v)}")
    print(f"Moda:   {moda}")

print("Teste analiseVetor")
analiseVetor([1,2,3,7,12,8])
print("FIM TESTE")

#f)

def elementosComuns(v1,v2):
    print(np.intersect1d(v1,v2))

print("Teste elementosComuns")
elementosComuns([1,2,3,4,5,6],[4,6])
print("FIM TESTE")

#g)

def elementosSemRepeticao(v1,v2):
    print(np.union1d(v1,v2))

print("Teste elementosSemRepeticao")
elementosSemRepeticao([1,2,3,4,5,6],[4,6])
print("FIM TESTE")

#h)











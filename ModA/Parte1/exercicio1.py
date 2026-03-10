import math
import statistics
#a)
def multiplosSeis(a):
    for n in range(a, a**2 + 1):
        if n % 6 == 0:
            print(n)

#b)
def mmc(a,b):
    print(math.lcm(a, b))

#c)

def primeirosNtermos(u,r,N):
    for n in range(0, N):
        print(u + n * r)

#d)

def formulaResolvente(a,b,c):
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Não existem raízes reais.")
    else:
        x = (-b + math.sqrt(delta)) / (2 * a)
        y = (-b - math.sqrt(delta)) / (2 * a)
        print(f"As raízes são: {x} e {y}")

#e)

def analiseVetor(v):
    v_min = min(v)
    v_max = max(v)

    media = statistics.mean(v)
    
    try:
        moda = statistics.mode(v)
    except statistics.StatisticsError:
        moda = "Não existe uma moda única"

    print(f"Vetor: {v}")
    print(f"Mínimo: {v_min}")
    print(f"Máximo: {v_max}")
    print(f"Média:  {media}")
    print(f"Moda:   {moda}")


import math
import statistics
import numpy as np
import matplotlib.pyplot as plt

# a) 
def multiplosSeis(a):
    for n in range(a, a**2 + 1):
        if n % 6 == 0:
            print(n)

# b)
def mmc(a, b):
    print(math.lcm(a, b))

# c) 
def primeirosNtermos(u, r, N):
    print(np.arange(u, u + N * r, r))

# d) 
def formulaResolvente(a, b, c):
    resultado = np.roots([a, b, c])
    print(f"As raizes sao: {resultado}")

# e)
def analiseVetor(v):
    try:
        moda = statistics.mode(v)
    except statistics.StatisticsError:
        moda = "Não existe uma moda única"
    print(f"Vetor: {v}")
    print(f"Mínimo: {np.min(v)} | Máximo: {np.max(v)}")
    print(f"Média: {np.mean(v)} | Moda: {moda}")

# f)
def elementosComuns(v1, v2):
    print(np.intersect1d(v1, v2))

# g)
def elementosSemRepeticao(v1, v2):
    print(np.union1d(v1, v2))

# h)
def inverter_ficheiro(nome_in, nome_out):
    with open(nome_in, 'r', encoding='utf-8') as f:
        conteudo = f.read()
    with open(nome_out, 'w', encoding='utf-8') as f:
        f.write(conteudo[::-1])
    print(f"Ficheiro '{nome_in}' invertido para '{nome_out}'.")
    analisar_e_apresentar(nome_in)
    analisar_e_apresentar(nome_out)

# i)
def analisar_e_apresentar(nome_ficheiro):
    with open(nome_ficheiro, 'r', encoding='utf-8') as f:
        texto = f.read()
    if not texto:
        return None
    
    dados = np.array(list(texto))
    simbolos, contagens = np.unique(dados, return_counts=True)
    idx_max = np.argmax(contagens)
    
    probs = contagens / len(dados)
    entropia = -np.sum(probs * np.log2(probs))
    
    print(f"Análise ao {nome_ficheiro}")
    print(f"Símbolo mais frequente: '{simbolos[idx_max]}'")
    print(f"Entropia: {entropia:.4f} bits/símbolo")
    return simbolos, contagens, entropia

# j)
def mostrar_histograma(nome_ficheiro):
    res = analisar_e_apresentar(nome_ficheiro)
    if res:
        simbolos, contagens, entropia = res
        plt.bar(simbolos, contagens)
        plt.title(f"Histograma - {nome_ficheiro}")
        plt.show()
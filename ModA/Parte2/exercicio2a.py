import random
import math
import collections
import os

def fonte_simbolos(N, alfabeto, probabilidades):
    if len(alfabeto) != len(probabilidades):
        print("O alfabeto e as probabilidades devem ter o mesmo tamanho.")
        return
    if not math.isclose(sum(probabilidades), 1.0, rel_tol=1e-5):
        print("A soma das probabilidades deve ser igual a 1.")
        return
       
    return random.choices(alfabeto, weights=probabilidades, k=N)

def teste_alínea_a():
    alfabeto = ['A', 'B', 'C']
    probabilidades = [0.7, 0.2, 0.1]
    N = 10000
   
    sequencia = fonte_simbolos(N, alfabeto, probabilidades)
    contagem = collections.Counter(sequencia)
   
    for simbolo in alfabeto:
        freq_relativa = contagem[simbolo] / N
        print(f"Símbolo {simbolo}: Prob. Teórica = {probabilidades[alfabeto.index(simbolo)]:.2f} | Freq. Prática = {freq_relativa:.4f}")
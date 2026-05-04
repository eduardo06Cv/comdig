import math
import collections
import matplotlib.pyplot as plt
import os



def analisar_fonte(caminho_ficheiro):
    print(f"ficheiro: {os.path.basename(caminho_ficheiro)}")
   
    try:
        with open(caminho_ficheiro, 'rb') as f:
            dados = f.read()
    except FileNotFoundError:
        print("Erro: Ficheiro não encontrado.")
        return

    total_simbolos = len(dados)
    if total_simbolos == 0:
        print("O ficheiro está vazio.")
        return

    frequencias = collections.Counter(dados)

    simbolo_mais_frequente, contagem_maxima = frequencias.most_common(1)[0]
    probabilidade_max = contagem_maxima / total_simbolos
   
    informacao_propria = -math.log2(probabilidade_max)

    print(f"Total de símbolos: {total_simbolos}")
    print(f"Símbolo mais frequente: {simbolo_mais_frequente} (Em texto: '{chr(simbolo_mais_frequente) if 32 <= simbolo_mais_frequente <= 126 else 'N/A'}')")
    print(f"Probabilidade: {probabilidade_max:.6f}")
    print(f"Informação própria: {informacao_propria:.4f} bits")

    entropia = 0
    for simbolo, contagem in frequencias.items():
        probabilidade = contagem / total_simbolos
        entropia -= probabilidade * math.log2(probabilidade)

    print(f"Entropia da fonte: {entropia:.4f} bits/símbolo\n")

    simbolos = list(frequencias.keys())
    contagens = list(frequencias.values())

    plt.figure(figsize=(10, 6))
    plt.bar(simbolos, contagens, width=1.0, color='steelblue')
    plt.title(f"Histograma de Símbolos - {os.path.basename(caminho_ficheiro)}")
    plt.xlabel("Valor do Símbolo / Byte (0 a 255)")
    plt.ylabel("Frequência Absoluta")
    plt.xlim([-1, 256])
    plt.grid(axis='y', alpha=0.5)
    plt.show()


def analisar_ficheiro(pasta_testes):
    for nome_ficheiro in os.listdir(pasta_testes):
        caminho = os.path.join(pasta_testes, nome_ficheiro) 
        if os.path.isfile(caminho): analisar_fonte(caminho)
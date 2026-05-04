import math
import collections
import matplotlib.pyplot as plt
import os
from exercicio3a import *

def gerar_grafico_entropia_compressao(pasta_testes):
    entropias = []
    bits_por_byte_lista = []
    nomes = []

    for nome_ficheiro in os.listdir(pasta_testes):
        caminho_completo = os.path.join(pasta_testes, nome_ficheiro)
        if os.path.isfile(caminho_completo):
            resultado = analisar_compressao(caminho_completo)
            if resultado:
                ent, bpb = resultado
                entropias.append(ent)
                bits_por_byte_lista.append(bpb)
                nomes.append(nome_ficheiro)

    plt.figure(figsize=(10, 6))
    plt.scatter(entropias, bits_por_byte_lista, color='darkorange', edgecolors='black', s=80, zorder=3)
   
    x_vals = [0, 8]
    plt.plot(x_vals, x_vals, 'k--', alpha=0.5, label='Limite Teórico Ideal ($y = x$)', zorder=2)

    for i, txt in enumerate(nomes):
        plt.annotate(txt, (entropias[i], bits_por_byte_lista[i]), fontsize=8, xytext=(5, 5), textcoords='offset points')

    plt.title("Relação entre Entropia do Ficheiro e Compressão Obtida")
    plt.xlabel("Entropia ($H$) do ficheiro original (bits/símbolo)")
    plt.ylabel("Compressão obtida (bits / byte original)")
    plt.xlim([0, 8.5])
    plt.ylim([0, 10])
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.show()
import os
import time
import math
import collections
import zipfile
import filecmp
import matplotlib.pyplot as plt

def calcular_entropia(dados):
    if not dados:
        return 0
    total = len(dados)
    frequencias = collections.Counter(dados)
    entropia = 0
    for contagem in frequencias.values():
        prob = contagem / total
        entropia -= prob * math.log2(prob)
    return entropia

def analisar_compressao(caminho_ficheiro):
    if not os.path.exists(caminho_ficheiro):
        print(f"Erro: Ficheiro {caminho_ficheiro} não encontrado.")
        return None

    tamanho_original = os.path.getsize(caminho_ficheiro)
    if tamanho_original == 0:
        print(f"O ficheiro {caminho_ficheiro} está vazio.")
        return None

    with open(caminho_ficheiro, 'rb') as f:
        dados = f.read()
   
    entropia = calcular_entropia(dados)

    ficheiro_zip = caminho_ficheiro + ".zip"
    ficheiro_descomprimido = caminho_ficheiro + ".unzipped"

    inicio_comp = time.time()
    with zipfile.ZipFile(ficheiro_zip, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
        zf.write(caminho_ficheiro, arcname=os.path.basename(caminho_ficheiro))
    tempo_comp = time.time() - inicio_comp

    tamanho_comprimido = os.path.getsize(ficheiro_zip)

    inicio_desc = time.time()
    with zipfile.ZipFile(ficheiro_zip, 'r') as zf:
        conteudo = zf.read(os.path.basename(caminho_ficheiro))
        with open(ficheiro_descomprimido, 'wb') as f_out:
            f_out.write(conteudo)
    tempo_desc = time.time() - inicio_desc

    razao_compressao = tamanho_original / tamanho_comprimido
    bits_por_byte = (tamanho_comprimido * 8) / tamanho_original

    sao_iguais = filecmp.cmp(caminho_ficheiro, ficheiro_descomprimido, shallow=False)

    print(f"Ficheiro: {os.path.basename(caminho_ficheiro)}")
    print(f"Entropia: {entropia:.4f} bits/símbolo")
    print(f"Tamanho: {tamanho_original} B -> {tamanho_comprimido} B")
    print(f"Razão de Compressão: {razao_compressao:.2f}:1")
    print(f"Taxa (Bits por Byte): {bits_por_byte:.4f} bits/byte")
    print(f"Tempo Compressão: {tempo_comp:.4f} s | Descompressão: {tempo_desc:.4f} s")
    print(f"Integridade verificada (Original == Descodificado)? {'SIM' if sao_iguais else 'NÃO'}\n")

    os.remove(ficheiro_zip)
    os.remove(ficheiro_descomprimido)

    return entropia, bits_por_byte
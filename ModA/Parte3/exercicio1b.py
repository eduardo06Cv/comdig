import numpy as np
import os
import matplotlib.pyplot as plt
from PIL import Image

imagem_original_path = 'Images/bird.png'
pasta_resultados = 'resultados_exercicio1B'

if not os.path.exists(pasta_resultados):
    os.makedirs(pasta_resultados)

def calcular_mae(img_orig, img_comp):
    arr_orig = np.array(img_orig.convert('L')).astype(float)
    arr_comp = np.array(img_comp.convert('L')).astype(float)
    return np.mean(np.abs(arr_orig - arr_comp))

qualidades = [5, 10, 20, 30, 50, 70, 90]
maes = []
taxas = []

tamanho_orig = os.path.getsize(imagem_original_path)
img_orig = Image.open(imagem_original_path)

print(f"{'Qualidade':<10} | {'Taxa':<10} | {'MAE':<10}")
print("-" * 35)

for q in qualidades:
    nome_saida = os.path.join(pasta_resultados, f'pepper_q{q}.jpg')
    img_orig.save(nome_saida, 'JPEG', quality=q)
    
    tamanho_novo = os.path.getsize(nome_saida)
    taxa = tamanho_orig / tamanho_novo
    taxas.append(taxa)
    
    img_comp = Image.open(nome_saida)
    erro = calcular_mae(img_orig, img_comp)
    maes.append(erro)
    
    print(f"{q:<10} | {taxa:<10.2f} | {erro:<10.2f}")

plt.figure(figsize=(10, 6))
plt.plot(taxas, maes, 'o-b', linewidth=2, markersize=8)
plt.xlabel('Taxa de Compressão (Original / Comprimido)')
plt.ylabel('Erro Absoluto Médio (MAE)')
plt.title('Análise de Perda: Taxa de Compressão vs MAE')
plt.grid(True, linestyle='--', alpha=0.7)

caminho_grafico = os.path.join(pasta_resultados, 'grafico_taxa_mae.png')
plt.savefig(caminho_grafico)
print(f"\nGráfico guardado em: {caminho_grafico}")
plt.show()
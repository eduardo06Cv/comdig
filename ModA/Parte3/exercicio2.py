import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.stats import entropy

imagem_input = 'Images/bird.png' 
pasta_2a = 'resultados_exercicio2A'
pasta_2b = 'resultados_exercicio2B'
coords = (100, 300, 150, 400) 

for pasta in [pasta_2a, pasta_2b]:
    if not os.path.exists(pasta):
        os.makedirs(pasta)

def calcular_entropia(img_array):
    hist, _ = np.histogram(img_array.ravel(), bins=256, range=(0, 256), density=True)
    hist = hist[hist > 0] 
    return -np.sum(hist * np.log2(hist))

print("A executar Exercício 2(a)...")

img_orig = cv2.imread(imagem_input)
if img_orig is None:
    print(f"Erro: Não foi possível encontrar {imagem_input}")
    exit()

img_cifrada = img_orig.copy()
y1, y2, x1, x2 = coords

roi = img_orig[y1:y2, x1:x2]

key = np.random.randint(0, 256, roi.shape, dtype=np.uint8)

roi_cifrada = cv2.bitwise_xor(roi, key)

img_cifrada[y1:y2, x1:x2] = roi_cifrada

cv2.imwrite(os.path.join(pasta_2a, 'original.png'), img_orig)
cv2.imwrite(os.path.join(pasta_2a, 'imagem_cifrada.png'), img_cifrada)
np.save(os.path.join(pasta_2a, 'chave.npy'), key)
cv2.imwrite(os.path.join(pasta_2a, 'visualizacao_chave.png'), key)

print("A executar Exercício 2(b)...")

img_decifrada = img_cifrada.copy()
roi_para_decifrar = img_cifrada[y1:y2, x1:x2]
roi_decifrada = cv2.bitwise_xor(roi_para_decifrar, key)
img_decifrada[y1:y2, x1:x2] = roi_decifrada

mae = np.mean(np.abs(img_orig.astype(float) - img_decifrada.astype(float)))
ent_orig = calcular_entropia(img_orig)
ent_cifr = calcular_entropia(roi_cifrada)

print("-" * 30)
print(f"MAE (Original vs Decifrada): {mae:.2f}")
print(f"Entropia Original: {ent_orig:.4f}")
print(f"Entropia Cifrada (ROI): {ent_cifr:.4f}")
print("-" * 30)

fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].hist(img_orig.ravel(), bins=256, range=(0,256), color='blue', alpha=0.7)
axs[0].set_title('Histograma: Original')

axs[1].hist(roi_cifrada.ravel(), bins=256, range=(0,256), color='red', alpha=0.7)
axs[1].set_title('Histograma: Cifrada (ROI)')

axs[2].hist(img_decifrada.ravel(), bins=256, range=(0,256), color='green', alpha=0.7)
axs[2].set_title('Histograma: Decifrada')

plt.savefig(os.path.join(pasta_2b, 'comparativo_histogramas.png'))
cv2.imwrite(os.path.join(pasta_2b, 'imagem_decifrada.png'), img_decifrada)

print(f"Processo concluído. Verifica as pastas '{pasta_2a}' e '{pasta_2b}'.")
plt.show()
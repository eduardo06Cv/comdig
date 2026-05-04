from PIL import Image
import os

nome_ficheiro = 'Images/bird.png'
pasta_saida = 'resultados_exercicio1A'

if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)
    print(f"Pasta '{pasta_saida}' criada")

try:
    img = Image.open(nome_ficheiro).convert('RGB')
    print(f"Sucesso: A abrir {nome_ficheiro}")

    qualidades = [10, 30, 60, 95]

    for q in qualidades:
        caminho_completo = os.path.join(pasta_saida, f'resultado_q{q}.jpg')
        
        img.save(caminho_completo, 'JPEG', quality=q)
        
        tamanho = os.path.getsize(caminho_completo) / 1024
        print(f"{q:<10} | {tamanho:<15.2f}")

except FileNotFoundError:
    print(f"Erro: Não encontrei o ficheiro '{nome_ficheiro}'.")
    print("Dica: Certifica-te que a imagem está na mesma pasta que este script!")
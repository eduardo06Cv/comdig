from exercicio1a import *
from exercicio2a import *
from exercicio2b import *
from exercicio2c import *
from exercicio3a import *
from exercicio3b import *


print("1(a)")
analisar_ficheiro(r"comdig\ModA\Parte2\TestFilesCD")

print("2(a)")
teste_alínea_a()

print("2(b)(i)")
jogo_dados(20, "dados.txt")

print("2(b)(ii)")
euromilhoes(50, "euromilhoes.txt")

print("2(c)(i)")
gerar_passwords("medio", 1000, "passwords.txt")

print("2(c)(ii)")
gerar_tabela_pessoas(1000, "pessoas.csv")

print("3(a)")
analisar_compressao(r"comdig\ModA\Parte2\TestFilesCD\barries.jpg")
    
print("3(b)")
gerar_grafico_entropia_compressao(r"comdig\ModA\Parte2\TestFilesCD")

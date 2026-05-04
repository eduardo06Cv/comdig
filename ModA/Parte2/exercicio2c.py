import string
from exercicio2a import *

def gerar_passwords(nivel, quantidade, nome_ficheiro):
    letras_min = list(string.ascii_lowercase)
    letras_mai = list(string.ascii_uppercase)
    digitos = list(string.digits)
    especiais = list("!@#$%&*/-+")
   
    if nivel == "baixo":
        alfabeto = letras_min
        tamanho = 6
    elif nivel == "medio":
        alfabeto = letras_min + letras_mai + digitos
        tamanho = 8
    elif nivel == "alto":
        alfabeto = letras_min + letras_mai + digitos + especiais
        tamanho = 12
    else:
        raise Exception("nivel nao conhecido")
       
    prob = [1/len(alfabeto)] * len(alfabeto)
   
    with open(nome_ficheiro, 'w', encoding='utf-8') as f:
        f.write(f"Passwords (Nível: {nivel})\n")
        for _ in range(quantidade):
            pwd = "".join(fonte_simbolos(tamanho, alfabeto, prob))
            f.write(pwd + "\n")

def gerar_tabela_pessoas(quantidade, nome_ficheiro):
    digitos_benford = list(range(1, 10))
    prob_benford = [math.log10(1 + 1/d) for d in digitos_benford]
   
    digitos_normais = list(range(0, 10))
    prob_normais = [1/10] * 10
   
   
    def ler_ficheiro(caminho):
        if os.path.exists(caminho):
            with open(caminho, 'r', encoding='utf-8', errors='replace') as f:
                return [linha.strip() for linha in f if linha.strip()]
        else:
            print(f"Erro: Ficheiro {caminho} não encontrado.")
            raise Exception()

    nomes_p = ler_ficheiro(r"comdig\ModA\Parte2\Nomes.txt")
    apelidos = ler_ficheiro(r"comdig\ModA\Parte2\Apelidos.txt")
    profissoes = ler_ficheiro(r"comdig\ModA\Parte2\Profissoes.txt")
    localidades = ler_ficheiro(r"comdig\ModA\Parte2\Localidades.txt")
   
    with open(nome_ficheiro, 'w', encoding='utf-8') as f:
        f.write("ID,Nome,Localidade,Profissao\n")
        for _ in range(quantidade):
            d1 = str(fonte_simbolos(1, digitos_benford, prob_benford)[0])
            d_resto = "".join(map(str, fonte_simbolos(7, digitos_normais, prob_normais)))
            id_pessoa = d1 + d_resto
           
            nome = fonte_simbolos(1, nomes_p, [1/len(nomes_p)]*len(nomes_p))[0]
            apelido = fonte_simbolos(1, apelidos, [1/len(apelidos)]*len(apelidos))[0]
            nome_completo = f"{nome} {apelido}"
            local = fonte_simbolos(1, localidades, [1/len(localidades)]*len(localidades))[0]
            prof = fonte_simbolos(1, profissoes, [1/len(profissoes)]*len(profissoes))[0]
           
            f.write(f"{id_pessoa},{nome_completo},{local},{prof}\n")
from exercicio2a import *

def extrair_sem_reposicao(alfabeto, probabilidades, k_necessarios):
    resultado = set()
    while len(resultado) < k_necessarios:
        simbolo = fonte_simbolos(1, alfabeto, probabilidades)[0]
        resultado.add(simbolo)
    return sorted(list(resultado))

def jogo_dados(L, nome_ficheiro):
    alfabeto_dados = [1, 2, 3, 4, 5, 6]
    prob_dados = [1/6] * 6
   
    with open(nome_ficheiro, 'w', encoding='utf-8') as f:
        f.write(f"Jogo de Dados ({L} Jogadas)\n")
        pontos_A = 0
        pontos_B = 0
       
        for jogada in range(1, L + 1):
            f.write(f"\nJogada {jogada}:\n")
            for jogador in ['A', 'B']:
                jogar_novamente = True
                while jogar_novamente:
                    dados = fonte_simbolos(2, alfabeto_dados, prob_dados)
                    soma = sum(dados)
                    if jogador == 'A':
                        pontos_A += soma
                    else:
                        pontos_B += soma
                   
                    f.write(f"Jogador {jogador} lançou {dados} (Soma: {soma})\n")
                   
                    if dados[0] == dados[1]:
                        f.write(f"Jogador {jogador} conseguiu par. Joga novamente.\n")
                    else:
                        jogar_novamente = False
       
        f.write("\nRESULTADO FINAL\n")
        f.write(f"Pontos A: {pontos_A} | Pontos B: {pontos_B}\n")
        if pontos_A > pontos_B:
            f.write("Vencedor: Jogador A\n")
        elif pontos_B > pontos_A:
            f.write("Vencedor: Jogador B\n")
        else:
            f.write("Empate\n")
    print(f"Jogo guardado em {nome_ficheiro}")

def euromilhoes(num_apostas, nome_ficheiro):
    alf_num = list(range(1, 51)); prob_num = [1/50] * 50
    alf_est = list(range(1, 13)); prob_est = [1/12] * 12
   
    with open(nome_ficheiro, 'w', encoding='utf-8') as f:
        f.write("EuroMilhões\n")
        venc_num = extrair_sem_reposicao(alf_num, prob_num, 5)
        venc_est = extrair_sem_reposicao(alf_est, prob_est, 2)
        f.write(f"CHAVE VENCEDORA: Números {venc_num} | Estrelas {venc_est}\n\n")
       
        for i in range(1, num_apostas + 1):
            ap_num = extrair_sem_reposicao(alf_num, prob_num, 5)
            ap_est = extrair_sem_reposicao(alf_est, prob_est, 2)
           
            acertos_num = len(set(ap_num) & set(venc_num))
            acertos_est = len(set(ap_est) & set(venc_est))
           
            f.write(f"Aposta {i:02d}: Números {ap_num} | Estrelas {ap_est} -> Acertos: {acertos_num}N + {acertos_est}E\n")
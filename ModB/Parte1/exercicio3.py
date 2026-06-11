import numpy as np
import zlib
import math
import collections

# 3 - A2 
def codificacao_fonte_sem_perdas(dados_bytes):
    dados_comprimidos = zlib.compress(dados_bytes.tobytes(), level=9)
    return np.frombuffer(dados_comprimidos, dtype=np.uint8)

def descodificacao_fonte_sem_perdas(dados_comprimidos):
    dados_originais = zlib.decompress(dados_comprimidos.tobytes())
    return np.frombuffer(dados_originais, dtype=np.uint8)

# 2 - A3
def cifra_vernam_array(dados, chave):
    return np.bitwise_xor(dados, chave)

def calcular_entropia(dados):
    if len(dados) == 0:
        return 0
    total = len(dados)
    frequencias = collections.Counter(dados)
    entropia = 0
    for contagem in frequencias.values():
        prob = contagem / total
        entropia -= prob * math.log2(prob)
    return entropia








#x^8 + x^2 + x + 1
def calculate_crc8(data_bytes, poly=0x07):
    crc = 0x00
    for byte in data_bytes:
        crc ^= byte
        for _ in range(8):
            if crc & 0x80:
                crc = (crc << 1) ^ poly
            else:
                crc <<= 1
            crc &= 0xFF
    return np.uint8(crc)


def codificacao_canal(data_bytes):
    crc_val = calculate_crc8(data_bytes)
    return np.append(data_bytes, crc_val)

def canal(transmit_bytes, burst_size, force_error=True):
    if not force_error:
        return transmit_bytes.copy()
        
    bits = np.unpackbits(transmit_bytes)
    bits_errored = bits.copy()
    
    if len(bits) >= burst_size:
        start_idx = np.random.randint(0, len(bits) - burst_size + 1)
        bits_errored[start_idx:start_idx + burst_size] = np.bitwise_xor(
            bits_errored[start_idx:start_idx + burst_size], 1
        )
        
    return np.packbits(bits_errored)

def descodificacao_canal(received_bytes):
    data_part = received_bytes[:-1]
    received_crc = received_bytes[-1]
    
    expected_crc = calculate_crc8(data_part)
    has_error = (expected_crc != received_crc)
    
    return data_part, has_error







def sistema_comunicacao_digital(ficheiro_entrada):
    print(f"\nficheiro: {ficheiro_entrada}")
    
    with open(ficheiro_entrada, 'rb') as f:
        A = np.frombuffer(f.read(), dtype=np.uint8)
    
    B = codificacao_fonte_sem_perdas(A)
    
    chave = np.random.randint(0, 256, size=len(B), dtype=np.uint8)
    C = cifra_vernam_array(B, chave)
    
    D = codificacao_canal(C)
    
    D_recebido = canal(D, burst_size=5, force_error=False) 
    
    C_recebido, erro_canal = descodificacao_canal(D_recebido)
    if erro_canal:
        print("Erro detetado")
        
    B_recebido = cifra_vernam_array(C_recebido, chave)
    
    E = descodificacao_fonte_sem_perdas(B_recebido)
    
    # Validação
    sao_iguais = np.array_equal(A, E)
    print(f"O ficheiro original (A) e o recebido (E) sao exatamente iguais? {'SIM' if sao_iguais else 'NÃO'}")
    
    return A, B, C, D, E


def analisar_dados_3c(dados, nome_etapa):
    dimensao = len(dados)
    entropia = calcular_entropia(dados)
    print(f"[{nome_etapa}] Dimensao: {dimensao} bytes | Entropia: {entropia:.4f} bits/simbolo")
    return dimensao, entropia

ficheiros_teste = [
    'Parte1\\ficheiros\\dados.txt',
    'Parte1\\ficheiros\\bird.png'
]

for caminho in ficheiros_teste:
    A, B, C, D, E = sistema_comunicacao_digital(caminho)

    print(f"\n 3c para: {caminho}")
    dim_A, _ = analisar_dados_3c(A, "A (Original)")
    dim_B, _ = analisar_dados_3c(B, "B (Comprimido)")
    analisar_dados_3c(C, "C (Cifrado)")
    analisar_dados_3c(D, "D (Codificado para Canal)")
    analisar_dados_3c(E, "E (Recebido)")

    razao = dim_A / dim_B if dim_B > 0 else 0
    print(f"Razao de Compressao (A/B): {razao:.2f}:1\n")
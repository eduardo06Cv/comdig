import numpy as np
from exercicio1 import read_file_to_bits


def rep_encode(bits, n):
    return np.repeat(bits, n)

def rep_decode(bits, n):
    reshaped = bits.reshape(-1, n)
    return (np.sum(reshaped, axis=1) > (n // 2)).astype(np.uint8)

def simulate_transmission(input_file, p_values):
    original_bits = read_file_to_bits(input_file)
    
    print(f"Resultados para o ficheiro: {input_file}")
    print(f"{'Configuracao':<15} | {'p':<5} | {'BER (Canal)':<12} | {'BER (Final)':<12} | {'Bits Transm.':<12}")
    print("-" * 65)
    
    for p in p_values:
        error_mask = np.random.choice([0, 1], size=len(original_bits), p=[1-p, p])
        rx_bits_none = np.bitwise_xor(original_bits, error_mask)
        ber_canal_none = np.mean(original_bits != rx_bits_none)
        print(f"{'Sem Codigo':<15} | {p:<5} | {ber_canal_none:<12.5f} | {ber_canal_none:<12.5f} | {len(original_bits):<12}")
        
        # Codigo de repeticao (3,1)
        encoded_3 = rep_encode(original_bits, 3)
        err_mask_3 = np.random.choice([0, 1], size=len(encoded_3), p=[1-p, p])
        rx_bits_3 = np.bitwise_xor(encoded_3, err_mask_3)
        decoded_3 = rep_decode(rx_bits_3, 3)
        ber_canal_3 = np.mean(encoded_3 != rx_bits_3)
        ber_final_3 = np.mean(original_bits != decoded_3)
        print(f"{'Repeticao (3,1)':<15} | {p:<5} | {ber_canal_3:<12.5f} | {ber_final_3:<12.5f} | {len(encoded_3):<12}")
        
        # Codigo de repeticao (5,1)
        encoded_5 = rep_encode(original_bits, 5)
        err_mask_5 = np.random.choice([0, 1], size=len(encoded_5), p=[1-p, p])
        rx_bits_5 = np.bitwise_xor(encoded_5, err_mask_5)
        decoded_5 = rep_decode(rx_bits_5, 5)
        ber_canal_5 = np.mean(encoded_5 != rx_bits_5)
        ber_final_5 = np.mean(original_bits != decoded_5)
        print(f"{'Repeticao (5,1)':<15} | {p:<5} | {ber_canal_5:<12.5f} | {ber_final_5:<12.5f} | {len(encoded_5):<12}")



valores_p = [0.001, 0.01, 0.05, 0.1]

simulate_transmission('Parte1\\ficheiros\\dados.txt', valores_p)

print("\n")
simulate_transmission('Parte1\\ficheiros\\bird.png', valores_p)
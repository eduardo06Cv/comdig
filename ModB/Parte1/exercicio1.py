import numpy as np


def single_bit_error(input_file, output_file, p):
    bits = read_file_to_bits(input_file)
    error_mask = np.random.choice([0, 1], size=len(bits), p=[1-p, p])
    bits_errored = np.bitwise_xor(bits, error_mask)
    write_bits_to_file(bits_errored, output_file)
    return bits, bits_errored

def burst_bit_error(input_file, output_file, B):
    bits = read_file_to_bits(input_file)
    bits_errored = bits.copy()
    
    if len(bits) > B:
        start_idx = np.random.randint(0, len(bits) - B + 1)
        bits_errored[start_idx:start_idx+B] = np.bitwise_xor(bits_errored[start_idx:start_idx+B], 1)
        
    write_bits_to_file(bits_errored, output_file)
    return bits, bits_errored




def read_file_to_bits(filepath):
    with open(filepath, 'rb') as f:
        bytes_data = np.frombuffer(f.read(), dtype=np.uint8)
    return np.unpackbits(bytes_data)

def write_bits_to_file(bits, filepath):
    bytes_data = np.packbits(bits)
    with open(filepath, 'wb') as f:
        f.write(bytes_data.tobytes())

def calc_ber_ser(original_bits, error_bits):
    ber = np.mean(original_bits != error_bits)
    orig_bytes = np.packbits(original_bits)
    err_bytes = np.packbits(error_bits)
    ser = np.mean(orig_bytes != err_bytes)
    return ber, ser


p_teste = 0.01


bits_originais_txt, bits_erro_txt = single_bit_error('Parte1\\ficheiros\\dados.txt', 'Parte1\\resultadosExercicio1\\texto_erro.txt', p_teste)
ber_txt, ser_txt = calc_ber_ser(bits_originais_txt, bits_erro_txt)

print("Teste de Texto")
print(f"Probabilidade pedida (p): {p_teste}")
print(f"BER calculado: {ber_txt:.4f}")
print(f"SER calculado: {ser_txt:.4f}\n")

bits_originais_img, bits_erro_img = single_bit_error('Parte1\\ficheiros\\bird.png', 'Parte1\\resultadosExercicio1\\imagem_erro.png', p_teste)
ber_img, ser_img = calc_ber_ser(bits_originais_img, bits_erro_img)

print("Teste de Imagem")
print(f"Probabilidade pedida (p): {p_teste}")
print(f"BER calculado: {ber_img:.4f}")
print(f"SER calculado: {ser_img:.4f}")
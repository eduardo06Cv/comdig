from exercicio1 import *

print("=== INÍCIO DOS TESTES ===\n")

print("Teste A (multiplosSeis):")
multiplosSeis(6)
multiplosSeis(3)
multiplosSeis(10)

print("\nTeste B (mmc):")
mmc(2, 21)
mmc(10, 5)
mmc(7, 3)

print("\nTeste C (primeirosNtermos):")
primeirosNtermos(0, 5, 5)
primeirosNtermos(1, 2, 10)
primeirosNtermos(10, -1, 5)

print("\nTeste D (formulaResolvente):")
formulaResolvente(1, -5, 6)
formulaResolvente(1, 0, 1)  
formulaResolvente(1, 2, 1)

print("\nTeste E (analiseVetor):")
analiseVetor([1, 1, 2, 3])
analiseVetor([10, 20, 30])
analiseVetor([5, 5, 5, 5])

print("\nTeste F (elementosComuns):")
elementosComuns([1, 2, 3], [2, 3, 4])
elementosComuns([10, 20], [30, 40])
elementosComuns([1, 1, 1], [1])

print("\nTeste G (elementosSemRepeticao):")
elementosSemRepeticao([1, 2], [2, 3])
elementosSemRepeticao([5, 5], [5, 6])
elementosSemRepeticao([], [1, 2])

print("\n=== TESTES DE FICHEIROS (H, I, J) ===")

print("Teste 1")
inverter_ficheiro("teste.txt", "saida_teste.txt")

print("Teste 2")
with open("repetidos.txt", "w") as f:
    f.write("AAAAAABBBCC")
inverter_ficheiro("repetidos.txt", "saida_repetidos.txt")

print("Teste 3")
mostrar_histograma("teste.txt")

print("\n=== FIM DOS TESTES ===")
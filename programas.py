"""
PROGRAMAS — CPU Simulada
AOC 2026.2

Armazena os programas utilizados na demonstração
e nos testes da CPU.
"""

# Programa principal de demonstração.
# Utiliza LOAD, STORE, operações da ULA, JMP e HALT.
PROGRAMA_DEMONSTRACAO = [
    "LOAD R0, 10",   # 0: R0 recebe 10
    "LOAD R1, 5",    # 1: R1 recebe 5
    "ADD R0, R1",    # 2: R0 = 10 + 5 = 15
    "STORE R0, 15",  # 3: salva 15 na memória[15]
    "SUB R0, R1",    # 4: R0 = 15 - 5 = 10
    "AND R0, R1",    # 5: R0 = 10 AND 5 = 0
    "LOAD R2, 12",   # 6: R2 recebe 12
    "OR R0, R2",     # 7: R0 = 0 OR 12 = 12
    "XOR R0, R1",    # 8: R0 = 12 XOR 5 = 9
    "JMP 11",        # 9: pula para a posição 11
    "LOAD R3, 99",   # 10: não será executado
    "HALT"           # 11: encerra a execução
]
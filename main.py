"""
MAIN — Demonstração da CPU Simulada
AOC 2026.2

Carrega um programa de programas.py e mostra
a execução passo a passo da CPU.
"""

from cpu import CPU
from programas import PROGRAMA_DEMONSTRACAO


# Cria a CPU e carrega o programa de demonstração.
cpu = CPU()
cpu.carregar_programa(PROGRAMA_DEMONSTRACAO)

print("======================================")
print("       CPU SIMULADA — 8 BITS")
print("======================================")
print("Executando programa de demonstração...")

# Executa as instruções e mostra o estado da CPU.
cpu.executar()

print()
print("======================================")
print("RESULTADO FINAL")
print("======================================")

cpu.mostrar_estado()
print("Memória[15] =", cpu.memoria[15])
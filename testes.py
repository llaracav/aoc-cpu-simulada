"""
TESTES DA CPU SIMULADA
AOC 2026.2

Verifica as instruções da CPU, as operações da ULA,
o contador de programa e a representação de 8 bits.
"""

from cpu import CPU
from ula import ula, limitar_8bits


def teste_load():
    cpu = CPU()
    cpu.memoria[0] = "LOAD R0, 25"
    cpu.memoria[1] = "HALT"
    cpu.executar()

    assert cpu.registradores["R0"] == 25
    print("[OK] LOAD")


def teste_jmp():
    cpu = CPU()
    cpu.memoria[0] = "LOAD R0, 10"
    cpu.memoria[1] = "JMP 4"
    cpu.memoria[2] = "LOAD R0, 99"
    cpu.memoria[3] = "HALT"
    cpu.memoria[4] = "LOAD R1, 20"
    cpu.memoria[5] = "HALT"
    cpu.executar()

    assert cpu.registradores["R0"] == 10
    assert cpu.registradores["R1"] == 20
    print("[OK] JMP")


def teste_halt():
    cpu = CPU()
    cpu.memoria[0] = "HALT"
    cpu.executar()

    assert cpu.halted is True
    print("[OK] HALT")


def teste_store():
    cpu = CPU()
    cpu.memoria[0] = "LOAD R0, 42"
    cpu.memoria[1] = "STORE R0, 15"
    cpu.memoria[2] = "HALT"
    cpu.executar()

    assert cpu.memoria[15] == 42
    print("[OK] STORE")


def teste_ula():
    assert ula("ADD", 5, 8) == 13
    assert ula("SUB", 8, 5) == 3
    assert ula("AND", 5, 8) == 0
    assert ula("OR", 5, 8) == 13
    assert ula("XOR", 5, 8) == 13
    print("[OK] Operações da ULA")


def teste_instrucoes_ula_cpu():
    # Testa cada operação por meio das instruções da CPU.
    casos = [
        ("ADD", 10, 5, 15),
        ("SUB", 10, 5, 5),
        ("AND", 10, 5, 0),
        ("OR", 10, 5, 15),
        ("XOR", 10, 5, 15),
    ]

    for operacao, a, b, esperado in casos:
        cpu = CPU()

        programa = [
            f"LOAD R0, {a}",
            f"LOAD R1, {b}",
            f"{operacao} R0, R1",
            "HALT"
        ]

        cpu.carregar_programa(programa)
        cpu.executar()

        resultado = cpu.registradores["R0"]

        assert resultado == esperado, (
            f"{operacao}: esperado {esperado}, recebido {resultado}"
        )

    print("[OK] Instruções da ULA na CPU")


def teste_pc():
    cpu = CPU()
    cpu.memoria[0] = "LOAD R0, 10"
    cpu.memoria[1] = "LOAD R1, 20"
    cpu.memoria[2] = "HALT"
    cpu.executar()

    assert cpu.pc == 2
    print("[OK] Avanço do PC")


def teste_8_bits():
    assert limitar_8bits(255) == 255
    assert limitar_8bits(256) == 0
    assert limitar_8bits(260) == 4
    assert ula("ADD", 250, 10) == 4
    assert ula("SUB", 5, 8) == 253
    print("[OK] Representação de 8 bits")


def teste_programa_completo():
    programa = [
        "LOAD R0, 10",
        "LOAD R1, 5",
        "ADD R0, R1",
        "STORE R0, 15",
        "SUB R0, R1",
        "HALT"
    ]

    cpu = CPU()
    cpu.carregar_programa(programa)
    cpu.executar()

    assert cpu.registradores["R0"] == 10
    assert cpu.registradores["R1"] == 5
    assert cpu.memoria[15] == 15
    print("[OK] Programa completo")


if __name__ == "__main__":
    print("Executando testes da CPU simulada...\n")

    teste_load()
    teste_jmp()
    teste_halt()
    teste_store()
    teste_ula()
    teste_instrucoes_ula_cpu()
    teste_pc()
    teste_8_bits()
    teste_programa_completo()

    print("\nTodos os testes foram aprovados!")


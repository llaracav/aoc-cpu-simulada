"""
ULA — AOC 2026.2

Implementação das operações aritméticas e lógicas.
"""

def limitar_8bits(valor):
    # Mantém o valor no intervalo de 0 a 255.
    return valor & 0xFF


def ula(operacao, a, b=0):
    # Garante que os operandos tenham 8 bits.
    a = limitar_8bits(a)
    b = limitar_8bits(b)

    # Executa a operação solicitada.
    if operacao == "ADD":
        resultado = a + b

    elif operacao == "SUB":
        resultado = a - b

    elif operacao == "AND":
        resultado = a & b

    elif operacao == "OR":
        resultado = a | b

    elif operacao == "XOR":
        resultado = a ^ b

    else:
        raise ValueError(f"Operação inválida: {operacao}")

    # Limita o resultado a 8 bits.
    return limitar_8bits(resultado)

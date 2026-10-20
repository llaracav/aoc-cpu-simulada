"""
CPU SIMULADA — AOC 2026.2

CPU de 8 bits com quatro registradores, memória de 16 posições,
contador de programa, ULA e conjunto de instruções.
"""

from ula import ula, limitar_8bits


class CPU:

    def __init__(self):
        # Quatro registradores gerais de 8 bits.
        self.registradores = {
            "R0": 0,
            "R1": 0,
            "R2": 0,
            "R3": 0
        }

        # Memória com 16 posições, numeradas de 0 a 15.
        self.memoria = [0] * 16

        # PC indica a posição da próxima instrução.
        self.pc = 0

        # Indica se a execução foi encerrada.
        self.halted = False

    def carregar_programa(self, programa):
        # Verifica se o programa cabe na memória.
        if len(programa) > len(self.memoria):
            raise ValueError(
                "O programa excede a memória de 16 posições"
            )

        # Verifica se todas as instruções são textos.
        if not all(isinstance(instrucao, str) for instrucao in programa):
            raise ValueError("Todas as instruções devem ser textos")

        # Limpa a memória e carrega o programa a partir da posição 0.
        self.memoria = [0] * 16

        for endereco, instrucao in enumerate(programa):
            self.memoria[endereco] = instrucao

        # Reinicia a execução.
        self.pc = 0
        self.halted = False

        # Reinicia os registradores.
        for registrador in self.registradores:
            self.registradores[registrador] = 0

    def decodificar_instrucao(self, instrucao):
        # Separa a operação dos operandos.
        partes = instrucao.replace(",", "").split()

        if not partes:
            raise ValueError("Instrução vazia")

        operacao = partes[0]
        operandos = partes[1:]

        formatos = {
            "LOAD": 2,
            "STORE": 2,
            "ADD": 2,
            "SUB": 2,
            "AND": 2,
            "OR": 2,
            "XOR": 2,
            "JMP": 1,
            "HALT": 0
        }

        if operacao not in formatos:
            raise ValueError(
                f"Instrução desconhecida: {operacao}"
            )

        if len(operandos) != formatos[operacao]:
            raise ValueError(
                f"Quantidade de operandos inválida para {operacao}"
            )

        # Mostra a etapa DECODE.
        print("DECODE")
        print("Operação identificada:", operacao)

        if operandos:
            print("Operandos:", ", ".join(operandos))
        else:
            print("Operandos: nenhum")

        return operacao, operandos

    def executar_instrucao(self, instrucao):
        # Obtém a operação e os operandos sem repetir o DECODE.
        partes = instrucao.replace(",", "").split()
        operacao = partes[0]
        operandos = partes[1:]

        # LOAD: carrega um valor em um registrador.
        if operacao == "LOAD":
            registrador = operandos[0]
            valor = int(operandos[1])

            if registrador not in self.registradores:
                raise ValueError("Registrador inválido")

            self.registradores[registrador] = limitar_8bits(valor)
            self.pc += 1

        # STORE: grava um registrador na memória.
        elif operacao == "STORE":
            registrador = operandos[0]
            endereco = int(operandos[1])

            if registrador not in self.registradores:
                raise ValueError("Registrador inválido")

            if endereco < 0 or endereco >= len(self.memoria):
                raise ValueError("Endereço de memória inválido")

            self.memoria[endereco] = self.registradores[registrador]
            self.pc += 1

        # Operações aritméticas e lógicas da ULA.
        elif operacao in ("ADD", "SUB", "AND", "OR", "XOR"):
            destino = operandos[0]
            origem = operandos[1]

            if destino not in self.registradores:
                raise ValueError("Registrador de destino inválido")

            if origem not in self.registradores:
                raise ValueError("Registrador de origem inválido")

            resultado = ula(
                operacao,
                self.registradores[destino],
                self.registradores[origem]
            )

            self.registradores[destino] = limitar_8bits(resultado)
            self.pc += 1

        # JMP: altera o PC para o endereço indicado.
        elif operacao == "JMP":
            endereco = int(operandos[0])

            if endereco < 0 or endereco >= len(self.memoria):
                raise ValueError("Endereço de salto inválido")

            self.pc = endereco

        # HALT: encerra a execução da CPU.
        elif operacao == "HALT":
            self.halted = True

    def ciclo(self):
        # Não executa novos ciclos depois de HALT.
        if self.halted:
            return

        # Verifica se o PC aponta para uma posição válida.
        if self.pc < 0 or self.pc >= len(self.memoria):
            raise ValueError("PC fora dos limites da memória")

        # FETCH: busca a instrução indicada pelo PC.
        instrucao = self.memoria[self.pc]

        if not isinstance(instrucao, str):
            raise ValueError(
                f"Não há instrução válida na posição {self.pc}"
            )

        print()
        print("--------------------------------")
        print("FETCH")
        print("PC:", self.pc)
        print("Instrução:", instrucao)

        # DECODE: identifica a operação e seus operandos.
        operacao, operandos = self.decodificar_instrucao(instrucao)

        # Guarda os valores anteriores para mostrar a operação.
        pc_anterior = self.pc
        valores_anteriores = self.registradores.copy()

        # EXECUTE: executa a instrução.
        print("EXECUTE")

        self.executar_instrucao(instrucao)

        # Mostra o cálculo realizado pela ULA.
        if operacao in ("ADD", "SUB", "AND", "OR", "XOR"):
            a = valores_anteriores[operandos[0]]
            b = valores_anteriores[operandos[1]]
            resultado = self.registradores[operandos[0]]

            simbolos = {
                "ADD": "+",
                "SUB": "-",
                "AND": "AND",
                "OR": "OR",
                "XOR": "XOR"
            }

            print(
                f"Operação: {a} {simbolos[operacao]} {b} = {resultado}"
            )

        elif operacao == "LOAD":
            print(
                f"Operação: carregado o valor "
                f"{self.registradores[operandos[0]]} "
                f"em {operandos[0]}"
            )

        elif operacao == "STORE":
            endereco = int(operandos[1])
            print(
                f"Operação: memória[{endereco}] recebe "
                f"{self.memoria[endereco]}"
            )

        elif operacao == "JMP":
            print(f"Salto realizado para a posição {self.pc}")

        elif operacao == "HALT":
            print("Execução encerrada.")

        # Mostra a atualização do PC.
        if operacao == "JMP":
            print(f"PC atualizado de {pc_anterior} para {self.pc}")
        elif operacao == "HALT":
            print(f"PC permanece em: {self.pc}")
        else:
            print(f"PC atualizado para: {self.pc}")

        # Mostra os registradores após a execução.
        self.mostrar_estado()

    def executar(self, max_ciclos=100):
        ciclos = 0

        # Executa até encontrar HALT.
        while not self.halted:
            if ciclos >= max_ciclos:
                raise RuntimeError(
                    "Número máximo de ciclos atingido. "
                    "Verifique se existe um loop infinito."
                )

            self.ciclo()
            ciclos += 1

    def mostrar_estado(self):
        # Exibe os registradores em hexadecimal e decimal.
        print("Registradores:")

        for nome, valor in self.registradores.items():
            print(f"  {nome} = {valor:02X} ({valor})")

# CPU Simulada — AOC 2026.2

## 1. Objetivo

Este projeto implementa uma CPU simulada de 8 bits em Python, com o objetivo de demonstrar o funcionamento básico de um processador e o ciclo de execução de instruções.

A CPU possui:

- Quatro registradores de uso geral: R0, R1, R2 e R3, cada um com 8 bits.
- Memória com 16 posições, endereçadas de 0 a 15.
- Contador de Programa (PC — Program Counter), que indica a posição da próxima instrução.
- Unidade Lógica e Aritmética (ULA), responsável pelas operações aritméticas e lógicas.
- Ciclo de execução Fetch → Decode → Execute.
- Visualização do estado dos registradores durante a execução.

## 2. Arquivos do projeto

- `cpu.py` — implementa a estrutura da CPU, os registradores, a memória, o PC e a execução das instruções.
- `ula.py` — implementa as operações aritméticas e lógicas e limita os resultados a 8 bits.
- `programas.py` — armazena o programa utilizado na demonstração.
- `main.py` — executa o programa de demonstração e apresenta o estado da CPU passo a passo.
- `testes.py` — contém testes automáticos para verificar o funcionamento das instruções, das operações da ULA e do comportamento da CPU.

## 3. Instruções implementadas

A CPU implementa as seguintes instruções:

| Instrução | Funcionamento |
|---|---|
| `LOAD R0, 10` | Carrega um valor imediato em um registrador. |
| `STORE R0, 15` | Armazena o valor de um registrador em uma posição da memória. |
| `ADD R0, R1` | Soma os valores dos registradores e armazena o resultado no primeiro. |
| `SUB R0, R1` | Subtrai o segundo registrador do primeiro e armazena o resultado no primeiro. |
| `AND R0, R1` | Executa a operação lógica AND entre os registradores. |
| `OR R0, R1` | Executa a operação lógica OR entre os registradores. |
| `XOR R0, R1` | Executa a operação lógica XOR entre os registradores. |
| `JMP 11` | Altera o PC para a posição indicada, realizando um salto no programa. |
| `HALT` | Encerra a execução do programa. |

Nos exemplos, `R0` e `R1` representam registradores, enquanto os números nas instruções `LOAD`, `STORE` e `JMP` representam valores ou endereços, conforme a instrução.

## 4. Representação de 8 bits

Os registradores e os resultados das operações trabalham com valores de 8 bits, limitados ao intervalo de 0 a 255.

Quando um resultado ultrapassa esse intervalo, ele é ajustado para permanecer em 8 bits.

Exemplos:

- `250 + 10 = 4`, considerando o limite de 8 bits.
- `5 - 8 = 253`, considerando a representação sem sinal de 8 bits.

## 5. Programa de demonstração

O arquivo `programas.py` contém um programa de demonstração com 12 instruções, utilizando operações aritméticas e lógicas, acesso à memória, salto e encerramento.

O programa:

1. Carrega valores nos registradores.
2. Executa as operações da ULA: ADD, SUB, AND, OR e XOR.
3. Armazena um resultado na memória.
4. Utiliza `JMP` para saltar uma instrução.
5. Encerra a execução com `HALT`.

Durante a execução, a CPU apresenta as três etapas do ciclo de instrução:

- **FETCH:** busca a instrução na posição indicada pelo PC.
- **DECODE:** identifica a operação e seus operandos.
- **EXECUTE:** executa a instrução e apresenta seu efeito.

Após cada instrução, são exibidos o estado dos registradores e a atualização do PC.

## 6. Como executar

É necessário ter Python instalado.

Abra o terminal na pasta do projeto e execute o programa de demonstração:

```bash
python main.py
```

Para executar os testes automáticos:

```bash
python testes.py
```

Se os testes forem aprovados, o terminal exibirá mensagens `[OK]` para as verificações realizadas e uma mensagem final indicando que todos os testes foram aprovados.

## 7. Testes realizados

O arquivo `testes.py` verifica:

- Instrução `LOAD`.
- Instrução `STORE`.
- Instrução `JMP`, incluindo o desvio de uma instrução.
- Instrução `HALT`.
- Operações `ADD`, `SUB`, `AND`, `OR` e `XOR` diretamente na ULA.
- Execução das cinco operações da ULA por meio das instruções da CPU.
- Avanço do contador de programa (PC).
- Limitação dos valores a 8 bits, incluindo casos de soma e subtração.
- Execução integrada de um programa com verificação dos registradores e da memória.

## 8. Regras do projeto

Foram preservadas as seguintes características definidas pelo professor:

- Os nomes dos arquivos.
- A assinatura da função `ula()`.
- A estrutura dos registradores.
- O tamanho da memória.
- A representação de 8 bits.

O projeto utiliza funções auxiliares e comentários para organizar o código e facilitar a compreensão da implementação.
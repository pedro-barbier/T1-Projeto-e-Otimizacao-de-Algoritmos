import sys

def recursiva(n):
    if n == 1:
        return 0

    operacoes = [recursiva(n - 1)]
    
    if n % 2 == 0:
        operacoes.append(recursiva(n // 2))
    
    if n % 3 == 0:
        operacoes.append(recursiva(n // 3))
    
    return 1 + min(operacoes)

def recursiva_com_memoria(n, mem: dict):
    if n == 1:
        return 0
    
    if n in mem:
        return mem[n]

    operacoes = [recursiva_com_memoria(n - 1, mem)]
    
    if n % 2 == 0:
        operacoes.append(recursiva_com_memoria(n // 2, mem))
    
    if n % 3 == 0:
        operacoes.append(recursiva_com_memoria(n // 3, mem))
    
    mem[n] = 1 + min(operacoes)
    return mem[n]

def nao_recursiva_com_operacoes(n):
    if n == 1:
        return 0, []

    dp = [0] * (n + 1)
    anterior = [0] * (n + 1)
    operacao = [""] * (n + 1)

    for i in range(2, n + 1):
        melhor = dp[i - 1]
        anterior[i] = i - 1
        operacao[i] = "-1"

        if i % 2 == 0 and dp[i // 2] < melhor:
            melhor = dp[i // 2]
            anterior[i] = i // 2
            operacao[i] = "/2"

        if i % 3 == 0 and dp[i // 3] < melhor:
            melhor = dp[i // 3]
            anterior[i] = i // 3
            operacao[i] = "/3"

        dp[i] = 1 + melhor

    operacoes = []
    atual = n
    while atual != 1:
        operacoes.append(operacao[atual])
        atual = anterior[atual]

    return dp[n], operacoes

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python trabalho_para_nasa.py <n> <versão do programa (recursiva, recursiva_com_memoria ou nao_recursiva)>")
        sys.exit(1)

    n = int(sys.argv[1])
    tipo = str(sys.argv[2])

    match tipo:
        case "recursiva":
            print(f"Menor número de operações para reduzir {n} até 1: {recursiva(n)}")
        case "recursiva_com_memoria":
            print(f"Menor número de operações para reduzir {n} até 1: {recursiva_com_memoria(n,{})}")
        case "nao_recursiva":
            operacoes, caminho = nao_recursiva_com_operacoes(n)
            print(f"Menor número de operações para reduzir {n} até 1: {operacoes}")
            print(f"Caminho de operações tomadas: {caminho}")
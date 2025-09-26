import sys

def recursiva(n):
    if n == 1:
        return 0

    operacoes = [recursiva_com_memoria(n - 1)]
    
    if n % 2 == 0:
        operacoes.append(recursiva_com_memoria(n // 2))
    
    if n % 3 == 0:
        operacoes.append(recursiva_com_memoria(n // 3))
    
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

def nao_recursiva(n):
    if n == 1:
        return 0

    dp = [0] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        melhor = dp[i - 1]

        if i % 2 == 0:
            melhor = min(melhor, dp[i // 2])

        if i % 3 == 0:
            melhor = min(melhor, dp[i // 3])

        dp[i] = 1 + melhor

    return dp[n]

if __name__ == "__main__":
    if len(sys.argv) < 2:
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
            print(f"Menor número de operações para reduzir {n} até 1: {nao_recursiva(n)}")
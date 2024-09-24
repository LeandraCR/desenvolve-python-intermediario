# Função recursiva que converte um número decimal em sua representação binária
def decimal_para_binario(n):
    # Caso base da recursão: se o número for 0, retorna uma string vazia
    if n == 0:
        return ""
    else:
        # Chamada recursiva: divide o número por 2 e concatena o resto da divisão (0 ou 1)
        # A função acumula os restos de cada divisão à medida que volta da recursão
        return decimal_para_binario(n // 2) + str(n % 2)

# Interação com o usuário
# O usuário insere um número decimal através da função input() e o converte para inteiro
numero_decimal = int(input("Digite um número decimal para converter em binário: "))

# Chamada da função decimal_para_binario passando o número inserido pelo usuário
binario = decimal_para_binario(numero_decimal)

# Exibe o resultado da conversão. Caso o número seja 0, retorna a string "0".
print(f"O número {numero_decimal} em binário é: {binario if binario else '0'}")

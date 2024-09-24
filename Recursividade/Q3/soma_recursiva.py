# Definimos a função recursiva chamada soma_recursiva que recebe um número inteiro n
def soma_recursiva(n):
    # Caso base: quando n for igual a 1, retornamos 1, pois a soma de 1 até 1 é 1
    if n == 1:
        return 1
    # Caso recursivo: somamos o valor atual de n com a chamada da função soma_recursiva(n-1)
    else:
        return n + soma_recursiva(n - 1)

# Solicitamos ao usuário que insira um número inteiro maior que 1
n = int(input("Digite um número maior que 1: "))

# Chamamos a função soma_recursiva passando o valor de n e armazenamos o resultado
resultado = soma_recursiva(n)

# Exibimos o resultado final, ou seja, a soma de n até 1
print(f'A soma dos valores de {n} até 1 é: {resultado}')

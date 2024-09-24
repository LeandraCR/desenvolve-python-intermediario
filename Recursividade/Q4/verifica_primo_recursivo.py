# Função recursiva para verificar se um número é primo
def eh_primo(n, divisor=2):
    # Caso base: se n for menor que 2, ele não é primo
    if n < 2:
        return False
    # Caso base: se o divisor for maior que a raiz quadrada de n, então n é primo
    if divisor * divisor > n:
        return True
    # Se n for divisível pelo divisor atual, então n não é primo
    if n % divisor == 0:
        return False
    # Chamada recursiva: tenta verificar com o próximo divisor
    return eh_primo(n, divisor + 1)

# Solicita a entrada do usuário para digitar um número
numero = int(input("Digite um número para verificar se é primo: "))

# Verifica se o número é primo chamando a função eh_primo
if eh_primo(numero):
    # Se for primo, exibe a mensagem indicando que é primo
    print(f"{numero} é primo.")
else:
    # Caso contrário, exibe a mensagem indicando que não é primo
    print(f"{numero} não é primo.")

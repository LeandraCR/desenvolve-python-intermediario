
# Imprimindo Números
## 1. A Função `imprimir_intervalo(a, b)`:
Uma função é como uma pequena máquina que faz um trabalho específico. Nesse caso, a função `imprimir_intervalo` pega dois números, `a` e `b`, e imprime todos os números entre eles, inclusive eles mesmos.

## 2. Verificando se os valores estão corretos:
Dentro da função, a primeira coisa que fazemos é verificar se os números estão na ordem certa:

```python
if a > b:
    print("Valores inválidos")
```

Aqui, o programa está dizendo: "Se o primeiro número (`a`) for maior que o segundo número (`b`), algo está errado, então eu vou imprimir **Valores inválidos**."

## 3. O caso base:
Se os números estiverem na ordem correta, passamos para a próxima parte. Aqui, verificamos se `a` é igual a `b`. Isso é importante porque precisamos saber quando parar de imprimir os números.

```python
if a == b:
    print(a)
```

Se `a` for igual a `b`, significa que chegamos ao final e só precisamos imprimir esse número e parar.

## 4. A parte recursiva:
Se `a` for menor que `b`, então imprimimos o número atual (`a`) e chamamos a função de novo, aumentando o valor de `a` em 1:

```python
else:
    print(a, end=" ")
    imprimir_intervalo(a + 1, b)
```

A linha `print(a, end=" ")` imprime o número `a` sem quebrar a linha (para que os números fiquem todos na mesma linha), e depois chamamos a função novamente, mas agora com `a + 1`.

Isso faz o programa continuar chamando a si mesmo e imprimindo os números seguintes até chegar ao valor de `b`.

## 5. Interação com o usuário:
Fora da função, temos duas partes que pedem para o usuário digitar os números iniciais:

```python
a = int(input("Digite o valor inicial (a): "))
b = int(input("Digite o valor final (b): "))
```

Aqui, estamos pedindo dois números: um valor inicial `a` e um valor final `b`.

## 6. Chamada da função:
Depois que o usuário digita os números, a função é chamada:

```python
imprimir_intervalo(a, b)
```

Ela então começa a imprimir todos os números entre `a` e `b`, chamando a si mesma até que o intervalo seja completamente impresso.

## Exemplo de funcionamento:
Se o usuário digitar **2** para o valor inicial e **5** para o valor final, o programa vai imprimir:

```
2 3 4 5
```

Esse é o conceito básico: a função vai repetindo o processo até chegar no número final, usando algo chamado recursão, que é quando uma função chama a si mesma para continuar o trabalho!


# Explicação do código de soma recursiva

1. **Definindo a função**: 
   A primeira linha do código define uma função chamada `soma_recursiva`. Essa função precisa de um número (`n`) como entrada, que será um número inteiro.

2. **Caso base (quando parar a função)**:
   Dentro da função, há uma condição que verifica se o número (`n`) é igual a 1. Se for, a função retorna o número 1, pois a soma de 1 até 1 é simplesmente 1. Isso é o que chamamos de "caso base" – é onde a função sabe que pode parar.

3. **Caso recursivo (chamando a função de novo)**:
   Se o número (`n`) for maior que 1, a função passa para a outra parte (o `else`). Aqui, o número `n` é somado ao resultado da mesma função, só que com o valor de `n-1`. Ou seja, a função "se chama" de novo, mas com um número menor (por exemplo, se `n` é 5, ela vai chamar `soma_recursiva(4)`).

4. **Entrada do usuário**:
   Depois de definir a função, o programa pede ao usuário para digitar um número inteiro maior que 1 (por exemplo, 5). O valor digitado é armazenado na variável `n`.

5. **Chamando a função**:
   O código chama a função `soma_recursiva(n)`, passando o número que o usuário digitou como argumento. O resultado dessa função será a soma de todos os números de `n` até 1.

6. **Exibindo o resultado**:
   Por fim, o código imprime o resultado da soma que foi calculada, dizendo ao usuário a soma de todos os números de `n` até 1.

### Exemplo prático:
Se o usuário digitar 5, a função será chamada várias vezes assim:
- `soma_recursiva(5)` retorna `5 + soma_recursiva(4)`
- `soma_recursiva(4)` retorna `4 + soma_recursiva(3)`
- `soma_recursiva(3)` retorna `3 + soma_recursiva(2)`
- `soma_recursiva(2)` retorna `2 + soma_recursiva(1)`
- `soma_recursiva(1)` retorna `1`

Então, a soma final será 5 + 4 + 3 + 2 + 1 = 15, e isso será exibido na tela.

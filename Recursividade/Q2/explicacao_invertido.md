# Função `imprimir_intervalo(a, b)`

1. **Função `imprimir_intervalo(a, b)`**
   - Esta função recebe dois números: `a` e `b`.
   - Dependendo dos valores de `a` e `b`, ela faz três coisas diferentes:
     1. Imprime os números de `b` até `a` se `a` for menor que `b`.
     2. Diz que os valores são inválidos se `a` for maior que `b`.
     3. Imprime apenas o valor de `a` (ou `b`, já que são iguais) se `a` for igual a `b`.

2. **Parte da verificação: `if a < b`**
   - Se `a` for menor que `b`, ou seja, `a` é um número mais "baixo", o código vai contar de trás para frente, começando em `b` e indo até `a`.
   - O `for` faz essa contagem para nós, indo de `b` até `a`, de 1 em 1 para trás.
   - Quando ele imprime, os números são mostrados com um espaço entre eles, tudo numa mesma linha.

3. **Parte da verificação: `elif a > b`**
   - Se `a` for maior que `b`, os valores não fazem sentido, então ele imprime "Valores inválidos", porque a contagem não pode acontecer nessa ordem.

4. **Parte da verificação: `else`**
   - Se `a` for igual a `b`, não tem um intervalo para contar, então só imprime o próprio valor de `a` (ou `b`, já que são iguais).

5. **Entradas do usuário**
   - O código pede para você digitar dois números: `a` e `b`.
   - Você coloca os números e o código usa a função `imprimir_intervalo(a, b)` para mostrar o que ele decidiu baseado nas regras acima.

Resumindo: se `a` for menor que `b`, ele conta de `b` até `a`. Se `a` for maior que `b`, diz que é inválido. Se forem iguais, só imprime esse número.

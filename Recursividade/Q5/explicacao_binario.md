
# Função que transforma o número em binário

1. **Função que transforma o número em binário**:  
   O código cria uma função chamada `decimal_para_binario`, que vai transformar um número normal (decimal) em um número binário. Binário é aquele número que só tem os dígitos 0 e 1.

2. **Recursão (vai chamando ela mesma)**:  
   Dentro dessa função, tem uma parte que fala: "se o número for 0, devolve uma frase vazia" (`""`). Isso é chamado de *caso base* e é o jeito do programa falar "cheguei no final, não preciso fazer mais nada".  
   Mas se o número **não for 0**, a função vai dividir o número por 2 e vai guardar o resto dessa divisão (0 ou 1) e continuar fazendo isso até que o número fique 0.  
   Exemplo:  
   Se você tentar converter o número 5, a função vai dividir 5 por 2 (o resultado é 2 e sobra 1), depois divide 2 por 2 (o resultado é 1 e sobra 0), e, por fim, divide 1 por 2 (o resultado é 0 e sobra 1). Todos esses restos vão formando o número binário.

3. **Interação com o usuário**:  
   O programa pede para o usuário digitar um número com a função `input()`. Como o que o usuário digita é um texto, o programa converte esse texto para um número com a função `int()`.

4. **Chama a função para converter**:  
   Depois, ele usa a função `decimal_para_binario` para converter o número que o usuário digitou em um número binário.

5. **Mostra o resultado**:  
   No final, ele imprime o número binário. Se o número que o usuário digitou for 0, o programa imprime '0', senão, ele imprime o número binário resultante da função.

Então, o código basicamente pega um número que você digita, transforma ele em binário dividindo por 2 várias vezes, e mostra o resultado.

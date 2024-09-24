
# Função recursiva para verificar se um número é primo

1. **Função recursiva para verificar se um número é primo**  
   O código define uma função chamada `eh_primo`, que serve para verificar se um número é **primo** ou não. Um número é primo quando só pode ser dividido por 1 e por ele mesmo, sem sobrar nada.

2. **Argumentos da função**  
   A função `eh_primo` recebe dois parâmetros:  
   - `n` é o número que queremos verificar.  
   - `divisor`, que começa em 2, é o número pelo qual vamos dividir `n` para ver se sobra resto (divisão exata).

3. **Primeira condição (n < 2)**  
   A primeira verificação é se o número `n` é menor que 2. Se for, a função retorna `False`, ou seja, o número **não é primo**, porque números menores que 2 não são considerados primos.

4. **Segunda condição (divisor * divisor > n)**  
   Aqui, o código faz uma checagem: se o quadrado do divisor (multiplicação dele por ele mesmo) for maior que `n`, a função retorna `True`. Isso significa que, se chegamos até aqui sem encontrar nenhum número que divida `n` com resto zero, então `n` **é primo**.

5. **Terceira condição (n % divisor == 0)**  
   Essa parte verifica se `n` pode ser dividido exatamente pelo divisor atual, ou seja, se sobra zero no resto da divisão. Se sobrar zero, o número **não é primo**, e a função retorna `False`.

6. **Chamada recursiva (eh_primo(n, divisor + 1))**  
   Se nenhuma das condições anteriores foi satisfeita, a função vai se chamar de novo, mas agora com o próximo divisor (o divisor é aumentado em 1). A ideia é continuar verificando divisões até ter certeza se o número é primo ou não.

7. **Solicita um número ao usuário**  
   Depois da função, o programa pede para o usuário digitar um número. Esse número é guardado na variável `numero`.

8. **Verificação se o número é primo**  
   O programa chama a função `eh_primo` para verificar se o número digitado é primo. Se for, ele imprime uma mensagem dizendo que o número é primo. Se não for, imprime que o número não é primo.

---

**Resumindo:**  
- O programa tem uma função que tenta dividir o número por vários outros números, começando do 2.
- Se achar algum número que divide sem deixar resto (exceto 1 e o próprio número), ele diz que o número **não é primo**.
- Se não achar, ele diz que o número **é primo**.
- O usuário digita um número, e o programa usa essa função para dar a resposta.

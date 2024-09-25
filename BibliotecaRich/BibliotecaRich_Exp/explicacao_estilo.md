# Documentação de Código

## 1. Importações:
O código usa duas coisas da biblioteca `rich`, que serve para formatar texto de uma maneira bonita no terminal:
- `Console`: É como uma "tela" onde a gente pode imprimir textos bonitos.
- `Text`: Permite criar textos com estilos (como cores e negrito).

## 2. Console:
Criamos um objeto chamado `console` usando `Console()`. Basicamente, isso é como ligar uma TV onde a gente vai mostrar as coisas depois.

## 3. Função `aplicar_estilo`:
A função serve para mudar a aparência do texto, tornando-o em **negrito vermelho**. Se `isArquivo` for `True`, o código vai ler o conteúdo de um arquivo e mudar o estilo desse conteúdo. Se `isArquivo` for `False`, ele simplesmente aplica o estilo ao texto que você passar.

### O que acontece dentro:
- Se `isArquivo` for `True`, ele abre o arquivo, lê o conteúdo e aplica o estilo "negrito vermelho" ao texto.
- Se `isArquivo` for `False`, aplica o estilo ao texto passado diretamente.
  
Depois disso, a função usa `console.print()` para mostrar o texto estilizado no terminal.

## 4. Função `destacar_palavra`:
Esta função serve para destacar uma palavra específica dentro de um texto. O destaque é feito em **amarelo negrito**.

### O que acontece dentro:
- Se `isArquivo` for `True`, ele abre o arquivo, lê o conteúdo e então procura a palavra que você quer destacar, aplicando o estilo de destaque.
- Se `isArquivo` for `False`, faz a mesma coisa, só que com o texto passado diretamente.

Depois, ele usa `console.print()` para mostrar o texto com a palavra destacada.

## 5. Parte de Testes:
A última parte do código testa as funções:
- Primeiro, aplica o estilo de **negrito vermelho** em um texto direto.
- Depois, lê o conteúdo de um arquivo (supostamente na pasta `BibliotecaRich/Personalizador`) e aplica o mesmo estilo.
- Em seguida, destaca a palavra "texto" no conteúdo do arquivo.
- Por último, destaca a palavra "destaque" num texto passado diretamente.

Essencialmente, o código tem duas funções principais: uma para deixar o texto em **negrito vermelho** e outra para destacar uma palavra específica com **amarelo negrito**. Ele pode fazer isso tanto com textos diretos quanto com textos lidos de um arquivo.

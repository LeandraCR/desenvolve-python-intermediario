from rich.console import Console
from rich.text import Text

# Inicializa o objeto Console para imprimir saídas formatadas no terminal
console = Console()

def aplicar_estilo(texto: str, isArquivo: bool):
    """Aplica um estilo ao texto fornecido ou ao conteúdo de um arquivo.
    
    Args:
        texto (str): O texto a ser estilizado ou o caminho do arquivo.
        isArquivo (bool): Define se o parâmetro `texto` é um texto direto (False)
                          ou o caminho de um arquivo (True).
    """
    if isArquivo:
        # Se o parâmetro for um arquivo, abre e lê o conteúdo do arquivo
        with open(texto, 'r') as arquivo:
            conteudo = arquivo.read()
            # Aplica o estilo "negrito" e "vermelho" ao texto do arquivo
            texto_estilizado = Text(conteudo, style="bold red")
    else:
        # Aplica o estilo "negrito" e "vermelho" ao texto fornecido
        texto_estilizado = Text(texto, style="bold red")
    
    # Imprime o texto estilizado no console
    console.print(texto_estilizado)

def destacar_palavra(texto: str, palavra: str, isArquivo: bool):
    """Destaca uma palavra específica no texto ou no conteúdo de um arquivo.
    
    Args:
        texto (str): O texto a ser analisado ou o caminho do arquivo.
        palavra (str): A palavra a ser destacada no texto.
        isArquivo (bool): Define se o parâmetro `texto` é um texto direto (False)
                          ou o caminho de um arquivo (True).
    """
    if isArquivo:
        # Se o parâmetro for um arquivo, abre e lê o conteúdo do arquivo
        with open(texto, 'r') as arquivo:
            conteudo = arquivo.read()
            # Cria um objeto Text a partir do conteúdo do arquivo
            texto_estilizado = Text(conteudo)
            # Destaca a palavra fornecida com estilo "negrito" e "amarelo"
            texto_estilizado.highlight_words([palavra], style="bold yellow")
    else:
        # Cria um objeto Text a partir do texto fornecido
        texto_estilizado = Text(texto)
        # Destaca a palavra fornecida com estilo "negrito" e "amarelo"
        texto_estilizado.highlight_words([palavra], style="bold yellow")

    # Imprime o texto com a palavra destacada no console
    console.print(texto_estilizado)

# Testando as funções no contexto principal
if __name__ == "__main__":
    # Teste com texto direto e aplicação de estilo
    aplicar_estilo("Este é um texto em vermelho e negrito", isArquivo=False)
    
    # Teste com estilo aplicado ao conteúdo de um arquivo
    caminho_arquivo = "BibliotecaRich/Personalizador/meutexto.txt"  # Caminho para o arquivo de texto
    aplicar_estilo(caminho_arquivo, isArquivo=True)
    
    # Teste de destaque de palavra no conteúdo do arquivo
    destacar_palavra(caminho_arquivo, "texto", isArquivo=True)
    
    # Teste de destaque de palavra em texto direto
    destacar_palavra("Este é um exemplo de destaque de palavra", "destaque", isArquivo=False)

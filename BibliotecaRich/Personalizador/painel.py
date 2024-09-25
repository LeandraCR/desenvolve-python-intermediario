from rich.console import Console
from rich.panel import Panel

# Cria um objeto Console da biblioteca Rich, usado para imprimir saída formatada no terminal
console = Console()

def mostrar_painel(texto: str, isArquivo: bool):
    """
    Função que imprime o conteúdo dentro de um painel formatado.
    Parâmetros:
    - texto: str -> pode ser o texto direto ou o caminho de um arquivo.
    - isArquivo: bool -> determina se o parâmetro 'texto' é um arquivo ou um texto direto.
    """
    if isArquivo:
        # Se 'isArquivo' for True, lê o conteúdo de um arquivo
        with open(texto, 'r') as arquivo:
            conteudo = arquivo.read()  # Lê todo o conteúdo do arquivo
            # Cria um painel com o conteúdo do arquivo, título "Arquivo" e borda verde
            panel = Panel(conteudo, title="Arquivo", border_style="green")
    else:
        # Caso contrário, cria um painel com o texto direto e título "Texto"
        panel = Panel(texto, title="Texto", border_style="green")
    
    # Imprime o painel no console
    console.print(panel)

def painel_somente_conteudo(texto: str, isArquivo: bool):
    """
    Função que imprime o conteúdo dentro de um painel sem título.
    Parâmetros:
    - texto: str -> pode ser o texto direto ou o caminho de um arquivo.
    - isArquivo: bool -> determina se o parâmetro 'texto' é um arquivo ou um texto direto.
    """
    if isArquivo:
        # Se 'isArquivo' for True, lê o conteúdo de um arquivo
        with open(texto, 'r') as arquivo:
            conteudo = arquivo.read()  # Lê todo o conteúdo do arquivo
            # Cria um painel sem título com o conteúdo do arquivo
            panel = Panel(conteudo)
    else:
        # Caso contrário, cria um painel sem título com o texto direto
        panel = Panel(texto)
    
    # Imprime o painel no console
    console.print(panel)

# Testando as funções
if __name__ == "__main__":
    # Teste com texto direto
    mostrar_painel("Este é um painel com texto", isArquivo=False)  # Mostra um painel com texto direto
    
    # Teste com arquivo
    caminho_arquivo = "BibliotecaRich/Personalizador/meutexto.txt"  # Caminho para o arquivo
    mostrar_painel(caminho_arquivo, isArquivo=True)  # Mostra o conteúdo do arquivo dentro de um painel
    
    # Teste de painel sem título com arquivo
    painel_somente_conteudo(caminho_arquivo, isArquivo=True)  # Mostra o conteúdo do arquivo sem título

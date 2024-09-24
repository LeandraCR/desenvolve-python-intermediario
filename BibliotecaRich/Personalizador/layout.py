from rich.console import Console
from rich.layout import Layout

# Cria uma instância da classe Console da biblioteca 'rich' para imprimir no terminal
console = Console()

def mostrar_layout(texto: str, isArquivo: bool):
    """Imprime um layout com o texto fornecido ou com o conteúdo de um arquivo."""
    
    # Cria um layout vazio
    layout = Layout()
    
    # Divide o layout em três colunas: 'header', 'body' e 'footer'
    layout.split_column(Layout(name="header"), Layout(name="body"), Layout(name="footer"))
    
    if isArquivo:
        # Se for para ler de um arquivo, abre o arquivo em modo de leitura ('r')
        with open(texto, 'r') as arquivo:
            conteudo = arquivo.read()  # Lê todo o conteúdo do arquivo
            layout['body'].update(conteudo)  # Atualiza a área 'body' do layout com o conteúdo do arquivo
    else:
        # Se não for um arquivo, usa o texto diretamente para atualizar o 'body'
        layout['body'].update(texto)
    
    # Imprime o layout no terminal usando o Console
    console.print(layout)

def layout_com_borda(texto: str, isArquivo: bool):
    """Imprime o conteúdo com um layout e borda."""
    
    # Cria um layout vazio
    layout = Layout()
    
    if isArquivo:
        # Se for para ler de um arquivo, abre o arquivo em modo de leitura ('r')
        with open(texto, 'r') as arquivo:
            conteudo = arquivo.read()  # Lê todo o conteúdo do arquivo
            # Atualiza o layout com o conteúdo do arquivo, formatando o texto com uma borda azul
            layout.update(f"[bold blue]{conteudo}[/bold blue]")
    else:
        # Se não for um arquivo, usa o texto diretamente e aplica o estilo com borda azul
        layout.update(f"[bold blue]{texto}[/bold blue]")

    # Imprime o layout formatado no terminal usando o Console
    console.print(layout)

# Testando as funções
if __name__ == "__main__":
    # Teste passando texto diretamente (não é arquivo)
    mostrar_layout("Este é um teste de layout", isArquivo=False)
    
    # Teste passando texto diretamente com borda
    layout_com_borda("Este é um layout com borda", isArquivo=False)

    # Teste com arquivo, fornecendo o caminho para um arquivo de texto
    caminho_arquivo = "BibliotecaRich/Personalizador/meutexto.txt"  # Caminho relativo ao arquivo de texto
    mostrar_layout(caminho_arquivo, isArquivo=True)



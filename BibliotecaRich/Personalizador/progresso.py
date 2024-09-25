from rich.console import Console  # Importa a classe Console da biblioteca Rich para exibir elementos no console
from rich.progress import Progress  # Importa a classe Progress para criar barras de progresso
import time  # Importa a biblioteca time para simular atrasos e pausas

console = Console()  # Cria uma instância de Console para utilizar as funcionalidades do Rich

def barra_progresso_simples():
    """Exibe uma barra de progresso simples."""
    with Progress() as progress:  # Inicializa uma barra de progresso dentro de um bloco `with`, que garante o gerenciamento do recurso
        task = progress.add_task("[green]Carregando...", total=100)  # Cria uma nova tarefa com o texto "Carregando..." e um total de 100
        while not progress.finished:  # Enquanto a tarefa não estiver finalizada
            progress.update(task, advance=5)  # Atualiza a barra avançando 5 unidades
            time.sleep(0.1)  # Aguarda 0,1 segundos antes de continuar para simular o tempo de processamento

def barra_progresso_leitura(texto: str, isArquivo: bool):
    """Exibe uma barra de progresso durante a leitura de um arquivo ou texto."""
    if isArquivo:
        # Caso isArquivo seja True, lê o conteúdo do arquivo e calcula o total de caracteres
        with open(texto, 'r') as arquivo:  # Abre o arquivo no modo leitura
            conteudo = arquivo.read()  # Lê o conteúdo do arquivo
            total = len(conteudo)  # Conta o número de caracteres no arquivo
    else:
        # Caso contrário, o total é o comprimento do texto passado diretamente
        total = len(texto)

    # Exibe a barra de progresso baseada no tamanho do conteúdo
    with Progress() as progress:  # Inicializa uma barra de progresso dentro de um bloco `with`
        task = progress.add_task("[blue]Processando...", total=total)  # Cria uma nova tarefa com o texto "Processando..." e o total calculado
        for i in range(total):  # Itera sobre cada caractere do conteúdo
            progress.update(task, advance=1)  # Atualiza a barra de progresso, avançando uma unidade a cada caractere
            time.sleep(0.05)  # Simula o tempo de processamento com uma pausa de 0,05 segundos

# Testando as funções
if __name__ == "__main__":
    # Teste da barra de progresso simples
    barra_progresso_simples()
    
    # Teste da barra de progresso com arquivo
    caminho_arquivo = "BibliotecaRich/Personalizador/meutexto.txt"  # Define o caminho do arquivo que será lido
    barra_progresso_leitura(caminho_arquivo, isArquivo=True)  # Chama a função para exibir a barra de progresso ao ler o arquivo
    
    # Teste da barra de progresso com texto direto
    barra_progresso_leitura("Este é um texto de teste para a barra de progresso", isArquivo=False)  # Exibe a barra de progresso para um texto


import argparse
from .estilo import aplicar_estilo, destacar_palavra
from .layout import mostrar_layout, layout_com_borda
from .painel import mostrar_painel, painel_somente_conteudo
from .progresso import barra_progresso_simples, barra_progresso_leitura

# Função principal para lidar com a entrada de argumentos
def main():
    # Inicializa o parser de argumentos, com uma descrição do que o script faz
    parser = argparse.ArgumentParser(description="Interface de linha de comando para o pacote Personalizador.")
    
    # Adiciona um argumento posicional obrigatório, que pode ser um texto ou caminho de arquivo
    parser.add_argument("input", type=str, help="Texto ou caminho para o arquivo que deseja formatar.")
    
    # Adiciona uma flag opcional (-a ou --arquivo), para indicar que o input é um arquivo
    parser.add_argument("-a", "--arquivo", action="store_true", help="Indica que o argumento fornecido é o caminho de um arquivo.")
    
    # Adiciona uma opção (-m ou --modulo), obrigatória, que permite ao usuário escolher um dos módulos disponíveis
    parser.add_argument(
        "-m", "--modulo", choices=["estilo", "painel", "progresso", "layout"],
        required=True, help="Escolha o módulo que deseja acessar: 'estilo', 'painel', 'progresso', ou 'layout'."
    )
    
    # Adiciona uma opção (-f ou --funcao), obrigatória, que permite ao usuário escolher uma função específica dentro do módulo selecionado
    parser.add_argument(
        "-f", "--funcao",
        choices=["aplicar_estilo", "destacar_palavra", "mostrar_layout", "layout_com_borda", 
                 "mostrar_painel", "painel_somente_conteudo", "barra_progresso_simples", "barra_progresso_leitura"],
        required=True, help="Escolha a função do módulo que deseja acessar."
    )
    
    # Faz o parsing dos argumentos passados pelo usuário
    args = parser.parse_args()

    # Verifica o módulo selecionado pelo usuário e executa a função correspondente
    if args.modulo == "estilo":
        if args.funcao == "aplicar_estilo":
            # Chama a função aplicar_estilo do módulo estilo
            aplicar_estilo(args.input, args.arquivo)
        elif args.funcao == "destacar_palavra":
            # Chama a função destacar_palavra, com a palavra "texto" sendo destacada no input
            destacar_palavra(args.input, "texto", args.arquivo)

    elif args.modulo == "layout":
        if args.funcao == "mostrar_layout":
            # Chama a função mostrar_layout do módulo layout
            mostrar_layout(args.input, args.arquivo)
        elif args.funcao == "layout_com_borda":
            # Chama a função layout_com_borda do módulo layout
            layout_com_borda(args.input, args.arquivo)

    elif args.modulo == "painel":
        if args.funcao == "mostrar_painel":
            # Chama a função mostrar_painel do módulo painel
            mostrar_painel(args.input, args.arquivo)
        elif args.funcao == "painel_somente_conteudo":
            # Chama a função painel_somente_conteudo do módulo painel
            painel_somente_conteudo(args.input, args.arquivo)

    elif args.modulo == "progresso":
        if args.funcao == "barra_progresso_simples":
            # Chama a função barra_progresso_simples do módulo progresso
            barra_progresso_simples()
        elif args.funcao == "barra_progresso_leitura":
            # Chama a função barra_progresso_leitura do módulo progresso
            barra_progresso_leitura(args.input, args.arquivo)

# Verifica se o script está sendo executado diretamente (e não importado como módulo)
if __name__ == "__main__":
    main()

    # Como usar: 
    # cd BibliotecaRich
    # python -m Personalizador.main "Este é um exemplo de texto" -m estilo -f aplicar_estilo 

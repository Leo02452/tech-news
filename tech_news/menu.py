import sys


# Requisito 12
def analyzer_menu():
    option = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por tag;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair."
    )

    if option == 0:
        input("Digite quantas notícias serão buscadas:")
    elif option == 1:
        input("Digite o título:")
    elif option == 2:
        input("Digite a data no formato aaaa-mm-dd:")
    elif option == 3:
        input("Digite a tag:")
    elif option == 4:
        input("Digite a categoria:")
    else:
        sys.stderr.write("Opção inválida")

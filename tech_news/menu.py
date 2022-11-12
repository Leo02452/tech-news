import sys
from tech_news.analyzer.ratings import top_5_news, top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_tag,
    search_by_category
)
from tech_news.scraper import get_tech_news


def print_top_five(option):
    if option == "5":
        print(top_5_news())
    elif option == "6":
        print(top_5_categories())


def search_by(option, param):
    if option == "1":
        print(search_by_title(param))
    elif option == "2":
        print(search_by_date(param))
    elif option == "3":
        print(search_by_tag(param))
    else:
        print(search_by_category(param))


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

    parameters_options = {
        "1": "Digite o título:",
        "2": "Digite a data no formato aaaa-mm-dd:",
        "3": "Digite a tag:",
        "4": "Digite a categoria:",
    }

    if option == "0":
        news_quantity = input("Digite quantas notícias serão buscadas:")
        print(get_tech_news(news_quantity))
    elif option in ["1", "2", "3", "4"]:
        parameter = input(parameters_options[option])
        search_by(option, parameter)
    elif option in ["5", "6"]:
        print_top_five(option)
    elif option == "7":
        print("Encerrando script")
    else:
        sys.stderr.write("Opção inválida\n")

import requests
from time import sleep

# Requisito 1
def fetch(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        sleep(2)
    except (requests.HTTPError, requests.ReadTimeout):
        pass
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""

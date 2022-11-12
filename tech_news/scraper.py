import requests
from time import sleep
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
        sleep(1)
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    news = []
    for new in selector.css('article.entry-preview'):
        news.append(
            new.css('h2.entry-title > a::attr(href)').get()
        )
    return news


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page = selector.css('a.next::attr(href)').get()

    return next_page


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    return {
                "url": selector.css('link[rel=canonical]::attr(href)').get(),
                "title": selector.css('h1.entry-title::text').get().strip(),
                "timestamp": selector.css('li.meta-date::text').get(),
                "writer": selector.css('span.author > a::text').get(),
                "comments_count": len(
                    selector.css('div.coment-content').getall()
                ),
                "summary": "".join(
                    selector.css(
                        "div.entry-content > p:nth-of-type(1) *::text"
                    ).getall()
                ).strip(),
                "tags": selector.css('a[rel=tag]::text').getall(),
                "category": selector.css('span.label::text').get(),
            }


# Requisito 5
def get_tech_news(amount):
    url = 'https://blog.betrybe.com/'
    news = []
    while len(news) <= amount:
        content = fetch(url)
        url_news_list = scrape_novidades(content)
        for url_new in url_news_list:
            new_content = fetch(url_new)
            news.append(scrape_noticia(new_content))
        url = scrape_next_page_link(content)
    create_news(news[:amount])
    return news[:amount]

from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news_list = find_news()
    news_list.sort(
        reverse=True, key=lambda new: new['comments_count']
    )
    return [
            (new['title'], new['url'])
            for new in news_list
        ][:5]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""

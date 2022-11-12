import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    return [
        (new['title'], new['url'])
        for new in search_news({'title': {'$regex': title, '$options': 'i'}})
    ]


# Requisito 7
def search_by_date(date):
    try:
        isodate = datetime.date.fromisoformat(date)
        db_date = f"{isodate.day:02}/{isodate.month:02}/{isodate.year:04}"
        return [
            (new['title'], new['url'])
            for new in search_news({'timestamp': db_date})
        ]
    except ValueError:
        raise ValueError('Data inválida')


# Requisito 8
def search_by_tag(tag):
    return [
            (new['title'], new['url'])
            for new in search_news({'tags': {'$regex': tag, '$options': 'i'}})
        ]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""

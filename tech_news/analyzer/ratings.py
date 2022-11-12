from tech_news.database import find_news
import collections


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
    news_list = find_news()
    categories_list = [new['category'] for new in news_list]

    categories_occurrences = collections.Counter(categories_list)
    new_categories_list = list(categories_occurrences.keys())
    new_categories_list.sort()
    new_categories_list.sort(
        key=lambda i: categories_occurrences[i], reverse=True
    )

    return new_categories_list[:5]

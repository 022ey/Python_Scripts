from newspaper import Article


def parse_article(url):
    article = Article(url)

    article.download()
    article.parse()
    article.nlp()
    
    return article
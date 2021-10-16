import requests


class Inshorts:
    def __init__(self, lang: str) -> None:
        self.base = f"https://inshorts.com/api/{lang}/"
        self.session = requests.Session()

    def request(self, url: str, params: dict = {}):
        res = self.session.get(url, params=params, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
        })
        return res.json()

    def by_catagory(self, category: str, max_result: int = 10, incl_cdata: str = "true"):
        return self.request(self.base + "news", {
            "category": category,
            "max_limit": max_result,
            "include_card_data": incl_cdata
        })

    def by_topic(self, topic: str, page: int = 1, type__: str = "NEWS_CATEGORY"):
        return self.request(self.base + f"search/trending_topics/{topic}?page={page}&type={type__}")

    @property
    def all_news(self):
        return self.by_catagory("all_news")

    @property
    def trending(self):
        return self.by_catagory("trending")

    @property
    def top_stories(self):
        return self.by_catagory("top_stories")


ins = Inshorts("en")
print(ins.by_topic("technology"))

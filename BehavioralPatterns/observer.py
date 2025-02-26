# Observer design pattern

# Observer Class
class Subscriber:
    def update(self, article):
        pass

# Concrete Observer
class NewsSubscriber(Subscriber):
    def __init__(self, name):
        self.name = name

    def update(self, article):
        print(f'{self.name} received the article: {article}')

# Subject class
class NewsAgency:
    def __init__(self):
        self.subscribers = []
        self.article = ''

    def attach(self, subscriber):
        self.subscribers.append(subscriber)

    def detach(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify(self):
        for subscriber in self.subscribers:
            subscriber.update(self.article)

    def add_article(self, article):
        self.article = article
        self.notify()

news_agency = NewsAgency()

subscriber1 = NewsSubscriber('Alice')
subscriber2 = NewsSubscriber('Bob')

news_agency.attach(subscriber1)
news_agency.attach(subscriber2)

news_agency.add_article("Breaking News: Observer Pattern in Python!")
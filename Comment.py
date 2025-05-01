class Comment:
    
    def __init__(self, site, url, topic, message, sentiment):
        self.site = site
        self.url = url
        self.topic = topic
        self.message = message
        self.sentiment = sentiment
    
    def __str__(self):
        return f"{self.site},{self.topic},{self.sentiment},{self.message},{self.url}"

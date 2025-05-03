class Comment:
    
    def __init__(self, site, url, topic, message, sentiment):
        self.site = site
        self.url = url
        self.topic = topic
        self.message = message
        self.sentiment = sentiment
    
    def __str__(self):
        return f'{self.site},{self.topic},{self.sentiment},"{self.message}",{self.url}'

def commentsToCSV(listofComments, path):
    with open(path, 'w') as file:
        file.write('Site,Topic,Polarity,Comment,Article URL\n')
        for comment in listofComments:
            comment.message.replace('"', '""')
            file.write(f'{comment.site},{comment.topic},{comment.sentiment},"{comment.message.replace('"','""')}",{comment.url}\n')
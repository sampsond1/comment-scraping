import requests
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from Comment import commentsToCSV
from Comment import Comment



def DeseretCommentRequest(url : str, topic : str):
    '''
    Takes two strings, a url of a KSL news article and a topic for that article. Returns a list of `Comment` objects, 
    one for each comment on the article.

    Uses a request from the Deseret News API to get the comments.
    '''

    # Gets the Post ID from the website HTML, which is used in the API call
    response = requests.get(url)
    print('Status code is', response.status_code)

    string = re.search(r'"post_id", "[A-Z0-9]+', response.text).group()
    postId = string[12:]

    print('postId is', postId)

    # Sets up headers and parameters for the API (curlconverter.com to get them)
    headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
    'content-type': 'application/json',
    'origin': 'https://www.deseret.com',
    'priority': 'u=1, i',
    'referer': 'https://www.deseret.com/',
    'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    'x-coral-client-id': '7e2d0ca0-26d0-11f0-bdea-77dd339da50f',
    }

    params = {
        'query': '',
        'id': '72fb962160f4024e41596efd0aa7a172',
        'variables': '{"storyID":"' + postId + '","storyURL":"' + url + '","commentsOrderBy":"CREATED_AT_DESC","tag":null,"storyMode":null,"flattenReplies":false,"ratingFilter":null,"refreshStream":false}',
    }

    # API request
    response = requests.get('https://deseretnews.coral.coralproject.net/api/graphql', params=params, headers=headers)

    # Error handling
    if response.status_code != 200:
        print('ERROR: Request returned status code', response.status_code)
        return []
    else:
        print('Request returned status code', response.status_code)

    # The comments and replies on Deseret News are stored recursively in the JSON. parsecomments() is a recursive
    # function that scrapes them all
    comments = response.json()['data']['story']['comments']
    processedComments = []

    def parsecomments(root,list):
        for comment in root['edges']:
            message = re.sub(r'<\/?..?.?.?>|<blockquote>.*<\/blockquote>|\n', '', comment['node']['body'])
            analyzer = SentimentIntensityAnalyzer()
            sentiment = analyzer.polarity_scores(message)['compound']
            newComment = Comment('Deseret', url, topic, message, sentiment)
            list.append(newComment)
            if 'replies' in comment['node']:
                parsecomments(comment['node']['replies'], processedComments)
    
    parsecomments(comments, processedComments)

    return processedComments

if __name__ == "__main__":
    comments = DeseretCommentRequest('https://www.deseret.com/u-s-world/2025/04/07/british-prime-minister-reaction-trump-tariff-us-uk/', 'Politics')
    commentsToCSV(comments, 'Deseretcomments.csv')


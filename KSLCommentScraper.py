import requests
from Comment import Comment
from Comment import commentsToCSV
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def KSLCommentRequest(url : str, topic : str):
    '''
    Takes two strings, a url of a KSL news article and a topic for that article. Returns a list of `Comment` objects, 
    one for each of up to 200 comments from that news article. The url must have `https://www.ksl.com/article/` at the beginning, as the
    article code needed for the api is grabbed using string indexing.

    Uses a request from the KSL API to get the comments.
    '''

    COMMENTS_TO_REQUEST = '200'

    headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
    'priority': 'u=1, i',
    'referer': url,
    'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    }

    params = {
        'page': '1',
        'pageSize': COMMENTS_TO_REQUEST,
        'sort': 'oldest',
        'showAllComments': 'false',
    }

    article_code = url[28:36] # Needs the https:// to work. Could use regex for better generalizablitiy
    api_url = 'https://www.ksl.com/api/2017/comments/' + article_code

    response = requests.get(api_url, params=params, headers=headers)

    if response.status_code != 200:
        print('ERROR: Request returned status code', response.status_code)
        return []
    else:
        print('Request returned status code', response.status_code)

    commentDict = response.json()['comments']
    processedComments = []

    for comment in commentDict:
        message = ''
        for line in comment['message']:
            message += line
            message += ' '
        analyzer = SentimentIntensityAnalyzer()
        sentiment = analyzer.polarity_scores(message)['compound']
        newComment = Comment('KSL', url, topic, message, sentiment)
        processedComments.append(newComment)
    
    return processedComments
        

if __name__ == "__main__":
    comments = KSLCommentRequest('https://www.ksl.com/article/51304393/us-senate-rejects-bill-to-rein-in-trump-tariffs-as-economy-contracts', 'Politics')
    commentsToCSV(comments, 'KSLcomments.csv')

from DeseretCommentScraper import DeseretCommentRequest
from KSLCommentScraper import KSLCommentRequest
from Comment import commentsToCSV

outputList = []
with open('./sampledata/deseretbusiness.txt','r') as deseretbusiness:
    num = 0
    for url in deseretbusiness:
        commentList = DeseretCommentRequest(url.replace('\n', ''), 'Business')
        outputList += commentList
        num += len(commentList)
    print(f'Successfully scraped {num} Business comments from Deseret')
with open('./sampledata/deseretpolitics.txt','r') as deseretpolitics:
    num = 0
    for url in deseretpolitics:
        commentList = DeseretCommentRequest(url.replace('\n', ''), 'Politics')
        outputList += commentList
        num += len(commentList)
    print(f'Successfully scraped {num} Politics comments from Deseret')
with open('./sampledata/deseretsports.txt','r') as deseretsports:
    num = 0
    for url in deseretsports:
        commentList = DeseretCommentRequest(url.replace('\n', ''), 'Sports')
        outputList += commentList
        num += len(commentList)
    print(f'Successfully scraped {num} Sports comments from Deseret')
with open('./sampledata/kslbusiness.txt', 'r') as kslbusiness:
    num = 0
    for url in kslbusiness:
        commentList = KSLCommentRequest(url.replace('\n', ''), 'Business')
        outputList += commentList
        num += len(commentList)
    print(f'Successfully scraped {num} Business comments from Deseret')
with open('./sampledata/kslpolitics.txt', 'r') as kslpolitics:
    num = 0
    for url in kslpolitics:
        commentList = KSLCommentRequest(url.replace('\n', ''), 'Politics')
        outputList += commentList
        num += len(commentList)
    print(f'Successfully scraped {num} Politics comments from Deseret')
with open('./sampledata/kslsports.txt', 'r') as kslsports:
    num = 0
    for url in kslsports:
        commentList = KSLCommentRequest(url.replace('\n', ''), 'Sports')
        outputList += commentList
        num += len(commentList)
    print(f'Successfully scraped {num} Sports comments from Deseret')
print(f'Scraped {len(outputList)} comments in total. Writing to CSV...')
commentsToCSV(outputList, './sampledata/commentdata.csv')
print('CSV written!')
from DeseretCommentScraper import DeseretCommentRequest
from KSLCommentScraper import KSLCommentRequest
from Comment import commentsToCSV
import sys
import random

'''
This code scrapes the urls in six .txt files: `deseretbusiness.txt`, `deseretpolitics.txt`, `deseretsports.txt`, 
`kslbusiness.txt`, `kslpolitics.txt`, and `kslsports.txt`. I manually copied and pasted those urls from between the
dates of April 6th and April 12th, but some code could pretty easily be arranged to store urls from the home page
of each news sites and scrape the topic tag from each one.

Arguments:'1' to scrape the websites to commentdata.csv, '2' to create a random sample (randomsample.csv) from those comments,
and 'all' to do both.
'''

if sys.argv[1] == '1' or sys.argv[1] == 'all':
    outputList = []
    with open('./data/deseretbusiness.txt','r') as deseretbusiness:
        num = 0
        for url in deseretbusiness:
            commentList = DeseretCommentRequest(url.replace('\n', ''), 'Business')
            outputList += commentList
            num += len(commentList)
        print(f'Successfully scraped {num} Business comments from Deseret')
    with open('./data/deseretpolitics.txt','r') as deseretpolitics:
        num = 0
        for url in deseretpolitics:
            commentList = DeseretCommentRequest(url.replace('\n', ''), 'Politics')
            outputList += commentList
            num += len(commentList)
        print(f'Successfully scraped {num} Politics comments from Deseret')
    with open('./data/deseretsports.txt','r') as deseretsports:
        num = 0
        for url in deseretsports:
            commentList = DeseretCommentRequest(url.replace('\n', ''), 'Sports')
            outputList += commentList
            num += len(commentList)
        print(f'Successfully scraped {num} Sports comments from Deseret')
    with open('./data/kslbusiness.txt', 'r') as kslbusiness:
        num = 0
        for url in kslbusiness:
            commentList = KSLCommentRequest(url.replace('\n', ''), 'Business')
            outputList += commentList
            num += len(commentList)
        print(f'Successfully scraped {num} Business comments from Deseret')
    with open('./data/kslpolitics.txt', 'r') as kslpolitics:
        num = 0
        for url in kslpolitics:
            commentList = KSLCommentRequest(url.replace('\n', ''), 'Politics')
            outputList += commentList
            num += len(commentList)
        print(f'Successfully scraped {num} Politics comments from Deseret')
    with open('./data/kslsports.txt', 'r') as kslsports:
        num = 0
        for url in kslsports:
            commentList = KSLCommentRequest(url.replace('\n', ''), 'Sports')
            outputList += commentList
            num += len(commentList)
        print(f'Successfully scraped {num} Sports comments from Deseret')
    print(f'Scraped {len(outputList)} comments in total. Writing to CSV...')
    commentsToCSV(outputList, './data/commentdata.csv')
    print('CSV written!')
if sys.argv[1] == '2' or sys.argv[1] == 'all':
    with open('./data/commentdata.csv', 'r', encoding='utf-8') as allcomments:
        lines = allcomments.readlines()

    # Stores the line indices of each treatment in separate lists.    
    DesBus = []
    DesPol = []
    DesSpo = []
    KSLBus = []
    KSLPol = []
    KSLSpo = []
    for i in range(len(lines)):
        if lines[i].startswith('Deseret,Business'):
            DesBus.append(i)
        elif lines[i].startswith('Deseret,Politics'):
            DesPol.append(i)
        elif lines[i].startswith('Deseret,Sports'):
            DesSpo.append(i)
        elif lines[i].startswith('KSL,Business'):
            KSLBus.append(i)
        elif lines[i].startswith('KSL,Politics'):
            KSLPol.append(i)
        elif lines[i].startswith('KSL,Sports'):
            KSLSpo.append(i)
    
    # Chooses 100 random lines from each list to write to a new file.
    with open('./data/randomsample.csv', 'w', encoding='utf-8') as randomsample:
        randomsample.write(lines[0])
        for list in (DesBus, DesPol, DesSpo, KSLBus, KSLPol, KSLSpo):
            for i in random.sample(list, 100):
                randomsample.write(lines[i])
else:
    print("Please use '1' for scraping all the comments, '2' for taking a random sample from them, and 'all' for both")
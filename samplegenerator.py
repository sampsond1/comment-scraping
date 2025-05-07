from DeseretCommentScraper import DeseretCommentRequest
from KSLCommentScraper import KSLCommentRequest
from Comment import commentsToCSV
import sys
import random

if sys.argv[1] == '1' or sys.argv[1] == 'all':
    # This
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
if sys.argv[1] == '2' or sys.argv[1] == 'all':
    # That
    with open('./sampledata/commentdata.csv', 'r', encoding='utf-8') as allcomments:
        lines = allcomments.readlines()
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
    with open('./sampledata/randomsample.csv', 'w', encoding='utf-8') as randomsample:
        randomsample.write(lines[0])
        for list in (DesBus, DesPol, DesSpo, KSLBus, KSLPol, KSLSpo):
            for i in random.sample(list, 100):
                randomsample.write(lines[i])
else:
    print("Please use '1' for scraping all the comments, '2' for taking a random sample from them, and 'all' for both")
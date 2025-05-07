import sys
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt

df = pd.read_csv('./sampledata/randomsample.csv')

if sys.argv[1] == '1' or sys.argv[1] == 'all':
    model = ols('Polarity ~ C(Site) + C(Topic) + C(Site):C(Topic)', data = df).fit()
    anovaTable = sm.stats.anova_lm(model, typ=1)
    modelSumSq = anovaTable.at['C(Site)','sum_sq'] + anovaTable.at['C(Topic)','sum_sq'] + anovaTable.at['C(Site):C(Topic)','sum_sq']
    etaSq = modelSumSq / (modelSumSq + anovaTable.at['Residual', 'sum_sq'])
    partEtaSqSite = anovaTable.at['C(Site)','sum_sq'] / (anovaTable.at['C(Site)','sum_sq'] + anovaTable.at['Residual','sum_sq'])
    partEtaSqTopic = anovaTable.at['C(Topic)','sum_sq'] / (anovaTable.at['C(Topic)','sum_sq'] + anovaTable.at['Residual','sum_sq'])
    partEtaSqInt = anovaTable.at['C(Site):C(Topic)','sum_sq'] / (anovaTable.at['C(Site):C(Topic)','sum_sq'] + anovaTable.at['Residual','sum_sq'])
    with open('./results/results.txt', 'w') as file:
        file.write(str(anovaTable))
        file.write('\n')
        file.write(f'\nEta-squared for model is {etaSq}.\n')
        file.write(f'Partial eta-squared for Site is {partEtaSqSite}.\n')
        file.write(f'Partial eta-squared for Topic is {partEtaSqTopic}.\n')
        file.write(f'Partial eta-squared for interaction is {partEtaSqInt}.\n')
if sys.argv[1] == '2' or sys.argv[1] == 'all':
    df['Polarity'].hist(by=df['Site'], bins=10, sharey = True)
    plt.savefig('./results/histbysite.png')
    plt.clf()
    df['Polarity'].hist(by=df['Topic'], bins=10, sharey = True)
    plt.savefig('./results/histbytopic.png')
    plt.clf()
    df.boxplot('Polarity', 'Site', color = {'boxes':'C0', 'whiskers':'black', 'medians':'black','caps':'black'}, patch_artist = True)
    plt.savefig('./results/boxbysite.png')
    plt.clf()
    df.boxplot('Polarity', 'Topic', color = {'boxes':'C0', 'whiskers':'black', 'medians':'black','caps':'black'}, patch_artist = True)
    plt.savefig('./results/boxbytopic.png')
    plt.clf()
    desbusmean = df.loc[(df['Site'] == 'Deseret') & (df['Topic'] == 'Business')]['Polarity'].mean()
    despolmean = df.loc[(df['Site'] == 'Deseret') & (df['Topic'] == 'Politics')]['Polarity'].mean()
    desspomean = df.loc[(df['Site'] == 'Deseret') & (df['Topic'] == 'Sports')]['Polarity'].mean()
    kslbusmean = df.loc[(df['Site'] == 'KSL') & (df['Topic'] == 'Business')]['Polarity'].mean()
    kslpolmean = df.loc[(df['Site'] == 'KSL') & (df['Topic'] == 'Politics')]['Polarity'].mean()
    kslspomean = df.loc[(df['Site'] == 'KSL') & (df['Topic'] == 'Sports')]['Polarity'].mean()
    y1 = [desbusmean, despolmean, desspomean]
    y2 = [kslbusmean, kslpolmean, kslspomean]
    x = ['Business', 'Politics', 'Sports']
    plt.plot(x, y1, label='Deseret')
    plt.plot(x, y2, label = 'KSL')
    plt.title('Interaction')
    plt.ylim((-1,1))
    plt.legend()
    plt.savefig('./results/interaction.png')
    plt.clf()
    # model.resid
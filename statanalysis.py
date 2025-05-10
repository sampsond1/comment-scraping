import sys
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt

'''
This code runs the statistical analysis on the data, as well as visualizes it using graphs and tables.
Arguments: '1' for data analysis exported to results.txt, '2' for data visualization in the directory 'results',
and 'all' for both.
'''

# Reads the csv as a DataFrame and runs a linear least squares model on it.
df = pd.read_csv('./data/randomsample.csv')
model = ols('Polarity ~ C(Site) + C(Topic) + C(Site):C(Topic)', data = df).fit()

# This separates the DataFrame into the six different treatments to calculate descriptive statistics by treatment.
desbus = df.loc[(df['Site'] == 'Deseret') & (df['Topic'] == 'Business')]['Polarity']
despol = df.loc[(df['Site'] == 'Deseret') & (df['Topic'] == 'Politics')]['Polarity']
desspo = df.loc[(df['Site'] == 'Deseret') & (df['Topic'] == 'Sports')]['Polarity']
kslbus = df.loc[(df['Site'] == 'KSL') & (df['Topic'] == 'Business')]['Polarity']
kslpol = df.loc[(df['Site'] == 'KSL') & (df['Topic'] == 'Politics')]['Polarity']
kslspo= df.loc[(df['Site'] == 'KSL') & (df['Topic'] == 'Sports')]['Polarity']

if sys.argv[1] == '1' or sys.argv[1] == 'all':
    # Creates the ANOVA table
    anovaTable = sm.stats.anova_lm(model, typ=1)

    # Calculates eta-squared and partial eta-squared statistics of interest.
    modelSumSq = anovaTable.at['C(Site)','sum_sq'] + anovaTable.at['C(Topic)','sum_sq'] + anovaTable.at['C(Site):C(Topic)','sum_sq']
    etaSq = modelSumSq / (modelSumSq + anovaTable.at['Residual', 'sum_sq'])
    partEtaSqSite = anovaTable.at['C(Site)','sum_sq'] / (anovaTable.at['C(Site)','sum_sq'] + anovaTable.at['Residual','sum_sq'])
    partEtaSqTopic = anovaTable.at['C(Topic)','sum_sq'] / (anovaTable.at['C(Topic)','sum_sq'] + anovaTable.at['Residual','sum_sq'])
    partEtaSqInt = anovaTable.at['C(Site):C(Topic)','sum_sq'] / (anovaTable.at['C(Site):C(Topic)','sum_sq'] + anovaTable.at['Residual','sum_sq'])
    
    # Writes the ANOVA table, eta-squareds, and descriptive statistics to resulst.txt.
    with open('./results/results.txt', 'w') as file:
        file.write(str(anovaTable))
        file.write('\n')
        file.write(f'\nEta-squared for model is {etaSq}.\n')
        file.write(f'Partial eta-squared for Site is {partEtaSqSite}.\n')
        file.write(f'Partial eta-squared for Topic is {partEtaSqTopic}.\n')
        file.write(f'Partial eta-squared for interaction is {partEtaSqInt}.\n\n')

        file.write(f'Deseret - Business: Mean - {desbus.mean():.5f}  Std dev - {desbus.std():.5f}.\n')
        file.write(f'Deseret - Politics: Mean - {despol.mean():.5f}  Std dev - {despol.std():.5f}.\n')
        file.write(f'Deseret - Sports: Mean - {desspo.mean():.5f}  Std dev - {desspo.std():.5f}.\n')
        file.write(f'KSL - Business: Mean - {kslbus.mean():.5f}  Std dev - {kslbus.std():.5f}.\n')
        file.write(f'KSL - Politics: Mean - {kslpol.mean():.5f}  Std dev - {kslpol.std():.5f}.\n')
        file.write(f'KSL - Sports: Mean - {kslspo.mean():.5f}  Std dev - {kslspo.std():.5f}.\n')

if sys.argv[1] == '2' or sys.argv[1] == 'all':
    
    # Histogram by Site
    df['Polarity'].hist(by=df['Site'], bins=10, sharey = True)
    plt.savefig('./results/histbysite.png')
    plt.clf()
    
    # Histogram by Topic
    df['Polarity'].hist(by=df['Topic'], bins=10, sharey = True)
    plt.savefig('./results/histbytopic.png')
    plt.clf()

    # Boxplot by Site
    df.boxplot('Polarity', 'Site', color = {'boxes':'C0', 'whiskers':'black', 'medians':'black','caps':'black'}, patch_artist = True)
    plt.savefig('./results/boxbysite.png')
    plt.clf()

    # Boxplot by Topic
    df.boxplot('Polarity', 'Topic', color = {'boxes':'C0', 'whiskers':'black', 'medians':'black','caps':'black'}, patch_artist = True)
    plt.savefig('./results/boxbytopic.png')
    plt.clf()

    # Interaction graph
    y1 = [desbus.mean(), despol.mean(), desspo.mean()]
    y2 = [kslbus.mean(), kslpol.mean(), kslspo.mean()]
    x = ['Business', 'Politics', 'Sports']
    plt.plot(x, y1, label='Deseret')
    plt.plot(x, y2, label = 'KSL')
    plt.title('Interaction')
    plt.ylim((-1,1))
    plt.legend()
    plt.savefig('./results/interaction.png')
    plt.clf()

    # Histogram of residuals
    plt.hist(model.resid, bins = 10)
    plt.xlim(-1,1)
    plt.title('Histogram of Residuals')
    plt.savefig('./results/residuals.png')
    plt.clf()

    # Histograms by Treatment
    figure, axis = plt.subplots(2,3)
    axis[0,0].hist(desbus, bins = [-1+(0.2*i) for i in range(0,11)])
    axis[0,0].set_title('Deseret - Business')
    axis[0,1].hist(despol, bins = [-1+(0.2*i) for i in range(0,11)])
    axis[0,1].set_title('Deseret - Politics')
    axis[0,2].hist(desspo, bins = [-1+(0.2*i) for i in range(0,11)])
    axis[0,2].set_title('Deseret - Sports')
    axis[1,0].hist(kslbus, bins = [-1+(0.2*i) for i in range(0,11)])
    axis[1,0].set_title('KSL - Business')
    axis[1,1].hist(kslpol, bins = [-1+(0.2*i) for i in range(0,11)])
    axis[1,1].set_title('KSL - Politics')
    axis[1,2].hist(kslspo, bins = [-1+(0.2*i) for i in range(0,11)])
    axis[1,2].set_title('KSL - Sports')
    figure.tight_layout()
    plt.savefig('./results/histbytreatment.png')
    plt.clf()

    # Histogram of Polarity
    plt.hist(df['Polarity'])
    plt.title('Polarity')
    plt.savefig('./results/histtotal.png')
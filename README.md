# Web Scraping News Comments

This is a project I did the summer of 2025 to learn more about data scraping and practice my data analysis. I designed a web scraper that scraped comments off of Deseret News ([https://deseret.com](https://deseret.com)) and KSL News ([https://ksl.com](https://ksl.com)). I then used an ANOVA model to analyze the data and wrote up my findings in a mini research paper. This project was mostly to learn the programming side, so the experiment design was a little scuffed. However, I acknowledged this in my paper when drawing conclusions and described what I'd do different with more resources.

## Features
- Scrape comments from a news site with just the URL!
- 9005 comments from 218 news sites
- An ANOVA analysis of the polarity of those comments
- A 1600 word write-up of my findings
- A LOT of graphs and charts (some of them are even useful)

## Skills
- Python libraries:
    - `requests`
    - `re` (RegEx)
    - `pandas`
    - `statsmodels`
    - `matplotlib`
- Web scraping from website APIs
- ANOVA analysis of categorical variables
- Technical writing of results and findings
- Data visualization

## Guide
- `Comment.py` is an object that the scrapers use to store the comments.
- `DeseretCommentScraper.py` and `KSLCommentScraper.py` are modules for scraping a news article from just the URL.
- `samplegenerator.py` is where the magic happens: this scrapes all the data from the urls I provided.
- `statanalysis.py` does the analysis of the data, including an ANOVA and various graphs
- `AnalysisPaper.md` is my write-up of my findings.
- `data` contains six .txt files of the urls I found to scrape, as well as the output .csv files from `samplegenerator.py`.
- `results` includes the output files from `statanalysis.py`.
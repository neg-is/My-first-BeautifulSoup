from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)

all_articles = soup.find_all(name="a", class_="storylink")
# print(article)

article_texts = []
article_links = []

for article_tag in all_articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

print(article_texts)
print(article_links)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
print(article_upvotes)

top_5_scores = sorted(article_upvotes, reverse=True)[:5]
print(top_5_scores)

top_5_texts = []
top_5_links = []
for i in top_5_scores:
    index = article_upvotes.index(i)
    text = article_texts[index]
    top_5_texts.append(text)
    link = article_links[index]
    top_5_links.append(link)

print(top_5_links)
print(top_5_texts)

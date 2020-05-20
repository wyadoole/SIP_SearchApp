# import libraries
import nltk
from newspaper import Article

url = 'https://www.crummy.com/software/BeautifulSoup/bs4/doc/#problems-after-installation'
article = Article(url)

article.download()
article.parse()
nltk.download('punkt')
article.nlp()

article.authors

article.publish_date

article.top_image

print(article.text)

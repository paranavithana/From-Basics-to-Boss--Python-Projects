from bs4 import BeautifulSoup

soup=BeautifulSoup("<title>test</Title>","html.parser")
print(soup.title.text)

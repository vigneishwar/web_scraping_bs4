from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = "https://www.amazon.com.au/s?k=playstation+5&rh=n%3A4852675051%2Cn%3A8019362051&dc&ds=v1%3A%2Bx1VAvgBxCdlJ" \
      "%2FamqYrHIh3N1Qd4L7GtjRzqHeH2U%2Bk&qid=1672235589&rnid=5367991051&sprefix=playst%2Caps%2C288&ref=sr_nr_n_3 "

HEADERS = ({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/108.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

webpage = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(webpage.content, "html.parser")

# fetching all the links in the <a> tags

links = soup.find_all("a", attrs={'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style '
                                           'a-text-normal'})
#print(links[0])
extracted_link = links[0].get('href')
#print(extracted_link)
final_link = "https://amazon.com.au" + extracted_link
# print(final_link)

new_webpage =requests.get(final_link, headers=HEADERS)
# print(new_webpage)

new_soup = BeautifulSoup(new_webpage.content, "html.parser")
# print(new_soup)

# extracting the title

extracted_title = new_soup.find("span", attrs={"id": 'productTitle'}).text.strip()
print(extracted_title)

extracted_price = new_soup.find("span", attrs={"class": 'a-price a-text-price'}).\
    find("span", attrs={"class": 'a-offscreen'}).text

print(extracted_price)

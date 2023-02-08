
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.flipkart.com/search?q=camera&sid=jek%2Cp31%2Ctrv&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_3_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_3_6_na_na_na&as-pos=3&as-type=RECENT&suggestionId=camera%7CDSLR+%26+Mirrorless&requestId=92aedfee-9d85-42f1-ae2f-d60898ce4433&as-searchtext=camera"

response = requests.get(url)
# print(response.content)
htmlcontent = response.content

soup = BeautifulSoup(htmlcontent, 'html.parser')
# print(soup.prettify())
# print(soup.title)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p.string)
# print(soup.a)
# print(soup.find_all('a'))

# for link in soup.find_all('a'):
# #     link.get('href')
# #     print(link)

# for image in soup.find_all('img'):
#     image.get('src')
#     print(image)

# product = soup.find_all('div', class_='_13oc-S')
# print(product)

titles=[]
prices=[]
images=[]

for d in soup.find_all('div', attrs={'class':'_2kHMtA'}):
    title = d.find_all('div', attrs={'class':'_4rR01T'})
    # print(title.string)

    price = d.find_all('div', attrs={'class':'_30jeq3 _1_WHN1'})
    # print(price)

    image = d.find('img', attrs={'class':'_396cs4'})
    # print(image.get('src'))

    titles.append(title)
    prices.append(price)
    images.append(image.get('src'))

    # print(titles)
    print(prices)
    # print(images)
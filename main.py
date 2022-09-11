import requests
import json
from bs4 import BeautifulSoup

url = "https://www.pravda.com.ua/rus/news/"
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

# link = soup.find('div', class_="article_header").find('a')["href"]
# print(link)
# who_are_u = "ого, ты тоже строка"
# if type(link) == type(who_are_u):
#     if link[0] == "/":
#         link = "https://www.pravda.com.ua" + link
#         print(link)
#         response1 = requests.get(link)
#         response1.raise_for_status()
#         soup = BeautifulSoup(response1.text, 'html.parser')
#         title = soup.find('h1', class_="post_title")
#         print(title.text)
#         for text_news in soup.find_all('p'):
#             print(text_news.get_text())
#     else:
#         response1 = requests.get(link)
#         response1.raise_for_status()
#         soup = BeautifulSoup(response1.text, 'html.parser')
#         title = soup.find('h1', class_="page-heading")
#         print(title.text)
#         for text_news in soup.find_all('p'):
#             #del text_news.tag['p']
#             print(text_news.get_text())




for link in soup.find_all('div', class_="article_header"):
    url1 = link.find('a')["href"]
    #print(url1)
    who_are_u = "ого, ты тоже строка"
    if type(url1) == type(who_are_u):
        try:
            if url1[0] == "/":
                url1 = "https://www.pravda.com.ua" + url1

                response1 = requests.get(url1)
                response1.raise_for_status()
                soup = BeautifulSoup(response1.text, 'html.parser')
                title_news = soup.find('h1', class_="post_title")
                text_all = ""
                for text_news in soup.find_all('p'):
                    text_all = text_all + " " + text_news.get_text()
                lite = {
                    'items': [
                        {
                            'title': title_news.text,
                            'text': text_all,
                            'site_url': url1
                        }
                    ]
                }
                with open('my.json', 'a', newline='\n') as file:
                    json.dump(lite, file, indent=2)
                print(lite)
            else:
                #print('сработало')
                response1 = requests.get(url1)
                response1.raise_for_status()
                #print('варим суп')
                soup = BeautifulSoup(response1.text, 'html.parser')
                # print(url1)
                title = soup.find('h1', class_="page-heading")
                text_all = ""
                for text_news in soup.find_all('p'):
                    text_all = text_all + " " + text_news.get_text()
                lite = {
                    'items': [
                        {
                            'title': title.text,
                            'text': text_all,
                            'site_url': url1
                        }
                    ]
                }
                with open('my.json', 'a', newline='\n') as file:
                    json.dump(lite, file, indent=2)
                print('OPA')
        except:
            print("ERROR")
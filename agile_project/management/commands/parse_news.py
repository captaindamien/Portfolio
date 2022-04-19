import requests
from bs4 import BeautifulSoup


habr = "https://habr.com"

portfolio_url = "https://habr.com/ru/search/?q=%D0%9F%D0%BE%D1%80%D1%82%D1%84%D0%BE%D0%BB%D0%B8%D0%BE&target_type=posts&order=relevance"


def parse_habr(portfolio_link):
    data = requests.get(portfolio_link)
    soup = BeautifulSoup(data.text, 'html.parser')
    for i in soup.find_all("article"):
        link = f'{habr}{i.h2.a.get("href")}'
        print(link)
        print(get_news(link))
        # поставил пока ограничитель - чтоб не тратить время"
        break


def get_news(link):
    data = requests.get(link)
    soup = BeautifulSoup(data.text, 'html.parser')

    # записать в базу 2 поля
    head = soup.h1.text
    body = soup.find('div', {'xmlns': 'http://www.w3.org/1999/xhtml'}).text
    return head


parse_habr(portfolio_url)



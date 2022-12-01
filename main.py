import random
from time import sleep
import requests
from bs4 import BeautifulSoup

# persons_url_list = []
#
# for i in range(0, 40, 20):
#     url = f'https://www.bundestag.de/ajax/filterlist/en/members/453158-453158/h_a45203fd0f1592191f1bda63b5d86d72?limit=20&noFilterSet=true&offset={i}'
#
#     q = requests.get(url)
#     result = q.content
#
#     soup = BeautifulSoup(result, 'lxml')
#     persons = soup.find_all('a')
#
#
#     for person in persons:
#         person_page_url = person.get('href')
#         persons_url_list.append(person_page_url)
#
#         sleep(random.randrange(3, 6))
#
# with open('persons_url_list.txt', 'a') as file:
#     for line in persons_url_list:
#         file.write(f'{line}\n')

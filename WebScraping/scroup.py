#! python3
# This script is created for scraping douban group topics
import requests, bs4
num = 0
url = 'http://www.douban.com/group/gz/discussion?start=' + str(num)
res = requests.get(url)
try:
    res.raise_for_status()
except Exception as e:
    print('There is a problem:', e)
'''
print(type(res))
page = open('topics.html', 'wb')
for chunk in res.iter_content(100000):
    page.write(chunk)
'''

soup = bs4.BeautifulSoup(res.text, 'lxml')
titles = soup.select('tr[class] > td[class="title"] > a[class=""]')
authors = soup.select('tr[class] > td[nowrap="nowrap"] > a[class=""]')
follows = soup.select('tr[class] > td[class="" nowrap="nowrap"]')



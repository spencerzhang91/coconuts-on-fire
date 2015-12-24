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
def showfunc(l1, l2, l3, l4):
    length = len(l1)
    for i in range(length):
        print('%s %s %s %s' %
              (l1[i].getText(), l2[i].getText(), l3[i].getText(), l4[i].getText()))

def StartOperation(init_url: str) -> None:
    '''
    type init_url: str
    rtype: None
    '''
    pass # to be done
    
soup = bs4.BeautifulSoup(res.text, 'lxml')
titles = soup.select('tr[class] > td[class="title"] > a[class=""]')
authors = soup.select('tr[class] > td[nowrap="nowrap"] > a[class=""]')
follows = soup.select('tr[class] > td[class=""]')
lastres = soup.select('tr[class] > td[class="time"]')

showfunc(titles, authors, follows, lastres)






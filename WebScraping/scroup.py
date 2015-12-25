#! python3
# This script is created for scraping douban group topics
# Should be able to scrape [topic,author,follow,lastresponse]
# info of all group topics
import requests, bs4, csv
'''
num = 0
url = 'https://www.douban.com/group/tianhezufang/discussion?start=' + str(num)
res = requests.get(url)
try:
    res.raise_for_status()
except Exception as e:
    print('There is a problem:', e)

print(type(res))
page = open('topics.html', 'wb')
for chunk in res.iter_content(100000):
    page.write(chunk)
'''

def showfunc(l1, l2, l3, l4):
    length = len(l1)
    for i in range(length):
        print('%s %s %s %s' %
              (l1[i].getText(),
               l2[i].getText(),
               l3[i].getText(),
               l4[i].getText()))

def saveLocal(col1, col2, col3, col4):
    '''
    type cols: list
    This function saves the scraped data into CSV file
    '''
    pass # to be done

def StartOperation(init_url: str, pages: int) -> None:
    '''
    type init_url: str
    rtype: None
    '''
    num = 0
    perpage = 25
    for i in range(pages):
        url = init_url + str(num + perpage * i)
        res = requests.get(url)
        try:
            res.raise_for_status()
        except Exception as e:
            print('There is a problem:', e)
    
    
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        titles = soup.select('tr[class] > td[class="title"] > a[class=""]')
        authors = soup.select('tr[class] > td[nowrap="nowrap"] > a[class=""]')
        follows = soup.select('tr[class] > td[class=""]')
        lastres = soup.select('tr[class] > td[class="time"]')

        showfunc(titles, authors, follows, lastres)


url = 'https://www.douban.com/group/tianhezufang/discussion?start='
StartOperation(url, 631)






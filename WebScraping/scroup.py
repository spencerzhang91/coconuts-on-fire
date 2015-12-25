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
    '''
    To print out the scraped topics
    '''
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
    local_file = open('topic_saver.csv', 'w')
    file_writer = csv.writer(local_file)
    for i in len(col1):
        file_writer.writerow([col1[i],
                              col2[i],
                              col3[i],
                              col4[i]])


def StartOperation(init_url: str, pages: int) -> None:
    '''
    type init_url: str
    rtype: None
    '''
    num = 0
    perpage = 25
    test_file = open('test.csv', 'w', newline='')
    test_writer = csv.writer(test_file)
    for i in range(pages):
        print('Scraping page %d...' % (i+1))
        url = init_url + str(num + perpage * i)
        res = requests.get(url)
        try:
            res.raise_for_status()
        except Exception as e:
            print('There is a problem:', e)
    
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        titles = soup.select('tr[class] > td[class="title"] > a[class=""]') # need to be modified: retrive the attribute value of tag <td>
        authors = soup.select('tr[class] > td[nowrap="nowrap"] > a[class=""]')
        follows = soup.select('tr[class] > td[class=""]')
        lastres = soup.select('tr[class] > td[class="time"]')
        print('titles: %d authors: %d follows: %d lastres: %d' %
              (len(titles), len(authors), len(follows), len(lastres)))
        # showfunc(titles, authors, follows, lastres)
        print('Saving page %d to local...' % (i+1))
        for j in range(len(titles)):
            try:
                test_writer.writerow([titles[j].getText(),
                                      authors[j].getText(),
                                      follows[j].getText(),
                                      lastres[j].getText()])
            except Exception as e:
                print('wrong page %d' % (i+1)) # try to find out why failure(1) happens
                print('error message:', e)
                continue
    test_file.close()

if __name__ == '__main__':
    
    url = 'https://www.douban.com/group/tianhezufang/discussion?start='
    StartOperation(url, 631)






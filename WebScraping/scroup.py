#! python3
# This script is created for scraping douban group topics
# Should be able to scrape [topic,author,follow,lastresponse]
# info of all group topics
import requests, bs4, csv

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


def StartOperation(init_url: str, pages: int) -> None:
    '''
    type init_url: str
    rtype: None
    '''
    num = 0
    error_counter = 0
    perpage = 25
    failure_urls = []
    file = open(r'C:\Users\spencer\Desktop\guangzhouzufang.csv',
                'w', newline='',
                encoding='utf8') # this solves the unicode problem
    writer = csv.writer(file)
    for i in range(pages):
        print('Scraping page %d...' % (i+1))
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
        
        print('[page info]titles: %d authors: %d follows: %d lastres: %d' %
              (len(titles), len(authors), len(follows), len(lastres)))      
        print('Saving page %d to cwd local file %s...' % (i+1, 'guangzhouzufang.csv'))
        
        for j in range(len(titles)):
            try:
                # the four lines below occur encoding error, help!
                writer.writerow([titles[j]['title'],
                                 authors[j].getText(),
                                 follows[j].getText(),
                                 lastres[j].getText()])
                # print(titles[j]['title'])
            except Exception as e:
                print('Error occured on page %d line %d' % (i+1, j+1))
                print(*[titles[j].getText(), authors[j].getText()])
                print('error message:', e)
                if url not in failure_urls:
                        failure_urls.append(url)
                error_counter += 1     
    file.close()
    print('\nTotal failed topic number: %d topics!' % error_counter)
    return failure_urls

if __name__ == '__main__':
    url_list = ['https://www.douban.com/group/tianhezufang/discussion?start=',
                'http://www.douban.com/group/gz020/discussion?start=']
    url = url_list[1]
    failures = StartOperation(url, 5)
    if failures:
        print('[The urls below occured problem]:')
        for url in failures:
            print(url)
    else:
        print('All pages successfully scraped!')


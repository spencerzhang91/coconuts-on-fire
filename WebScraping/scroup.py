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
    error_counter = 0
    perpage = 25
    failure_urls = []
    test_file = open(r'C:\Users\spencer\Desktop\test.csv', 'w', newline='')
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
        titles = soup.select('tr[class] > td[class="title"] > a[class=""]')
        # need to be modified: retrive the attribute value of tag <td>
        authors = soup.select('tr[class] > td[nowrap="nowrap"] > a[class=""]')
        follows = soup.select('tr[class] > td[class=""]')
        lastres = soup.select('tr[class] > td[class="time"]')
        print('[page info]titles: %d authors: %d follows: %d lastres: %d' %
              (len(titles), len(authors), len(follows), len(lastres)))
        # showfunc(titles, authors, follows, lastres)
        print('Saving page %d to cwd local file %s...' % (i+1, 'test.csv'))
        for j in range(len(titles)):
            try:
                test_writer.writerow([titles[j].getText().encode('utf-8'),
                                      authors[j].getText().encode('utf-8'),
                                      follows[j].getText().encode('utf-8'),
                                      lastres[j].getText().encode('utf-8')])
            except Exception as e:
                print('Error occured on page %d line %d' % (i+1, j+1))
                print(*[titles[j].getText(), authors[j].getText(),
                       follows[j].getText(), lastres[j].getText()])
                # try to find out why failure(1) happens
                print('error message:', e)
                if url not in failure_urls:
                    failure_urls.append(url)
                error_counter += 1
    test_file.close()
    print('\nTotal failed topic number: %d topics!' % error_counter)
    return failure_urls

if __name__ == '__main__':
    url = 'https://www.douban.com/group/tianhezufang/discussion?start='
    failures = StartOperation(url, 10)
    print('[The urls below occured problem]:')
    for url in failures:
        print(url)


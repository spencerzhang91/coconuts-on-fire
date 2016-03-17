#! python3
# This script is created for scraping douban group topics
# Should be able to scrape [topic,author,follow,lastresponse]
# info of all group topics
# TODO: reorganize this long code into classes.

import requests, bs4, csv
import datetime
import time
# import psycopg2

class CSVfileNameError(Exception):
    def __str__(self):
        return 'Invalid file name, please add .csv at the end of name.'

class WrongURL(Exception):
    def __str__(self):
        return 'Invalid url input, input should be valid url of douban group.'

class NoPageNumber(Exception):
    def __str__(self):
        return 'Failed to get total group topic page numbers.'
    
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

def initialization():
    '''
    This function asks user to input the needed initialization
    informations of the scraping mission.
    '''
    url = pagenum = filename = None
    while True:
        if not url:
            try:
                url = input('Please copy the url here(drop num after"="):')
            except WrongURL as wurl:
                print(wurl)
                url = None
                continue
        if not pagenum:
            try:
                pagenum = int(input('Please enter the page numbers you want'
                                ' to scrape:'))
            except ValueError:
                print('Please enter an integer!')
                pagenum = None
                continue
        if not filename:
            try:
                filename = input('Please enter the file name to save data'
                         '(file name must include postfix ".csv"):')
                if filename[-4:] != '.csv':
                    raise CSVfileNameError
            except CSVfileNameError as cfne:
                print(cfne)
                filename = None
                continue
        if url and pagenum and filename:
            break
    return (url, pagenum, filename)

def getGroupName(soup:bs4.BeautifulSoup)->str:
    '''
    This function is a part of the scroup application, retriving
    group name from the topic table page.
    '''
    groupname = soup.select('div > div > div[class="info"]\
                            > div[class="title"] > a')[0].getText()
    return groupname

def startOperation(init_url:str, pages:int=None, filename:str):
    '''
    type init_url: str
    rtype: None
    '''
    if not pages:
        try:
            pages = getPages(init_url+'0')
        except Exception as e:
            print("Exception occured:")
            print(e)
            print("Set page number to default 5 pages.")
            pages = 5

    start_page = 22630
    error_counter = 0
    perpage = 25
    failure_urls = []
    # proxy config
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) "
                                                "Gecko/20100101 Firefox/43.0",
               "Connection": "keep-alive"
               }
    proxies = {'http':'http://192.99.246.183:9000'}
    file = open(r'C:\Users\spencer\Desktop\%s' % filename, 'w', newline='',
                encoding='utf8')
    writer = csv.writer(file)
    for i in range(pages):
        url = init_url + str(start_page + perpage * i)
        time.sleep(1)
        res = requests.get(url, headers=headers)
        if res.status_code != 200:
            print('Caught by Douban keeper!')
            break
        try:
            res.raise_for_status()
        except Exception as e:
            print('There is a problem:', e)
            print('Waiting 10 seconds to recover...')
            time.sleep(10)
            i -= 1
            continue
    
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        print('Scraping page %d...' % (i+1))
        titles = soup.select('tr[class] > td[class="title"] > a[class=""]')
        authors = soup.select('tr[class] > td[nowrap="nowrap"] > a[class=""]')
        follows = soup.select('tr[class] > td[class=""]')
        lastres = soup.select('tr[class] > td[class="time"]')
        urls = soup.select('tr[class] > td[class="title"] > a[class=""]')
        print('[page info]titles: %d authors: %d follows: %d lastres: %d' %
              (len(titles), len(authors), len(follows), len(lastres)))      
        print('Saving page %d to desktop local file %s...' % (i+1, filename))
        
        for j in range(len(titles)):
            try:
                writer.writerow([titles[j]['title'],
                                 authors[j].getText(),
                                 follows[j].getText(),
                                 lastres[j].getText(),
                                 urls[j]['href']])

                # detect if target appeared
                result = hasAuthor('ToSaturday', authors[j])
            except Exception as e:
                print('Error occured on page %d line %d' % (i+1, j+1))
                print(*[titles[j].getText(), authors[j].getText()])
                print('error message:', e)
                if url not in failure_urls:
                        failure_urls.append(url)
                error_counter += 1
        print('page wrote.')
    file.close()
    if error_counter:
        print('\nTotal failed topic number: %d topics!' % error_counter)
    return failure_urls

def hasAuthor(person:str, tag:bs4.element.Tag)->bool: # just a printer for now
    '''
    This function is an add-on function that check if the interested
    author appeared in the group which is currently under process. If
    so, then the whole information will be saved along side with main
    process.
    '''
    if person == tag.text:
        print("#######################Target found###########################")
        title = tag.parent.parent.select('td > a[class=""]')[0]['title']
        follows = tag.parent.parent.select('td[class=""]')[0].text
        lastres = tag.parent.parent.select('td[class="time"]')[0].text
        url = tag.parent.parent.select('td > a[class=""]')[0]['href']
        print("[Found]%s %s %s %s %s" % (title, person, follows, lastres, url))
    else:
        return False


def searchDate(date:str, groups:list)->list:
    '''
    This function should be capable of searching a douban group or multiple
    groups' topics within a certain time period or date.
    # Arguments
    date: {type: str; formate: "yyyy-mm-dd"(str)}
    groups: {type: [str, ...]} (list of url strings)
    Returns a list to contain applied url strings.
    '''
    raise NotImplementedError

def getPages(url:str, headers=headers):
    """
    This function gets total page number of a group discussion.

    """
    res = requests.get(url, headers=headers)
    psoup = bs4.BeautifulSoup(res.text, 'lxml')
    # the line below need to be validated. The needed message is in html tag
    # attribute value, the problem is how to extract it properly.
    paginator_list = psoup.select('div[class="paginator"] > span')
    if paginator_list:
        return int(paginator_list[1]['data-total-page'])
    else:
        raise NoPageNumber
    
    

"""
def insertData(row:list):
    '''
    This function insert a row of data in douban group topic table into local
    PostgreSQL database.
    '''
    conn = psycopg2.connect(database='shop', user='postgres',
                            host='localhost', password='123456')
    cur = conne.cursor()
    # TODO: finish this function
    cur.excute("INSERT INTO xiaozu VALUES (%d, %s, %s, %d, %s, %s)" % (row[0],
                                       row[1], row[2], row[3], row[4], row[5])
              )
"""


if __name__ == '__main__':
    # The following is for development test:
    # TODO: change url_list into url dictionary
    url_list = ['https://www.douban.com/group/tianhezufang/discussion?start=',
                'http://www.douban.com/group/gz020/discussion?start=',
                'http://www.douban.com/group/kaopulove/discussion?start=',
                'http://www.douban.com/group/wexin/discussion?start=',
                'https://www.douban.com/group/yuexiuzufang/discussion?start=',
                'https://www.douban.com/group/gz020/discussion?start=',
                'https://www.douban.com/group/spoil/discussion?start=',
                'https://www.douban.com/group/chen19891018/discussion?start=']
    
    url = url_list[6]
    pgm = 1435
    fln = "Tosaturday.csv"
    # url, pgm, fln = initialization()
    start = time.clock()
    failures = startOperation(url, pgm, fln)
    if failures:
        print('[The urls below occured problem]:')
        for item in failures:
            print(item)
    else:
        print('All pages successfully scraped!')
    end = time.clock()
    total_time = end - start
    m , s = divmod(total_time, 60)
    h , m = divmod(m, 60)
    print ("It takes %d hours %d minutes %.2f seconds." % (h, m, s))
    # The main problem right now is the speed.
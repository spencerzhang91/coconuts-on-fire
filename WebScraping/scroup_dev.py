#! python3
# This script is created for scraping douban group topics
# Should be able to scrape [topic,author,follow,lastresponse]
# info of all group topics
import requests, bs4, csv
import date

class CSVfileNameError(Exception):
    def __str__(self):
        return 'Invalid file name, please add .csv at the end of name.'

class WrongURL(Exception):
    def __str__(self):
        return 'Invalid url input, input should be valid url of douban group.'
    
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

def Initialization():
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
    """
    This function is a part of the scroup application, retriving
    group name from the topic table page.
    """
    groupname = soup.select('div > div > div[class="info"]\
                            > div[class="title"] > a')[0].getText()
    return groupname

def StartOperation(init_url:str, pages:int, filename:str)->None:
    '''
    type init_url: str
    rtype: None
    '''
    num = 0
    error_counter = 0
    perpage = 25
    failure_urls = []
    file = open(r'C:\Users\spencer\Desktop\%s' % filename, 'w', newline='',
                encoding='utf8')
    writer = csv.writer(file)
    for i in range(pages):
        url = init_url + str(num + perpage * i)
        res = requests.get(url)
        try:
            res.raise_for_status()
        except Exception as e:
            print('There is a problem:', e)
    
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        groupname = getGroupName(soup)
        print('Scraping page %d of %s...' % ((i+1), groupname))
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
                result = hasAuthor('Raina', authors[j])  
            except Exception as e:
                print('Error occured on page %d line %d' % (i+1, j+1))
                print(*[titles[j].getText(), authors[j].getText()])
                print('error message:', e)
                if url not in failure_urls:
                        failure_urls.append(url)
                error_counter += 1
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


def SearchDate(date:str, groups:list)->list:
    '''
    This function should be capable of searching a douban group or multiple
    groups' topics within a certain time period or date.
    # Arguments
    date: {type: str; formate: "yyyy-mm-dd"(str)}
    groups: {type: [str, ...]} (list of url strings)
    Returns a list to contain applied url strings.
    '''
    pass
    # to be done before Jan 25


if __name__ == '__main__':

    # The following is for development test:
    url_list = ['https://www.douban.com/group/tianhezufang/discussion?start=',
                'http://www.douban.com/group/gz020/discussion?start=',
                'http://www.douban.com/group/kaopulove/discussion?start=',
                'http://www.douban.com/group/wexin/discussion?start=']
    
    url = url_list[2]
    pgm = 10
    fln = "dev_test_file.csv"
    # url, pgm, fln = Initialization()
    failures = StartOperation(url, pgm, fln)
    if failures:
        print('[The urls below occured problem]:')
        for item in failures:
            print(item)
    else:
        print('All pages successfully scraped!')
class CSVfileNameError(Exception):
    def __str__(self):
        return 'Invalid file name, please add .csv at the end of name.'

class WrongURL(Exception):
    def __str__(self):
        return 'Invalid url input, input should be valid url of douban group.'
    
def Initialization():
    '''
    This function asks user to input the needed initialization
    informations of the scraping mission.
    '''
    url = pagenum = filename = None
    while True:
        try:
            url = input('Please copy the url here:')
        except WrongURL as wurl:
            print(wurl)
            url = None
            continue
        try:
            pagenum = int(input('Please enter the page numbers you want'
                            'to scrape:'))
        except ValueError:
            print('Please enter an integer!')
            pagenum = None
            continue
        try:
            filename = input('Please enter the file name to save data'
                     '(file name must include postfix ".csv"):')
            if filename[-4:] != '.csv':
                raise CSVfileNameError
        except CSVfileNameError as cfne:
            print(cfne)
            filename = None
            continue         
        
    return (url, pagenum, filename)

if __name__ == '__main__':
    res = Initialization()
    print(res)

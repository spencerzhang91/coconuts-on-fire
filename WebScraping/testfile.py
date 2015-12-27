def Initialization():
    '''
    This function asks user to input the needed initialization
    informations of the scraping mission.
    '''
    url = input('Please copy the url here:')
    while True:
        try:
            pagenum = int(input('Please enter the page numbers you want'
                            'to scrape:'))
            break
        except ValueError as a:
            print(a)
            print('Please enter an integer!')
        
    filename = input('Please enter the file name to save data:')
    return (url, pagenum, filename)

if __name__ == '__main__':
    res = Initialization()
    print(res)

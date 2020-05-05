import re



def GatherId(url):
    
    '''
    This function retrives the unique Id from the url
    '''    

    pattern = r'(?<=/d/).*?(?=/edit)'
    matchobj = re.findall(pattern,url)
    SpreadSheetId = matchobj[0]
    return SpreadSheetId



if __name__ == '__main__':
    
    print('\nThis is a test\n')
    url = input('Inserisci URL della sheet: ')

    SpreadSheetId = GatherId(url)

    print(SpreadSheetId)
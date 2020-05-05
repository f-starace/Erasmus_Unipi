from selenium import webdriver                                          # permette di eseguire script su un browser automatizzato
from selenium.webdriver.firefox.options import Options  as F_Options    # [Nel caso di Firefox] permette di aprire il browser automatizzato in modalità headless (invisibile)
from selenium.webdriver.chrome.options import Options  as C_Options     # [Nel caso di Chrome] permette di aprire il browser automatizzato in modalità headless (invisibile)

import ezsheets                                                         # serve per interagire con l'API di google sheets

from tqdm import tqdm                                                   # per avere una interfaccia grafica che mostra il progresso dell'operazione di scraping


import sys                                                              # sys e os permettono di cambiare la working directory in quella contenente lo script (si evitano così errori relativi a un path sbagliato)
import os 

import re                                                               # necessario per identificare il pattern di testo relativo all'ID univoco della spreadsheet dall'url

from GatherID import GatherId                                           # Imports the gatherId function

from colors import Color                                                # Imports the Color class (per i colori dell'interfaccia)




def EM_Scraper(ss):
    

    # Creating a new sheet and opening it
    print('Verrà creata un nuovo foglio all\'interno della spreadsheet che conterrà i dati riguardanti le sedi')

    name_s = input('Nome del nuovo foglio di lavoro: ')
    ss.createSheet(name_s)
    s = ss[-1]
    print(f'"{s.title}" Sheet Opened')




    '''
    Creo delle liste contenenti all'indice iniziale il valore che poi corrisponderà alla prima riga della tabella
    A ciascuna di queste liste verranno mano mano aggiunti i valori di riferimento per ogni singola sede
    '''


    paese = ['Paese']
    code = ['Codice Università']
    name = ['Nome completo Università']
    posti = ['Posti']
    periodo = ['Periodo']
    lang = ['Requisiti di Lingua']
    note = ['Note']







    #SCRAPING DATA FROM THE WEB

    try:
        print('Trying to connect using Firefox geckodriver...\n')
        
        # HEADLESS MODE FOR FIREFOX
        options = F_Options()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        print('Headless Firefox Initialized')
        
    except:
        print('Firefox geckodriver not found\n')
        try:
            print('Trying to connect using Chrome chromedriver...')
            #HEADLESS MODE FOR CHROME
            chrome_options = C_Options()
            chrome_options.add_argument("--headless")
            driver = webdriver.Chrome(options=chrome_options)
            print('Headless Chrome Initialized')
            
        except:
            print('Error while trying to locate the driver\n Please follow guide on:')
            print('https://www.seleniumeasy.com/python/getting-started-selenium-webdriver-using-python')
        

    print('Driver connected successfully')
    driver.get('https://unipi.erasmusmanager.it/studenti/elencoAccordi.aspx')




    Medicina = ['medicine', 'medicina']



    # Looping through the table

    for i in tqdm(range(2,1172)):

        x_paese = f'//*[@id="dbGrid"]/tbody/tr[{i}]/td[3]'
        x_code = f'//*[@id="dbGrid"]/tbody/tr[{i}]/td[4]'
        x_name = f'//*[@id="dbGrid"]/tbody/tr[{i}]/td[5]'
        x_posti = f'//*[@id="dbGrid"]/tbody/tr[{i}]/td[11]'
        x_periodo = f'//*[@id="dbGrid"]/tbody/tr[{i}]/td[12]'
        x_lang = f'//*[@id="dbGrid"]/tbody/tr[{i}]/td[13]'
        x_notes = f'//*[@id="dbGrid"]/tbody/tr[{i}]/td[14]'
        
        x_course = f'//*[@id="dbGrid"]/tbody/tr[{i}]/td[6]'


        if driver.find_element_by_xpath(x_course).text.lower() in Medicina:
            # NOTA: Questo loop prende solo le sedi assegnate a medicina, non tiene conto di altre professioni sanitarie
            # E' possibile però aggiungerle 
            
            paese.append(driver.find_element_by_xpath(x_paese).text)
            code.append(driver.find_element_by_xpath(x_code).text)
            name.append(driver.find_element_by_xpath(x_name).text)
            posti.append(driver.find_element_by_xpath(x_posti).text)
            periodo.append(driver.find_element_by_xpath(x_periodo).text)
            lang.append(driver.find_element_by_xpath(x_lang).text)
            note.append(driver.find_element_by_xpath(x_notes).text)

    

    print(Color.green + 'Data successfully scraped'+ Color.end)     


    driver.quit()



    print('Loading data to the sheet')


    s.updateColumn(1, paese)
    s.updateColumn(2, code)
    s.updateColumn(3, name)
    s.updateColumn(4, posti)
    s.updateColumn(5, lang)
    s.updateColumn(6, note)
    s.updateColumn(7, periodo)



    print(Color.green + 'Data successfully loaded into the spreadsheet'+ Color.end)


    
    

if __name__ == '__main__':
    
    #Changing the Current Working Directory to the one containing the script

    os.chdir(sys.path[0])




    # Retriving the SpreadsheetId from the url
        
    url = input('Inserisci l\'url contenente la tabella [premi solo invio per default]\n')
    if url == '':
        url = 'https://docs.google.com/spreadsheets/d/1DoMqVZql9YTRED2Cb4uZkSm_ILZvrewzxELShvfTaC8/edit#gid=0'
        
    try:
        SpreadSheetID = GatherId(url)
    except:
        print(Color.red +'\nErrore, non sono riuscito a ricavare l\'ID dal link. Assicurati che sia corretto\n'+ Color.end)
        quit()



    # Opening the spreadsheet

    print('opening the SpreadSheet')
    ss = ezsheets.Spreadsheet(SpreadSheetID)
    print(f'"{ss.title}" opened')
    
    EM_Scraper(ss)


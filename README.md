# Erasmus_Unipi

Raccolta di Script che automatizzano il processo di raccolta dati per l'assegnazione dei posti ai bandi Erasmus dell'Università di Pisa

Non essendo stato testato a fondo, consiglio un controllo ulteriore a mano per la corretta assegnazione dei posti

# Requisiti:
- Python 3.6 o superiore
- Alcuni moduli che si trovano nel file requirements.txt
- Driver per far partire Selenium, nel caso si voglia provare a vedere come funziona la raccolta di dati dal sito ErasmusManager (Guida per la corretta Installazione di Selenium: https://www.seleniumeasy.com/python/getting-started-selenium-webdriver-using-python)


# Note:
- Funziona solo per i candidati iscritti al CdL di Medicina e Chirurgia. Ulteriori CdL potrebbero però poter essere aggiunti facilmente in futuro
- Per attivare lo script, eseguire il file main.py
- ErasmusManager.py può essere eseguito sia come script a se stante, sia come modulo di main.py
- ErasmusScoreCalculator.py non è integrato all'interno dello script principale. Potrebbe essere comodo in futuro però per calcolare il punteggio dei candidati con il minore sforzo possibile.

# Funzionamento:
Verrà chiesto di azionare lo script ErasmusManagerScraper.py, Questo è necessario la prima volta per recuperare i dati corretti del numero delle sedi in Medicina e chirurgia

In caso affermativo, viene chiesto di impostare un nome per il nuovo foglio di lavoro all'interno della spreadsheet
<img width="709" alt="1" src="https://user-images.githubusercontent.com/64803153/81043601-d2317180-8eb2-11ea-8a27-6a4ef4ce3a6c.png">
Il foglio di lavoro viene creato
<img width="674" alt="2" src="https://user-images.githubusercontent.com/64803153/81043611-d8275280-8eb2-11ea-8a86-9e25d6820037.png">
Vengono recuperati i dati dal sito erasmus manager attraverso selenium
<img width="713" alt="3" src="https://user-images.githubusercontent.com/64803153/81043616-dbbad980-8eb2-11ea-8ebb-0cf2652d189f.png">
I risultati vengono automaticamente collocati nel nuovo foglio creato
<img width="970" alt="4" src="https://user-images.githubusercontent.com/64803153/81043618-dfe6f700-8eb2-11ea-85cf-90483827ead7.png">

Correzione di discrepanze tra i codici:
Per poter effettuare il calcolo dei posti delle mete è fondamentale che il primo foglio (che dovrebbe contenere le graduatorie) e l'ultimo foglio (che dovrebbee contenere i dati da ErasmusManager) siano identici 
<img width="716" alt="5" src="https://user-images.githubusercontent.com/64803153/81043668-f68d4e00-8eb2-11ea-9dbd-553a47168b78.png">
Nel caso non lo fossero verrà chiesta la risoluzione del conflitto:
<img width="516" alt="5 2:3" src="https://user-images.githubusercontent.com/64803153/81043682-ff7e1f80-8eb2-11ea-9dc2-cce79d2a1a60.png">

<img width="368" alt="5 3:3" src="https://user-images.githubusercontent.com/64803153/81043692-06a52d80-8eb3-11ea-8ae2-0ca76611704e.png">

Infine viene creato un file excel nella cartella dello script chiamatoo results.xlsx
<img width="712" alt="6" src="https://user-images.githubusercontent.com/64803153/81043675-fab96b80-8eb2-11ea-904e-c7c8458b42c1.png">


# Erasmus_Unipi

Raccolta di Script che automatizzano il processo di raccolta dati per l'assegnazione dei posti ai bandi Erasmus dell'Università di Pisa

Non essendo stato testato a fondo, consiglio un controllo ulteriore a mano per la corretta assegnazione dei posti

# Requisiti:
- Firefox
- Python 3.6 o superiore
- Alcuni moduli che si trovano nel file requirements.txt

# Installazione e Set-up per Windows:

1) Scarica il browser Firefox (se non presente)

2) Scarica Python al seguente Link

- Windows x86-64 executable installer [Per sistemi a 64-bit]
https://www.python.org/ftp/python/3.8.3/python-3.8.3rc1-amd64.exe


- Windows x86 executable installer    [Per sistemi a 32-bit] 
https://www.python.org/ftp/python/3.8.3/python-3.8.3rc1.exe


3) Prosegui con l'installazione, facendo attenzione di spuntare la casella 'Aggiungi Python a Path':

<img width="564" alt="Schermata 2020-05-05 alle 14 08 58" src="https://user-images.githubusercontent.com/64803153/81064464-066c5880-8eda-11ea-91ec-004e4c92dc48.png">


4) Al termine dell'installazione disabilita il Path Limit Lenght



4) Sul prompt dei comandi digitare:

pip install -r `path`requirements.txt

Sostituendo `path` con il percorso che contiene il file requirements



# Set-up di Google Sheets:
- Ottieni link condivisibile nel foglio google e permetti la modifica 

<img width="390" alt="Schermata 2020-05-05 alle 16 58 50" src="https://user-images.githubusercontent.com/64803153/81081115-cb761f00-8ef1-11ea-85f8-85de85243125.png">



# Note:
- Funziona solo per i candidati iscritti al CdL di Medicina e Chirurgia. Ulteriori CdL possono essere aggiunti in futuro
- Per attivare lo script, eseguire il file main.py
- ErasmusManager.py può essere eseguito sia come script a se stante, sia come modulo di main.py
- ErasmusScoreCalculator.py non è integrato all'interno dello script principale. Può tornare comodo in futuro però per calcolare il punteggio dei candidati con il minore sforzo possibile.

# Funzionamento:

### Scraper del sito erasmus manager
Verrà chiesto di azionare lo script ErasmusManagerScraper.py, Questo è necessario la prima volta per recuperare i dati corretti del numero delle sedi in Medicina e chirurgia

In caso affermativo, viene chiesto di impostare un nome per il nuovo foglio di lavoro all'interno della spreadsheet



![](/images/1.png)



Il foglio di lavoro viene creato




![](/images/2.png)



Vengono recuperati i dati dal sito erasmus manager attraverso selenium



![](/images/3.png)



I risultati vengono automaticamente collocati nel nuovo foglio creato




![](/images/4.png)



### Correzione di discrepanze tra i codici:

Per poter effettuare il calcolo dei posti delle mete è fondamentale che il primo foglio (che dovrebbe contenere le graduatorie) e l'ultimo foglio (che dovrebbee contenere i dati da ErasmusManager) siano identici 




![](/images/5.png)



Nel caso non lo fossero verrà chiesta la risoluzione del conflitto:



![](/images/5,2.png)

![](/images/5,3.png)


Nel caso fosse stata scelta dal candidato una meta non rientrante tra quelle del proprio CdL, questa potrà essere eliminata semplicemente premendo invio e confermando con y

![](/images/5,4.png)


![](/images/5.5.png)


Infine viene creato un file excel nella cartella dello script chiamato results.xlsx



![](/images/6.png)



![](/images/res1.png)


![](/images/res2.png)




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


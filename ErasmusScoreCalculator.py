from datetime import datetime   # importo questo modulo per elaborare l'anno e il mese corrente in automatico per evitare riarrangiamenti del codice

anno_corrente = datetime.now().year
mese_corrente = datetime.now().month  # Se il mese è maggiore o uguale a settembre viene applicata la formula dell'apertura del secondo bando


p_lode = 30 #il valore assegnato alla lode








def ES_calculator(CFU, media_ponderata, anno_immatricolazione):
    '''
    Questa funzione calcola automaticamente il punteggio dello studente, prendendo come input solo i valori in argomento
    '''
    delta = anno_corrente - anno_immatricolazione
    
    if mese_corrente >= 9:
        # Se il mese corrente è > o uguale a quello di settembre, viene applicata la formula per l'apertura del secondo bando
        print('\nApplico la formula per l\'apertura del secondo bando\n')
        NA = delta * 60
        
    else:
        print('\nApplico la formula per l\'apertura del primo bando\n')
        NA = delta  * 60 -30

    RS  = (CFU/ NA) * 100

    ES  = (media_ponderata/p_lode) * RS
    
    '''
    Approssimo il risultato a 2 decimali
    '''
    ES = round(ES,2)
    
    return ES







if __name__ == '__main__':
    print('\nTest della funzione: \n\n')
    t_CFU = int(input('Numero crediti studente:  '))
    t_media_ponderata = float(input('Media Pesata studente:  '))
    t_anno_immatricolazione = int(input('Anno immatricolazione studente:  '))
    
    t_score = ES_calculator(t_CFU, t_media_ponderata, t_anno_immatricolazione)
    print(f'Il punteggio erasmus dello studente è: {t_score}')
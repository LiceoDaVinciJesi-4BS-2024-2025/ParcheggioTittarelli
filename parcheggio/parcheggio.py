#Silvia Tittarelli
#4BS
#file parcheggio

#importo gli altri file della cartella

from postomezzo import *
from veicolo import *
from auto import *
from moto import *
import datetime

class Parcheggio:
    def __init__(self): #Un parcheggio può contenere fino a 1000 auto, 200 moto
        """
        inizializza la funzione
        """
        self.__auto = []
        self.__moto = []
        self.MAX_AUTO = 1000
        self.MAX_MOTO = 200
            
    @property
    def auto(self):
        return self.__auto
    
    @property
    def moto(self):
        return self.__moto
    
    #ritorna una stringa  con le variabili
    def __str__(self):
        return __class__.__name__ + str(self.__dict__)
           
    #serve per il programmatore, è come str
    def __repr__(self):
        return __class__.__name__ + str(self.__dict__)
    
    def parcheggiaVeicolo(self, mezzo:Veicolo):
        if isinstance(mezzo, Auto):#controlla che il mezzo sia della classe auto
            if len(self.__auto) >= self.MAX_AUTO:
                return False # impossibile parcheggiare, posto occupato
            
            posto = PostoMezzo( mezzo.targa , datetime.datetime.now())
            self.__auto.append(posto)
            return True
        
        # qui lo faccio per le moto...
        if isinstance(mezzo, Moto): #controlla che il mezzo sia della classe moto
            if len(self.__moto) >= self.MAX_MOTO:
                return False #posto già occupato
            
            posto = PostoMezzo( mezzo.targa, datetime.datetime.now())
            self.__moto.append(posto)
            return True
        
    def rimuoviVeicolo(self, mezzo:Veicolo):
        if isinstance(mezzo, Auto):
            targaDaCercare = mezzo.targa
            for posto in self.__auto:
                if posto.targaPresente == targaDaCercare:
                    self.__auto.remove(posto)
                    return True
                
        # qui lo faccio per le moto
        if isinstance(mezzo, Moto):
            targaDaCercareM = mezzo.targa
            for posto in self.__moto:
                if posto.targaPresente == targaDaCercareM:
                    self.__moto.remove(posto)
                    return True
 
#Definire un sistema di prenotazione per i posteggi dei veicoli in modo tale che:
# • si possa sapere in ogni istante quanti posti sono liberi per ogni tipo di veicolo
# • al momento dell’arrivo del veicolo si possa prenotare un posto indicando il tipo di veicolo,
# la targa e il numero di ore di sosta e quindi saldare quanto dovuto.
# • Si mantenga il conto del guadagno totale del parcheggio, considerando la seguente tabella:
# Auto 1.5 €/h
# Moto 1.2 €/h
# Camion 1.8 €/h
# Autobus 2.4 €/h
# • A volontà del gestore dell’applicazione si possa salvare lo stato attuale del parcheggio su un opportuno file di testo.
#Lo stato attuale del parcheggio è descritto dai veicoli in sosta in questo momento e dal totale del guadagno raggiunto.
#Tutte queste info vanno salvate nel file park.data (un comunissimo file di testo) nella stessa cartella dello script corrente.
# • Al momento del caricamento dei dati, se il file park.data è presente, la situazione del
# parcheggio va ripristinata allo stato descritto nel file.

#--------------------------------------------------------------------------------
if __name__ == "__main__":
    #creo un parcheggio
    parcheggio = Parcheggio()
    print(parcheggio)
    mezzo1 = Auto("ER456YH")
    print(parcheggio.parcheggiaVeicolo(mezzo1))
    mezzo2 = Moto("TY765UH")
    print(parcheggio.parcheggiaVeicolo(mezzo2))
    print(parcheggio.rimuoviVeicolo(mezzo1))
    print(parcheggio)
    
    
    
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

        self.__soldiIntascati = 0
            
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
                    diff = datetime.datetime.now() - posto.dataInizioOccupazione
                    ore = diff.total_seconds() / 3600
                    tot = ore * 1.5
                    self.__soldiIntascati += tot
                    return tot
                
        # qui lo faccio per le moto
        if isinstance(mezzo, Moto):
            targaDaCercareM = mezzo.targa
            for posto in self.__moto:
                if posto.targaPresente == targaDaCercareM:
                    self.__moto.remove(posto)
                    return True
        return 0
 
#--------------------------------------------------------------------------------
if __name__ == "__main__":
    #creo un parcheggio
    parcheggio = Parcheggio()
    print(parcheggio)
    print("")
    mezzo1 = Auto("ER456YH")
    print("aggiungo un veicolo all'interno del parcheggio", parcheggio.parcheggiaVeicolo(mezzo1))
    mezzo2 = Auto("TY678HO")
    print("aggiungo un altro veicolo all'interno del parcheggio", parcheggio.parcheggiaVeicolo(mezzo2))
    mezzo3 = Moto("TY765UH")
    print("aggiungo un terzo veicolo all'interno del parcheggio", parcheggio.parcheggiaVeicolo(mezzo3))
    print("rimuovo il primo veicolo che ho aggiunto all'interno del parcheggio:", parcheggio.rimuoviVeicolo(mezzo1))
    print("ora nel percheggio i mezzi rimasti sono", parcheggio)
    

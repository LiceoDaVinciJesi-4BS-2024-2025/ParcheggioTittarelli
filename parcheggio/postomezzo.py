#Silvia Tittarelli
#4BS
#classe postomezzo

alfabetoMaiuscolo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cifre = "1234567890"
import datetime

#Definisco la classe PostoMezzo, che permette di parcheggiare un mezzo specifico, ad esempio un Auto, oppure una Moto
#Definisco in esso se è libero oppure occupato, la targa del mezzo che lo occupa, la data/ora di termine occupazione
class PostoMezzo:
    def __init__(self, targaPresente : str, dataInizioOccupazione : datetime.datetime):
        """
        inizializza la funzione
        """
        self.__targaPresente = targaPresente
        self.__dataInizioOccupazione = dataInizioOccupazione
    
    @property
    def targaPresente(self):
        return self.__targaPresente
    
    @property
    def dataInizioOccupazione(self):
        return self.__dataInizioOccupazione
    
    #ritorna una stringa  con le variabili
    def __str__(self):
        return __class__.__name__ + str(self.__dict__)
           
    #serve per il programmatore, è come str
    def __repr__(self):
        return __class__.__name__ + str(self.__dict__)
    
    def parcheggio(self):
        """
        dice se il parcheggio è libero o meno
        """
        if self.__targaPresente == "":
            return "Il posto è vuoto"
        else:
            return "il posto è occupato da :", self.__targaPresente, "dalle:",  self.__dataInizioOccupazione
    

#---------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    #
    targaPresente = "WE456WE"
    dataInizioOccupazione = (2025, 11, 6, 21, 12, 00)
    postomezzo1 = PostoMezzo(targaPresente, dataInizioOccupazione)
    print(postomezzo1)

    #
    print(postomezzo1.parcheggio())
    #
    print(postomezzo1)
    

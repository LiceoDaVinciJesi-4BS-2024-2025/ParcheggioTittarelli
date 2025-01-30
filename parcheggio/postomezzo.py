#Silvia Tittarelli
#4BS
#classe postomezzo

alfabetoMaiuscolo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cifre = "1234567890"
import datetime

#Definisco la classe PostoMezzo, che permette di parcheggiare un mezzo specifico, ad esempio un Auto, oppure una Moto
#Definisco in esso se è libero oppure occupato, la targa del mezzo che lo occupa, la data/ora di termine occupazione
class PostoMezzo:
    def __init__(self, targaPresente : str, dataTermineOccupazione : datetime.datetime):
        """
        inizializza la funzione
        """
        self.__targaPresente = targaPresente
        self.__dataTermineOccupazione = dataTermineOccupazione
   
#         #controlla la targa
#         if len(targaPresente) != 7:
#             raise ValueError("impossibile, targa non accettabile!")
#         if targaPresente[0] in alfabetoMaiuscolo and targaPresente[1] in alfabetoMaiuscolo and targaPresente[5] in alfabetoMaiuscolo and targaPresente[6] in alfabetoMaiuscolo and targaPresente[2] in cifre and targaPresente[3] in cifre and targaPresente[4] in cifre:
#             self.__targaPresente= targaPresente
#         else:
#             raise ValueError("Targa fatta male, controllala!")
    
    @property
    def targaPresente(self):
        return self.__targaPresente
    
    @property
    def dataTermineOccupazione(self):
        return self.__dataTermineOccupazione
    
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
            return "il posto è occupato da :", self.__targaPresente, "è termina alle:",  self.__dataTermineOccupazione
    
    def libera(self):
        """
        libera il parcheggio
        
        """
        self.__dataTermineOccupazione = ""
        self.__targaPresente = ""
        return "il posto è vuoto"
#---------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    #
    targaPresente = "WE456WE"
    dataTermineOccupazione = (2025, 11, 6, 21, 12, 00)
    postomezzo1 = PostoMezzo(targaPresente, dataTermineOccupazione)
    print(postomezzo1)

    #
    print(postomezzo1.parcheggio())
    #
    print(postomezzo1.libera())
    print(postomezzo1)
    
#Silvia Tittarelli
#4BS
#classe postomezzo

alfabetoMaiuscolo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cifre = "1234567890"
targhePresenti = []
import datetime

#Definire la classe PostoMezzo, che permette di parcheggiare un mezzo specifico, ad esempio un Auto, oppure una Moto, oppure un Autobus e un Camion.
#Definire in esso se è libero oppure occupato, la targa del mezzo che lo occupa, la data/ora di termine occupazione
class PostoMezzo:
    def __init__(self, targa : str, dataTermineOccupazione : datetime.datetime):
        """
        inizializza la funzione
        """
        targaEora = (targa, dataTermineOccupazione)
        self.__targaEora = targaEora
        targhePresenti.append(self.__targaEora)
        
        #controlla la targa
        for (targa, dataTermineOccupazione) in targhePresenti:
            if len(targa) != 7:
                raise ValueError("impossibile, targa non accettabile!")
            if targa[0] in alfabetoMaiuscolo and targa[1] in alfabetoMaiuscolo and targa[5] in alfabetoMaiuscolo and targa[6] in alfabetoMaiuscolo and targa[2] in cifre and targa[3] in cifre and targa[4] in cifre:
                self.__targaEora = targaEora
            else:
                raise ValueError("Targa fatta male, controllala!")
    
    @property
    def targaEora(self):
        return self.__targaEora
        
#     @property
#     def dataTermineOccupazione(self):
#         return self.__dataTermineOccupazione
#         
#     @property
#     def targaPresente(self):
#         return self.__targaPresente 
#     
#     @targaPresente.setter  #aggiungo la targa presente nel parcheggio alle lista della targhe creata
#     def targaPresente(self, targa):
#         if targa not in targhePresenti:
#             targhePresenti.append(targa)
#             self.__targaPresente = targa
    
    #ritorna una stringa  con le variabili
    def __str__(self):
        return __class__.__name__ + str(self.__dict__)
           
    #serve per il programmatore, è come str
    def __repr__(self):
        return __class__.__name__ + str(self.__dict__)
    
    def parcheggio(self, targaDaInserire : str):
        if targaDaInserire == self.__targaEora:
            print("il posto è occupato e termina :", self.__targaEora)
        else:
            print("posto libero")
        return
#---------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    targhePresenti = [("AB123FG", (2025, 12, 6, 21, 12, 00)), ("EF234RG", (2025, 9, 7, 17, 13, 11))]
    print(targhePresenti)
    #
    targa1 = "WE456WE"
    dataTermineOccupazione1 = (2025, 11, 6, 21, 12, 00)
    postomezzo1 = (targa1, dataTermineOccupazione1)
    print(postomezzo1)

    #
    targaDaInserire1 = "CY765FG"
    print(postomezzo1.parcheggio(targaDaInserire1))
    #
    targaDaInserire2 = "WE456WE"
    print(postomezzo1.parcheggio(targaDaInserire2))
    
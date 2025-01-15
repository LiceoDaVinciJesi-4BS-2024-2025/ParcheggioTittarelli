#Silvia Tittarelli
#4BS
#livello 1
#classe moto

#importo la classe Veicolo
from veicolo import Veicolo

# Definisco la classe auto derivata dalla classe Veicolo.
class Moto(Veicolo):
    def __init__(self, targa):
        """
        inizializza la funzione
        """
        super().__init__(targa)
        
        if numeroMaxPasseggeri == 2:
            numeroMaxPasseggeri = self.__numeroMaxPassaggeri
        
        numeroPersoneTrasportate = self.__numeroPersoneTrasportate
        if numeroPersoneTrasportate > numeroMaxPasseggeri:
            raise ValueError("impossibile, troppe persone!!!")
        
    @property
    def targa(self):
        return self.__targa
    
    @property
    def numeroMaxPasseggeri(self):
        return self.__numeroMaxPasseggeri
    
    @property
    def numeroPersoneTrasportate(self):
        return self.__numeroPersoneTrasportate
    
    #ritorna una stringa  con le variabili
    def __str__(self):
        return __class__.__name__ + str(self.__dict__)
           
    #serve per il programmatore, è come str
    def __repr__(self):
        return __class__.__name__ + str(self.__dict__)
    

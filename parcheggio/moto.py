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
        
    @property
    def targa(self):
        return self.__targa
    
    @property
    def numeroMaxPasseggeri(self):
        return self.__numeroMaxPasseggeri
    
    @numeroMaxPasseggeri.setter
    def numeroMaxPasseggeri(self, numero : int):
        """
        imposta il numero massimo di passeggeri
        """
        if numero <= 0:
            raise ValueError("impossibile!, controlla il numero di passeggeri inserito")
        self.__numeroMaxPasseggeri = numero
        return
    
    @property
    def numeroPersoneTrasportate(self):
        return self.__numeroPersoneTrasportate
    
    @numeroPersoneTrasportate.setter
    def numeroPersoneTrasportate(self, numero: int):
        """
        indica il numero di persone presenti nel veicolo
        """
        if numero <= 0 or numero > self.__numeroMaxPasseggeri:
            raise ValueError("ci deve essere un errore, controlla meglio il numero di persone presenti nel veicolo")
        self.__numeroPersoneTrasportate = numero
        return
        
    #ritorna una stringa  con le variabili
    def __str__(self):
        return __class__.__name__ + str(self.__dict__)
           
    #serve per il programmatore, è come str
    def __repr__(self):
        return __class__.__name__ + str(self.__dict__)
#-------------------------------------------------------------------------------
if __name__ == "__main__":
    moto = Moto("CF235UG")
    print(moto)
    
    moto.numeroMaxPasseggeri = 1
    print("numero massimo di passeggeri:", moto.numeroMaxPasseggeri)
    
    moto.numeroPersoneTrasportate = 1
    print("numero di persone trasportate:", moto.numeroPersoneTrasportate)
    
    

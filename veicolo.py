#Tittarelli Silvia
#4BS
#classe veicolo

#Definisco una serie di liste per marca, colore e alimentazione per indicare i valori accettabili.
marcheMoto = ["suzuki", "honda", "yamaha", "ktm", "vespa", "beta"]
marcheAuto = ["jeep", "toyota", "lamborghini", "lancia", "tesla", "ford", "fiat", "suzuki", "alfa romeo"]
coloriAccettabili = ["nero", "bianco", "giallo", "blu", "rosso", "viola", "rosa", "verde"]
alimentazioneAccettabili = ["GPL", "benzina", "diesel", "ibride"]

#Definire la classe Veicolo, contenente le seguenti informazioni: marca, modello, colore, cilindrata(int), alimentazione, targa.
class Veicolo:
    def __init__(self, targa : str):   #L’unica informazione obbligatoria è la targa,
        """
        inizializza la funzion
        """
        self.__targa = targa
        
        if marca in marcheMoto or marca in marcheAuto:
            marca = self.__marca
            
        self.__modello = ""
        
        if colore in coloriAccettabili:
            colore = self.__colore
       
        self.__cilindrata = 0
        
        if alimentazione in alimentazioneAccettabili:
            alimentazione = self.__alimentazione
        
    @property
    def targa(self):
        return self.__targa 
    
    @property
    def marca(self):
        return self.__marca
    
    @property
    def modello(self):
        return self.__modello
    
    @property
    def colore(self):
        return self.__colore
    
    @property
    def cilindrata(self):
        return self.__cilindrata
    
    @property
    def alimentazione(self):
        return self.__alimentazione
    
    #ritorna una stringa  con le variabili
    def __str__(self):
        return __class__.__name__ + str(self.__dict__)
           
    #serve per il programmatore, è come str
    def __repr__(self):
        return __class__.__name__ + str(self.__dict__)
    
        

# che deve essere della forma AB 123 CD (dove al posto delle ABCD ci va una qualunque lettera maiuscola dell’alfabeto e al posto di 123 ci va una qualunque sequenza numerica di 3 cifre).

# Cilindrata deve essere un intero positivo multiplo di 100. 
# Aggiungere un ordinamento implicito fra gli oggetti di tipo Veicolo in modo da renderli ordinabili alfabeticamente per marca, modello e numericamente (dal più piccolo al più grande) per cilindrata.
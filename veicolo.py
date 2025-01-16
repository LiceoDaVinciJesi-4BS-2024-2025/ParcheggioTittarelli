#Tittarelli Silvia
#4BS
#classe veicolo

#Definisco una serie di liste per marca, colore e alimentazione per indicare i valori accettabili.
marcheMoto = ["suzuki", "honda", "yamaha", "ktm", "vespa", "beta"]
marcheAuto = ["jeep", "toyota", "lamborghini", "lancia", "tesla", "ford", "fiat", "suzuki", "alfa romeo"]
coloriAccettabili = ["nero", "bianco", "giallo", "blu", "rosso", "viola", "rosa", "verde"]
alimentazioneAccettabili = ["GPL", "benzina", "diesel", "ibride"]
alfabetoMaiuscolo = "QWERTYUIOPASDFGHJKLZXCVBNM"
cifre = "1234567890"
listaMarche = []
listaModelli = []
listaCilindrate = []

#Definisco la classe Veicolo, contenente le seguenti informazioni: marca, modello, colore, cilindrata(int), alimentazione, targa.
class Veicolo:
    def __init__(self, targa : str):   #L’unica informazione obbligatoria è la targa,
        """
        inizializza la funzione
        """
        self.__marca = ""
        self.__modello = ""
        self.__colore = ""
        self.__cilindrata = 0
        self.__alimentazione = ""
        
        #la targa deve essere della forma AB 123 CD (dove al posto delle ABCD ci va una qualunque lettera maiuscola dell’alfabeto e al posto di 123 ci va una qualunque sequenza numerica di 3 cifre).
        if len(targa) != 7:
            raise ValueError("£Che cavolo di targa hai messo?")
        if targa[0] in alfabetoMaiuscolo and targa[1] in alfabetoMaiuscolo and targa[5] in alfabetoMaiuscolo and targa[6] in alfabetoMaiuscolo and targa[2] in cifre and targa[3] in cifre and targa[4] in cifre:
            self.__targa = targa
        else:
            raise ValueError("Targa fatta male")
        
    @property
    def targa(self):
        return self.__targa
    
    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, marca):
        if marca not in marcheAuto or marca not in marcheMoto:
            raise ValueError("marca non valida")
        self.__marca = marca
        return
    
    @property
    def modello(self):
        return self.__modello
    
    @modello.setter
    def modello(self, modello):
        if modello not in listaModelli:
            raise ValueError("modello non valido")
        self.__modello = modello
        return
    
    @property
    def colore(self):
        return self.__colore
    
    @colore.setter
    def colore(self, colore):
        if colore not in coloriAccettabili:
            raise ValueError("colore non valido")
        self.__colore = colore
        return
        
    @property
    def cilindrata(self):
        return self.__cilindrata
    
    @cilindrata.setter
    def cilindrata(self, cilindrata):
        if cilindrata % 100 != 0:
            raise ValueError("cilindrata non valida")
        self.__cilindrata = cilindrata
        return
            
    @property
    def alimentazione(self):
        return self.__alimentazione
    
    @alimentazione.setter
    def alimentazione(self, alimentazione):
        if alimentazione not in alimentazioneAccettabili:
            raise ValueError("alimentazione non valida")
        self.__alimentazione = alimentazione
        return
    #ritorna una stringa  con le variabili
    def __str__(self):
        return __class__.__name__ + str(self.__dict__)
           
    #serve per il programmatore, è come str
    def __repr__(self):
        return __class__.__name__ + str(self.__dict__)
    
#Aggiungo un ordinamento implicito fra gli oggetti di tipo Veicolo
#in modo da renderli ordinabili alfabeticamente per marca, modello e numericamente (dal più piccolo al più grande) per cilindrata
 
    def __lt__(self, other):
        if self.__marca < other.__marca:
            return True
        elif self.__marca == other.__marca:
            if self.__modello < other.__modello:
                return True
        elif self.__modello == other.__modello:
            if self.__cilindrata < other.__cilindrata:
                return True       
           
#----------------------------------------------------------------------------
if __name__ == "__main__":
    veicolo1 = Veicolo("AB123CD")
    print(veicolo1)
    
    #veicolo2 = Veicolo("C41236D")
    #print(veicolo2)
    

    
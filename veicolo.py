#Tittarelli Silvia
#4BS
#classe veicolo

#Definisco una serie di liste per marca, colore e alimentazione per indicare i valori accettabili.
marcheMoto = ["suzuki", "honda", "yamaha", "ktm", "vespa", "beta"]
marcheAuto = ["jeep", "toyota", "lamborghini", "lancia", "tesla", "ford", "fiat", "suzuki", "alfa romeo"]
coloriAccettabili = ["nero", "bianco", "giallo", "blu", "rosso", "viola", "rosa", "verde"]
alimentazioneAccettabili = ["GPL", "benzina", "diesel", "ibride"]
alfabetoMaiuscolo = ["QWERTYUIOPASDFGHJKLZXCVBNM"]
cifre = ["1234567890"]
listaMarche = []
listaModelli = []
listaCilindrate = []

#Definisco la classe Veicolo, contenente le seguenti informazioni: marca, modello, colore, cilindrata(int), alimentazione, targa.
class Veicolo:
    def __init__(self, targa : str):   #L’unica informazione obbligatoria è la targa,
        """
        inizializza la funzione
        """
        #la targa deve essere della forma AB 123 CD (dove al posto delle ABCD ci va una qualunque lettera maiuscola dell’alfabeto e al posto di 123 ci va una qualunque sequenza numerica di 3 cifre).
        if targa[0] and targa[1] and targa[7] and targa[8] in alfabetoMaiuscolo and targa[3] and targa[4] and targa[5] in cifre:
            targa = self.__targa
        else:
            raise ValueError("targa non valida!")
        
        if marca in marcheMoto or marca in marcheAuto:
            marca = self.__marca
            
        self.__modello = ""
        
        if colore in coloriAccettabili:
            colore = self.__colore
              
        #la cilindrata deve essere un intero positivo multiplo di 100. 
        if cilindrata % 100 == 0:
            self.__cilindrata = cilindrata
        else:
            raise ValueError("cilindrata non valida")
        
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
    
#Aggiungo un ordinamento implicito fra gli oggetti di tipo Veicolo
#in modo da renderli ordinabili alfabeticamente per marca, modello e numericamente (dal più piccolo al più grande) per cilindrata
    def ordinamentoMarca(self):
        listaMarche.append(self.__marca)
        listaMarche.sort()
        return
        
    def ordinamentoModello(self):
        listaModelli.append(self.__modello)
        listaModelli.sort()
        return
        
    def ordinamentoCilindrata(self):
        listaCilindrate.append(self.__cilindrata)
        listaCilindrate.sort()
        return
    
    #controllo cilindrata
    def __lt__(self, other):
        if self.__cilindrata < other.__cilindrata:
            return True
        else:
            return False
            
           
#----------------------------------------------------------------------------
if __name__ == "__main__":
    veicolo1 = Veicolo("AB 123 CD")
    print(veicolo1)
    
    veicolo2 = Veicolo("C4 123 6D")
    print(veicolo2)
    

    
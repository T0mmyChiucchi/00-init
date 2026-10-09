class Libro:
    # Def: keyword per definire una funzione
    # __init__: costruttore della classe 
    # self: riferimento all'oggetto stesso
    # PS: nelle esercitazioni metti sempre i tipi
    def __init__(self, titolo: str, autore: str, anno: int, editore: str, pagine: int):
        self.titolo = titolo #self.titolo è una property di libro (= titolo)
        self.autore = autore
        self.anno = anno
        self.editore = editore
        self.pagine = pagine

    def reading_time(self) -> str: # metodo ma senza parametri | -> str è il return type (si può anche omettere)
        if self.pagine < 100:
            return "1 ora"
        if self.pagine < 200:
            return "2 ore"
        return "più di 2 ore"

    def __str__(self): # ToString()
        # f è il $ in C# per interpolazione dentro una unica stringa
        return f"{self.titolo} - {self.autore} ({self.anno}), {self.pagine} pagine"

class Prestito:
    def __init__(self, libro: Libro, utente: str):
        self.libro = libro
        self.utente = utente

    def __str__(self):
        return f"{self.utente} ha preso in prestito: {self.libro.titolo}"

class Biblioteca:
    def __init__(self, nome: str):
        self.nome = nome
        self.libri = [] # creazione di una lista vuota

    def aggiungi_libro(self, libro: Libro) -> None:
        self.libri.append(libro)

    def cerca_per_titolo(self, testo: str) -> Libro:
        testo = testo.lower() # converto in minuscolo (.Lower() in C#)
        
        for libro in self.libri:
            if testo in libro.titolo.lower():
                return libro
        
        return None

    def cerca_per_autore(self, autore: str):
        autore = autore.lower()
        libri_con_autore_uguale = []
        
        for libro in self.libri:
            if autore == libro.autore.lower():
                libri_con_autore_uguale.append(libro)
        
        return libri_con_autore_uguale
        # list comprehension
        # return [libro for libro in self.libri if autore in libro.autore.lower()]

    def conta_libri(self) -> int:
        return len(self.libri) # restituisce il numero di libri nella lista (.Length() in C#)

# punto di partenza di questo file python
if __name__ == "__main__":
    libro1 = Libro("", "", 1000, "", 200) # istanza di Libro, l'oggetto

    biblioteca = Biblioteca("Biblioteca Scolastica")

    biblioteca.aggiungi_libro(Libro("Il nome della rosa", "Umberto Eco", 1980, "Bompiani", 568))
    biblioteca.aggiungi_libro(Libro("Il piccolo principe", "Antoine de Saint-Exupéry", 1943, "Reynal & Hitchcock", 96))
    biblioteca.aggiungi_libro(Libro("Se questo è un uomo", "Primo Levi", 1947, "Einaudi", 180))

    print(f"Numero libri: {biblioteca.conta_libri()}")
    print("Risultati ricerca per titolo 'eco':")
    for libro in biblioteca.cerca_per_autore("eco"):
        print(f"- {libro} | tempo lettura: {libro.reading_time()}")

    prestito = Prestito(biblioteca.libri[0], "Marco")
    print(prestito)
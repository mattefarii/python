prezzi_prodotti=(
    ("Mela","Lunedì",1.0),
    ("Mela","Martedì",1.2),
    ("Mela","Mercoledì",1.1),
    ("Banana","Lunedì",0.8),
    ("Banana","Martedì",0.9),
    ("Banana","Mercoledì",0.7),
    ("Mela","Giovedì",1.0),
    ("Mela","Venerdì",1.2),
    ("Mela","Sabato",1.1),
    ("Banana","Giovedì",0.8),
    ("Banana","Venerdì",0.9),
    ("Banana","Sabato",0.7),
)


def prezzoMedio(prezzi_prodotti,prodottoScelto,giornoScelto):
    mediaPrezzo=0
    cont=0
    for prodotto,giorno,prezzo in prezzi_prodotti:
        if(prodotto==prodottoScelto and giorno==giornoScelto):
            mediaPrezzo+=prezzo
            cont+=1

    return mediaPrezzo/cont

sceltaGiorno=input("Inserisci un giorno della settimana: ")
sceltaProdotto=input("Inserisci un prodotto: ")
media=prezzoMedio(prezzi_prodotti,sceltaProdotto,sceltaGiorno)
print("Il prezzo medio dell'articolo: ",sceltaProdotto," il giorno: ",sceltaGiorno," è di: ", media)
  
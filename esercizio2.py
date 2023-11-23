prezzi_prodotti=(
("Mela",("Lunedì",1.0),("Martedì",1.2),("Mercoledì",1.1),("Giovedì",1.0),("Venerdì",1.2),("Sabato",1.1)),
("Banana",("Lunedì",0.8),("Martedì",0.9),("Mercoledì",0.7),("Giovedì",0.8),("Venerdì",0.9),("Sabato",0.7)),
)

def prezzoMedio(prezzi_prodotti,prodottoScelto):
    mediaPrezzo=0
    cont=0
    for prodotto,*altro in prezzi_prodotti:
        for giorno,prezzo in altro:
            if(prodotto==prodottoScelto):
                mediaPrezzo+=prezzo
                cont+=1
    return mediaPrezzo/cont

def prezzoMedioAll(prezzi_prodotti):
    cont=0
    mediaPrezzoAll=0
    for prodotto,*altro in prezzi_prodotti:
        for giorno,prezzo in altro:
            mediaPrezzoAll+=prezzo
            cont+=1
    return mediaPrezzoAll/cont

prodotto=input("Inserisci un prodotto per verificarne il prezzo medio: ")
print("Il prezzo medio del prodotto:",prodotto," è di: ",prezzoMedio(prezzi_prodotti,prodotto))
print("Il prezzo medio di tutti i prodotti è di: ",prezzoMedioAll(prezzi_prodotti))
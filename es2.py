tupla_vendite = (
                (("RepartoA","Informatica"),("Prodotto A", ("contanti",1000))),
                (("RepartoA","Informatica"),("Prodotto B", ("carta di credito",1500))),
                (("RepartoA","Informatica"),("Prodotto C", ("carta di credito",1200))),
                (("RepartoA","Informatica"),("Prodotto D", ("contanti",200))),
                (("RepartoA","Informatica"),("Prodotto E", ("contanti",800))),
                (("RepartoA","Informatica"),("Prodotto F", ("N/D",200))),
                (("RepartoB","Elettronica"),("Prodotto A", ("contanti",1500))),
                (("RepartoB","Elettronica"),("Prodotto B", ("carta di credito",900)))
                )



def media_globale(tupla_vendite):
    media=0
    cont=0
    for reparto,(prodotto,(metodoP,prezzo)) in tupla_vendite:
        media+=prezzo
        cont+=1
        
    return (media/cont)

def media(tupla_vendite):
    media=0
    cont=0
    for reparto,(prodotto,(metodoP,prezzo)) in tupla_vendite:
        if(reparto==cat):
            if(metodoP==tipPag):
                media+=prezzo
                cont+=1
    return (media/cont)

def venditaMax(tupla_vendite):
    vMax=0
    for reparto,(prodotto,(metodoP,prezzo)) in tupla_vendite:
        if (vMax<prezzo):
            rep=reparto
            prod=prodotto
            metodoPag=metodoP
            costo=prezzo
    return rep,prod,metodoPag,prezzo

def venditaMin(tupla_vendite):
    vMin=9999
    for reparto,(prodotto,(metodoP,prezzo)) in tupla_vendite:
        if (vMin>prezzo):
            rep=reparto
            prod=prodotto
            metodoPag=metodoP
            costo=prezzo
    return rep,prod,metodoPag,prezzo
    

mediaTot=media_globale(tupla_vendite)
mediaScelte=media_globale(tupla_vendite)
valMax=venditaMax(tupla_vendite)
valMin=venditaMin(tupla_vendite)

while(True):
    menu=int(input("1) media globale,2) media,3)venditaMax,4)venditaMin,5)vednitaPer: "))
    if(menu==1):
        print("La media totale è di: ",mediaTot)
    elif(menu==2):
        cat=input("Inserisci la categoria: ")
        tipPag=input("Inserisci la tipologia di pagamento: ")
        print("La media di importi con il metodo di pagamento: ",cat," è di: ",mediaScelte)
    elif(menu==3):
        print("Il valore massimo è: ",valMax)
    elif(menu==4):
        print("Il valore massimo è: ",valMin)
    elif(menu==5):
        print("B")
    else:
        break



print("La media totale è di: ",mediaTot)
print("La media di importi con il metodo di pagamento: ",cat," è di: ",mediaScelte)
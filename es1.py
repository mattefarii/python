dati_pioggie=(
    ("Milano", [("Gennaio", 12),("Febbraio", "N/D"),("Marzo",24),("Aprile",0),("Maggio",3),("Giugno",21),("Luglio",4),("Agosto",5),("Settembre",2),("Ottobre",4),("Novembre",0),("Dicembre",0)]),
    ("Monza", [("Gennaio", 0),("Febbraio", 7),("Marzo",8),("Aprile",2),("Maggio",5),("Giugno",1),("Luglio","N/D"),("Agosto",29),("Settembre",9),("Ottobre",3),("Novembre",1),("Dicembre",3)]),
    ("Brescia", [("Gennaio", 10),("Febbraio", 15),("Marzo",40),("Aprile",35),("Maggio",14),("Giugno",0),("Luglio",3),("Agosto","N/D"),("Settembre",2),("Ottobre",3),("Novembre",15),("Dicembre",0)]),
)
def verifica_dati(dati_pioggie):
    media=0
    mediaPioggie=0
    cont=0
    vMax=0
    vMin=1
    meseMax=0
    meseMin=0
    for citta,*altro in dati_pioggie:
        dati=altro[0]
        for mese,pioggia in dati:
            if(pioggia==0 or pioggia=="N/D"):
                cont+=cont
            else:
                media+=pioggia
                cont+=1
                if(pioggia!="N/D"):
                    if(pioggia>vMax):
                        vMax=pioggia
                        meseMax=mese
                        if(pioggia<vMin):
                            vMin=pioggia
                            meseMin=mese
                            print(mese)
    mediaPioggie=media/cont
    return ((mediaPioggie),(vMax,meseMax),(vMin,meseMin))

mediaTot,massimo,minimo=verifica_dati(dati_pioggie)
print("La media delle precipitazioni è:",mediaTot," il valore massimo delle precipitazioni è stato di: ",massimo[0]," avvenuto nel mese di: ",massimo[1], " il valore minimo delle precipitazioni è stato di: ",minimo[0]," avvenuto nel mese di: ",minimo[1])

    
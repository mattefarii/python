# Inizializza la struttura dati
pagella = {
    "studente1": [
        ("Matematica", (7, 2), (8, 1)),
        ("Italiano", (6, 3), (7, 2)),
        ("Inglese", (8, 1), (9, 0)),
    ],
    "studente2": [
        ("Matematica", (8, 4), (8, 6)),
        ("Italiano", (5, 6), (4, 0)),
        ("Inglese", (9, 1), (10, 0)),
    ],
    "studente3": [
        ("Matematica", (5, 3), (6, 4)),
        ("Italiano", (7, 1), (8, 7)),
        ("Inglese", (4, 3), (5, 2)),
    ]
    
}

pagella["Albert Einstein"]=[("Matematica", (10, 0),(10,0)),
                            ("Italiano", (10, 0),(10,0)), 
                            ("Inglese", (10, 0),(10,0)),
]

pagella["studente1"].append(("Fisica",9.5,0))
pagella["studente2"].append(("Fisica",8,1))
pagella["studente3"].append(("Fisica",8,3))
pagella["Albert Einstein"].append(("Fisica",10,0))


def stampa_dati1():
    dati=0
    studenteIns=input("Inserisci il nome di uno studente per visualizzare i dati:")
    if studenteIns in pagella.keys():
        for vettore in pagella[studenteIns]:
            if(vettore[0]=="Matematica"):
                dati=(vettore[1])
    else:
        print("studente inesistente")
               
    return dati

def stampa_dati2():
    dati=0
    studenteIns=input("Inserisci il nome di uno studente per visualizzare i dati:")
    materiaIns=input("Inserisci una materia per visualizzare i dati:")
    if studenteIns in pagella.keys():
        for vettore in pagella[studenteIns]:
            if(vettore[0]==materiaIns):
                dati=(vettore[2])
    return dati

def cont_assenze():
    contA=0
    indVet=1
    indVet2=2
    studenteIns=input("Inserisci il nome di uno studente per visualizzare i dati:")
    if studenteIns in pagella.keys():
        for vettore in pagella[studenteIns]:
            contA+=vettore[indVet][1]
            contA+=vettore[indVet2][1]
            indVet+=1
            indVet2+=1
            totAss=contA
            if(totAss>contA):
                contA=vettore[indVet][1][1]
                contA+=vettore[indVet][2][1]
    return contA
                
                
datiMate=stampa_dati1()
datiGenerali=stampa_dati2()
contAssenze=cont_assenze()
print("Dati matematica per lo studente selezionato:",datiMate)
print("Dati per lo studente selezionato:",datiGenerali)
print("Materia con più assenze per lo studente selezionato:",contAssenze)
#MEDIA VOTI DI N STUDENTI
"""1.Creare un dizionario di N studenti.
Ogni elemento del dizionario contiene come chiave il nome
dello studente e come valore una lista di tre numeri, cioè
i voti in [Matematica, Fisica e Chimica].
2.Inserendo il nome di uno studente, il programma restituisce
in output la media dei suoi voti
(arrotandata a due cifre dopo la virgola)."""

studenti={}
media=0


def aggiungi_voti(nStud):
    Mate=""
    Fisica=""
    Chimica=""
    media=0
    for i in range (nStud):
        nomeStud=input("Inserisci il nome dello studente:")
        Mate=int(input("Inserisci il voto per matematica:"))
        Fisica=int(input("Inserisci il voto per fisica:"))
        Chimica=int(input("Inserisci il voto per chimica:"))
        studenti[nomeStud]=[Mate,Fisica,Chimica]
       
nStud=int(input("Inserisci il numero di studenti:"))
aggiungi_voti(nStud)
print("voti studenti:",studenti)

def media(nomeMedia):
    voti=studenti[nomeMedia]
    somma=0
    for voto in voti:
        somma+=voto
    return somma/len(voti)

nomeMedia=input("Inserisci il nome di uno studente per calcolarne la media:")
mediaStud=media(nomeMedia)
print("La media dello studente:",nomeMedia,"è di:",mediaStud)


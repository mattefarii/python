# Inizializza una lista vuota per le prenotazioni
prenotazioni = []



# Esempio di utilizzo delle funzioni
aggiungi_prenotazione(prenotazioni, "Maria", "04-10-2023", 4, 3)
aggiungi_prenotazione(prenotazioni, "Pietro", "04-10-2023", 2, 2)
aggiungi_prenotazione(prenotazioni, "Carlo", "04-10-2023", 5, 5)
print("Tavoli disponibili per il 04-10-2023:", tavoli_disponibili(prenotazioni, "04-10-2023"))
print("Prenotazioni di Maria:", prenotazioni_cliente(prenotazioni, "Maria"))
print("Conto totale per il 04-10-2023:", conto_totale(prenotazioni, "04-10-2023"))

#output atteso 
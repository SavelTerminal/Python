scelte_menu = ["1", "2", "3", "4"]
eventi = []

def statistiche_eventi(lista_eventi):
    if not lista_eventi:
        print("La lista è vuota!\n")
    else:
        somma_durata = 0
        numero_eventi = len(lista_eventi)
        for evento in (lista_eventi):
            durata = evento['Durata']
            somma_durata += durata

        media_durata = somma_durata / numero_eventi
        
        print(f"Somma durata: {somma_durata}")
        print(f"Numero eventi: {numero_eventi}")
        print(f"La media della durata è: {round(media_durata, 2)}\n")
        



def aggiungi_evento():
    tipo_evento = input("Che tipo di evento vuoi registrare? ")
    descrizione_evento = input("Inserisci la descrizione dell'evento: ")
    while True:
        durata_evento = input("Durata (Minuti): ")
        try:
            durata_evento = int(durata_evento)
            break
        except:
            print("Caratteri invalidi\n")

    dizionario_evento = {
        "Tipo": tipo_evento,
        "Descrizione": descrizione_evento,
        "Durata": durata_evento
    }
    return dizionario_evento

def mostra_eventi(lista_eventi):
    if not lista_eventi:
        print("\nLa lista è vuota!\n")
    else:
        for evento in lista_eventi:
            print(f"Tipo: {evento['Tipo']}")
            print(f"Descrizione: {evento['Descrizione']}")
            print(f"Durata: {evento['Durata']}\n")

while True:
    print(f"--Tracker--")
    print("1) Aggiungi evento")
    print("2) Mostra eventi")
    print("3) Statistiche")
    print("4) Esci\n")


    scelta_menu = input("Digita la tua scelta: ")
    

    if scelta_menu not in scelte_menu:
        print("Comando non valido, Riprova")

    elif scelta_menu == "1":
        print("\nHai scelto aggiungi evento\n")
        evento1 = aggiungi_evento()
        eventi.append(evento1)
        # Altro codice

    elif scelta_menu == "2":
        print("\nHai scelto mostra eventi\n")
        mostra_eventi(eventi)
        # Altro codice

    elif scelta_menu == "3":
        
        print("\nHai scelto statistiche\n")

        statistiche_eventi(eventi)

    elif scelta_menu == "4":
        print("\nAlla prossima!\n")
        break
    # Nessun codice, siamo usciti dall'app

    

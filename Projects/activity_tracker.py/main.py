scelte_menu = ["1", "2", "3", "4"]
eventi = []
evento_aggiunto = ""

def aggiungi_evento():
    evento_aggiunto = input("Inserisci l'evento che vuoi aggiungere: ")
    print(evento_aggiunto + " E' stato aggiunto ai tuoi eventi correttamente.")
    return evento_aggiunto

def mostra_eventi():
    if not eventi:
        print("Non ci sono eventi.")
    else:
        for evento in eventi:
            print(evento) 

while True:
    print(f"--Tracker--")
    print("1) Aggiungi evento")
    print("2) Mostra eventi")
    print("3) Statistiche")
    print("4) Esci")


    scelta_menu = input("Digita la tua scelta: ")
    

    if scelta_menu not in scelte_menu:
        print("Comando non valido, Riprova")

    elif scelta_menu == "1":
        print("Hai scelto aggiungi evento")
        evento1 = aggiungi_evento()
        eventi.append(evento1)
        # Altro codice

    elif scelta_menu == "2":
        print("Hai scelto mostra eventi")
        mostra_eventi()
        # Altro codice

    elif scelta_menu == "3":
        print("Hai scelto statistiche")
        # Altro codice

    elif scelta_menu == "4":
        print("Alla prossima!")
        break
    # Nessun codice, siamo usciti dall'app

    

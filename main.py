import tkinter as tk
import math

#TODO Trova modo di mostrare parole solo un po' per volta (a ogni spacebar, le parole scorrono di uno)

FONT_NAME = "courier new"
TEXT = ["casa", "tempo", "giorno", "mondo", "vita", "mano", "parte", "occhio", "donna", "uomo", "stato", "lavoro",
        "parola", "problema", "momento", "strada", "forza", "paese", "punto", "bambino", "notte", "storia", "voce",
        "testa", "aria", "gioco", "libertà", "amore", "amico", "scuola", "chiave", "tempo", "giro", "corso", "lume",
        "mare", "terra", "fuoco", "vento", "fiore", "pietra", "fiume", "bosco", "montagna", "stella", "luna", "sole",
        "nuvola", "ombra", "luce", "colore", "suono", "musica", "porta", "finestra", "muro", "tetto", "stanza",
        "tavolo", "sedia", "libro", "penna", "foglio", "lettera", "quadro", "specchio", "tempo", "strada", "città",
        "paese", "regione", "popolo", "stato", "governo", "legge", "diritto", "pace", "guerra", "forza", "mente",
        "cuore", "anima", "spirito", "pensiero", "idea", "sogno", "verità", "segreto", "mistero", "dubbio", "ragione",
        "scelta", "azione", "opera", "frutto", "seme", "pianta", "foglia", "ramo", "radice"]
# STRING_TEXT = " ".join(TEXT)

#TODO  CORREGGI TIMER Fai avviare countdown all'inizio della digitazione; interruzione allo scadere del minuto
#
# def start_timer(count, label):
#         global timer
#         count_min = math.floor(count / 60)  # senza i decimali per aver i minuti che mancano
#         count_sec = count % 60  # ci dà il remainder, quindi i secondi che mancano
#
#         if count_sec < 10:
#                 count_sec = f"0{count_sec}"  # Dynamic Typing: cambiare il tipo di una variabile semplicemente scrivendo il nuovo valore di tipo diverso
#
#         label.config(text=f"{count_min}:{count_sec}")
#         if COUNT > 0:
#                 timer = root.after(1000, start_timer, count - 1)

#TODO Fai funzione di restituzione (numero parole e caratteri digitati; eventuali errori (cosa è stato tolto dal conteggio)

root = tk.Tk()
root.title("Typing Speed Test")
root.config(padx=100, pady=50)
root.minsize(500, 700)

main_label = tk.Label(text="Welcome to the Typing Speed Test by Alis!", fg="blue")
main_label.config(font=(FONT_NAME, 18, "bold"))
main_label.pack()

timer = tk.Label(text="00:00", font=(FONT_NAME, 16, "bold"))
timer.pack()

explanation_label = tk.Label(text="Premi la barra spaziatrice dopo ogni parola.\nDa quando inizi a digitare hai 1 "
                                  "minuto di tempo.\nCopia il testo seguente:")
explanation_label.config(font=(FONT_NAME, 12, "bold"), pady=25)
explanation_label.pack()

text_label = tk.Label(text=f"{TEXT[0]} {TEXT[1]} {TEXT[2]}", width=50)
text_label.config(font=(FONT_NAME, 12), bd=1, relief="sunken")
text_label.pack()

entry = tk.Entry(width=50, bd=1, font=(FONT_NAME, 12))
# entry.focus()
#entry.get()
entry.pack()

# start_timer(count=60, label=timer)

#TODO Salvataggio dei punteggi (es. record per ogni utente, fai scegliere nome utente all'inizio)

root.mainloop()
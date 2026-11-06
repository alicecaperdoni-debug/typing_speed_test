import tkinter as tk
from tkinter import messagebox as mb
import math
import itertools

FONT_NAME = "courier new"
#TODO randomizza le parole per averle in ordine casuale ogni volta; fai contare il punteggio con la lista randomizzata
TEXT = ["casa", "tempo", "giorno", "mondo", "vita", "mano", "parte", "occhio", "donna", "uomo", "stato", "lavoro",
        "parola", "problema", "momento", "strada", "forza", "paese", "punto", "bambino", "notte", "storia", "voce",
        "testa", "aria", "gioco", "libertà", "amore", "amico", "scuola", "chiave", "tempo", "giro", "corso", "lume",
        "mare", "terra", "fuoco", "vento", "fiore", "pietra", "fiume", "bosco", "montagna", "stella", "luna", "sole",
        "nuvola", "ombra", "luce", "colore", "suono", "musica", "porta", "finestra", "muro", "tetto", "stanza",
        "tavolo", "sedia", "libro", "penna", "foglio", "lettera", "quadro", "specchio", "tempo", "strada", "città",
        "paese", "regione", "popolo", "stato", "governo", "legge", "diritto", "pace", "guerra", "forza", "mente",
        "cuore", "anima", "spirito", "pensiero", "idea", "sogno", "verità", "segreto", "mistero", "dubbio", "ragione",
        "scelta", "azione", "opera", "frutto", "seme", "pianta", "foglia", "ramo", "radice"]

timer = None
first = 0
second = 1
third = 2

#TODO Rischiacciare invio non fa ripartire il countdown

# Key handlers
def return_key_handler(event):
        start_timer(10)
        # start_timer(60)
        text_label.config(text=f"{TEXT[first]} {TEXT[second]} {TEXT[third]}", fg="black")

def space_key_handler(event):
        global first, second, third
        first += 1
        second += 1
        third +=1
        text_label.config(text=f"{TEXT[first-1]}\n{TEXT[first]} {TEXT[second]} {TEXT[third]}")

# Get Value
def get_value():
    answer = entry.get()
    return answer

# Calcolo punteggio
def check_result():
    correct_words = []
    wrong_words = []
    words_list = get_value().split()
    char_list = get_value()
    for word in words_list:
        if word == TEXT[words_list.index(word)]:
            correct_words.append(word)
        else:
            wrong_words.append(word)

    wrong_char = list(itertools.chain(*wrong_words))
    points = len(char_list) - len(wrong_char)

    if len(wrong_words) > 0:
        see_errors = mb.askyesno("Tempo scaduto!", message=f"Hai digitato {len(char_list)} caratteri.\n"
                                         f"Parole scritte correttamente: {len(correct_words)}\n"
                                         f"Parole sbagliate: {len(wrong_words)}\n"
                                         f"Il tuo punteggio finale è: {points}\n\n"
                                         f"Vuoi vedere le parole che hai sbagliato?")
        if see_errors:
            wrong_list = ', '.join(wrong_words)
            mb.showinfo("Errori", message=f"{wrong_list}")

    else:
        mb.showinfo("Tempo scaduto!", message=f"Hai digitato {len(char_list)} caratteri.\n"
                                         f"Parole scritte correttamente: {len(correct_words)}\n"
                                         f"Parole sbagliate: {len(wrong_words)}\n"
                                         f"Il tuo punteggio finale è: {points}")

# Timer
def start_timer(count):
        global timer
        count_min = math.floor(count / 60)  # senza i decimali per aver i minuti che mancano
        count_sec = count % 60  # ci dà il remainder, quindi i secondi che mancano

        if count_sec < 10:
            count_sec = f"0{count_sec}"  # Dynamic Typing: cambiare il tipo di una variabile

        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        if count > 0:
            timer = root.after(1000, start_timer, count - 1)
        if count == 0:
            canvas.itemconfig(timer_text, fill="red")
            check_result()

# GUI
root = tk.Tk()
root.title("Typing Speed Test")
root.config(padx=100, pady=50)
root.minsize(300, 600)

main_label = tk.Label(text="TYPING SPEED TEST\nBenvenuto/a!", fg="blue")
main_label.config(font=(FONT_NAME, 18, "bold"))
main_label.pack()

canvas = tk.Canvas(width=300, height=200, highlightthickness=0) #colore background + eliminare "cornice" che rimaneva bianca
timer_text = canvas.create_text(100, 100, text="1:00", fill="green", font=(FONT_NAME, 35, "bold")) #testo sopra all'immagine canvas
canvas.pack()

explanation_label = tk.Label(text="Dovrai copiare delle parole; ogni parola dovrà essere seguita da uno SPAZIO.\n"
                                  "Premi invio per iniziare.")
explanation_label.config(font=(FONT_NAME, 12, "bold"), pady=10)
explanation_label.pack()

text_label = tk.Label(text="Le parole compariranno qui", fg="grey", width=50)
text_label.config(font=(FONT_NAME, 12), bd=1, relief="sunken")
text_label.pack()

entry = tk.Entry(width=50, bd=1, font=(FONT_NAME, 12))
entry.focus()
entry.pack()

root.bind("<Return>", return_key_handler)
root.bind("<space>", space_key_handler)

#TODO Crea tasto annulla (se uno vuole ripartire)

#TODO Salvataggio dei punteggi (es. record per ogni utente, fai scegliere nome utente all'inizio)

root.mainloop()
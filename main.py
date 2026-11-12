import tkinter as tk
from tkinter import messagebox as mb, simpledialog
import csv
import os
import math
import itertools
import random

FONT_NAME = "courier new"
WORDS = ["casa", "tempo", "giorno", "mondo", "vita", "mano", "parte", "occhio", "donna", "uomo", "stato", "lavoro",
        "parola", "problema", "momento", "strada", "forza", "paese", "punto", "bambino", "notte", "storia", "voce",
        "testa", "aria", "gioco", "libertà", "amore", "amico", "scuola", "chiave", "tempo", "giro", "corso", "lume",
        "mare", "terra", "fuoco", "vento", "fiore", "pietra", "fiume", "bosco", "montagna", "stella", "luna", "sole",
        "nuvola", "ombra", "luce", "colore", "suono", "musica", "porta", "finestra", "muro", "tetto", "stanza",
        "tavolo", "sedia", "libro", "penna", "foglio", "lettera", "quadro", "specchio", "tempo", "strada", "città",
        "paese", "regione", "popolo", "stato", "governo", "legge", "diritto", "pace", "guerra", "forza", "mente",
        "cuore", "anima", "spirito", "pensiero", "idea", "sogno", "verità", "segreto", "mistero", "dubbio", "ragione",
        "scelta", "azione", "opera", "frutto", "seme", "pianta", "foglia", "ramo", "radice"]
random_words = []

timer = None
game_on = False
first = 0
second = 1
third = 2

# Key handlers
def return_key_handler(event):
        global game_on
        if not game_on:
            game_on = True
            start_timer(60)
            for i in range(len(WORDS)):
                random_words.append(random.choice(WORDS))
            text_label.config(text=f"{random_words[first]} {random_words[second]} {random_words[third]}", fg="black")
        else:
            pass

def space_key_handler(event):
        global first, second, third
        first += 1
        second += 1
        third +=1
        text_label.config(text=f"{random_words[first-1]} {random_words[first]} {random_words[second]} {random_words[third]}")

# Get Value
def get_value():
    answer = entry.get()
    return answer

# Salvare il punteggio
def save_score(username, new_score, file_path="scores.csv"):
    scores = {}

    # 1. Leggi il file esistente (se esiste) e carica i dati nel dizionario
    if os.path.exists(file_path):
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if "Name" in row and "High Score" in row:
                    user = row["Name"]
                    try:
                        score = int(row["High Score"])
                    except ValueError:
                        score = 0
                    scores[user] = score

    # 2. Verifica se l'utente esiste già e confronta il punteggio
    if username in scores:
        if new_score > scores[username]:
            mb.showinfo("Salvataggio", message=f"Nuovo record personale per {username}! {new_score} (Precedente: {scores[username]})")
            scores[username] = new_score
        else:
            mb.showinfo("Salvataggio", message=f"Punteggio non superato. Il tuo record resta {scores[username]}.")
    else:
        # Se è un nuovo utente, aggiungilo
        mb.showinfo("Salvataggio", message=f"Primo punteggio registrato per {username}: {new_score}!")
        scores[username] = new_score

    # 3. Riscrivi il file CSV usando le intestazioni "Name" e "High Score"
    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = ["Name", "High Score"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for user, score in scores.items():
            writer.writerow({"Name": user, "High Score": score})

# Calcolo punteggio
def check_result():
    correct_words = []
    wrong_words = []
    words_list = get_value().split()
    char_list = get_value()
    for word in words_list:
        if word == random_words[words_list.index(word)]:
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

    save = mb.askyesno("Salvataggio", message="Vuoi salvare/aggiornare il tuo punteggio?")
    if save:
        username = simpledialog.askstring("Il tuo nome", prompt="Scrivi il tuo nickname:")
        save_score(username, points)

# Timer
def start_timer(count):
        global timer
        count_min = math.floor(count / 60)
        count_sec = count % 60

        if count_sec < 10:
            count_sec = f"0{count_sec}"

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
timer_text = canvas.create_text(150, 100, text="1:00", fill="green", font=(FONT_NAME, 35, "bold")) #testo sopra all'immagine canvas
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

root.mainloop()
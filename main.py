import tkinter as tk
from tkinter import messagebox as mb, simpledialog
import csv
import pandas
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
            start_timer(10)
            # start_timer(60)
            for i in range(len(WORDS)):
                random_words.append(random.choice(WORDS))
            print(random_words)
            text_label.config(text=f"{random_words[first]} {random_words[second]} {random_words[third]}", fg="black")
        else:
            pass

#TODO rendere più chiara la parola che è da scrivere

def space_key_handler(event):
        global first, second, third
        first += 1
        second += 1
        third +=1
        text_label.config(text=f"{random_words[first-1]}\n{random_words[first]} {random_words[second]} {random_words[third]}")

# Get Value
def get_value():
    answer = entry.get()
    return answer

# Salvare il punteggio
def save_score(score):
    fields = ['Name', 'High Score']
    save = mb.askyesno("Salvataggio", message="Vuoi salvare/aggiornare il tuo punteggio?")

    if save:
        username = simpledialog.askstring("Il tuo nome", prompt="Scrivi il tuo nickname:")
        new_row = {'Name': username,
                   'High Score': score}

        data = pandas.read_csv("scores.csv")
        users_list = data['Name'].to_list()

        if username in users_list:
            user_data = data[data['Name'] == username]
            print(type(user_data))
#TODO l'if qua sotto crea nuova riga e nuova colonna nella copia
            if (user_data['High Score'] < score).any():
                new_data_copy = data.copy()
                new_data_copy.loc[username, 'High Score'] = score
                new_data_copy.to_csv("scores.csv")
                # data.at[user_data['Name']]['High Score'] = score
                # user_data['High Score'] = user_data['High Score'].replace({user_data['High Score']: score})
                # data.to_csv("scores.csv", index=False)
                mb.showinfo("Salvataggio", message="Il tuo punteggio più alto è stato aggiornato.")

            else:
                mb.showinfo("Salvataggio", message=f"Non hai superato il tuo punteggio più alto "
                                                   f"({user_data['High Score']})")

        else:
            with open("scores.csv", "a", newline='') as s2:
                writer = csv.DictWriter(s2, fields)
                writer.writerow(new_row)
                mb.showinfo("Salvataggio", message="Il tuo primo punteggio è stato inserito!")

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
    save_score(points)

#TODO Allo scadere del tempo i tasti non fanno andare avanti i messagebox

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
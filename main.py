import tkinter as tk
import json
import random
import time
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

# Загрузка JSON файла
def load_sentences():
    try:
        # Сначала пробуем загрузить из ресурсов (для EXE)
        with open(resource_path('sentences.json'), 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        # Если не получается, пробуем загрузить обычным способом
        try:
            with open('sentences.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            # Если файл не найден, создаем базовую структуру
            return {
                "Easy": {1:["Bruh, there is an error"]},
                "Normal": {1:["I messed up"]},
                "Hard": {1:["R.I.P"]}
            }
def click():
    global n, cor, cor_sent, text
    ur_sent = entry.get()
    n += 1
    entry.delete(0, tk.END)
    entry.focus()
    if ur_sent.lower().strip(' .') == cor_sent.lower().strip(' .'):
        cor += 1
    new_sent()

def new_sent():
    global n, cor_sent
    if n < 20:
        i = list(text)[random.randrange(0, len(list(text)))]
        j = random.randrange(0, len(text[i]))
        sent = text[i].pop(j)
        if len(text[i]) == 0:
            text.pop(i)
        cor_sent = sent
        sent = sent.split()
        random.shuffle(sent)
        sent = ' '.join(sent).lower()
        task.config(text = f'{n+1})' + sent)
    else:
        result()

def result():
    global n, cor_sent, cor, start
    if n < 20:
        n+=1
        ur_sent = entry.get()
        entry.delete(0, tk.END)
        entry.focus()
        if ur_sent.lower().strip(' .') == cor_sent.lower().strip(' .'):
            cor += 1
    frame2.pack_forget()
    frame3.pack(fill="both", expand=True)
    end = time.time()
    deltime = (end - start)
    label3.config(text = dif + f', Correct sentances: {cor}/{n}')
    label4.config(text = f'{int(cor / n * 100)} % correct')
    timer.config(text = f'time: {int(deltime // 3600)}:{int(deltime % 3600 // 60)}:{int(deltime % 3600 % 60)}')

def re():
    global n, cor_sent, dif, cor, choice, start
    frame3.pack_forget()
    frame1.pack(fill="both", expand=True)
    n = 0
    dif = str()
    cor = 0
    cor_sent = str()
    choice = load_sentences() 
    start = time.time()

def easy():
    global dif, text, start
    start = time.time()
    frame1.pack_forget()
    frame2.pack(fill="both", expand=True)
    dif = 'Easy'
    text = choice[dif]
    new_sent()
def normal():
    global dif, text, start
    start = time.time()
    frame1.pack_forget()
    frame2.pack(fill="both", expand=True)
    dif = 'Normal'
    text = choice[dif]
    new_sent()
def hard():
    global dif, text, start
    start = time.time()
    frame1.pack_forget()
    frame2.pack(fill="both", expand=True)
    dif = 'Hard'
    text = choice[dif]
    new_sent()


n = 0
dif = str()
cor = 0
cor_sent = str()
start = time.time()
choice = load_sentences()
window = tk.Tk()
window.title("Sentence Builder")
window.geometry("500x300")
window.resizable(False, False)
window.configure()

frame1 = tk.Frame(window, bg='DodgerBlue4')
frame1.pack(fill="both", expand=True)

label1 = tk.Label(frame1, text = 'Select difficulty', bg='DodgerBlue4', font = ("Arial", 20))
label1.pack(pady = 20)
btn1 = tk.Button(frame1, text = 'Easy', fg = 'black', bg = 'DodgerBlue', width = 20, height = 2, command = easy)
btn1.pack(side = 'left', padx = 10)
btn2 = tk.Button(frame1, text = 'Normal', fg = 'black', bg = 'DodgerBlue', width = 20, height = 2, command = normal)
btn2.pack(side = 'left', padx = 10)
btn3 = tk.Button(frame1, text = 'Hard', fg = 'black', bg = 'DodgerBlue', width = 20, height = 2, command = hard)
btn3.pack(side = 'left', padx = 10)

frame2 = tk.Frame(window, bg='DodgerBlue4')
label2 = tk.Label(frame2, text = 'Write the correct sentence', bg='DodgerBlue4', font = ("Arial", 20))
label2.pack(pady = 20)
task = tk.Label(frame2, bg = 'DodgerBlue4', font = ("Arial", 12))
task.pack(pady = 20)
entry = tk.Entry(frame2, bg  = 'azure2', width = 30, font = ("Arial", 14))
entry.pack(pady = 10)
btn_check = tk.Button(frame2, text = "Check", bg  = 'DodgerBlue', width = 20, height = 2, font = ("Arial", 12), command = click)
btn_check.pack(pady = 20)
btn_exit = tk.Button(frame2, text = "Stop", bg  = 'DodgerBlue', width = 5, height = 2, font = ("Arial", 10), command = result)
btn_exit.pack(anchor='ne')

frame3 = tk.Frame(window, bg='DodgerBlue4')
label3 = tk.Label(frame3, bg='DodgerBlue4', font = ("Arial", 20))
label3.pack(pady = 20)
label4 = tk.Label(frame3, bg='DodgerBlue4', font = ("Arial", 15))
label4.pack(pady = 20)
timer = tk.Label(frame3, bg='DodgerBlue4', font = ("Arial", 15))
timer.pack(pady = 20)
btn_return = tk.Button(frame3, text = "Return", bg  = 'DodgerBlue', width = 20, height = 2, font = ("Arial", 10), command = re)
btn_return.pack(pady = 20)

window.mainloop()
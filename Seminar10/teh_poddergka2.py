# Задача 2. Добавьте боту модуль, который позволяет считывать из файла вопрос,
# отвечать на него и отправлять ответ обратно пользователю.

import telebot
from tkinter import *
from tkinter import ttk


bot = telebot.TeleBot(
    "", parse_mode=None)

with open('teh_poddergka.txt', 'r+', encoding='utf-8') as data:
    temp = data.readlines()
i=0
window = 0

@bot.message_handler(commands=['voprosi'])
def nachalo(message):
    global i
    def clicked():  
        res = bot.reply_to(message,format(txt.get()))   
    window = Tk()  
    window.title("Администратор технической поддержки клиентов")  
    window.geometry('500x450')  
    lbl = Label(window, text=temp)  
    lbl.grid(column=0, row=0)  
    txt = Entry(window,width=50)  
    txt.grid(column=1, row=0)  
    btn = Button(window, text="Ответить", command=clicked)  
    btn.grid(column=2, row=0)
    i+=1
    bot.register_next_step_handler(message, wind)  
    window.mainloop()
        
def wind(message):
    def clicked():  
        res = bot.reply_to(message,format(txt.get()))
    global window
    lbl = Label(window, text=temp)  
    lbl.grid(column=0, row=0)  
    txt = Entry(window,width=50)  
    txt.grid(column=1, row=0)  
    btn = Button(window, text="Ответить", command=clicked)  
    btn.grid(column=2, row=0)
    bot.register_next_step_handler(message, wind)  
    window.mainloop()

bot.infinity_polling()
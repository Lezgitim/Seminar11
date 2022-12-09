# Задача 1. Напишите бота для техподдержки.
# Бот должен записывать обращения пользователей в файл.

import telebot
from tkinter import *
from tkinter import ttk

bot = telebot.TeleBot(
    "5790030707:AAErS3FPc9-b4CkM7QlHPFgXGDRbbb8NTss", parse_mode=None)


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Какой у Вас вопрос?")
    bot.register_next_step_handler(message, teh) 


window = 0


def teh(message):
    with open('teh_poddergka.txt', 'r+', encoding='utf-8') as data:
        data.writelines(str(message.from_user.id)+':'+str(message.text)+'\n')
    def clicked():  
        res = bot.reply_to(message,format(txt.get()))   
    window = Tk()  
    window.title("Администратор технической поддержки клиентов")  
    window.geometry('500x450')  
    lbl = Label(window, text=message.text)  
    lbl.grid(column=0, row=0)  
    txt = Entry(window,width=50)  
    txt.grid(column=1, row=0)  
    btn = Button(window, text="Ответить", command=clicked)  
    btn.grid(column=2, row=0)
    bot.register_next_step_handler(message, wind)  
    window.mainloop()
    
def wind(message):
    def clicked():  
        res = bot.reply_to(message,format(txt.get()))
    with open('teh_poddergka.txt', 'r+', encoding='utf-8') as data2:
        temp = data2.readlines()
        data2.writelines(str(message.from_user.id)+':'+str(message.text)+'\n')
    global window
    lbl = Label(window, text=message.text)  
    lbl.grid(column=0, row=0)  
    txt = Entry(window,width=50)  
    txt.grid(column=1, row=0)  
    btn = Button(window, text="Ответить", command=clicked)  
    btn.grid(column=2, row=0)
    bot.register_next_step_handler(message, wind)  
    window.mainloop()

bot.infinity_polling()





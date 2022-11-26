
import controller

def Fio(x):
    for i in range(len(x)):
        if x[i].isnumeric():
            print(f'{x} не является ФИО')
            print("Введите повторно!")
            exit()
    with open('FIO.txt', 'r+', encoding='utf-8') as data:
        temp = data.readlines()
        data.writelines(list(x.capitalize())+list(" "))


       
def Number(x):
    x = input()
    with open('Number.txt', 'r+', encoding='utf-8') as data:
        temp = data.readlines()
        data.writelines(x)

def Adress(x):
    x = input()
    with open('Adress.txt', 'r+', encoding='utf-8') as data:
        temp = data.readlines()
        data.writelines(x)

with open('FIO.txt', 'r+', encoding='utf-8') as data:
    imyatext = data.readlines()


with open('Number.txt', 'r+', encoding='utf-8') as data:
    numbertext = data.readlines()


with open('Adress.txt', 'r+', encoding='utf-8') as data:
    adresstext = data.readlines()



def vivod_po_imeni():
    print("Введите имя:")
    m = input()
    m = m.capitalize()
    for i in imyatext:
        if m in i:
            n=imyatext.index(i)
            print(imyatext[n], numbertext[n], adresstext[n])
    

def novaya_zapis():
    print("Запишите фамилию:")
    familiya = input()
    Fio(familiya)
    print("Запишите Имя:")
    imya=input()
    Fio(imya)
    print("Запишите Отчество:")
    otchestvo=input()
    Fio(otchestvo)
    with open('FIO.txt', 'r+', encoding='utf-8') as data:
        temp = data.readlines()
        data.writelines("\n")

    print("Запишите номер телефона:")
    nomer = None
    Number(nomer)
    with open('Number.txt', 'r+', encoding='utf-8') as data:
        temp = data.readlines()
        data.writelines("\n")

    print("Запишите адрес:")
    adr = None
    Adress(adr)
    with open('Adress.txt', 'r+', encoding='utf-8') as data:
        temp = data.readlines()
        data.writelines("\n")


def vivod_spravochnika():
    print("Весь справочник:")
    for i in range(len(imyatext)):
        print(imyatext[i], numbertext[i], adresstext[i])
    

      
        
 
        


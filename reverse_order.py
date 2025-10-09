alf_rus = sorted(('йцукенгшщзхъфывапролджэячсмитьбюё'), reverse = True)
alf_eng = sorted(('qwertyuiopasdfghjklzxcvbnm'), reverse = True)

a1 = input() #вводим слова с консоли
b1 = input()

if a1[0] in alf_rus: #определяем язык работы
    alf = alf_rus
else:
    alf = alf_eng
#Функция для сравнения слов в обратном алфавитном порядке
def reverse_order(a,b):
    for i in range(len(min(a,b,key = len))):
        if alf.index(a[i]) < alf.index(b[i]): #сравниваем позиции символов в алфавите
            return True
        elif a == b:
            return 0
        else:
            return False
print(reverse_order(a1,b1))


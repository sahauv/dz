s1, s2, s3 = input("Введите первое слово: "), input("Введите второе слово: "), input("Введите третье слово: ")
alf="zabcdefghijklmnopqrstuvwxyza"
alf2=["z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a"]
def s(s1,s3): #1
    global a1,a
    if len(s1) % 2 == 0:
        a = int((len(s1) / 2 - 1))
        a1 = (alf2[alf.find(s1[a]) - 1]) #прошлая буква в алфавите
    else:
        a = int((len(s3) // 2 ))
        a1 = (alf2[alf.find(s3[a])+4]) #буква в алфавите через 3 позиции
def f():    #2
    global a2
    a2 = ((alf2[alf.find(s2[len(s2) - 1]) - 1])) #предшествующая буква в алфавите последнего символа втрого слова
def g(): #3
    global a3
    a3 = ((alf2[alf.find(s3[0])+1])) #буква, которая в алфавите следует за буквой, являющейся первым символом третьего слова
def h(): #4
    global a4
    if len(s1)+len(s2)-1 <26: #буква,которая в алфавите стоит на месте, соответствующей сумме количеств символов в первом и втором словах минус 1 символ
         a4 = alf[(len(s1)+len(s2)-1)]
    else:
         a4 = alf[((len(s1) + len(s2) - 1)//26)]

s(s1,s3)
f()
g()
h()
print(a1+a2+a3+a4)

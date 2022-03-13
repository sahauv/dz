import random
par = ''
for x in range(10):
    par = par + random.choice(list('1234567890ABCDEFGHIGKLMNOPQRSTUVYXWZ'))
print("Пароль: "+par)

import random

n = int(input("Masukkan jumlah bilangan acak: "))
count = 0

while count < n:
    bilangan = random.random()
    if bilangan < 0.5:
        print(bilangan)
        count += 1

# Faça um código que execute a contagem regressiva de uma bomba, informando o número de segundos para explodir.
# Ele deverá mostrar a mensagem “iniciando contagem regressiva”, os segundos passados e, no final, a mensagem “BUM!”.

import time

print("A contagem irá começar em tres segundos...")
time.sleep(1)
x = 0
while x != 4:
    print(x)
    x += 1
    time.sleep(1)
print("Iniciando contagem regressiva...")
y = 1
while y != 8:
    print(f'Restam {y} segundos')
    y += 1
    time.sleep(1)
z = 4
for num in range(1, z):
    print(f'A bomba explodirá em {num} segundos')
    time.sleep(1)
print("BUM!")

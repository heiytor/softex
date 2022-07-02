# Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021. A partir
# dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).
#
# Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará
# perguntando até que um valor correto seja preenchido.

import datetime
import re


def monthconverter(num):
    try:
        num = int(num)
        if num <= 0 or num > 12:
            return "error"
        else:
            return num
    except:
        return "error"


def yearconverter(num):
    try:
        num = int(num)
        if num < 1922 or num > 2021:
            return "error"
        else:
            return num
    except:
        return "error"


current_time = datetime.datetime.now()


while True:
    print("Qual seu nome?")
    name = input("")
    if re.search('\d', name):
        print("Digite um nome válido")
        continue
    else:
        break
print("")
while True:
    print("Em que ano você nasceu")
    year = input()
    if yearconverter(year) == "error":
        print("Digite um ano entre 1922 e 2021")
        continue
    else:
        year = yearconverter(year)
        break
print("")
while True:
    print("Em que mês você nasceu?")
    month = input()
    if monthconverter(month) == "error":
        print("Digite um mês valido")
        continue
    else:
        month = monthconverter(month)
        break

if current_time.month < month:
    yo = 2021 - year
else:
    yo = 2022 - year

print(f"Seu nome é {name.title()}. Você nasceu no ano de {year} no mês {month}, e possui {yo}")
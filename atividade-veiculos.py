# Desenvolva um código que utilize as seguintes características de um veículo:
# - Quantidade de rodas;
# - Peso bruto em quilogramas;
# - Quantidade de pessoas no veículo.
#
# Com essas informações, o programa mostrará qual é a melhor categoria de habilitação para o veículo informado a partir
# das condições:
# A: Veículos com duas ou três rodas;
# B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
# C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
# D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas;
# E: Veículos com quatro rodas ou mais e com mais de 6000 kg.




# Perguntas sobre o veiculo

while True:
    wheel = input("Quantas rodas possui o veiculo? ")
    try:
        wheel = int(wheel)
        if wheel < 2:
            print("O veículo precisa possuir mais de uma roda!")
            continue
        break
    except:
        print("Digite um número válido.")
        continue

while True:
    people = input("Quantas pessoas você planeja acomodar no veículo? ")
    try:
        people = int(people)
        if people < 1:
            print("É impossível acomodar 0 pessoas.")
            continue
        break
    except:
        print("Digite um número válido.")
        continue

while True:
    weight = input("Qual peso do veículo? (em KG) " )
    try:
        weight = int(weight)
        if weight < 100:
            print("Nem motos pesam menos que 100 quilos")
            continue
        break
    except:
        print("Digite um número válido.")

# Decisoes

if wheel >= 4 and people <= 8 and weight <= 3500:
    print("Você precisa de uma habilitação tipo B")
elif wheel >= 4 and 3500 <= weight <= 6000:
    print("Você precisa de uma habilitação tipo C")
elif wheel >= 4 and people > 8:
    print("Você precisa de uma habilitação tipo D")
elif wheel >= 4 and weight >= 6000:
    print("Você precisa de uma habilitação tipo E")
else:
    print("Você precisa de uma habilitacão tipo A")
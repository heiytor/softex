# Desenvolva um código que simule uma eleição com três candidatos.
# - candidato_X => 889
# - candidato_Y => 847
# - candidato_Z => 515
# - branco => 0
#
# O código deve perguntar se deseja finalizar a votação depois do voto. Caso o número do voto não corresponda a nenhum
# candidato ou seja branco, ele deve ser tratado como nulo. Se for inserido um texto ao invés de número, o código deve
# retornar uma mensagem para votar novamente.
#
# Quando a votação for finalizada, o código deverá mostrar o vencedor, aquele com o maior número de votos e, também, a
# quantidade de votos de cada candidato, os brancos e nulos

x_votes = 0
y_votes = 0
z_votes = 0
null_votes = 0
finish = False

while not finish:
    while True:
        print("Em quem voc� deseja votar? [889]x | [847]y | [515]z | [0]nulo")
        vote = input()
        try:
            vote = int(vote)
            if vote == 889:
                x_votes += 1
                break
            elif vote == 847:
                y_votes += 1
                break
            elif vote == 515:
                z_votes += 1
                break
            elif vote == 0:
                null_votes += 1
                break
            else:
                print("Digite um numero v�lido!")
                continue
        except:
            print("Digite um numero v�lido")
            continue
    while True:
        print("Deseja votar novamente? [S]im | [N]�o")
        decision = input()
        decision = decision.upper()
        if decision == "S":
            break
        elif decision == "N":
            finish = True
            break
        else:
            continue

print("A contagem de votos ficou da seguinte maneira:")
print(f"Candidato X com {x_votes}.")
print(f"Candidato Y com {y_votes}.")
print(f"Candidato Z com {z_votes}.")
print(f"A contagem de nulos ficou em {null_votes}.")


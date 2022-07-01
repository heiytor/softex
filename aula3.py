# Desenvolva um programa que utiliza o nome de um aluno, duas notas e a quantidade de faltas que ele teve. Conclua se o
# aluno está aprovado ou reprovado de acordo com as especificações:
#
# - Se a média do aluno for menor que sete, o sistema deve informar o nome do aluno e que ele está reprovado;
# - Se o aluno possuir mais de três faltas, o sistema deve informar o nome do aluno e que ele está reprovado;
# - Se a média do aluno for maior ou igual a sete, o sistema deve informar o nome do aluno e que ele está aprovado.
#
# No sistema, todos os valores devem estar armazenados em variáveis.
#

def verificar_nota_bim(nota):
    try:
        nota = float(nota)
        if nota > 10 or nota < 0:
            print("A nota do aluno precisa estar entre 10 e 0.\n")
            return False
        elif 7 <= nota < 11:
            print("O aluno foi aprovado no bimestre\n")
            return True
        else:
            print(f'O aluno precisa de {7 - nota} pontos para ser aprovado no bimestre\n')
            return True
    except:
        print("Digite uma nota valida!\n")
        return False


def verificar_aprovacao(nota1, nota2, nota3, nota4):
    try:
        nota1 = float(nota1)
        nota2 = float(nota2)
        nota3 = float(nota3)
        nota4 = float(nota4)
    except:
        return False
    if (nota1 + nota2 + nota3 + nota4) / 4 >= 7:
        return (nota1 + nota2 + nota3 + nota4) / 4
    else:
        return False


####################################################################################################

# Conferir as faltas do aluno
while True:
    falta = input('Quantas faltas o aluno possui? ')
    try:
        falta = int(falta)
    except:
        print("Digite um numero valido")
        continue
    if falta > 3:
        print("O aluno foi reprovado")
        reprovado = True
        break
    elif falta < 0:
        print("Nao e possivel faltar negativo")
        continue
    else:
        reprovado = False
        break


########################################################################################################

# Conferir as medias
if not reprovado:
    while True:
        nota_1bim = input("Digite a nota do 1o bimestre do aluno: ")
        if verificar_nota_bim(nota_1bim):
            break
        else:
            continue

    while True:
        nota_2bim = input("Digite a nota do 2o bimestre do aluno: ")
        if verificar_nota_bim(nota_2bim):
            break
        else:
            continue

    while True:
        nota_3bim = input("Digite a nota do 3o bimestre do aluno: ")
        if verificar_nota_bim(nota_3bim):
            break
        else:
            continue

    while True:
        nota_4bim = input("Digite a nota do 4o bimestre do aluno: ")
        if verificar_nota_bim(nota_4bim):
            break
        else:
            continue

    aprovacao = verificar_aprovacao(nota_1bim, nota_2bim, nota_3bim, nota_4bim)
    if not aprovacao:
        print(f"O aluno foi reprovado.")
    else:
        print(f"O aluno foi aprovado com {verificar_aprovacao(nota_1bim, nota_2bim, nota_3bim, nota_4bim)} de media.")


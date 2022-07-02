# Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando
# infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:
# 1: Soma
# 2: Subtração
# 3: Multiplicação
# 4: Divisão
# 0: Sair
#
# Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a
# mensagem “Essa opção não existe” e voltar ao menu de opções.
#
# Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa
# executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.
#
# É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado.

def conversor(num):
    try:
        return float(num)
    except:
        return "error"


print("Bem-vindo. O que você gostaria de fazer?")
while True:
    print("[1]Somar [2]Subtrair [3]Multiplicar [4]Dividir [0]Sair")
    choice = input()
    if conversor(choice) == "error":
        print("Escolha uma alternativa válida")
        continue
    else:
        choice = conversor(choice)
        if choice < 0 or choice > 4:
            print("Escolha uma alternativa valida")
            continue

    # ENCERRAMENTO
    if choice == 0:
        print("\nO programa será encerrado!")
        break

    # SOMA
    elif choice == 1:
        while True:
            sum1 = input("\nDigite o número o qual você quer somar: ")
            if conversor(sum1) == "error":
                print("Digite um número")
                continue
            else:
                sum1 = conversor(sum1)
                break
        while True:
            sum2 = input("Digite outro numero o qual você quer somar: ")
            if conversor(sum2) == "error":
                print("Digite um número")
                continue
            else:
                sum2 = conversor(sum2)
                break
        end_sum = sum1 + sum2
        print(f"O resultado da operação {sum1} + {sum2} é igual à {end_sum}\n")

    #S SUBTRAÇ�O
    elif choice == 2:
        while True:
            sub1 = input("\nDigite o número o qual você quer subtrair: ")
            if conversor(sub1) == "error":
                print("Digite um número")
                continue
            else:
                sub1 = conversor(sub1)
                break
        while True:
            sub2 = input("Digite outro numero o qual você quer subtrair: ")
            if conversor(sub2) == "error":
                print("Digite um número")
                continue
            else:
                sub2 = conversor(sub2)
                break
        end_sub = sub1 - sub2
        print(f"O resultado da operação {sub1} - {sub2} é igual à {end_sub}\n")

    # MULTIPLICAÇ�O
    elif choice == 3:
        while True:
            mut1 = input("\nDigite o número o qual você quer multiplicar: ")
            if conversor(mut1) == "error":
                print("Digite um número")
                continue
            else:
                mut1 = conversor(mut1)
                break
        while True:
            mut2 = input("Digite outro numero o qual você quer multiplicar: ")
            if conversor(mut2) == "error":
                print("Digite um número")
                continue
            else:
                mut2 = conversor(mut2)
                break
        end_mut = mut1 * mut2
        print(f"O resultado da operação {mut1} * {mut2} é igual à {end_mut}\n")

    # DIVISAO
    elif choice == 4:
        while True:
            div1 = input("\nDigite o número o qual você quer dividir: ")
            if conversor(div1) == "error":
                print("Digite um número")
                continue
            else:
                div1 = conversor(div1)
                break
        while True:
            div2 = input("Digite outro numero o qual você quer dividir: ")
            if conversor(div2) == "error":
                print("Digite um número")
                continue
            else:
                div2 = conversor(div2)
                break
        end_div = div1 / div2
        print(f"O resultado da operação {div1} - {div2} é igual à {end_div}\n")
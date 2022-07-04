# Crie uma situação em que ocorra uma exceção dentro de um código. Utilize try/catch para realizar a captura e
# tratamento dessa exceção.

while True:
    sub = input("Digite um numero para subtrair por 10: ")
    if "," in sub:
        sub = sub.replace(",", ".")
    try:
        sub = float(sub)
        result = sub - 10
        print(f"O resultado da subtração de {sub} com 10 é igual à {round(result, 3)}")
        break
    except:
        print("Digite um numero válido")
        continue
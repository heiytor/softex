# Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o
# terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão
#
# Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.


def mathoperations(num1, num2, operator):
    if 1 < operator > 4:
        return 0
    elif operator == 1:
        sum = num1 + num2
        return sum
    elif operator == 2:
        subtraction =  num1 - num2
        return subtraction
    elif operator == 3:
        multiplication = num1 * num2
        return multiplication
    else:
        division = num1 / num2
        return division


print(mathoperations(5, 9, 8))
print((mathoperations(98, 55, 2)))
print((mathoperations(24, 6, 3)))
print((mathoperations(564, 6548, 1)))
print((mathoperations(800, 10, 4)))
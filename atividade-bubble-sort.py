# Construa um algoritmo de ordenação, utilizando o método bubble sort estudado. (Lembre-se que se trata de uma série de
# instruções que devem ser seguidas passo a passo).
# Para isso, você deve criar um método em que o tamanho do vetor seja dez e deve estar em ordem crescente.
#
# O vetor deverá:
# - comparar seus elementos dois a dois adjacentes;
# - se os elementos não estiverem em ordem, então ordenar;
# - senão, avançar para o próximo par;
# - repetir a operação até que nenhuma troca possa ser feita no vetor inteiro.


def algoritm(list):
    for _ in range(len(list) - 1):
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
    return list


print(algoritm([5, 9, 8, 2, 4, 6, 7, 3, 1, 10]))



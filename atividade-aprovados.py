# '# Após uma prova de vestibular, uma escola quer identificar quantos dos seus alunos foram aprovados em cada turma de formandos.
# Ela quer saber qual aluno teve a maior nota e de qual turma ele é. Nessa escola, há quatro turmas (A, B, C e D) com vinte e cinco alunos cada.

# # Elabore um algoritmo que solicite o nome e a nota do vestibular aos alunos. Depois, informe quantos deles foram aprovados, 
# de que turma são, qual a maior nota em cada turma e qual aluno teve a maior nota de todas.

# # Para que o aluno seja aprovado no vestibular, ele deverá obter nota maior ou igual a 7.

# # ATENÇÃO: As notas por turma não podem se repetir.'

def max_nota(dicionario):
    max_nota = 0
    for _, nota in dicionario.items():
        if float(nota) > float(max_nota):
            max_nota = nota
    return max_nota
    
def aprovados(dicionario):
    aprovados = 0
    for _, nota in dicionario.items():
        if nota >= 7:
            aprovados += 1
    return aprovados

def reprovados(dicionario):
    reprovados = 0
    for _, nota in dicionario.items():
        if nota < 7:
            reprovados += 1
    return reprovados
    

turma_A = {
    'aluno_1' : 7,
    'aluno_2' : 6.3,
    'aluno_3' : 9,
    'aluno_4' : 10,
    'aluno_5' : 9.2,
    'aluno_6' : 5.1,
    'aluno_7' : 4.8,
    'aluno_8' : 7.2,
    'aluno_9' : 3.2,
    'aluno_10' : 2.7,
    'aluno_11' : 1.9,
    'aluno_12' : 4.5,
    'aluno_13' : 8.9,
    'aluno_14' : 7,
    'aluno_15' : 7,
    'aluno_16' : 7.3,
    'aluno_17' : 7.7,
    'aluno_18' : 4.2,
    'aluno_19' : 9.1,
    'aluno_20' : 8.1,
    'aluno_21' : 7.1,
    'aluno_22' : 6,
    'aluno_23' : 5.4,
    'aluno_24' : 9.6,
    'aluno_25' : 4.2,
}

turma_B = {
    'aluno_1' : 6,
    'aluno_2' : 7,
    'aluno_3' : 4,
    'aluno_4' : 9.2,
    'aluno_5' : 9.6,
    'aluno_6' : 5,
    'aluno_7' : 8,
    'aluno_8' : 2,
    'aluno_9' : 3.2,
    'aluno_10' : 7.4,
    'aluno_11' : 9.5,
    'aluno_12' : 9.2,
    'aluno_13' : 8.9,
    'aluno_14' : 8.4,
    'aluno_15' : 7.1,
    'aluno_16' : 4,
    'aluno_17' : 2,
    'aluno_18' : 6,
    'aluno_19' : 8,
    'aluno_20' : 3.1,
    'aluno_21' : 9.3,
    'aluno_22' : 9,
    'aluno_23' : 7,
    'aluno_24' : 6.1,
    'aluno_25' : 8.8,
}

turma_C = {
    'aluno_1' : 4,
    'aluno_2' : 6,
    'aluno_3' : 1,
    'aluno_4' : 9.8,
    'aluno_5' : 5.1,
    'aluno_6' : 4.1,
    'aluno_7' : 8,
    'aluno_8' : 2,
    'aluno_9' : 3,
    'aluno_10' : 9,
    'aluno_11' : 2.9,
    'aluno_12' : 5.3,
    'aluno_13' : 9.9,
    'aluno_14' : 9.8,
    'aluno_15' : 6,
    'aluno_16' : 4,
    'aluno_17' : 3.2,
    'aluno_18' : 4.7,
    'aluno_19' : 9.1,
    'aluno_20' : 7.1,
    'aluno_21' : 9,
    'aluno_22' : 4,
    'aluno_23' : 2,
    'aluno_24' : 7,
    'aluno_25' : 7,
}

turma_D = {
    'aluno_1' : 4.3,
    'aluno_2' : 6.7,
    'aluno_3' : 9.2,
    'aluno_4' : 8.1,
    'aluno_5' : 9.4,
    'aluno_6' : 5.1,
    'aluno_7' : 4.9,
    'aluno_8' : 7.7,
    'aluno_9' : 1.3,
    'aluno_10' : 7.2,
    'aluno_11' : 9.1,
    'aluno_12' : 5.4,
    'aluno_13' : 8.7,
    'aluno_14' : 8.1,
    'aluno_15' : 7.2,
    'aluno_16' : 9.7,
    'aluno_17' : 9.9,
    'aluno_18' : 10,
    'aluno_19' : 4.7,
    'aluno_20' : 6.2,
    'aluno_21' : 7.9,
    'aluno_22' : 9.2,
    'aluno_23' : 8.4,
    'aluno_24' : 8,
    'aluno_25' : 7,
}


print(f'A turma A aprovou {aprovados(turma_A)} e reprovou {reprovados(turma_A)} alunos. A maior nota foi {max_nota(turma_A)}.')
print(f'A turma B aprovou {aprovados(turma_B)} e reprovou {reprovados(turma_B)} alunos. A maior nota foi {max_nota(turma_B)}.')
print(f'A turma C aprovou {aprovados(turma_C)} e reprovou {reprovados(turma_C)} alunos. A maior nota foi {max_nota(turma_C)}.')
print(f'A turma D aprovou {aprovados(turma_D)} e reprovou {reprovados(turma_D)} alunos. A maior nota foi {max_nota(turma_D)}.')
print(max_aluno(turma_B))
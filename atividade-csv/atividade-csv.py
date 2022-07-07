# Desenvolva um programa que deve ler um arquivo csv intitulado “notas_alunos.csv”. O arquivo deve ter a seguinte
# estrutura:
#
# aluno: Nome do aluno;
# nota_1: Primeira nota;
# nota_2: Segunda nota;
# faltas: Número de faltas;
#
# O programa lerá esse arquivo e criará duas colunas. A primeira coluna será “media”, que terá a média das duas notas
# do aluno. A segunda será “situacao”, com os valores: APROVADO ou REPROVADO.
#
# O aluno que tiver mais de 5 faltas ou possuir média menor que sete, será reprovado. O programa deverá salvar esse novo
# dataframe com o nome “alunos_situacao.csv”.
#
# Por fim, o programa deverá mostrar na tela:
# - o maior número de faltas;
# - a média geral das notas dos alunos;
# - e a maior média.

import pandas as pd

df = pd.read_csv("notas_alunos.csv")
df['Media'] = (df['Nota_1'] + df['Nota_2']) / 2
df.loc[(df['Media'] >= 7) & (df['Faltas'] <= 5), 'Situacao'] = 'Aprovado'
df.loc[(df['Media'] < 7) | (df['Faltas'] > 5), 'Situacao'] = 'Reprovado'
df.to_csv('alunos_situacao.csv')
print(df)

print("")
print(f'A maior m�dia foi {max(df["Media"])}, o maior n�mero de faltas {max(df["Faltas"])}, e a m�dia geral foi '
      f'{sum(df["Media"] / 4)}.')
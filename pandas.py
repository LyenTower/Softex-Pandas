import pandas as pd
import numpy as np

df=pd.read_cvs("./notas_alunos.csv")

#Criando as colunas médias e Situação
df["media"]=(df["nota_1"]+df["nota_2"])/2
df["situacao"]=np.where((df["media"]<7) | (df["faltas"]>5),"Reprovado","Aprovado")

print(df)
df.to_csv("alunos_situacao.csv")

#O maior número de faltas
falta=df["faltas"].max()
print(f"O maior número de faltas é : {falta}")
#Media das notas dos alunos
media_geral=(df["media"]).median()
print(f"A média geral da turma é: {media_geral}")
#A maior média
maior_media= df["media"].max()
print(f"A maior média foi: {maior_media}")

import pandas as pd

df=pd.read_cvs("notas_alunoc.csv")

#Média
media=(df["nota_1"]+df["nota_2"])/2
#Situação
df.loc[df["falta"]>5,"situacao"]="REPROVADO"
df.loc[df["media"]>=7,"situacao"] = "APROVADO"
df.loc[df["media"]<7, "situacao"] = "REPROVADO"
#NÃO ENTENDI PARA SALVAR
#def.to_csv()

#O maior número de faltas
falta=df["faltas"].max()
print(f"O maior número de faltas é : {falta}")
#Media das notas dos alunos
media_geral=(df["nota_1"]+df["nota_2"]).median()
print(f"A média geral da turma é: {media_geral}")
#A maior média
maior_media= df["media"].max()
print(f"A maior média foi: {maior_media}")

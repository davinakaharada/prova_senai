# (20) Utilizando a biblioteca pandas, crie um DataFrame com os dados da matriz acima.
# Os nomes das colunas devem ser ["hora_1", "hora_2",..., "hora_10"] e as linhas 
# representam as regiões ["us-east-1", "us-west-2", "eu-central-1", "sa-east-1" ].
# Em seguida, adicione uma nova coluna ao DataFrame com o nome "uso_médio" que contenha a média
# de uso de CPU de cada hora. Exiba o DataFrame resultante. 
import pandas as pd
uso_cpu = [
[20, 25, 40, 50, 45, 60, 55, 35, 70, 65],
[30, 35, 50, 60, 40, 55, 60, 45, 50, 55],
[15, 20, 30, 25, 35, 40, 45, 50, 55, 60],
[10, 15, 25, 35, 45, 50, 55, 60, 65, 70],
]

linhas = ["us-east-1", "us-west-2", "eu-central-1", "sa-east-1"]

colunas = [f'hora_{i+1}' for i in range(10)]

df = pd.DataFrame(uso_cpu, index=linhas,columns=colunas)
df['Uso_medio'] = df.mean(axis=1)

print(df)


# (20) Crie uma função chamada acima_da_media()
# que receba uma lista com os dados de uma região e retorne quantos valores estão acima da média daquela região.
# Teste a função para todas as regiões da matriz.

import statistics

uso_cpu = [
[20, 25, 40, 50, 45, 60, 55, 35, 70, 65],
[30, 35, 50, 60, 40, 55, 60, 45, 50, 55],
[15, 20, 30, 25, 35, 40, 45, 50, 55, 60],
[10, 15, 25, 35, 45, 50, 55, 60, 65, 70],
]


def acima_da_media(soma):
    for indice,valor in enumerate(uso_cpu[0]):
        media = sum(uso_cpu[0]) / len(uso_cpu[0])
        if valor > media:
            soma +=1
    return soma
    
        
print(acima_da_media(0))


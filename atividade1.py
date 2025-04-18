# (20) Considerando a matriz abaixo, crie uma função chamada uso_maximo()
# que receba como parâmetro uma lista com os valores de uso de CPU de uma região e retorne o valor máximo de uso.
# Teste essa função para cada região da matriz.
    
uso_cpu = [
[20, 25, 40, 50, 45, 60, 55, 35, 70, 65],
[30, 35, 50, 60, 40, 55, 60, 45, 50, 55],
[15, 20, 30, 25, 35, 40, 45, 50, 55, 60],
[10, 15, 25, 35, 45, 50, 55, 60, 65, 70],
]

# lista = []

def uso_maximo(lista):
    for valor in uso_cpu[1]:
        lista.append(valor)
    maior_valor = max(lista)
    return maior_valor

print(uso_maximo([]))



    
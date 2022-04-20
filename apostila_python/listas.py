#maior valor
lista = [12, -2, 4, 8, 29, 45, 78, -17, 2, 12, 8, 3, 3, 52]
maiorValor = lista[0]
for index in  range (0, len(lista)):
    if (maiorValor < lista[index]):
        maiorValor = lista[index]
print('maior valor: ' + str(maiorValor))

#pares da lista

listaPares = []
for index in range (0, len(lista)):
    if (lista [index] % 2 == 0):
        listaPares.append(lista[index])
print(listaPares)

#media dos elementos
mediaElemntos = 0

for index in range (0, len(lista)):
    mediaElemntos =+ mediaElemntos + lista[index]
mediaElemntos = mediaElemntos / len(lista)
print(mediaElemntos)

#soma dos elementos negativos

somaNegativos = 0

for index in range (0, len(lista)):
    if (lista[index] < 0):
        somaNegativos = somaNegativos + lista[index]
print(somaNegativos)


lista1 = [1,6,9,8,74]
lista2 = [2,8,74]
lista3 = []
print(lista1+lista2) #stampa tutti elementi liste


for i in lista1 and lista2:
    if i in lista1 and lista2:
        lista1.remove(i)





print('***********************************************')
print(lista1+lista2) # stampa elementi liste escludendo quelli ugugali

lista4 = [1,6,9,8,74]
lista5 = [2,8,74]
lista6 = []

for i in lista4 and lista5:
    if i  in lista4 and lista5:
        lista6.append(i)

print(lista6)

for i in lista4 and lista6:
    if i in lista4 and lista6:
        lista4.remove(i)
print(lista4)
for i in lista5 and lista6:
    if i in lista5 and lista6:
        lista5.remove(i)
print(lista5)

print(lista4 + lista5)
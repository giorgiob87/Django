def contatore(lista1):
    lista2 = []
    for item in lista1:
        lista2.append(len(item))

    print(lista2)










list = []

choice = input ('vuoi inserire un elemenrto alla lista? s/n')

while choice == 's':
    item = input('inserisci un elemento alla lista')
    list.append(item)
    choice = input('vuoi ancora inserire un elemento alla lista? s/n')


contatore(list)
#print(list)
def istogramma(lista):
    for numero in lista:
        print("*" * numero)






list=[]

choice = input('vuoi inserire un elemento alla lista? s/n')

while choice == 's':
    item = input('inserisci un elemento alla lista')
    item = int(item)
    list.append(item)
    choice = input('vuoi ancora inserire un elemento alla lista? s/n')

istogramma(list)
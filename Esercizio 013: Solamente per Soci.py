def max_in_list(lista, val):
    if val in lista:
        print ('elemento presente')
    else:
        print('elemento non presente')






valore = input('inserisci il valore da confrontare---->')
list = []
choice = input('vuoi inserire un elemento alla lista? s/n')
while choice == 's':
    item = input('digita un elemento da inserire----> ')
    list.append(item)
    choice = input('vuoi ancora inserire un elemento alla lista? s/n')


max_in_list(list, valore)
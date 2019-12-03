def max_in_list(lista):
    max = 0

    for item in list :
        if item > max:
            max = item
    print('Il numero più grande della lista passata è ' + str(max))








list = []
choice = input('vuoi inserire un elemento alla lista? s/n')
while choice == 's':
    item = input('digita un elemento da inserire----> ')
    list.append(int(item))
    choice = input('vuoi ancora inserire un elemento alla lista? s/n')

max_in_list(list)
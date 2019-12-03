def somma_Lista(list):
    somma = 0
    for numero in list:
        somma+=numero
    print('il risultato della somma è: ' + str(somma))






list = []
count = 0
item_in_list = input('quanti elementi vuoi inserire nella lista?---->')

while count< int(item_in_list):
    i= input('inserisci gli elementi della lista---->')
    list.append(int(i))
    count+=(1)

somma_Lista(list)
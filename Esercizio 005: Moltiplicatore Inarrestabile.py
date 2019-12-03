def moltiplica_Lista(list):
    prodotto= 1
    for numero in list:
        prodotto*=numero
    print('Il risultato della moltiplicazione tra tutti gli elementi della lista è... ' + str(prodotto))









list = []
count = 0
item_in_list = input('quanti elementi vuoi inserire nella lista?---->')

while count< int(item_in_list):
    i= input('inserisci gli elementi della lista---->')
    list.append(int(i))
    count+=(1)

moltiplica_Lista(list)
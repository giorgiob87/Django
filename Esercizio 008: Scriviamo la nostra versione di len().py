def mia_len(lista_o_stringa):
    #print(len(lista_o_stringa))
    lunghezza = 0
    for item in lista_o_stringa:
        lunghezza+=1
    print('La lunghezza è----> '+ str(lunghezza))






#string = input('inserisci la parola---->')
list = []
choice = input('Vuoi inserire un elemento alla lista? S/N')


while choice == 'S':
    item = input('quale elemento vuoi inserire---->')
    list.append(item)
    choice = input('Vuoi ancora inserire un elemento alla lista? S/N')

mia_len(list)


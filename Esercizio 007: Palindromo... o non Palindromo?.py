def testa_parole(parola):
    indice = len(parola)-1
    parola2 = ''
    while indice>= 0:
        parola2+= parola[indice]
        indice-=1

    if parola == parola2:
        print('è un palindromo')
    else:
        print('non è un palindromo')









string = input('inserisci la parola---->')
testa_parole(string)


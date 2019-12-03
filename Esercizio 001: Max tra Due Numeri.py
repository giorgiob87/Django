def printMax(a,b):
    if a == b:
        print('i numeri sono uguali')
    elif a>b:
        print('il numero maggiore è: ' + a)
    else:
        print('il numero maggiore è: ' + b)

a = input('Inserisci il primo numero--->')
b = input('Inserisci il secondo numero--->')

printMax(a,b)
def maxNum(a,b,c):
    if a > b and a>c:
        print('il  numero maggiore è: '+ a)
    elif b > a and b>c:
        print('il  numero maggiore è: ' + b)
    elif c > a and c>b:
        print('il  numero maggiore è: ' + c)
    else:
        print('i numeri sono uguali')

a=input('inserisci il primo numero----> ')
b=input('inserisci il secondo numero----> ')
c=input('inserisci il terzo numero----> ')
maxNum(a,b,c)

print('***************************************************')

def maxNumero(a,b,c,d):
    print(max(a,b,c,d))

a=input('inserisci il primo numero----> ')
b=input('inserisci il secondo numero----> ')
c=input('inserisci il terzo numero----> ')
d = input('inserisci il quarto numero----> ')

maxNumero(a,b,c,d)
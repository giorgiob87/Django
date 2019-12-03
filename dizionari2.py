d = {'a': 1, 'b': 2, 'c': 3}  # nuovo dict di 3 elementi
print(len(d))  # verifica che siano 3

print('***********************************************')

print(d.items())  # restituisce gli elementi

print('***********************************************')

print(d.keys())  # restituisce le chiavi

print('***********************************************')

print(d.values()) # restituisce i valori

print('***********************************************')

print(d.get('c', 0))  # restituisce il valore corrispondente a 'c'

print('***********************************************')

print(d.get('x', 0))  # restituisce il default 0 perché 'x' non è presente

print('***********************************************')

print(d)  # il dizionario contiene ancora tutti gli elementi

print(d.pop('a', 0))  # restituisce e rimuove il valore corrispondente ad 'a'

print(d)

print('***********************************************')

print(d.pop('x', 0))  # restituisce il default 0 perché 'x' non è presente

print('***********************************************')

print(d.popitem())  # restituisce e rimuove un elemento arbitrario

print(d)

print('***********************************************')

d.update({'a': 1, 'c': 3, 'z':7})  # aggiunge di nuovo gli elementi 'a' e 'c

print(d)

print('***********************************************')

d.clear()  # rimuove tutti gli elementi

print(d)
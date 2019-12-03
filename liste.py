nums = [0, 1, 2, 3] # nuova lista di 4 elementi
print(nums)

print('********************************************')

letters = ['a', 'b', 'c', 'd', 'e', 'c']

print(letters[0]) # le liste supportano indexing

print(letters[-1])

print('********************************************')

print(letters[1:4])  # slicing da indice 1 incluso a indice 4 escluso

print('********************************************')

print('a' in letters) # gli operatori di contenimento "in" e "not in"
print('z' in letters)

print('********************************************')

print(letters + ['f', 'g', 'h']) # concatenazione (ritorna una nuova lista)

print('********************************************')

print([1, 2, 3] * 3)# ripetizione (ritorna una nuova lista)

print('********************************************')

print(len(letters)) # numero di elementi

print('********************************************')

print(min(letters)) # elemento più piccolo (alfabeticamente nel caso di stringhe)

print('********************************************')

print(max(letters))  # elemento più grande

print('********************************************')

print(letters.index('c')) # indice dell'elemento 'c'

print('********************************************')

print(letters.count('c')) # numero di occorrenze di 'c'

print('********************************************')

#letters.append('d') # aggiunge 'd' alla fine
print(letters)

print('********************************************')

letters.extend(['e', 'f']) # aggiunge 'e' e 'f' alla fine

print(letters)

print('********************************************')

letters.pop() # rimuove e ritorna l'ultimo elemento

print(letters)

print('********************************************')

letters.pop(0) # rimuove e ritorna l'elemento in posizione 0 ('a')

print(letters)

print('********************************************')

letters.remove('d') # rimuove l'elemento 'd'

print(letters)

print('********************************************')

letters.reverse()


print(letters)

print('********************************************')

letters.sort()

print(letters)

print('********************************************')

letters[1] = 'x' # sostituisce l'elemento in posizione 1

print(letters)

print('********************************************')

del letters[1] # rimuove l'elemento in posizione 1 ('x')

print(letters)

print('********************************************')

letters.clear() # rimuove tutti gli elementi rimasti

print(letters)

print('********************************************')



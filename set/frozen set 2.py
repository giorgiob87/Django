nums = {10, 20, 30, 40}

print(nums)
print('***********************************')

print(len(nums))  # numero di elementi

print('***********************************')

print(min(nums))  # elemento più piccolo

print('***********************************')

print(max(nums))  # elemento più grande

print('***********************************')

print(10 in nums)

print('***********************************')

print(100 in nums)

print('***********************************')

nums.add(50)  # aggiunge 50

print(nums)

print('***********************************')

nums.remove(10)  # rimuove 10

print(nums)

print('***********************************')

#nums.remove(10)  # restituisce KeyError perché 10 non è più presente

nums.discard(20)  # rimuove 20, se l'elemento non è presente, discard non dà errore

print(nums)

print('***********************************')

print(nums.pop())  # rimuove e restituisce un elemento arbitrario

print(nums)

print('***********************************')

nums.clear()  # rimuove gli elementi rimanenti

print(nums)
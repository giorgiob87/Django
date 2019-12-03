nums = {10, 20, 30, 40}  # nuovo set di 4 elementi
print(nums)
print(type (nums))

print('*************************************************')

fnums = frozenset(nums)  # nuovo frozenset a partire dal set nums

print(fnums)

print('*************************************************')

print(type (fnums))

print('*************************************************')

{'Python'}  # set di 1 elemento (una stringa)

#print('*************************************************')

frozen = ({1, 2, 3, 2, 1})  # gli elementi sono unici, i duplicati vengono rimossi

print(frozen)



print('*************************************************')

setval = set('abracadabra')  # trova l'insieme di lettere nella stringa 'abracadabra'

print(setval)

print('*************************************************')

frozensetval = frozenset('abracadabra')

print(setval)

print(type(frozensetval))

print('*************************************************')


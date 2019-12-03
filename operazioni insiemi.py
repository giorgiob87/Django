s1 = {10, 20, 30, 40}

#s1 = {30,40}

s2 = {30,40,50,60}

#s2 = {20,30}

#s1.isdisjoint(s2), Restituisce True se i due set non hanno elementi in comune

print(s1.isdisjoint(s2))





#print({1, 2, 3}.isdisjoint({4, 5, 6}))  # hanno un elemento in comune (il 3)

print('************************************************************************')

#Restituisce True se s2 è un sottoinsieme di s1

print(s1.issubset(s2)) #Restituisce True se s1 è un sottoinsieme di s2

print('************************************************************************')

print(s1.issuperset(s2))  #Restituisce True se s2 è un sottoinsieme di s1

print('************************************************************************')

print(s1.union(s2)) #Restituisce l’unione degli insiemi (tutti gli elementi)

print('************************************************************************')

print(s1.intersection(s2)) #Restituisce l’intersezione degli insieme (elementi in comune a tutti i set)

print('************************************************************************')

print(s1.difference(s2)) #Restituisce la differenza tra gli insiemi (elementi di s1 che non sono negli altri set)

print('************************************************************************')

print(s1.symmetric_difference(s2)) #Restituisce gli elementi dei due set senza quelli comuni a entrambi

print('************************************************************************')

s1.update(s2) #Aggiunge a s1 gli elementi degli altri insiemi

print(s1)

print('************************************************************************')

s1.intersection_update(s2) #Aggiorna s1 in modo che contenga solo gli elementi comuni a tutti gli insiemi

print(s1)

print('************************************************************************')

(s1.difference_update(s2)) #Rimuove da s1 tutti gli elementi degli altri insiemi

print(s1)

print('************************************************************************')

s1.symmetric_difference_update(s2)#Aggiorna s1 in modo che contenga solo gli elementi non comuni ai due insiemi

print(s1)

print('************************************************************************')
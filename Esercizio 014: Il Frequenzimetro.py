def frequenza_car(stringa):
    mappa = {}
    for carattere in stringa:
        if carattere in mappa:
            mappa[carattere] += 1
        else:
            mappa[carattere] = 1
    return mappa








string = input('inserisci la parola---->')
print(frequenza_car(string))
def cerca_vocali(carattere):
    vocali = "AaEeIiOoUu"
    if carattere in vocali:
        print('il carattere ' + carattere + ' è una vocale')
    else:
        print('il carattere ' + carattere + ' non è una vocale')


carattere = input('inserisci il carattere---->')
cerca_vocali(carattere)
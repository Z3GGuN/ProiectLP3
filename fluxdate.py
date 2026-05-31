import matplotlib.pyplot as plt
import numpy as np
import requests
import csv
import time

while True:     #actualizare automata cu un interval de 10 secunde
    time.sleep(10)
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MNST&interval=5min&apikey=02VXKSGG85KQ84VT&datatype=csv'
    r = requests.get(url)
    with open('datacsv.csv', 'wb') as fhand:
        fhand.write(r.content)            #preluarea datelor cu Alphavantage API si scrierea lor intr-un fisier de tip csv


    with open('datacsv.csv') as data:
        reader = csv.DictReader(data)   #deschidem fisierul csv ca si data si citim din el
        timestamps = []
        close_prices = []
        volum = []                      #liste goale
        for row in reader:
            timestamps.append(row['timestamp'])
            close_prices.append(row['close'])
            volum.append(row['volume'])  #in fiecare din  listele de mai sus punem datele pentru timestamps, close prices si volum pe care le avem in fisierul csv


    timestamps = timestamps[:15]
    close_prices = close_prices[:15]
    volum = volum[:15]        #Feliem toate listele pentru a folosi ultimele 15 zile si toate 100 de zile

    timestamps = np.array(timestamps, dtype='datetime64')
    close_prices = np.array(close_prices, dtype='float64')
    volum = np.array(volum, dtype='float64')   # Trasnformam toate datele in datetime64 si float64 pentru ca matplotlib sa poata lucra cu ele

    timestamps = np.flip(timestamps)
    close_prices = np.flip(close_prices)
    volum = np.flip(volum)                      #Inversam listele cu ajutorul functiei np.flip pentru a avea listele in ordine

    fig, ax = plt.subplots()

    ax.plot(timestamps, close_prices, lw=3)  #afisam pe grafic timestamps si close prices cu un linewidth de 3
    ax.set_ylabel('Pret (Dolari)')  #punem nume axei y
    ax.set_xlabel('Ultimele 15 zile') #punem nume axei x

    ax2 = ax.twinx()        # cream o axa secundara Y pentru a afisa volumul
    ax2.bar(timestamps, volum/1000000, color='tab:gray', alpha=0.3)  #Afisam pe graficul facut, inca un grafic cu bare pentru volum reprezentat in milioane si opacitate 0.3 cu coloarea gri
    ax2.set_ylabel('Volum (Milioane)')

    ax.set_title('Evolutia stock-ului Monster')  #punem nume graficului
    fig.autofmt_xdate() # roteste textul cu timestamps pentru a nu se suprapune
    plt.show()          #Afiseaza graficul


"""
Bibliografie:
-Documnetatie primita
-AI(https://gemini.google.com/share/aa22fa60f622)
"""
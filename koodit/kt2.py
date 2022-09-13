from tkinter.font import names
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

""" 
Tehtävä 1: 
- lataa Latest https://covidtracking.com/data/download/national-history.csv
  tiedosto pandas kirjaston avulla Pandas dataframeksi. 
- "Irroita" siitä ladattaessa'date','deaths','hospitalInc','hospitalNow' sarakkeet
- Piirrä matplotlib.pyplot kirjaston ja plt.subplot, plt.plot, plt.title, plt.show 
  komentojen avulla kuva, josta nähdään kuolleiden lukumäärät, sairaalapotilaiden
  inkrementaalinen kasvu ja kuinka paljon sairaalassa on potilaita eri päivinä.
- Selvitä minä päivänä potilaiden kasvu on ollut suurinta ja mikä on tuon päivän potilasmäärä

Tehtävä 2:
- Muuta kaikki dataFramen sarakkeet numpy arrayksi to_numpy() funktion avulla
- Tulosta kuolleiden määrä ja sairaalassa olleiden lukumäärät oikeassa järjestyksessä
  (huom päivämäärät ovat tiedostossa viimeisin päivämäärä ensin. Eli käännä tulostusjärjestys
   siten, että kuvaan tulostetaan deaths sarakkeen viimeisin alkio ensin jne.) C:\koulu\koneoppi\teht2data.csv
""" 

df = pd.read_csv('C:\\koulu\\koneoppi\\teht2data.csv',
    header=0,
    names=['date','deaths','hospitalinc','hospitalnow'],
    usecols=[0,1,5,6] )


dates = df['date'].to_numpy()
dead = df['deaths'].to_numpy()
Hinc = df['hospitalinc'].to_numpy()
Hnow = df['hospitalnow'].to_numpy()

plt.figure(1)
plt.subplot(3,1,1)
plt.plot(dead)
plt.title('Deaths')

plt.subplot(3,1,2)
plt.plot(Hinc)
plt.title("HospitalInc")

plt.subplot(3,1,3)
plt.plot(Hnow)
plt.title("HospitalNow")

plt.figure(2)  # kuvaajat käänteisenä käyttäen [::-1]
plt.subplot(3,1,1)
plt.plot(dead[::-1])

plt.title('Deaths')
plt.subplot(3,1,2)
plt.plot(Hinc[::-1])

plt.title('Hospitalized Increased')
plt.subplot(3,1,3)
plt.plot(Hnow[::-1])
plt.title('Hospitalized Currently')


plt.show()
   
hosmax = Hinc.max()
indeksi = np.where(Hinc == hosmax)

print(Hinc.max()) #hospital inc max luku 17155
print(dates[indeksi]) #hospital max date = 2020-05-26



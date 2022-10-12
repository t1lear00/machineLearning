'''
Install scikit-learn module with pip install scikit-learn command.

Tehtävät:
1. Luetaan dataout.csv tiedosto pandas data frameksi siten, että tiedostosta luetaan vai
   sarakkeet xyz ja labels. Eli jätetään se indeksi sarake, joka koostuu 0,1,2 jonosta pois. 
   Käytä dataframen read_csv funktiota ja sieltä parametreja delimiter=, header=, usecols=

2. Poistetaan edellä luetusta dataframesta sen ensimmäinen rivi, jossa siis xyz ja labels tieto.
   Tämä siksi, että jäljelle jäänyttä 60,3 matriisia ja string saraketta käytetään eri algoritmien
   opettamiseen. Käytä dataframe iloc metodia

3. Seuraavaksi suodatetaan dataframesta pois sellaiset rivit, joissa x,y tai z arvo on suurempi
   kuin 1023, mikä on Arduinon analogia muuntimen maksimi lukema. Eli poistetaan virheelliset 
   mittaustulokset. Tulosta dataframe rivistä 40 eteenpäin (iloc käsky) ennen suodatusta ja 
   suodatuksen jälkeen, jotta varmistut siitä, että osa riveistä poistuu suodatuksen avulla
   Selvitä internetin avulla kuinka pandas dataframen sarakkeen arvoja voi suodattaa.

4. Seuraavaksi irroitetaan dataframesta labels tiedot left, right, up ja down tietoja
   kertova sarake (sen pitäisi olla neljäs sarake. Voit kokeilla esim print(df[4]) komennolla)
   Muutetaan sarakkeen tyyppi as_type komennolla 'category' tyypiksi ja luodaan dataframeen
   vielä viides sarake ja alustetaan sinne df[4].cat.codes funktion avulla numeeriset arvot
   left, rigth, up ja down arvoja vastaamaan.

5. Seuraavaksi "irroitetaan" dataframesta x,y,z sarakkeet ja muodostetaan niistä yksi 
   NumPy array, jossa on kolme saraketta ja N kpl rivejä. Tämä array = matriisi = data on sitten
   se, mitä käytetään eri mallien datana opettamiseen. Irroitetaan myös numpy arrayksi
   se viides sarake joka edellisessä vaiheessa saatiin tehtyä. Ja tätä käytetään opetuksessa
   kertomaan, mitä kukin data matriisin rivi edustaa = labels. Ja muutetaan molemmat irroitetut
   data ja labels int tyyppisiksi.

6. Ja nyt vihdoin data on käsitelty algoritmin opettamiseen sopivaksi. Jaetaan data vielä
   training ja test datasetteihin ja käytetään siihen sklearn kirjaston train_test_split luokkaa
   jonka voi importata komennolla from sklearn.model_selection import train_test_split. Tee
   sellainen jako, että datasta 20% jätetään testaukseen ja 80% datasta käytetään opetukseen.
   Netistä löytyy taas hyviä esimerkkejä, miten tämä tehtään: https://realpython.com/train-test-split-python-data/

7. Ja lopuksi testataan random forest ja K-means algoritmien toimivuutta. Eli opetetaan opetusdatalla
   x_train,y_train sekä random forest että K-means malli. Ja sen jälkeen testataan mallin tarkkuus
   x_test,y_test datalla. Ja ylimääräisenä tehtävänä voi vielä mitata kummastakin algoritmista kuinka
   kauaan mallin opettaminen kestää ja kuinka kauan yhden ennustuksen tekeminen mallilla kestää. Ja
   apuja löytyy taas netistä seuraavasti:
   K-means: https://towardsdatascience.com/knn-using-scikit-learn-c6bed765be75
   Random Forests:https://www.datacamp.com/tutorial/random-forests-classifier-python

       
'''

import sklearn # This is anyway how package is imported
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics


N=47

df = pd.read_csv('C:\\koulu\\koneoppi\\dataout.csv',
    delimiter='\t',
    usecols=['x','y','z','labels'])
#df.drop([0])
#print(df)
df=df.iloc[1:]

print('lines 40: before filter \n',df.iloc[40:])

rsdf = df[(df['x']<1024) & (df['y']<1024) & (df['z']<1024)]
print('lines 40: after filter \n',(rsdf.iloc[40:]))

#df['labels'] = df.astype('category')
rsdf = df.astype({"labels": 'category'})

#df=df.assign('viides'= df['labels'].cat.codes)
rsdf['viides']= rsdf['labels'].cat.codes
#print (df['viides'])

#npxyz = np.array([rsdf['x'], rsdf['y'], rsdf['z']]).reshape(N,3)
npxyz = rsdf[['x','y','z']].to_numpy()
#print(len(npxyz))
#npv = np.array([df['viides']])
npv = rsdf['viides'].to_numpy()
print('npxyz= ',npxyz)
print('npv= ',npv)
#print(df)
x_train, x_test, y_train, y_test = train_test_split(npxyz, npv, test_size=0.2)

model = KNeighborsClassifier(n_neighbors=4)
#krange = range(1,4)
scores={}
scoreslist =[]
#for k in krange:
model = KNeighborsClassifier(n_neighbors=4) 
model.fit(x_train,y_train)
arvaus = model.predict(x_test)
print("kmeans tarkkuus ", metrics.accuracy_score(y_test,arvaus))


clf=RandomForestClassifier(n_estimators=4)
clf.fit(x_train,y_train)
arvattu= clf.predict(x_test)
print("tree tarkkuus: ",metrics.accuracy_score(y_test, arvattu))
#scores[k] = (metrics.accuracy_score(y_test,arvaus))
#scoreslist.append(metrics.accuracy_score(y_test,arvaus))

#print(scoreslist[1])








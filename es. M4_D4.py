#ESERCIZIO 1
"""
elementi = "NPKOHC"

for elemento in elementi:
    print("-", elemento)
"""

#ESERCIZIO 2
#CON CICLO FOR

"""
string="marmalade"

for parola in string:
    if "e" in parola :
        print("a")
    else:
        print(parola)
"""
#CICLO WHILE
"""    
string = "marmalade"

index = 0

while index < len(string):
    if string[index] == "e":
        print("a")
        index += 1
    else:
        print(string[index])
        index += 1
"""
#METODO STRINGHE
"""
string="marmalde"

new_string=string.replace("e","a")
print(new_string)

"""

#ESERCIZIO 3 e 4
"""

potenza_2=[]

for contatore in range(10):
    potenza_2.append(2**contatore)
    
print(potenza_2)

"""

#ESERCIZIO 4 SOLO WHILE
"""
esponente=0
fortwo=1
count=0
potenza_2=[]

print("Le prime 10 potenze del 2")
while count < 10:
    potenza_2.append(fortwo)
    esponente += 1
    fortwo *= 2
    count += 1
    
    
print(potenza_2)
"""

#ESERCIZIO 5 "FOR"
"""
potenza_3=[]

for contatore in range(10):
    potenza_3.append(3**contatore)
    
print(potenza_3)
"""

#ESERCIZIO 5 "WHILE"
"""
esponente=0
forthree=1
count=0
potenza_3=[]

print("Le prime 10 potenze del 3")
while count < 10:
    potenza_3.append(forthree)
    esponente += 1
    forthree *= 3
    count += 1
    
    
print(potenza_3)
"""

"""Calcolare (ma non stampare) le prime N potenze di K; ognuna di esse andrà
memorizzata in coda a una lista.
Alla fine, stampare la lista risultante.
Proviamo con diversi valori di K, oppure facciamola inserire all'utente.

k = int(input("Inserisci un numero: "))
n = int(input("Inserisce quante N potenze vuoi calcolare: "))

count = 0
potenza=[]
num = 1

while count < n:
    num *= k
    count += 1
    potenza.append(num)
    
    
print(potenza)
    

#FOR
k = int(input("Inserisci un numero: "))
n = int(input("Inserisce quante N potenze vuoi calcolare: "))

potenza=[]

for contatore in range(1,n):
    potenza.append(k**contatore)
    
print(potenza)
"""

"""Calcolare e stampare tutte le potenze di 2 minori di 25000."""

"""
potenza_2=[]

#FOR

for contatore in range(100):
    if (2**contatore) <= 25000:
        potenza_2.append(2**contatore)
    else:
        break
    
print(potenza_2)
"""
#WHILE
"""
esponente=0
fortwo=1
count=0
potenza_2=[]

print("Le prime 10 potenze del 2")

while True:
        esponente += 1
        fortwo *= 2
        count += 1
        if fortwo <= 25000:
            potenza_2.append(fortwo)
        else:
            break
        
print(potenza_2)

"""

"""Calcolare e stampare tutte le potenze di 2 minori di un certo numero N."""
"""
#for

potenza_2 = []
N= int(input("Dimmi quale numero massimo della potenza del 2 vuoi mostrato: "))


for contatore in range(N):
        if (2**contatore) < N:
            potenza_2.append(2**contatore)
        else:
            break
    
print(potenza_2)
"""

#while
"""
esponente=0
fortwo=1
count=0
potenza_2=[]

N= int(input("Dimmi quale numero massimo della potenza del 2 vuoi mostrato: "))

while True:
        esponente += 1
        fortwo *= 2
        count += 1
        if fortwo <= N:
            potenza_2.append(fortwo)
        else:
            break
        
print(potenza_2)
"""

"""Calcolare e stampare tutte le prime 100 potenze di 2, ogni 3 (e.g. 2⁰, 2³, 2⁶, 2⁹,
…).
Oltre a stamparle, memorizzarle in coda a una lista e stamparla alla fine.
Usate due metodi diversi:
1. usare un costrutto for e range(100), e poi un costrutto if per visualizzare
e memorizzare solo ogni 3
2. usare un costrutto for e range(0, 100, 3)"""

"""
potenza_2=[]

for contatore in range(10):
    if contatore % 3 == 0:
        potenza_2.append(2**contatore)
    
    
print(potenza_2)

for contatore in range (0,10,3):
    potenza_2.append(2**contatore)
    
print(potenza_2)

"""

"""Abbiamo una lista con dei numeri:
numeri = [4, 9, 5, 1, 7, 10, 2, 3]
utilizzando un costrutto for, trovare il massimo di questa lista e stamparlo a
video."""
"""
numeri = [4, 9, 5, 1, 7, 10, 2, 3]
max=numeri[0]

for numero in numeri:
    if numero > max:
        max = numero
        
print(max)

numeri = [4, 9, 5, 1, 7, 10, 2, 3]
for contatore in range(0,len(numeri)):
    
    if numeri[contatore] > numeri[0]:
        numeri[0] = numeri[contatore]
        
print(numeri[0])
"""

"""Abbiamo raccolto tutte le età degli studenti in una lista:
eta_studenti = [20, 30, 40, 50, 60]
utilizzando un ciclo for, calcolare la media delle età. Alla fine, stampa (a video)
il risultato.""" 

"""
eta_studenti = [20, 30, 40, 50, 60]


for i in range(len(eta_studenti)):
    media_eta = sum(eta_studenti)/len(eta_studenti)
    
print(media_eta)

"""

"""Abbiamo una lista con i guadagni degli ultimi 12 mesi:
guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50,
50]
usando un costrutto for, calcolare la media dei guadagni e stamparla a video."""
"""
guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50]

for i in range (len(guadagni)):
    media_guadagni = sum(guadagni)/len(guadagni)

print(int(media_guadagni))
"""

"""Abbiamo una lista con i guadagni degli ultimi N mesi:
guadagni = [100, 90, 70, 40, 50, 80, 90, 120]
usando un costrutto for, calcolare la media dei guadagni e stamparla a video;
stampare anche il numero di mesi considerati."""
"""
#LOOPING OVER ITEMS
guadagni = [100, 90, 70, 40, 50, 80, 90, 120]

N = 12
totale = 0

for guadagno in guadagni:
    totale += guadagno
    
media = totale/N
print(media)

#LOOPING OVER INDICES-- NON SERVE A NIENTE, SOLO STILE
for i in range(len(guadagni)):
    
    media=sum(guadagni)/N
    
print(media)

"""

"""Abbiamo una lista di studenti:
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace",
"Henry"]
utilizzare un ciclo for per stampare i nomi di tutti gli studenti con questa formattazione:
Studenti:
- Alex
- Bob
- Cindy"""
"""
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace","Henry"]
##LOOPING OVER INDICES
for i in range(len(studenti)):
    print("-", studenti[i])

##LOOPING OVER ITEMS  
for studente in studenti:
    print("-",studente)
"""

"""Abbiamo tre liste (sono tutte della stessa lunghezza):
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace",
"Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend",
"Data Analyst", "Backend", "Frontend", "Cybersecurity"]
edizioni = [1, 2, 3, 2, 2, 1, 3, 3]
stampare a video, usando print(), ogni studente che corso segue e di che edizione,
e.g.:
Alex segue Cybersecurity, edizione 1
Bob segue Data Analyst, edizione 2
...
facendo in modo che non ci sia uno spazio tra il corso e la virgola subito dopo"""
"""
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace","Henry"]

corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend","Data Analyst", "Backend", "Frontend", "Cybersecurity"]

edizioni = [1, 2, 3, 2, 2, 1, 3, 3]

for student, course, ed in zip (studenti,corsi,edizioni):
    print(f"{student} segue {course}, edizione {ed}")
"""

"""Abbiamo una lista di parole:
parole = ["Albergo", "Sedia", "Borgo", "Petalo",
"Belvedere", "Semestre", "Sosta", "Orpello", "Abete"]
stampiamo, per ogni parola, quante volte appare la lettera "e"."""
"""

##LOOPING OVER ITEMS
parole = ["Albergo", "Sedia", "Borgo", "Petalo", "Belvedere", "Semestre", "Sosta", "Orpello", "Abete"]
letter="e"
for parola in parole:
    count = parola.count(letter)
    print((parola + ' ')*count)

#LOOPING OVER INDEX

parole = ["Albergo", "Sedia", "Borgo", "Petalo", "Belvedere", "Semestre", "Sosta", "Orpello", "Abete"]
letter="e"
for i in range(len(parole)):
    count = parole[i].count(letter)
    print(str(parole[i]+ ' ') *count)
"""

"""parole = ["Albergo", "Sedia", "Borgo", "Petalo", "Eremo",
"Belvedere", "Semestre", "Esteta", "Sosta", "Orpello",
"Abete", "Orologio", "Cesta", "Ermellino"]
stampiamo, per ogni parola, quante volte appare la lettera "e"; facciamo
attenzione al fatto che appare sia maiuscola che minuscola."""
"""
parole = ["Albergo", "Sedia", "Borgo", "Petalo", "Eremo",
"Belvedere", "Semestre", "Esteta", "Sosta", "Orpello",
"Abete", "Orologio", "Cesta", "Ermellino"]

##LOOPING OVER ITEMS
for parola in parole:
    count = parola.lower().count('e')
    print((parola + ' ')*count)

#LOOPING OVER INDEX

for i in range(len(parole)):
    count=parole[i].lower().count('e')
    print(str(parole[i]+ ' ')*count)
"""
"""Abbiamo una lista di codici fiscali:
lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C",
"MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F",
"DEFGHI95J06A987G"]
trovare i codici fiscali che contengono "95", metterli in una lista, e alla fine
stamparla.

lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C",
"MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F",
"DEFGHI95J06A987G"]
#LOOPING OVER ITEMS
new_cf = []

for cf in lista_cf:
    if "95" in cf:
        new_cf.append(cf)
        
print(new_cf)
#LOOPING OVER INDICES
new_cf=[]

for i in range(len(lista_cf)):
    if lista_cf[i].find('95') != -1:
        new_cf.append(lista_cf[i])
        
print(new_cf)


#LOOPING OVER INDICES BY ENUMERATE "SOLO PER STILE" ENUMERATE SERVE A GESTIRE GLI INDICI SE CI SONO PIU' LISTE CORRELATE o tenere traccia dell'indice
new_cf= []
for index, cf in enumerate(lista_cf):
    if cf.find('95') != -1:
        new_cf.append(cf)
        
print(new_cf)
    
"""

"""Abbiamo una lista di codici fiscali:
lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C",
"MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F",
"DEFGHI95J06A987G"]
Per ognuno di essi, stampare a video i caratteri relativi al nome e quelli relativi al
cognome."""
"""
lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C",
"MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F",
"DEFGHI95J06A987G"]
 #LOOPING OVER ITEMS
for cf in lista_cf:
    print(cf[0:6])
  #LOOPING OVER INDEX   
for i in range(len(lista_cf)):
    print(lista_cf[i][0:6])
"""   
    
"""studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace",
"Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend",
"Data Analyst", "Backend", "Frontend", "Cybersecurity"]
edizioni = [1, 2, 3, 2, 2, 1, 3, 3]
dove ogni elemento nella medesima posizione si riferisce ai dati dello stesso studente.
Stampare a video tutti e soli gli studenti che frequentano una prima edizione; utilizzare
solo i dati necessari."""
"""
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace",
"Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend",
"Data Analyst", "Backend", "Frontend", "Cybersecurity"]
edizioni = [1, 2, 3, 2, 2, 1, 3, 3]

for index, studente in enumerate(studenti):
    if edizioni[index] == 1:
     print(f"{studente} segue {corsi[index]}, edizione {edizioni[index]}")
  
for studente, corso, edizione in zip (studenti,corsi,edizioni):
    if edizione == 1:
         print(f"{studente} segue {corso}, edizione {edizione}")
"""

"""Dove ogni elemento nella medesima posizione si riferisce ai dati dello stesso studente.
Riuscite a vedere una similarità di qualche tipo con la logica che si usa in SQL e le tabelle
relazionali?
E' come se avessimo 3 tabelle STUDENTI: IDStudente, NomeStudente
                              CORSI: IDCorso, DescrizioneCorse
                              EDIZIONI: IDStudente, IDCorso, IDEdizione
                              
ID Studente | Nome Studente
----------------------------
1           | Alex
2           | Bob
3           | Cindy
4           | Dan
5           | Emma
6           | Faith
7           | Grace
8           | Henry

ID Corso | Nome Corso
--------------------
1        | Cybersecurity
2        | Data Analyst
3        | Backend
4        | Frontend

ID Studente | ID Corso | Numero Edizione
--------------------------------------
1           | 1        | 1
2           | 2        | 2
3           | 3        | 3
4           | 2        | 2
5           | 2        | 2
6           | 1        | 1
7           | 3        | 3
8           | 3        | 3



Replichiamo SQL in Python


studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace",
"Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend",
"Data Analyst", "Backend", "Frontend", "Cybersecurity"]
edizioni = [1, 2, 3, 2, 2, 1, 3, 3]

findstudent='Alex'
indexstudent=studenti.index(findstudent)

course=corsi[indexstudent]

print(f"{findstudent} segue il corso {course}")

"""

"""Creiamo un dizionario che assegni ad ogni proprietario la sua auto, sapendo
che:
• Ada guida una Punto
• Ben guida una Multipla
• Charlie guida una Golf
• Debbie guida una 107 Poi stampiamo il dizionario per intero, e poi l'auto
associata a Debbie."""
"""
proprietari_auto = { 'Ada' : 'Punto',
                     'Ben' : 'Multipla',
                     'Charlie' : 'Golf',
                     'Debbie'   : '107'
                    }

print(proprietari_auto)
print(proprietari_auto['Debbie'])
"""

"""Abbiamo un dizionario che assegni ad ogni proprietario la sua auto:
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla",
"Charlie": "Golf", "Debbie": "107"}
Aggiungere i proprietari Emily e Fred che posseggono rispettivamente una A1 e
una Octavia; eliminare i dati relativi a Ben.
Stampare il dizionario per controllare che sia tutto corretto."""
"""
proprietari_auto = { 'Ada' : 'Punto',
                     'Ben' : 'Multipla',
                     'Charlie' : 'Golf',
                     'Debbie'   : '107'
                    }

proprietari_auto['Emily'] = 'A1'
proprietari_auto['Fred'] = 'Octavia'
del proprietari_auto['Ben']

print(proprietari_auto)

"""

"""Abbiamo due dizionari che assegnano ad ogni proprietario la propria auto:
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla",
"Charlie": "Golf", "Debbie": "107", "Emily": "A1"}
nuovi_proprietari = {"Ben": "Polo", "Fred": "Octavia",
"Grace": "Yaris", "Hugh": "Clio"}
Aggiornare il dizionario dizionario_auto con i dati contenuti in
nuovi_proprietari e stamparlo. Cosa è successo a Ben? E' STATO SOVRASCRITTO
"""
"""
proprietari_auto = { 'Ada' : 'Punto',
                     'Ben' : 'Multipla',
                     'Charlie' : 'Golf',
                     'Debbie'   : '107'
                    }

proprietari_auto_new = ({'Ben': 'Polo', 'Fred': 'Octavia',
'Grace': 'Yaris', 'Hugh': 'Clio'})

proprietari_auto.update(proprietari_auto_new)

print(proprietari_auto)
"""

"""Abbiamo un dataset che assegna ad ogni proprietario la propria auto, in forma
di dizionario:
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla",
"Charlie": "Golf", "Debbie": "107", "Emily": "A1", "Fred":
"Octavia", "Grace": "Yaris", "Hugh": "Clio"}
Viene richiesto di ricercare in questo dataset i dati di Hugh, Ada, Emily e
Debbie, e visualizzare le auto relative."""
"""

dizionario_auto = {"Ada": "Punto", "Ben": "Multipla",
"Charlie": "Golf", "Debbie": "107", "Emily": "A1", "Fred":
"Octavia", "Grace": "Yaris", "Hugh": "Clio"}

lista_proprietari = ['Hugh','Ada','Emily','Debbie']



for proprietario in lista_proprietari:
    if proprietario in dizionario_auto:
        print(proprietario , ' ', dizionario_auto[proprietario])

"""

"""Abbiamo un dataset che assegna ad ogni proprietario la propria auto, in forma di
dizionario:
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie":
"Golf", "Debbie": "107", "Emily": "A1", "Fred": "Octavia", "Grace":
"Yaris", "Hugh": "Clio"}
Viene richiesto di ricercare in questo dataset i dati di Ada, Emily, Jade, Ben, Hugh, Kelly e
Charlie, e visualizzare le auto relative.
Non tutti i dati potrebbero essere presenti nel dataset, quindi quando un nome non è
presente visualizzeremo un messaggio adeguato."""  
"""
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie":
"Golf", "Debbie": "107", "Emily": "A1", "Fred": "Octavia", "Grace":
"Yaris", "Hugh": "Clio"}


lista_proprietari = ['Ada', 'Emily', 'Jade', 'Ben', 'Hugh','Kelly','Charlie']

for proprietario in lista_proprietari:
    if proprietario in dizionario_auto:
        print(proprietario , ' ', dizionario_auto[proprietario])
    else:
        print(proprietario, "non presente in memoria")
"""

"""Abbiamo un dizionario:
diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k":
12, "clap": 9}
utilizzando il metodo .keys(), stampiamone tutte le chiavi."""

"""
diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k":
12, "clap": 9}

print(diz.keys())

for key in diz.keys():
    print(key)
"""

"""Abbiamo un dizionario:
diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k":
12, "clap": 9}
utilizzando il metodo .values(), stampiamone tutte i valori."""
"""
diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k":
12, "clap": 9}

print(diz.values())

for values in diz.values():
    print(values)
"""

"""diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k":
12, "clap": 9}
utilizzando il metodo dei dizionari .items() stampate le coppie chiave-valore
presenti nel dizionario su righe diverse"""
"""
diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k":
12, "clap": 9}

for key in diz.items():
    print(key)
"""

"""diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k":
12, "clap": 9}
utilizzando il metodo dei dizionari .values(), calcolare il valore massimo, il
valore minimo, la somma, e stampiamo i risultati.  """

"""
diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k":
12, "clap": 9}

print(sum(diz.values()))
print(max(diz.values()))
print(min(diz.values()))
"""

"""Abbiamo un dizionario che assegna ad ogni proprietario la sua auto:
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla",
"Charlie": "Golf", "Debbie": "107"}
Con un ciclo for, e usando il metodo .items(), stampiamo ogni proprietario
e la sua auto, formattandolo come:
Ada guida una Punto
Ben guida una Multipla
...
"""
"""
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla",
"Charlie": "Golf", "Debbie": "107"}

for proprietario, auto in dizionario_auto.items():
    print(f"{proprietario} guida una {auto}")
"""

"""Abbiamo un dizionario che assegna ad ogni proprietario la sua auto:
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla",
"Charlie": "Golf", "Debbie": "107"}
Con un ciclo, e usando il metodo .values(), stampiamo a video tutte le auto
che non sono una Multipla."""
"""
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla",
"Charlie": "Golf", "Debbie": "107"}

for valore in dizionario_auto.values():
    if valore != 'Multipla':
        print(valore)
"""

"""Abbiamo i seguenti dati riguardo dei collezionisti e le loro collezioni:
• Ada ha 10 Funko Pop, 5 action figures e 35 manga
• Ben ha 2 Funko Pop, 6 action figures, 40 manga e 2 graphic novels
• Charlie ha 31 action figures e 18 graphic novels
• Debbie ha 1 Funko Pop, 9 graphic novels, 25 manga e 2 action figures
Creare dei dizionari innestati che contengano questi dati, e quindi visualizzarli."""
"""
collezionisti = { 
                 'Collezionista': { 'Collezione' : ['Funko Pop', 'Action Figures', ' Manga', 'Graphic Novels'] },
                 'Ada': { 'Collezione' : [10, 5, 35, None] },
                 'Ben': { 'Collezione' : [2, 6, 40, 2] },
                 'Charlie' : { 'Collezione' : [31, None, None, 18] },
                 'Debbie' : { 'Collezione' : [1, 2, 25, 9] }
                }

print(str(collezionisti['Collezionista']))
print(str(collezionisti['Ada']))
print(str(collezionisti['Ben']))
print(str(collezionisti['Charlie']))
print(str(collezionisti['Debbie']))


collezionisti = {
    'Ada': {
        'Funko Pop': 10,
        'Action Figures': 5,
        'Manga': 35
    },
    'Ben': {
        'Funko Pop': 2,
        'Action Figures': 6,
        'Manga': 40,
        'Graphic Novels': 2
    },
    'Charlie': {
        'Action Figures': 31,
        'Graphic Novels': 18
    },
    'Debbie': {
        'Funko Pop': 1,
        'Graphic Novels': 9,
        'Manga': 25,
        'Action Figures': 2
    }
}
"""

"""Abbiamo i seguenti dati riguardo dei collezionisti e le loro collezioni:
• Ada ha 10 Funko Pop, 5 action figures e 35 manga
• Ben ha 2 Funko Pop, 6 action figures, 40 manga e 2 graphic novels (entrambe
della DC)
• Charlie ha 31 action figures e 18 graphic novels (di cui 10 della Marvel e 8
della DC)
• Debbie ha 1 Funko Pop, 9 graphic novels (di cui 4 della DC e 5 della Marvel),
25 manga e 2 action figures
Creare dei dizionari innestati che contengano questi dati, e quindi visualizzarli"""
"""Riguardo l'esercizio precedente, stampiamo le risposte a:
1. quanti Funko Pop ha Ada?
2. quanti manga ha Ben?
3. quante graphic novels della Marvel ha Debbie?
4. quanti Funko Pop hanno Ada e Ben in tutto?
5. quanti manga hanno in tutto i collezionisti?
6. quante graphic novel della DC hanno in tutto i collezionisti?
7. quante graphic novel hanno in tutto i collezionisti?"
"""
"""
collezionisti = {
    'Ada': {
        'Funko Pop': 10,
        'Action Figures': 5,
        'Manga': 35
    },
    'Ben': {
        'Funko Pop': 2,
        'Action Figures': 6,
        'Manga': 40,
        'Graphic Novels': {
            'DC': 2
        }
    },
    'Charlie': {
        'Action Figures': 31,
        'Graphic Novels': {
            'DC': 8,
            'MARVEL': 10
        }
    },
    'Debbie': {
        'Funko Pop': 1,
        'Graphic Novels': {
            'DC': 4,
            'MARVEL': 5
        },
        'Manga': 25,
        'Action Figures': 2
    }
}

"""
"""

 #1. quanti Funko Pop ha Ada?
 
print(collezionisti['Ada']['Funko Pop'])

#2. quanti manga ha Ben?

print(collezionisti['Ada']['Manga'])

#3. quante graphic novels della Marvel ha Debbie?

print(collezionisti['Debbie']['Graphic Novels']['MARVEL'])

#4. quanti Funko Pop hanno Ada e Ben in tutto?

tot_funkopop = collezionisti['Ada'].get('Funko Pop') + collezionisti['Ben'].get('Funko Pop')
print(tot_funkopop)


#5. quanti manga hanno in tutto i collezionisti?

tot_manga = 0

for collezionista in collezionisti.values():
    tot_manga += collezionista.get('Manga', 0)
    
print(tot_manga)



#6.quante graphic novel della DC hanno in tutto i collezionisti?


    
       
    
tot_grnov_dc = 0

for collezionista in collezionisti.values():
    graphnovels = collezionista.get('Graphic Novels', {})
    tot_grnov_dc += graphnovels.get('DC', 0)
    
print("Totale Graphic Novels DC: " , tot_grnov_dc )

#7. quante graphic novel hanno in tutto i collezionisti?"


tot_graphic = 0

for collezionista in collezionisti.values():
    graphic_novels = collezionista.get('Graphic Novels', {})
    tot_graphic += sum(graphic_novels.values())

print("Totale Graphic Novels:", tot_graphic)

"""
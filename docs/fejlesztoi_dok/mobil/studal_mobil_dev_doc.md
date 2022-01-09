# Studal
# Fejlesztői dokumentáció
### 2022


## Szerkezetek

A mobilalkalmazás React Native Expo rendszerrel
készült. Az expo parancssoros varázslójával 
a "tabs (TypeScript) lehetőségével készült. 
Az expo "tabs" választása ezeket a felületeket 
screeneknek nevezi, amit a továbbiakban magyarul
nézeteknek fogok nevezni.

Az expo alapértelmezetten osztályok nélkül,
függvényekkel dolgozik, ami így is maradt.


Három felület került megvalósításra:
- Student nézet - Tanulók megjelenítése
- Group nézet -Csoportok megjelenítése
- Névjegy

### Student nézet

A Student nézeten két list van FlatList komponenssel
egymás alatt. A felső lista tartalmazza a csoportokat,
amire tapintva alul megjelennek az adott csoport 
tanulói. 

### Group nézet

A Group nézet egyetlen FlatList komponest tartalmaz,
a list felett egy betöltő gombbal. A lisában
a csoportok jelennek azonsítóval.

### REST API elérése

A REST API elérése az api.ts fájlban egy fetch()
függvénnyel történik. 

Két függvény lett megvalósítva:
 - getStudents()
 - getClassgroups()

### Az api.ts függvényei

A getStudents függvény szintaxisa:

```
getStudents(id: number)
```

Paraméterként fogadja a megjelenítendő csoport azonosítóját,
és visszaadja a csoport tanulóinak adatait.

A getClassgroups függvény szintaxisa:

```
getClassgroups()
```

A getClassgroups függvény visszaadja a csoportok
adatait.


Mindkét függvény a host globális változóból helyettesíti be
a használandó szerver útvonalát, és függvényen belül 
beállítja az elérendő végpontot.  




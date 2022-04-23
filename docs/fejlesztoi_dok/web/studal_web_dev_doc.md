# Studal

## Fejlesztői dokumentáció - web

## 2021, 2022

## Minta

## Fejlesztői nézet

Lépjünk be a studal/web/studal/ könyvtárba:

```bash
cd studal/web/studal
```

Most le kell töltenünk a függőségeket. Ez két paranccsal lehetséges, az npm és a yarn. Kettő közül használjuk a yarn parancsot:

```bash
yarn install
```

A webes felület indítása:

```bash
ng serve -o
```

## Felépítés

### Könyvtárszerszerkezet

```txt
studal/
  |-node_modules/
  |-src/
  |  |-app/
  |  |  |-class/
  |  |  |-institute/
  |  |  |-login/
  |  |  |-nopage/
  |  |  |-shared/
  |  |  |-student/
  |  |  |-app.component.css
  |  |  |-app.component.html
  |  |  |-app.component.ts
  |  |  |-app.component.spec.ts
  |  |  |-app.module.ts
  |  |  `-app-routing.module.ts
  |  |-assets/
  |  |-environments/
  |  |-favicon.ico
  |  |-index.html
  |  |-main.ts
  |  |-polyfill.ts
  |  |-styles.css
  |  `-test.ts
  |-angular.json

```

A webes felület egy SPA alkalmazás Angular keretrendszerrel összeállítva.

A következő vizuális komponensek lettek létrehozva:

* app.component - Fő konténer
* class.component - az osztályok kezelése
* institue.component - intézményi oldal
* login.component - beléptető felület
* nopage.component - nem létező oldalak helyett megjelenő lap
* student.component - tanulók megjelenítése kezelése

A következő nem vizuális komponensek lettek beépítve:

* api.service - a tanulók kezelése a REST API felületen
* apiclass.service - az osztályok kezelése a REST API felületen
* auth.guard - Útvonalak védelme
* auth.service - Azonosítás

### AuthService osztály

Az Angularban elérhető HttpClient osztály segítségével elvégzi a beléptetést, a kiléptetést, és lehetőséget ad annak ellenőrzésére, hogy be vagyunk-e jelentkezve.

#### login metódus

Két bemenő paramtére van, a felhasználónév és a jelszó string típusként. A metódus visszatér egy Observer objektummal, ami kapcsolódik az REST API /login végpontjához POSt metódussal.

#### logouot metódus

Bemenő paramétere nincs. Visszatér egy Observer objektummal, ami kapcsolódik a REST API szerver /logout végpontjához POST metódussal.

#### isLoggedIn metódus

Nincs bemenő paramétere. A metódus Window.localStorage tulajdonsággal
currentUser néven elmentett felhasználót keresi. Ha nincs ilyen false értékkel tér vissza. Ha van ilyen a tokennel tér vissza.

### AuthGuard osztály

Az útvonalak védelmét teszi lehetővé, az Angular beépített guard szolgáltatásán keresztül.

#### canActivate metódus

A gurad szolgáltatás esetén ez a metódus egy kötelező elem. Ha be vagyunk jelentkezve vissaztér true értékkel, másként a beléptető felületre navigál.

### ApiService

A tanulók kezelését végzi a REST API szerveren.

#### addStudent metódus

Egyetlen bemenő paramétere tartalmazza, a felvenni kívánt tanuló adatait. Egy Observer objektummal tér vissza, amiből kiolvasható
a szerver válasza.

#### getStudents metódus

Nincs bemenő paramétere. Lekéri az össze felhasználó adatait, majd visszatér egy Observer objektummal, ami szolgáltatja az összes tanuló adatait.

#### getGroupStudents metódus

Egy osztály tanulóit szolgáltatja. Bemenő paramétere a kívánt osztály vagy csoport azonosítója. Visszaad egy Observer objektumot, amiből megkaphatók az osztály tanulói.

#### deleteStudent metódus

Egy tanuló törlésére szolgál. Bemenő paramétere, a törltendő tanuló azonosítója. A törléshez azonosítást használ. Visszatér a szerver válaszával, egy Observer objektum formájában.

#### updateStudent metódus

Egy tanuló adatit képes frissíteni. Bemenő első paramétere a frisített tanulói adatok. Második paramétere a tanuló azonosítója. A metódus azonosításhoz tokent küld a REST API szervernek. Visszatérési értéke egy Observer objektum, amely tartalmazza a szerver válaszát.

### ApiclassService osztály

A tanulói osztályok vagy csoportok kezelésére használható.

#### host változó

A REST API eléréshez egy URL-t tartalmaz

#### addClassgroup metódus

A metódus segítségével felvehető egy új osztály. Bemenő paramtére az osztály adatai. A művelethez azonosítást végez, a tárolt token elküldésével. A metódus visszatér egy Observer objektummal, ami tartalmazza a szerver válaszát.

#### getClassgroups metódus

Az összes osztály adatait kérdezi le. Nincs bemenő paramétere. Visszatér egy Observer objektummal, ami tartalmazza az összes osztály adatait.

#### deleteClassgroup metódus

Egy osztály törlésére használható metódus. Bemenő paraméter a törlendő osztály azonosítója. Azonosításhoz a tárolt tokent elküldi a szerver számára. A metódus visszaad egy Observer objektumot, ami tartalmazza a szerver válaszát.

#### updateClassgroup metódus

Egy osztály adatait frissíti. Első bemenő paramétere a frissített adatok, a második a frissítendő osztály azonosítója. A metódus azonosításhoz elküdli a tárolt tokent, majd visszaad egy Observer
objektumot, ami tartalmazza a szerver válaszát.

### Class komponens

A komponens a szokásos Angular komponenseket tartalmazza, plusz egy osztályt, ami modelként szolgál az osztályok tárolására.

A komponens Reaktív űrlapot használ, a következő osztályokkal:

* FormGroup
* FormBuilder

#### classgroupData objektum

Tartalmazza az összes osztály adatait. Ebből renderelődik a táblázat.

#### ClassComponent.addClassgroup metódus

A metódusnak nincs bemenőparamétere. A .html fájlban megjelenített űrlapból olvassa az új komponens nevét, majd eltárolja az apiclass szolgáltatás használatával.

#### ClassComponent.getAllClassgroup metódus

A metódusnak nincs bemenő paramétere. Az apiclass szolgáltaáson keresztül lekéri az összes osztályt, majd betölti a classgroupData objektumba.

#### ClassComponent.deleteClassgroup metódus

A metódus paraméterként fogadja a törlendő osztály azonosítóját. Az apiclass szolgáltatáson keresztül törli a megadott osztályt. Törlés
után újragenerálja a weboldalon a táblázatot.

#### ClassComponent.onEdit metódus

Megjeleníti a szerkesztő űrlapot.

#### ClassComponent.updateClassgorup metódus

Frissíti a megadott osztály. A metódusnak nincs bemenőparamétere. Az adatbázist az apiclass szolgáltatáson keresztül telepíti. A frissítés után újragenerálja a táblázatot.

#### ClassComponent.clickAddClassgroup metódus

Megjeleníti az új osztály hozzáadási lehetőséget.

### InstituteComponent komponens

A programot haszlnáló intézmény adatait
tartalmazza.

#### instituteName változó

Az intézmény nevét tartalmazza.

#### courses objektum

Az intézmény által futtatott tanfolyamok listája.

### LoginComponent komponens

#### loginForm objektum

A beléptető felület űrlapjának leképezése, FormGroup és FormBuilder osztályok használatával.

#### LoginComponent.login() metódus

A beléptető űrlap alapján elvégzi az azonosítást az auth szolgáltatás segítségével. A szervertől kapott tokent és a felhasználónevet eltárolja Window.localStorage tulajdonsággal.

### nopage komponens

Ha nemlétező weboldalra hivatkozik egy látogató, ez a weblapot szolgáljuk ki.

### StudentComponent komponens

A tanulók kezelését végzi ez a komponens.

#### studentForm objetkum

Új tanuló felvételéhez használt űrlap leképezése.

#### studentsData objektum

Az összes tanuló adatait tartalmazza.

#### classgroups objektum

Az összes osztály adatait tartalmazza. Az osztályok válaszhatók a webes felületen.

#### selectedClassgroup objektum

A kiválaszott osztály adatait tartalmazza.

#### onChangeGroupSelect() metódus

Ha változik a kiválasztott osztály, újratölti a tanulókat.

#### StudentComponent.getClassgroups() metódus

A metódus letölti az osztályokat, az apiclass szolgáltatás segítségével, majd betölti a classgroups objektumba.

#### StudentComponent.addStudent() metódus

Új tanulót vesz fel. A tanuló adatait komponens studentForm űrlapjából veszi. Az adatbázisban az auth szolgáltatás segítségével rögzíti az új tanuló adatait.

#### StudentComponent.getAllStudent() metódus

Lekéri az összes tanuló adatát az api szolgáltatáson keresztül,
majd betölti az osztály studentsData objektumába.

#### StudentComponent.getGroupStudent() metódus

Bemenő paraméterként fogadja egy osztály azonosítóját. Az azonosító alapján lekérdezi az osztályba tartozó tanulók adatatit, majd beállítja azokat az osztály studentsData objektumába.

#### StudentComponent.deleteStudent() metódus

A metódus paramterként fogadja annaka a tanulónak a nevét, akit
szeretnénk törölni. A törlést az api szolgáltatás segítségével valósítja meg.

#### StudentComponent.onEdit() metódus

Megjeleníti a szerkesztőfelületet, beállítva az összes adatot.

#### StudentComponent.updateStudent() metódus

A szerkesztő űrlapból kiszedi a tanuló adatait, majd menti az api szolgáltatáson keresztül adatbázisba.

#### StudentComponent.clickAddStudent() metódus

Megjeleníti az új tanuló felvételéhez szükséges űrlapot.

### AppComponent komponens

Az alkalmazás fő komponense. A sablon fájlban felül jelenik meg az alkalmazás menüje. Alul a hivatkozott komponensek.

#### AppComponent.logout() metódus

Az auth szolgáltatás segítségével kilépést hajt végre.

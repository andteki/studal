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

A webes felület egy SPA alkalmazás Angular
keretrendszerrel összeállítva.
Az app komponens tartalmazza a menüt.


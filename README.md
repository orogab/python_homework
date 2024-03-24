# python_homework
python házi feladat leírás

## A feladat

Készíts egy webscraping megoldást az "index.hu"-ra. Az oldalról a cikkek címét kiszedi a script.
Ha ezzel megvagy, készíts egy leírást is "README.md" fájlba, ahol elmagyarázod röviden, mit csinál a
scripted, és leírod a logikáját is saját szavaiddal.
Nem kötelező, extra feladat

Ha tudod, a kapott adatokat írd is ki egy fájlba, a script könyvtárával megegyező helyre, a neveddel. Pl.:
"mikaczo_peter_index.txt"

## Ellenőrzés
A házi feladat ellenőrzése során az alábbiakról bizonyosodok meg:
Tudsz python scriptet készíteni.
Tudsz modult importálni.
Tudsz Osztályt, azaz class-ot készíteni.
Tudsz objektumot, azaz object-et írni.
Tudsz FOR ciklust használni.
Tudsz változót használni.
Tudsz értelmezhető dokumentációt készíteni a scriptedhez.
Semmiképp sem töltesz fel secret-et a repository-ba!
A python scriptedet elindítva megkapom a cikkek címét. Nem muszáj mindet, a megoldás szabadsága adott,
azonban nem elegendő csak 1 db cikk!
Hasonló megoldást várok, mint az órán is bemutatott BBC webscraping python script.

## használat

```
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

Majd a powershellen keresztül futtasd a 'python_hazi.py' scriptet python-al, pl `python .\python_hazi.py`. 

## Program működése

Ez a Python szkript a `BeautifulSoup` és `requests` könyvtárak segítségével kinyeri az "index.hu" hírportál cikkeinek címét.

A szkript a következő lépéseken megy keresztül:

1. A használt modulok importja.
2. Egy függvénnyel lekéri az index.hu tartalmát.
3. Ellenőrzi, hogy a válasz státuszkódja 200-e. Ha nem, hibaüzenetet jelenít meg a program lefutásának végén.
4. Amennyiben a státuszkód 200, kinyeri a cikkek címeit a megfelelő HTML elemek alapján.
5. A vissza adott címeket egy listába menti, majd a listát kiírja a "orosz_gabor_index.txt" fájlba.

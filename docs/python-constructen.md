# Python-constructen

In deze appendix vind je een overzicht van de Python-constructen die in de module aan bod komen. Per construct staat een korte uitleg en een voorbeeld, soms aangevuld met een toelichting. De appendix is bedoeld als naslagwerk. Als je iets wilt teruglezen of opzoeken, dan ben je hier aan het juiste adres.

Wil je meer weten over een Python-construct? Of wil je meer leren over Python? In _Think Python_ van Allen B. Downey vind je uitgebreidere uitleg en extra oefeningen. Het boek is gratis beschikbaar op [https://allendowney.github.io/ThinkPython/](https://allendowney.github.io/ThinkPython/). 

## Variabelen

Een variabele is een naam waaronder je een waarde opslaat. Je maakt een variabele aan door een naam te kiezen, een `#!py =` te schrijven en daarna de waarde te geven.
```python
age = 18
```
Nu je de variabele `#!py age` hebt aangemaakt, kun je de naam `#!py age` gebruiken in je code. Python onthoudt welke waarde de variabele heeft. 

Je kunt de waarde van een variabele ook later aanpassen, dan overschrijf je de oude waarde.
```python
age = 18
age = 19
```
Na de tweede regel heeft `#!py age` de waarde `#!py 19`. De waarde `#!py 18` is overschreven.

Kies altijd een duidelijke, beschrijvende naam voor een variabele. Gebruik bij namen met meerdere woorden een underscore als verbinding, dit heet _snake_case_. Een naam als `#!py age` of `#!py blood_pressure` maakt meteen duidelijk wat de variabele bevat. Een naam als `#!py x` of `#!py a` (meestal) niet. Een variabelenaam mag niet beginnen met een cijfer en mag geen spaties bevatten. `01patient` en `#!py blood pressure` zijn dus geen goede namen, `#!py patient01` en `#!py blood_pressure` wel. 

## Commentaar

Goede code is leesbaar, voor jezelf als je er later op terugkijkt en voor anderen die ermee werken. Commentaar helpt daarbij. Commentaar is tekst die uitlegt wat de code doet, maar door Python negeert wordt. Je schrijft commentaar met een `#!py #`. Alles wat daarna op dezelfde regel staat, wordt door Python genegeerd.

Je kunt commentaar achter een regel code plaatsen, bijvoorbeeld om de eenheid van een grootheid aan te geven:
```python
heart_rate = 72  # beats per minute
```
Ook kun je commentaar op een eigen regel plaatsen, vóór de code waar het bij hoort:
```python
# convert hours to seconds
seconds = hours * 3600
```
Meerdere opeenvolgende commentaarregels zijn ook mogelijk:
```python
# calculate BMI
# weight in kg; height in m
bmi = weight / height**2
```

Niet elke regel code heeft commentaar nodig. Gebruik commentaar daar waar de code zelf niet meteen duidelijk maakt _wat_ er gebeurt of _hoe_ iets werkt. Duidelijke variabelenamen, zoals `#!py heart_rate`, maken commentaar vaak overbodig.

## Datatypes

Python kent verschillende datatypes. Een datatype bepaalt wat voor soort waarde een variabele bevat en daarmee ook wat Python ermee kan doen. Zo betekent `#!py +` afhankelijk van het datatype iets anders: `#!py 2 + 2` is optellen en geeft `#!py 4`, terwijl `#!py "2" + "2"` samenvoegen is en `#!py "22"` geeft. Pas je een bewerking toe op een datatype waar die niet voor bedoeld is, zoals `#!py "2" + 2`, dan geeft Python een foutmelding. 

### String 
Een string (`#!py str`) is een stuk tekst. Dat kunnen letters zijn, maar ook cijfers of een combinatie. Je schrijft een string altijd tussen aanhalingstekens.
```python
module = "BMC"
patient_id = "042"
```

### Integer
Een integer (`#!py int`) is een geheel getal, zonder decimalen. Het kan zowel een positief als negatief getal zijn.
```python
year = 2026
temperature_change = -2  # degrees Celsius
```

### Float
Een float (`#!py float`) is een decimaal getal. Het kan zowel een positief als negatief decimaal getal zijn. Let op: ook een geheel getal met een decimaal punt is een float. 
```python
height = 1.83  # meter
freezing_point = 0.0  # degrees Celsius
```

## `#!py print()`

Met `#!py print()` geef je Python de opdracht iets weer te geven. Wat je tussen haakjes zet, wordt geprint in de terminal.
```python
print("Hello, world!")
print(42)
```
geven als uitvoer `Hello, world!` en `42`.

Je kunt ook variabelen printen in de terminal:
```python
blood_sugar = 5.4  # mmol/L
print(blood_sugar)
```
Python print dan de waarde die in de variabele is opgeslagen, niet de naam van de variabele. In dit geval dus `5.4`.

Je kunt meerdere waarden meegeven door ze te scheiden met een komma. Python voegt automatisch een spatie in tussen de waarden:
```python
name = "Alice"
print("Hello", name)
```
Dit geeft als uitvoer `Hello Alice`.

???+ meer-leren "f-strings"

    Met een f-string heb je meer controle over de opmaak van je uitvoer. Bij een f-string schrijf je een `#!py f` voor de aanhalingstekens en zet je variabelenamen tussen accolades:
    ```python
    name = "Anna"
    blood_sugar = 5.4  # mmol/L
    print(f"Patient {name} has a blood sugar of {blood_sugar} mmol/L.")
    ```
    Dit geeft als uitvoer `Patient Anna has a blood sugar of 5.4 mmol/L.` F-strings zijn handig als je tekst en variabelen wilt combineren tot een leesbare zin in je code.

    Je kunt binnen een f-string ook `#!py {variable=}` schrijven. In de terminal print Python dan zowel de variabelenaam als de waarde af:
    ```python
    blood_sugar = 5.4  # mmol/L
    print(f"{blood_sugar=}")
    ```
    Dit geeft als uitvoer `blood_sugar=5.4`. Handig als je meerdere variabelen print en wilt weten welke waarde bij welke variabele hoort.
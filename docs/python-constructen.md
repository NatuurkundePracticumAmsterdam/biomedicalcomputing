# Python-constructen

In deze appendix vind je een overzicht van de Python-constructen die in de module _Biomedical Computing_ aan bod komen. Per construct staat een korte uitleg en een voorbeeld, soms aangevuld met een toelichting. De appendix is bedoeld als naslagwerk. Als je iets wilt teruglezen of opzoeken, dan ben je hier aan het juiste adres.

Wil je meer weten over een Python-construct? Of wil je meer leren over Python? In _Think Python_ van Allen B. Downey vind je uitgebreidere uitleg en extra oefeningen. Het boek is een goed startpunt en is gratis beschikbaar op [https://allendowney.github.io/ThinkPython/](https://allendowney.github.io/ThinkPython/). 

## Commentaar

Goede code is leesbaar, voor jezelf als je er later naar terugkijkt en voor anderen die ermee werken. Commentaar helpt daarbij. Commentaar is tekst die uitlegt wat de code doet, maar door Python negeert wordt. Je schrijft commentaar met een `#!py #`. Alles wat na het `#!py #` op dezelfde regel staat, wordt door Python genegeerd.

Je kunt commentaar achter een regel code plaatsen, bijvoorbeeld om de eenheid van een grootheid aan te geven:
```py
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

## Datatypes

Python kent verschillende datatypes. Een datatype bepaalt wat voor soort waarde een variabele bevat en daarmee ook wat Python ermee kan doen. Zo betekent `#!py +` afhankelijk van het datatype iets anders: `#!py 2 + 2` is optellen en geeft `#!py 4`, terwijl `#!py "2" + "2"` samenvoegen is en `#!py "22"` geeft. Pas je een bewerking toe op een datatype waar die niet voor bedoeld is, zoals `#!py "2" + 2`, dan geeft Python een foutmelding. 

### String 
Een string (`#!py str`) is een stuk tekst. Dat kunnen letters zijn, maar ook cijfers of een combinatie. Je schrijft een string altijd tussen aanhalingstekens.
```python
module = "BMC"
patient_id = "042"
```
Strings ondersteunen [indexing en slicing](#indexing-en-slicing). Je kunt de lengte van een string opvragen met `#! len()`:
```py
module ="BMC"
print(len(module))  # 3
```

### Integer
Een integer (`#!py int`) is een geheel getal, zonder decimalen. Het kan zowel een positief als een negatief getal zijn.
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

### Boolean
Een boolean (`#!py bool`) bevat één van de volgende twee waarden: `#!py True` of `#!py False`. Je komt booleans vooral tegen als resultaat van een vergelijking:

* `#!py 6 > 2` geeft `#!py True`
* `#!py 6 < 2` geeft `#!py False`

Je kunt een boolean ook rechtstreeks toekennen aan een variabele. Let op: `#!py True` en `#!py False` schrijf je altijd met een hoofdletter.

### Lists
Een `#!py list` is een lijst van elementen. Deze lijst kan alle andere datatypes bevatten: strings, ints, floats, booleans en zelfs andere lists. Je kunt deze zelfs door elkaar gebruiken:
```py
base_positions = [428, 846, 3128, 5237]
elements = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne"]
grades = [7.0, 7.0, 6.5, 8.5, 8.0]
mix_and_match = [4, "times", 2.5, "is", 10]
```
Lists ondersteunen [indexing en slicing](#indexing-en-slicing). Je kunt de lengte van een lijst opvragen met `#! len()`:
```py
numbers = [1, 2, 3, 4, 5]
print(len(numbers))  # 5
```
en elementen toevoegen aan een lijst met `#!py .append()`:
```py
numbers = [1, 2, 3]
numbers.append(4)
numbers.append(5)
print(numbers)  # [1, 2, 3, 4, 5]

new_list = []
new_list.append(10)
new_list.append(20)
print(new_list)  # [10, 20]
```
Bij lists kun je ook bestaande elementen _vervangen_ met index-notatie:
```py
numbers = [1, 2, 4, 4, 5]  # oeps, de 3 vergeten
numbers[2] = 3
print(numbers)  # 1, 2, 3, 4, 5
```

### Datatypes omzetten
Je kunt een waarde van het ene datatype omzetten naar een ander datatype. Dit doe je met `#!py str()`, `#!py int()` en `#!py float()`:
```python
int("42")  # string to integer: 42
float("3.14")  # string to float: 3.14
str(29)  # integer to string: "29"
```
Dit komt bijvoorbeeld van pas bij [`#!py input()`](#sec:input), omdat de invoer van de gebruiker dan altijd een string is.

???+ meer-leren "Omzetten naar boolean"

    Je kunt een waarde ook omzetten naar een boolean met `#!py bool()`. Getallen zijn `#!py False` als ze nul zijn en `#!py True` als ze een andere waarden hebben. Voor strings geldt: een lege string is `#!py False` en een string met inhoud is `#!py True`.
    ```python
    bool(0)  # False
    bool(42)  # True
    bool("")  # False
    bool("text")  # True
    ```

## `#!py print()`

Met `#!py print()` geef je Python de opdracht iets in de terminal te tonen. Wat je tussen haakjes zet, verschijnt als tekst op het scherm.
```python
print("Hello, world!")
print(42)
```
geven als uitvoer `Hello, world!` en `42`. De aanhalingstekens om `#!py "Hello, world!"` zie je in de uitvoer niet terug, die geven alleen aan dat het hier om tekst gaat.

Je kunt ook variabelen printen in de terminal:
```python
blood_sugar = 5.4  # mmol/L
print(blood_sugar)
```
Python print dan de waarde die in de variabele is opgeslagen, niet de naam van de variabele. In dit geval dus `5.4`.

Je kunt meerdere waarden meegeven door ze te scheiden met een komma. Python voegt automatisch een spatie in tussen de waarden.
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

    Je kunt binnen een f-string ook `#!py {variable=}` schrijven. In de terminal print Python dan zowel de variabelenaam als de waarde:
    ```python
    blood_sugar = 5.4  # mmol/L
    print(f"{blood_sugar=}")
    ```
    Dit geeft als uitvoer `blood_sugar=5.4`. Handig als je meerdere variabelen print en wilt weten welke waarde bij welke variabele hoort.

<div id="sec:input"></div>
## `#!py input()`

Met `#!py input()` kun je de gebruiker iets laten typen in de terminal. Gebruik `#!py input()` als je programma invoer van de gebruiker nodig heeft. Die invoer sla je op in een variabele, zodat je er later in het programma iets mee kunt doen.
```python
medication = input("Which medication did the patient receive? ")
print("Medication administered:", medication)
```
Wat je tussen haakjes zet, verschijnt als tekst in de terminal. Daar achter typt de gebruiker zijn invoer.

De invoer van de gebruiker is altijd een string. Wil je er een berekening mee doen, dan zet je de invoer eerst om naar een integer of een float:
```python
dose = int(input("What is the dose in mg? "))
weight = float(input("What is the patient's weight in kg? "))
```

## Operatoren

Operatoren zijn symbolen waarmee je een bewerking uitvoert op een of meer waarden. Python heeft onder andere operatoren voor berekeningen en voor het vergelijken van waarden.

### Rekenkundige operatoren

Met rekenkundige operatoren doe je wiskundige berekeningen. 

* `+` voor optellen: `#!py 6 + 2` geeft `#!py 8`
* `-` voor aftrekken: `#!py 6 - 2` geeft `#!py 4`
* `*` voor vermenigvuldigen: `#!py 6 * 2` geeft `#!py 12`
* `/` voor delen: `#!py 6 / 2` geeft `#!py 3`
* `**` voor machtsverheffen: `#!py 6**2` geeft `#!py 36`

Naast de mogelijkheid om waarden op elkaar te delen, heeft Python ook twee andere operatoren die samenhangen met de deling:

* `//` voor het gehele deel van een deling: `#!py 7 // 2` geeft `#!py 3`
* `%` voor de rest na deling: `#!py 7 % 2` geeft `#!py 1`

???+ meer-leren "Toewijzingsoperatoren"

    Je hebt de toewijzingsoperator `=` al gezien bij variabelen. Er zijn ook verkorte notaties die een bewerking en toewijzing combineren:

    * `+=`: `#!py x += 2` is hetzelfde als `#!py x = x + 2`
    * `-=`: `#!py x -= 2` is hetzelfde als `#!py x = x - 2`
    * `*=`: `#!py x *= 2` is hetzelfde als `#!py x = x * 2`
    * `/=`: `#!py x /= 2` is hetzelfde als `#!py x = x / 2`

### Vergelijkingsoperatoren

Met vergelijkingsoperatoren vergelijk je twee waarden. Het resultaat is altijd `#!py True` (waar) of `#!py False` (niet waar). Python kent de volgende vergelijkingsoperatoren:

* `#!py ==` voor gelijk aan: `#!py 6 == 6` geeft `#!py True`
* `#!py !=` voor ongelijk aan: `#!py 6 != 2` geeft `#!py True`
* `#!py <` voor kleiner dan: `#!py 6 < 2` geeft `#!py False`
* `#!py >` voor groter dan: `#!py 6 > 2` geeft `#!py True`
* `#!py <=` voor kleiner dan of gelijk aan: `#!py 6 <= 2` geeft `#!py False`
* `#!py >=` voor groter dan of gelijk aan: `#!py 6 >= 6` geeft `#!py True`

Let op: `#!py ==` vergelijkt twee waarden, terwijl `=` een waarde toekent aan een variabele.

<div id="sec:logische-operatoren"></div>
???+ meer-leren "Logische operatoren"

    Bij `#!py if`-statements en loops wil je soms meerdere voorwaarden combineren. Je kunt dan de volgende logische operatoren gebruiken: 

    * `#!py and`: beide voorwaarden moeten waar zijn
    * `#!py or`: minstens één voorwaarde moet waar zijn
    * `#!py not`: keert een boolean om, dus `#!py True` wordt `#!py False` en andersom
    
    Je kunt je code ook schrijven zonder logische operatoren, de code is dan alleen wat langer. Hieronder een voorbeeld zonder logische operatoren:
    ```python
    if age >= 18:
        if age <= 67:
            print("working age")
    ```
    Hetzelfde kun je korter schrijven met `#!py and`:
    ```python
    if age >= 18 and age <= 67:
        print("working age")
    ```

## Indexing en slicing

Van sommige datatypes, zoals strings en lists, kun je afzonderlijke elementen benaderen. Dit noem je _indexing_. Dit doe je door Python te vertellen welk element je wilt hebben (eerste, tweede, derde, laatste) door de _index_ tussen blokhaakjes te zetten:
```py
study = "MNW"
print(study[0])  # M
print(study[1])  # N
print(study[2])  # W

years = [2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029]
print(years[0])  # 2020
print(years[5])  # 2025
print(years[-1])  # 2029
```
Let op: zoals heel veel programmeertalen begint Python te tellen vanaf nul. Zet je een min-teken vóór de index, dan telt hij vanaf het eind terug: `-1` is het laatste element, `-2` het één-na-laatste, enzovoorts.

Met _slicing_ kun je stukjes uit een lijst of string pakken met een _vanaf_ / _tot_-notatie. Als je de _vanaf_ weglaat dan begint hij aan het begin. Als je de _tot_ weglaat stopt hij aan het eind:
```py
module = "BiomedicalComputing"
print(module[3:10])  # medical
print(module[:10])  # Biomedical
print(module[10:])  # Computing
```
Zowel indexing als slicing kunnen heel handig zijn in [for-loops](#indexeren-met-rangelen).

## `#!py if`-statements

In een programma wil je soms specifieke acties uitvoeren afhankelijk van een voorwaarde. Stel dat je een lichaamstemperatuur uitleest: is de temperatuur te hoog, dan wil je een waarschuwing geven en is de temperatuur normaal, dan niet. Met een `#!py if`-statement kun je dit programmeren: 
```python
if temperature > 38:
    print("fever")
```
Python voert de code in het blok onder `#!py if` alleen uit als de voorwaarde waar is, dus als de temperatuur hoger dan 38 graden Celsius is. Let erop dat de code is ingesprongen met vier spaties, zodat duidelijk is welke code bij de voorwaarde hoort.

Als je ook iets wilt doen wanneer de voorwaarde niet waar is, dan gebruik je `#!py else`:
```python
if temperature > 38:
    print("fever")
else:
    print("normal temperature")
```

Heb je meerdere voorwaarden, dan gebruik je `#!py elif`. Python controleert de voorwaarden van boven naar beneden en voert het blok code uit behorende bij de _eerste_ voorwaarde die waar is.
```python
if temperature < 36:
    print("temperature too low")
elif temperature <= 38:
    print("normal temperature")
else:
    print("fever")
```

Soms wil je een voorwaarde verder opdelen. Dat kan met geneste `#!py if`-statements, een `#!py if`-statement binnen een `#!py if`-statement.
```python
if temperature >= 36:
    if temperature <= 38:
        print("normal temperature")
```
Geneste `#!py if`-statements kun je korter schrijven met [logische operatoren](#sec:logische-operatoren).

???+ meer-leren "Een variabele als voorwaarde"

    Je hebt gezien dat een voorwaarde in een `#!py if`-statement iets vergelijkt, zoals `#!py temperature > 38`. Deze voorwaarde is waar of niet waar. Maar soms is een variabele zelf al `#!py True` of `#!py False`. In dat geval kun je de vergelijking weglaten. Een voorbeeld:
    ```python
    if is_raining == True:
        print("bring an umbrella")
    ```
    Dit kun je ook schrijven als:
    ```python
    if is_raining:
        print("bring an umbrella")
    ```
    Beide doen hetzelfde, maar de kortere versie is gebruikelijker in Python.

## Loops

Met een loop voer je dezelfde code meerdere keren uit. Dat is handig als je een bewerking wilt herhalen zonder de code steeds opnieuw te schrijven. Python heeft twee soorten loops: de `#!py for`-loop en de `#!py while`-loop. Gebruik een `#!py for`-loop als je van tevoren weet hoe vaak je iets wilt herhalen, bijvoorbeeld een vast aantal keer of voor elk karakter in een string. Gebruik een `#!py while`-loop als je vooraf nog niet weet hoe vaak je iets wilt herhalen. Je herhaalt dan net zolang totdat een bepaalde voorwaarde niet meer geldt.

### `#!py for`-loop

Met een `#!py for`-loop herhaal je code een vast aantal keren. De loop doorloopt een reeks, bijvoorbeeld een string, een reeks getallen of een lijst, en voert voor elk element in de reeks de code in de loop uit.
```python
dna = "ATCG"

for base in dna:
    print(base)
```
De variabele `#!py base` krijgt bij elke herhaling de waarde van het volgende element in de reeks. Dus eerst `A`, daarna `T`, enzovoorts. In dit geval wordt de code vier keer herhaald en worden `A`, `T`, `C` en `G` onder elkaar in de terminal geprint. De code die herhaald wordt, staat ingesprongen onder de regel met `#!py for`. 


#### Itereren met `#!py range()`

Met `#!py range()` maak je een reeks getallen. Dat is handig als je een loop een bepaald aantal keren wilt herhalen.
```python
for i in range(5):
    print(i)
```
De variabele `i`is hier de zogeheten loopvariabele en krijgt bij elke herhaling de waarde van het volgende getal in de reeks. De naam van de loopvariabele kies je bij voorkeur passend bij wat de variabele voorstelt, bij een teller is `i` een gangbare keuze. `#!py range()` begint standaard bij 0 en telt op tot, maar niet inclusief, het opgegeven getal. De code hierboven print dus `0`, `1`, `2`, `3` en `4` onder elkaar in de terminal. Je kan ook een begin- en eindwaarde opgeven:
```python
for i in range(2, 6):
    print(i)
```
Nu worden de getallen `2`, `3`, `4`, en `5` onder elkaar in de terminal geprint.

???+ meer-leren "Weggooivariabele"

    Soms gebruik je een `#!py for`-loop puur om iets een aantal keer te herhalen, zonder dat je de loopvariabele zelf nodig hebt. In dat geval is het een gangbare conventie om `#!py _` als naam te kiezen. Dat is een signaal aan de lezer dat de variabele bewust niet gebruikt wordt.
    ```python
    for _ in range(5):
        print("Hello!")
    ```
    Dit print vijf keer `Hello!` in de terminal.

#### Indexeren met `#!py range(len(...))`

Eerder doorliep je de string `#!py dna` direct met een `#!py for`-loop. Soms wil je niet alleen elk element doorlopen, maar ook weten op welke positie dat element staat. Daarvoor combineer je `#!py range()` met `#!py len()`. 
```python
dna = "ATCG"

for i in range(len(dna)):
    print(i)
```
`#!py len(dna)` geeft de lengte van de string terug, in dit geval `4`. `#!py range(len(dna))` maakt dan de reeks `0`, `1`, `2` en `3` en deze getallen worden onder elkaar in de terminal geprint. Je krijgt dus de positie van de basen in de string terug.

Met de positie kun je ook het bijbehorende element opvragen. Dit heet indexering: je gebruikt een getal, de index, om een specifiek element op te vragen.
```python
dna = "ATCG"

for i in range(len(dna)):
    print(dna[i])
```
`#!py dna[i]` geeft het element op positie `i`. Python telt posities vanaf 0, dus `#!py dna[0]` is `A`, `#!py dna[1]` is `T`, enzovoorts. De kracht van indexering zit in het combineren van de positie en het element: je weet niet alleen _wat_ er op een positie staat, maar ook _waar_.
```python
dna = "ATCG"

for i in range(len(dna)):
    print(i, dna[i])
```

### `#!py while`-loop

Met een `#!py while`-loop herhaal je een blok code zolang een bepaalde voorwaarde geldt.
```python
number = 120

while number > 100:
    print(number)
    number = number - 10
```
De variabele `number` begint op 120. Bij elke herhaling controleert de loop of `#!py number > 100` nog steeds `#!py True` is. Als dat zo is, dan wordt de waarde van `number` in de terminal geprint en daarna met `10` verlaagd. Zodra `#!py number` de waarde `100` bereikt, stopt de loop.

Het is belangrijk dat de voorwaarde van de `#!py while`-loop uiteindelijk `#!py False` wordt, anders stopt de loop nooit. Een loop die voor altijd draait, heet een _oneindige loop_. Als je per ongeluk een oneindige loop hebt gestart, dan kun je het programma onderbreken met de sneltoetscombinatie ++cmd+c++ (macOS) / ++ctrl+c++ (Windows) in de terminal.

#### `#!py while`-loop onderbreken met `#!py break`

Soms hangt de stopconditie af van iets wat pas tijdens de loop bekend wordt, bijvoorbeeld gebruikersinvoer. In dat geval start je een loop met `#!py while True:`: de voorwaarde is altijd `#!py True`, dus de loop draait in principe oneindig. Met `#!py break` onderbreek je de loop wanneer jij dat wilt.
```python
while True:
    resistance = float(input("Enter the resistance (Ohm): "))
    print("Recorded resistance (Ohm)", resistance)

    last_measurement = input("Was this the last measurement? (yes/no) ")
    if last_measurement == "yes":
        break
```
Deze loop blijft metingen registreren totdat de gebruiker aangeeft dat de laatste meting is ingevoerd.

## Modules importeren

Python bevat een aantal ingebouwde functies, zoals `#!py print()` en `#!py input()`, maar lang niet alle functies zijn in Python standaard beschikbaar. Extra functionaliteit kun je toevoegen door gebruik te maken van _modules_. Dit zijn bestanden met kant-en-klare functies die je kunt importeren. Sommige modules worden meegeleverd met Python, zoals `pathlib` en `math`. Andere, zoals `matplotlib` en `sounddevice`, moet je eerst installeren in je virtual environment. 

Met `#!py import` laad je een module in je script. Daarna gebruik je de naam van de module gevolgd door een punt om functies aan te roepen. In het voorbeeld hieronder wordt de functie `#!py Path` aangeroepen van de module `#!py pathlib`:
```python
import pathlib

path = pathlib.Path("data.txt")
```

Sommige modulenamen zijn lang. Met `#!py as` geef je een module een kortere naam. Dit is bij sommige modules, zoals `#!py matplotlib.pyplot`, zelfs de standaard.
```python
import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [4, 5, 6]

plt.plot(x, y)
plt.show()
```

Met `#!py from` importeer je specifieke functies direct uit een module. Je hoeft dan niet steeds de modulenaam op te schrijven.
```python
from math import pi, sin

result = sin(pi / 2)
print(result)
```

## Functies

Wanneer scripts langer worden is het lastiger om het overzicht te bewaren. Je kunt dan commentaarregels toevoegen om blokken te scheiden. Een heel eenvoudig voorbeeld:
```py
# get patient data (returns height, weight)
height = float(input("Height (m): "))
weight = float(input("Weight (kg): "))

# calculate BMI (needs height, weight)
BMI = weight / height**2

# print results (needs BMI)
print("The patient's BMI is", BMI)
```
Hier hebben we ook aangegeven welke informatie ieder blokje teruggeeft of juist nodig heeft (height, weight of BMI). Deze blokjes zijn nog kort, maar zodra ze langer worden is het voor het overzicht in je script veel makkelijker als die code er niet tussendoor staat:
```py
# get patient data (returns height, weight)
# calculate BMI (needs height, weight)
# print results (needs BMI)
```
Dat kan, met functies. Als je de stukken code in functies hebt gestopt (dat laten we verderop zien) dan kun je het hoofdbestanddeel van je script als volgt schrijven:
```py
height, weight = get_patient_data()
BMI = calculate_BMI(height, weight)
print_results(BMI)
```
Kijk goed naar de informatie die bij iedere stap nodig is (tussen haakjes) en de informatie die teruggegeven wordt (vóór het is-gelijk-teken). Een functie definieer je met `#!py def functie_naam()` en kun je dan verderop in je script aanroepen:
```py
def get_squared_number(n):
    return n**2

print(get_squared_number(4))  # 16
print(get_squared_number(5))  # 25
print(get_squared_number(12))  # 144
```
De functie `#!py get_squared_number(n)` accepteert de _parameter_ `n`. De _waardes_ die je meegeeft als parameter noem je _arguments_ (hier 4, 5 en 12). In de _body_ van de functie staat de code en kun je de parameter gebruiken als variabele en heeft die dus de waarde van het argument. Wil je iets teruggeven als resultaat, dan kan dat met `#!py return` gevolgd door de _return value_. Wil je meerdere waardes teruggeven dan kun je ze scheiden met een komma:
```py
def get_quotient_and_remainder(number, divisor):
    quotient = number // divisor
    remainder = number % divisor
    return quotient, remainder

a, b = get_quotient_and_remainder(7, 5)
print("7 divided by 5 is", a, "with a remainder of", b)
```
De namen `a` en `b` zijn niet per se slim gekozen maar illustreert dat de functie twee waardes teruggeeft (`quotient` and `remainder`) en dat je die dan in twee variabelen kunt vangen (hier `a` en `b`). Het maakt dus niet uit dat die verschillende namen hebben. Bovenstaand hebben we een functie `get_quotient_and_remainder()` met _parameters_ `number` en `divisor` en _return values_ `quotient` en `remainder` die we aanroepen met de _argumenten_ `7` en `5`.

Schrijf de naam van functies in snake case, net als de namen van variabelen. Je kunt de naam vrij kiezen, maar gebruikelijk is het om de gebiedende wijs te gebruiken: `get_patient_data()`, `calculate_bmi()`, `print_results()`. Kies ook zoveel mogelijk namen waarmee je direct snapt wat de functie doet en je daar niet naar hoeft te raden. In bovenstaand voorbeeld zie je ook een ander veelgebruikt voordeel van functies: herhaaldelijk code uitvoeren kan door simpelweg de functie nog een keer aan te roepen. Je kunt ook op heel verschillende plekken in je code dezelfde functie aanroepen.

Als je functies gaat gebruiken word je script in eerste instantie _langer_. Voor korte scripts heeft het gebruik van functies dus niet heel veel zin. Voor langere scripts of zodra er veel stappen gezet moeten worden geeft het gebruik van functies veel meer overzicht en gemak.

### Samenvattend

Terugkerend naar het oorspronkelijke voorbeeld kunnen we het script met functies schrijven als:
=== "Met functies"
    ```py
    def get_patient_data():
        height = float(input("Height (m): "))
        weight = float(input("Weight (kg): "))
        return height, weight


    def calculate_BMI(height, weight):
        return weight / height**2


    def print_results(BMI):
        print("The patient's BMI is", BMI)


    height, weight = get_patient_data()
    BMI = calculate_BMI(height, weight)
    print_results(BMI)
    ```
=== "Zonder functies"
    ```py
    # get patient data (returns height, weight)
    height = float(input("Height (m): "))
    weight = float(input("Weight (kg): "))

    # calculate BMI (needs height, weight)
    BMI = weight / height**2

    # print results (needs BMI)
    print("The patient's BMI is", BMI)
    ```

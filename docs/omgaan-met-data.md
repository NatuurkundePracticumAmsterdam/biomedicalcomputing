# Omgaan met data

## Visual Studio Code

Visual Studio Code is een gratis, open-source _code editor._ VS Code is heel populair en is beschikbaar voor Windows, macOS en Linux. Je kunt het gebruiken om code te schrijven, maar ook om de code uit te voeren en de resultaten te bekijken. Verder zit de editor vol snufjes die je helpen bij het schrijven van de code waardoor je minder hoeft te typen en minder fouten maakt.

Het is handig om de code die bij elkaar hoort in één map te plaatsen en die map te openen met VS Code. De editor weet dan wat er bij elkaar hoort en dat helpt bij het schrijven en uitvoeren van je code. We gaan alle code voor deze cursus in één map plaatsen. Binnen die map mag je best submapjes aanmaken, maar open met VS Code steeds de map van de cursus. Noem, voor het gemak, de map _BiomedicalComputing._

!!! opdracht-basis "Sessie starten in VS Code"

    Start Visual Studio Code en open de map `BiomedicalComputing` via **File > Open Folder...** of, in een leeg venster, het map-icoontje met `Open...` onder het kopje **Start**. Dan, omdat het de eerste keer is dat je deze map opent, doe nog het volgende:

    1.  Links onderin verschijnt een blauwe knop met `Restricted Mode`. Klik daarop, dan op Trust (je vertrouwt je eigen map en geeft dan rechten om je eigen code uit te voeren) en dan rechtsboven in dat nieuwe venster klik je op het kruisje. Als het goed is, is het blauwe `Restricted Mode` verdwenen.
    2.  Open een nieuwe _Terminal_ via het menu **Terminal > New Terminal**. Er opent nu een venster onderin Visual Studio Code. Hier kun je commando's typen die vervolgens door het systeem worden uitgevoerd. Type in:
    ```
    uv venv
    ```
        Met deze regel voer je het commando `uv` uit en vraag je die om een _virtual environment_ aan te maken voor jouw project. Dit is een omgeving met Python en alle extra's die je nodig hebt.
    3.  Aan de linkerkant zie je een lege balk met bovenin het woord `Explorer` met daaronder `BIOMEDICALCOMPUTING`. Hier krijg je een overzicht te zien van al je bestanden en submappen. Zodra je je muis in die kolom beweegt verschijnen er vier nieuwe icoontjes naast de naam van onze map. De eerste is de knop om een nieuw bestand aan te maken en de tweede is een knop om een nieuwe submap aan te maken. Klik om een nieuw bestand aan te maken en type in het lege veld met blauwe rand de naam `hello.py`. Visual Studio Code denkt even na en kan je dan een pop-up geven met de mededeling dat Python niet gevonden kan worden en de vraag of je wilt dat VS Code dat voor je installeert. Klik op `Don't Ask Again`. We hebben Python immers zojuist geïnstalleerd...

!!! opdracht-basis "Hello World"

    Klik in het centrale deel van VS Code (de editor). Hier kun je de code typen in het bestand {{file}}`hello.py` die je daarna uit kunt voeren. Type in:

    ``` py
    print("Hello World!")
    ```

    met **File > Save** of ++ctrl+s++. Druk dan rechtsbovenin het venster op het driehoekje {{run_small}} om de code uit te voeren. In de terminal onderaan het scherm verschijnt nu automatisch het commando om {{file}}`hello.py` uit te voeren én daarna de tekst `Hello World!` voordat er een nieuwe regel verschijnt waar je weer commando's kunt typen.

Het is gelukt om een werkomgeving aan te maken en je eerste code uit te voeren!

## Versiebeheer met GitHub

Heel hoofdstuk uit ECPC overnemen maar de opdrachten even doorlopen en de namen wijzigen.

## Eerste stappen

Nu we onze werkomgeving helemaal hebben ingericht kunnen we aan de slag met de eerste stappen. Je hebt al wat Pythoncode gezien; nu gaan we het schrijven. We beginnen (heel) eenvoudig, maar gaan deze sessie verder uitbreiden naar code die echt bruikbaar is.

Opdracht: naam\_en\_leeftijd.py

In het allereerste voorbeeld heb je al gezien dat je met print() dingen kunt _printen _naar het beeldscherm. Met input() kun je dingen _vragen_ aan de gebruiker. Het antwoord van de gebruiker slaan we op in een _variabele_. Zie ook de vorige sessie.

Schrijf een script dat eerst vraagt hoe je heet, en dan hallo zegt en je naam gebruikt. Een voorbeeld van een sessie:

“Hoe heet je?”

Alice

“Hoi Alice!”

Breid nu je script uit zodat hij controleert of je naam gelijk is aan “admin”, de standaardnaam voor accounts met alle rechten op een computersysteem. Alleen als je naam gelijk is aan “admin” moet je script roepen: “je bent een baas!” In alle andere gevallen zegt hij je nog steeds gedag, zoals hierboven.

Breid je script uit zodat hij ook vraagt om je leeftijd (maar alleen als je naam _niet_ admin is). LET OP: INT() GEBRUIKEN. Als je leeftijd hoger of gelijk is aan 13 jaar, print dan “Je mag op social media!” Als je 16 jaar of ouder bent, print dan “Je mag een scooter besturen.” Print, vanaf 17 jaar, “Je mag je rijbewijs halen.” Vanaf 18 jaar: “Je bent volwassen en mag stemmen.” Vanaf 30 jaar: “Je mag geen studiefinanciering meer aanvragen.” Hoe ouder je bent, hoe langer het lijstje wordt dat op het scherm verschijnt.

Soms wil je juist _niet_ dat het lijstje steeds langer wordt. Pas het script aan zodat hij _alleen_ de regel print die nog net bij je leeftijd hoort. Dus als je 17 invult, print dan _alleen_ “Je mag je rijbewijs halen.” Gebruik hiervoor een if … elif construct.

OPLETTEN: IN HET GERAAMTE STAAT GEKOPPELDE IF-ELSE-STATEMENTS maar ik weet niet wat we daarmee bedoelden. Pas later komt in een paarse opdracht and en or voor? Dus deze verwijderen? Soms wil je testen of meerdere condities tegelijk waar zijn. Dit kan met een if … and … of een if … or … construct. Laat je script, als je tussen de 18 en 20 jaar oud bent, printen “Je bent nog een tiener, maar al wel volwassen!” Controleer ook of de persoon jonger is dan 4 of ouder dan 68. In dat geval hoef je niet te werken en heb je lekker veel vrije tijd.

PAARS: Leg f-strings uit en laat herschrijven.

### DNA-replicatie

Een klusje is pas echt stom als je het heel vaak achter elkaar moet doen. Computers zijn dan superhandig: je hoeft het klusje maar één keer te schrijven en te vertellen hoe vaak hij het moet uitvoeren.

PREDICT THE OUTCOME IN EEN SCRIPT

Jullie hebben al eerder, handmatig, in DNA gezocht naar een fout die is ontstaan tijdens DNA-replicatie waarbij in de nieuwe streng soms een foutje kan ontstaan. We gaan allereerst een script schrijven dat het proces van DNA-replicatie nabootst.

Opdracht: replicatie.py.

We beginnen met een stukje streng1 = “ATATAGAGTC”. Print de letters van de bijbehorende tweede streng los onder elkaar. Dus, voor iedere letter uit streng1, als de letter een A is, print een T, als de letter een C is, print een G, enz.

Het is duidelijker om beide strengen naast elkaar te printen. Als de letter uit streng1 een A is, print A — T, enz.

PAARS: Je hebt nu waarschijnlijk een verzameling print-statements. Als je de vorm van de output wilt veranderen, bijvoorbeeld A == T wilt printen in plaats van A — T, dan moet je dat op vier plekken aanpassen. Dat kan beter. Pas het script aan zodat hij hetzelfde doet, maar slechts één print-statement bevat. Tip: maak een nieuwe variabele aan voor de letter uit streng2.

Nu we het proces van DNA-replicatie een beetje doorhebben, kunnen we onze kennis van wat de tweede streng zou _moeten_ zijn gebruiken om op zoek te gaan naar de fout.

Opdracht: find\_DNA\_mistake.py.

Neem weer streng1 = “ATATAGAGTC”. Daarnaast is streng2 = “AATATCGCAA”. We willen nu weer een for-loop schrijven, maar hierbij de eerste letter uit streng1 vergelijken met de eerste letter uit streng2, en vervolgens de tweede letter uit streng1 vergelijken met de tweede letter uit streng2, enz. Dit betekent dat we een specifieke vorm van for-loop nodig hebben. Overleg welke.

Schrijf een script dat op zoek gaat naar _alle_ fouten in streng2. Voor iedere gevonden fout: print de positie van de fout (tel de eerste base als 1), print wat de fout is, en print wat de correcte base zou moeten zijn. Controleer met de hand of de output van je script klopt.

Fijn dat het werkt, maar fouten zoeken in zo’n klein stukje DNA kan natuurlijk veel sneller gewoon met de hand. Programmeren is pas nuttig als het zoeken met de hand veel langer duurt dan het programmeren. Dat is bijvoorbeeld het geval wanneer we een fout zoeken in 10.000 baseparen.

Maak een schatting van hoe lang je daar met de hand mee bezig zou zijn.

Je hebt al een script dat de fout kan zoeken in kleine stukjes DNA. Maar je hoeft niet veel aan te passen om te zoeken in 10.000 baseparen. Je hoeft alleen maar de regels streng1 = … en streng2 = … aan te passen. Het kopiëren en plakken van 10.000 baseparen per streng is niet handig in een script. Daarom is het makkelijker om de gegevens op te slaan in bestanden en die bestanden in te lezen in je script. Download de gegevens voor beiden strengen \[hier\] en \[hier\]. Gebruik de volgende regel om de data van streng1 in te lezen en te bewaren in de variabele: streng1 = pathlib.path().read\_text().

Pas ook de regel voor streng2 aan en zoek de fouten.

PAARS: als je code geneste if-statements bevat, pas je code aan met AND of OR zodat je maar vier if-statements nodig hebt.

### NOG: COMMENTS en WHILE-loop

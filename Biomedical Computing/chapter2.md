
# 2. Omgaan met data

### Visual Studio Code

Visual Studio Code is een gratis, open-source *code editor.* VS Code is heel populair en is beschikbaar voor Windows, macOS en Linux. Je kunt het gebruiken om code te schrijven, maar ook om de code uit te voeren en de resultaten te bekijken. Verder zit de editor vol snufjes die je helpen bij het schrijven van de code waardoor je minder hoeft te typen en minder fouten maakt.

Het is handig om de code die bij elkaar hoort in één map te plaatsen en die map te openen met VS Code. De editor weet dan wat er bij elkaar hoort en dat helpt bij het schrijven en uitvoeren van je code. We gaan alle code voor deze cursus in één map plaatsen. Binnen die map mag je best submapjes aanmaken, maar open met VS Code steeds de map van de cursus. Noem, voor het gemak, de map *Biomedical Computing.*

Opdracht: Open de map uit sessie 1 in VS Code.

Opdracht: trust workspace.

Opdracht: open terminal en maak venv aan. (uv venv).

Opdracht: schrijf helloworld.py en selecteer/verifieer venv indien nodig.

Opdracht: run helloworld.py.

Het is gelukt om een werkomgeving aan te maken en je eerste code uit te voeren!

### Versiebeheer met GitHub

Heel hoofdstuk uit ECPC overnemen maar de opdrachten even doorlopen en de namen wijzigen.

### Eerste stappen

Nu we onze werkomgeving helemaal hebben ingericht kunnen we aan de slag met de eerste stappen. Je hebt al wat Pythoncode gezien; nu gaan we het schrijven. We beginnen (heel) eenvoudig, maar gaan deze sessie verder uitbreiden naar code die echt bruikbaar is.

Opdracht: naam\_en\_leeftijd.py

In het allereerste voorbeeld heb je al gezien dat je met print() dingen kunt *printen *naar het beeldscherm. Met input() kun je dingen *vragen* aan de gebruiker. Het antwoord van de gebruiker slaan we op in een *variabele*. Zie ook de vorige sessie.

Schrijf een script dat eerst vraagt hoe je heet, en dan hallo zegt en je naam gebruikt. Een voorbeeld van een sessie:

“Hoe heet je?”

Alice

“Hoi Alice!”

Breid nu je script uit zodat hij controleert of je naam gelijk is aan “admin”, de standaardnaam voor accounts met alle rechten op een computersysteem. Alleen als je naam gelijk is aan “admin” moet je script roepen: “je bent een baas!” In alle andere gevallen zegt hij je nog steeds gedag, zoals hierboven.

Breid je script uit zodat hij ook vraagt om je leeftijd (maar alleen als je naam *niet* admin is). LET OP: INT() GEBRUIKEN. Als je leeftijd hoger of gelijk is aan 13 jaar, print dan “Je mag op social media!” Als je 16 jaar of ouder bent, print dan “Je mag een scooter besturen.” Print, vanaf 17 jaar, “Je mag je rijbewijs halen.” Vanaf 18 jaar: “Je bent volwassen en mag stemmen.” Vanaf 30 jaar: “Je mag geen studiefinanciering meer aanvragen.” Hoe ouder je bent, hoe langer het lijstje wordt dat op het scherm verschijnt.

Soms wil je juist *niet* dat het lijstje steeds langer wordt. Pas het script aan zodat hij *alleen* de regel print die nog net bij je leeftijd hoort. Dus als je 17 invult, print dan *alleen* “Je mag je rijbewijs halen.” Gebruik hiervoor een if … elif construct.

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

Nu we het proces van DNA-replicatie een beetje doorhebben, kunnen we onze kennis van wat de tweede streng zou *moeten* zijn gebruiken om op zoek te gaan naar de fout. 

Opdracht: find\_DNA\_mistake.py.

Neem weer streng1 = “ATATAGAGTC”. Daarnaast is streng2 = “AATATCGCAA”. We willen nu weer een for-loop schrijven, maar hierbij de eerste letter uit streng1 vergelijken met de eerste letter uit streng2, en vervolgens de tweede letter uit streng1 vergelijken met de tweede letter uit streng2, enz. Dit betekent dat we een specifieke vorm van for-loop nodig hebben. Overleg welke.

Schrijf een script dat op zoek gaat naar *alle* fouten in streng2. Voor iedere gevonden fout: print de positie van de fout (tel de eerste base als 1), print wat de fout is, en print wat de correcte base zou moeten zijn. Controleer met de hand of de output van je script klopt.

Fijn dat het werkt, maar fouten zoeken in zo’n klein stukje DNA kan natuurlijk veel sneller gewoon met de hand. Programmeren is pas nuttig als het zoeken met de hand veel langer duurt dan het programmeren. Dat is bijvoorbeeld het geval wanneer we een fout zoeken in 10.000 baseparen.

Maak een schatting van hoe lang je daar met de hand mee bezig zou zijn.

Je hebt al een script dat de fout kan zoeken in kleine stukjes DNA. Maar je hoeft niet veel aan te passen om te zoeken in 10.000 baseparen. Je hoeft alleen maar de regels streng1 = … en streng2 = … aan te passen. Het kopiëren en plakken van 10.000 baseparen per streng is niet handig in een script. Daarom is het makkelijker om de gegevens op te slaan in bestanden en die bestanden in te lezen in je script. Download de gegevens voor beiden strengen \[hier\] en \[hier\]. Gebruik de volgende regel om de data van streng1 in te lezen en te bewaren in de variabele: streng1 = pathlib.path().read\_text().

Pas ook de regel voor streng2 aan en zoek de fouten.

PAARS: als je code geneste if-statements bevat, pas je code aan met AND of OR zodat je maar vier if-statements nodig hebt.

### NOG: COMMENTS en WHILE-loop

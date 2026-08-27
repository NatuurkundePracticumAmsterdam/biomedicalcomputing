# Sessie 2: DNA-mutaties

## Visual Studio Code

Visual Studio Code is een gratis, open-source _code editor._ VS Code is heel populair en is beschikbaar voor Windows, macOS en Linux. Je kunt het gebruiken om code te schrijven, maar ook om de code uit te voeren en de resultaten te bekijken. Verder zit de editor vol snufjes die je helpen bij het schrijven van de code waardoor je minder hoeft te typen en minder fouten maakt.

Het is handig om de code die bij elkaar hoort in één map te plaatsen en die map te openen met VS Code. De editor weet dan wat er bij elkaar hoort en dat helpt bij het schrijven en uitvoeren van je code. We gaan alle code voor deze cursus in één map plaatsen. Binnen die map mag je best submapjes aanmaken, maar open met VS Code steeds de map van de cursus. Noem, voor het gemak, de map _BiomedicalComputing._


!!! opdracht-basis "Map aanmaken voor de cursus"

    Veel computers synchroniseren hun bestanden naar OneDrive of iCloud. Dat kan heel handig zijn: je kunt vanaf meerdere computers bij je bestanden en als je computer stukgaat of gestolen wordt dan zijn je bestanden nog steeds veilig. Maar het kan ook voor problemen zorgen: als je mappen synchroniseert met veel kleine bestanden dan kunnen OneDrive en iCloud overstuur raken en dat zorgt dan ook voor problemen met je andere bestanden. Om dat te voorkomen[^venvs-sync] gaan we in deze cursus een map aanmaken _buiten_ OneDrive, iCloud, of een andere service.

    === "macOS"
        
        1. Open Finder.
        1. Ga via de menubalk naar **Ga -> Thuismap**.
        1. Ga via de menubalk naar **Archief -> Nieuwe map**.
        1. Type als naam `BiomedicalComputing` (zonder spatie).

    === "Windows"

        1. Open Verkenner.
        1. Klik op het :octicons-chevron-right-16:-symbool meteen rechts naast het :fontawesome-regular-home:-icoon.
        1. Klik onderin het menu op je eigen naam.
        1. Klik linksboven op **Nieuw** en kies dan **Map**.
        1. Type als naam `BiomedicalComputing` (zonder spatie).
    
!!! warning "Open altijd de goede map"
    Test nog een keer of "select environment" nodig is, of zeg daar in ieder geval iets over. VS Code -> Visual Studio Code. Versiebeheer verplaatsen (zie geraamte). 

!!! opdracht-basis "Sessie starten in VS Code"

    Start Visual Studio Code en open de map {{folder}}`BiomedicalComputing` via **File > Open Folder...** of, in een leeg venster, het map-icoontje met `Open...` onder het kopje **Start**. In het venster dat opent is normaal gesproken direct je thuismap gekozen en zie je {{folder}}`BiomedicalComputing` er tussenstaan. Dan, omdat het de eerste keer is dat je deze map opent, doe nog het volgende:

    1.  Links onderin verschijnt een blauwe knop met `Restricted Mode`. Klik daarop, dan op Trust (je vertrouwt je eigen map en geeft dan rechten om je eigen code uit te voeren) en dan rechtsboven in dat nieuwe venster klik je op het kruisje. Als het goed is, is het blauwe `Restricted Mode` verdwenen.
    2.  Open een nieuwe _Terminal_ via het menu **Terminal > New Terminal**. Er opent nu een venster onderin Visual Studio Code. Hier kun je commando's typen die vervolgens door het systeem worden uitgevoerd. Type in:
    ```
    uv venv
    ```
        Met deze regel voer je het commando `uv` uit en vraag je die om een _virtual environment_ aan te maken voor jouw project. Dit is een omgeving met Python en alle extra's die je nodig hebt.
    3.  Aan de linkerkant zie je een lege balk met bovenin het woord `Explorer` met daaronder `BiomedicalComputing`. Hier krijg je een overzicht te zien van al je bestanden en submappen. Zodra je je muis in die kolom beweegt verschijnen er vier nieuwe icoontjes naast de naam van onze map. De eerste is de knop om een nieuw bestand aan te maken en de tweede is een knop om een nieuwe submap aan te maken. Klik om een nieuw bestand aan te maken en type in het lege veld met blauwe rand de naam `hello.py`. Visual Studio Code denkt even na en kan je dan een pop-up geven met de mededeling dat Python niet gevonden kan worden en de vraag of je wilt dat VS Code dat voor je installeert. Klik op `Don't Ask Again`. We hebben Python immers zojuist geïnstalleerd...

!!! opdracht-basis "Hello World"

    Klik in het centrale deel van VS Code (de editor). Hier kun je de code typen in het bestand {{file}}`hello.py` die je daarna uit kunt voeren. Type in:

    ``` py
    print("Hello World!")
    ```

    met **File > Save** of ++ctrl+s++. Druk dan rechtsbovenin het venster op het driehoekje {{run_small}} om de code uit te voeren. In de terminal onderaan het scherm verschijnt nu automatisch het commando om {{file}}`hello.py` uit te voeren én daarna de tekst `Hello World!` voordat er een nieuwe regel verschijnt waar je weer commando's kunt typen.

Het is gelukt om een werkomgeving aan te maken en je eerste code uit te voeren!

!!! info "Open altijd de goede map"

    De map {{folder}}`BiomedicalComputing` is je projectmap. Hierin komt alle code te staan die we tijdens deze cursus gaan schrijven. Je mag, als je dat wilt, submapjes aanmaken en je code organiseren. Bijvoorbeeld per sessie, of per onderwerp. _Maar:_ als je Visual Studio Code opnieuw opent, open dan _altijd_ de {{folder}}`BiomedicalComputing` map, en _niet_ een submapje.[^vscode-submap]

## Eerste stappen

Nu we onze werkomgeving helemaal hebben ingericht kunnen we aan de slag met de eerste stappen. Je hebt al wat Pythoncode gezien; nu gaan we het schrijven. We beginnen (heel) eenvoudig, maar gaan deze sessie verder uitbreiden naar code die echt bruikbaar is.

!!! opdracht-basis "Naam en leeftijd"

    In het allereerste voorbeeld heb je al gezien dat je met `#!py print()` dingen kunt _printen_ naar het beeldscherm. Met `#!py input()` kun je dingen _vragen_ aan de gebruiker. Het antwoord van de gebruiker slaan we op in een _variabele_. Zie ook de vorige sessie. In de volgende opdrachten gaan we hier gebruik van maken. Wij schrijven alle code in het Engels, dus bestandsnamen, variabelenamen, én berichten die op het scherm worden geprint zijn in onze opdrachten Engelstalig. Werk je liever in het Nederlands, wees dan het liefst wel consequent en doe _alles_ in het Nederlands.

    1. Schrijf een script {{file}}`name_and_age.py` dat eerst vraagt hoe je heet, en dan hallo zegt en je naam gebruikt. Een voorbeeld van een sessie:
        ```
        What is your name? Alice
        Hi Alice
        ```
    2. Breid nu je script uit zodat hij controleert of je naam gelijk is aan `admin`, de standaardnaam voor accounts met alle rechten op een computersysteem. Alleen als je naam gelijk is aan `admin` moet je script roepen: `You're a legend!` In alle andere gevallen zegt hij je nog steeds gedag, zoals hierboven. Zorg dat je ook (kort) comments schrijft in je script om duidelijk te maken welk stukje wat doet.
    3. Breid je script uit zodat hij ook vraagt om je leeftijd (maar alleen als je naam _niet_ admin is). Hint: gebruik `#!py int(input(...))`. Als je leeftijd hoger of gelijk is aan 13 jaar, print dan `You're allowed on social media!` Als je 16 jaar of ouder bent, print dan `You can drive a scooter.` Print, vanaf 17 jaar, `You can get a driving license.` Vanaf 18 jaar: `You're a grown-up now and are allowed to vote.` Vanaf 30 jaar: `You can no longer apply for student finance.` Hoe ouder je bent, hoe langer het lijstje wordt dat op het scherm verschijnt.
    4. Soms wil je juist _niet_ dat het lijstje steeds langer wordt. Pas het script aan zodat hij _alleen_ de regel print die nog net bij je leeftijd hoort. Dus als je 17 invult, print dan _alleen_ `You can get a driving license.` Hint: gebruik hiervoor een `#!py if ... elif` construct.
    5. Ga naar GitHub Desktop en commit de code van deze opdracht.

!!! opdracht-meer "Meerdere condities"
    
    Soms wil je testen op meerdere condities tegelijk. Een bepaalde vrucht kan een banaan zijn, _en_ groot. Het kan een appel _of_ een peer zijn (één van de twee), en niet iets anders. Dit kan met een `#!py if ... and ...` of een `#!py if ... or ...` construct. Bijvoorbeeld:
    ```py
    # Banaan en groot
    if fruit == "banana" and size_cm > 20:
        print("Yes, a large banana!")
    
    # Appel of peer
    if fruit == "apple" or fruit == "pear":
        print("Phew, I only like apples and pears.")
    ```
    Laat je script, als je tussen de 18 en 20 jaar oud bent, printen `You're still a teenager, but already an adult!` Controleer ook of de persoon jonger is dan 4 of ouder dan 68. In dat geval hoef je niet te werken en heb je lekker veel vrije tijd.

!!! opdracht-meer "F-strings"
    
    Misschien heb je gemerkt dat als je `#!py print("Hi", naam, "!")` gebruikt, dat Python automatisch spaties invoegt tussen de verschillende stukken. Dus `Hi Alice !` in plaats van `HiAlice!`. Als je meer controle wilt over waar wel en niet spaties komen, kun je zogeheten _f-strings_ gebruiken. Een f-string is een string (`#!py "Hi"`) waar je de letter `f` vóór schrijft (`#!py f"Hi"`). Als je dat doet dan werkt dat hetzelfde als een gewone string, _behalve_ dat dingen die tussen accolades `{}` staan worden vervangen. Je kunt dan schrijven: `#!py print(f"Hi {naam}!")` met als uitvoer `Hi Alice!`. De variabele die tussen haakjes stond is vervangen door de _waarde_ van die variabele. Hierbij heb je dus kunnen kiezen voor _wel_ een spatie tussen Hi en Alice, maar niet tussen Alice en het uitroepteken.

    Pas je script aan zodat je f-strings gebruikt, maar _alleen_ waar dat nodig of handig is, en commit de wijzigingen.

## Versiebeheer

We hebben de map {{folder}}`BiomedicalComputing` nu niet op OneDrive, iCloud Drive, Dropbox, Google Drive of wat dan ook staan. We hebben dus geen cloud-opslag en géén backup. Dat is niet zo mooi als je je laptop kwijtraakt of als je per ongeluk bestanden wist. Bij veel cloudaanbieders kun je een gewist bestand nog 30 dagen terughalen. OneDrive bewaart zelfs (tijdelijk) oude versies van een bestand, maar daar hebben wij dus nu niets aan. We gaan dit oplossen, op een manier die veel gebruikt wordt door programmeurs: met _versiebeheer_.

Versiebeheer (Engels: _version control_) stelt je in staat om af en toe een momentopname te maken van al je bestanden in een bepaalde map, inclusief alle submappen. Dit doe je niet na iedere regel code, maar bijvoorbeeld wel als je een stukje code af hebt en na het testen weet dat het werkt. Zo'n momentopname heet een _commit_. Bij het maken van een commit type je een korte notitie: wat heb je toegevoegd, gewijzigd, of gefixt? Je houdt eigenlijk een soort labjournaal bij, maar dan heel kort. Hoe vaak je commit is aan jou; maar wacht niet te lang &mdash; anders is het geen versiebeheer meer. Een verzameling van scripts en alle wijzigingen met labjournaal-achtige notities noem je samen een _repository_.

Je versiebeheersysteem geeft duidelijk al je wijzigingen weer ten opzichte van de laatste momentopname. Ook kun je de wijzigingen tussen oudere versies bekijken. Je bladert dan als het ware door een labjournaal.

Er zijn tegenwoordig veel websites die een plek bieden voor repositories. Die zijn dus een soort online backup, maar je kunt daar ook je code delen met anderen als je dat wilt. De bekendste websites zijn GitHub, GitLab, en Codeberg. GitHub, aangekocht door Microsoft, is op dit moment het bekendste en grootste platform. Veel bekende softwareprojecten vinden daar hun thuis.

In deze cursus ga je werken met GitHub. Je moet hiervoor wel een (gratis) account aanmaken. Als student kom je ook nog in aanmerking voor een educatiekorting op een pro-account.[^pro-account] Je betaalt dan nog steeds niets.

!!! opdracht-basis "Account aanmaken"

    Ga naar [https://github.com/](https://github.com/) en klik op `Sign up for GitHub`. Maak een account aan onder je _privé-emailadres_. Op deze manier blijf je toegang houden tot je account ook nadat je afgestudeerd bent.

Om het programmeurs makkelijker te maken met GitHub te werken heeft GitHub een desktopapplicatie ontwikkeld met de naam GitHub Desktop.[^git] Je gaat GitHub Desktop gebruiken om een repository te maken van de _BiomedicalComputing_ map.

!!! opdracht-basis "GitHub Desktop inloggen"

    Start GitHub Desktop en log nu in met jouw account.

<div id="opd:add_repository"></div>

!!! opdracht-basis "Van bestaande map repository maken"

    <div class="grid-tree" markdown>
        <div>
        **Zorg dat Visual Studio Code is afgesloten en geen bestanden meer open heeft staan.** Je gaat een repository maken van een bestaande map: {{folder}}`BiomedicalComputing`.
        <br>
        <br>
        Je gaat naar GitHub Desktop. Je vindt onder het dropdownmenu **File** drie opties:  `New repository...`, `Add local repository...` en `Clone repository...`. Hoewel `New repository...` een goede optie lijkt, is dit niet wat je zoekt. Op het moment dat je een nieuwe repository maakt, wordt er ook een nieuwe map aangemaakt en dat is niet wat je wilt. Daarom kies je voor `Add local repository...`. Je geeft de map {{folder}}`BiomedicalComputing` op als locatie en krijgt in rode tekst een waarschuwing. De waarschuwing geeft aan dat de map wel bestaat maar dat het geen `Git repository` is, daarom klik je op de blauwe tekst `create a repository`. Je vinkt `Initialize this repository with a README` aan en kiest bij `Git ignore` voor <q>Python</q>. Daarna klik je op de blauwe knop `Create Repository`. 
        <br>
        <br>
        De repository {{github}}`BiomedicalComputing` is in GitHub Desktop geopend en als je op het tabblad 'History' klikt dan zie je dat er een `Initial commit` is met wat `git`-bestanden en de Pythonscripts die je in de map hebt gezet. Vanaf nu staat {{github}}`BiomedicalComputing` in versiebeheer en houdt Git je wijzigingen bij. Het is wel belangrijk dat je met regelmaat zelf [commit](#commit)!
        <br>
        <br>
        Open de repository in Visual Studio Code door op de knop `Open in Visual Studio Code` te klikken _of_ via het pulldown-menu: **Menu > Repository > Open in Visual Studio Code**. Probeer maar eens of je het {{file}}`hello.py` script kunt runnen.
    </div>
        <div>
        {{folder}}`BiomedicalComputing`  
        {{T}} {{file}} `hello.py`  
        {{L}} {{dots}} 
        </div>
    </div>  

    !!! info "{{github}}-symbool"

        Vanaf nu duiden we een repository aan met het {{github}}-symbool.

    !!! info "Git ignore Python"

        Waarom zou je bij `Git ignore` voor Python kiezen, je gaat toch juist Python bestanden maken? De `Git ignore` zorgt ervoor dat allerlei _hulpbestanden_ van Python niet bewaard worden als commit. Maar de Pythoncode zelf wordt wel bewaard.

Alle wijzigingen aan bestanden in de repository kun je vanaf nu bijhouden door regelmatig een commit te maken. Met een commit maak je als het ware een snapshot van alle bestanden en hang je daar een labeltje aan.
Dit kan in GitHub Desktop. Elke commit geef je een begeleidend schrijven mee, een _commit message_. Je hoopt dat jij &mdash; maar ook je collega &mdash; na het lezen van de commit message snel begrijpt wat er veranderd is én waarom.

Hieronder zie je een aantal voorbeelden van commit messages. De titel (_summary_) is kort en krachtig. In de beschrijving (_description_) staat specifieke en uitgebreidere informatie.

--8<-- "docs/html-snippets/commit.html"

!!! opdracht-basis "Commit"

    Voer de volgende opdrachten uit:

    1. Open GitHub Desktop, klik op _Current repository_ (links onder de menubalk) en selecteer de repository {{github}}`BiomedicalComputing`.
    2. Ga naar het dropdownmenu **Repository** en kies voor `Open in Visual Studio Code` (of druk op ++ctrl+shift+a++ ) en open de repository {{github}}`BiomedicalComputing` in Visual Studio Code.
    3. Open in Visual Studio Code één van je Pythonscripts.
    4. Type een stukje code erbij &mdash; bijvoorbeeld een `#!py print`-statement &mdash; en haal ergens anders iets weg. Sla het bestand op.
    5. Ga terug naar GitHub Desktop. Controleer bij _Current repository_ (links onder de menubalk) of de repository {{github}}`BiomedicalComputing` nog steeds is geopend.
    6. Klik daaronder op het tabblad _Changes_.
    7. Als er meerdere bestanden gewijzigd zijn, kun je met een blauwe vinkje aangeven voor welke bestanden je een commit schrijft.
    8. Onder de lijst met gewijzigde bestanden vind je twee invulvelden. Een smal veld voor een titel en een groot veld voor een uitgebreide beschrijving (_Description_). In het veld voor een titel staat in lichtgrijs een nietzeggende commit, bijvoorbeeld _Update test.py_. Schrijf daar een nuttige commit message. Dus niet: <q>opdracht: commit</q>. Maar meer zoiets als: <q>feat: add age verification</q>. Houd de titel in de commit message kort en krachtig. Een uitgebreidere beschrijving kun je kwijt in het grote veld.
    9. Klik op _Commit to main_. Gefeliciteerd! {{feesttoeter}} Je hebt je eerste commit gedaan!

In GitHub Desktop zie je nu bij _History_ de commit staan, met in één oogopslag alle wijzigingen.

!!! info

    Als je wilt opzoeken hoe iets werkt bij GitHub Desktop, kijk dan in de documentatie: [https://docs.github.com/en/desktop](https://docs.github.com/en/desktop).

!!! opdracht-basis "Push en pull"

    De repository {{github}}`BiomedicalComputing` bestaat alleen nog maar op de computer. Het kan fijn zijn om de repository ook in de cloud te hebben op [github.com](https://github.com/). Het geeft de mogelijkheid je code op andere computers binnen te halen en te delen met anderen. Bovendien ben je dan beschermd tegen verlies van je laptop of bestanden.

    In GitHub Desktop vind je een knop `Publish repository; Publish this repository to GitHub`. Als je daar op drukt kun je nog een andere naam aan de repository geven (deze naam bepaalt de url op [github.com](https://github.com/)), een beschrijving toevoegen en aangeven of de code privé moet zijn. Daarna klik je op de blauwe knop `Publish repository`. Als je nu naar [github.com](https://github.com) gaat zie je bij jouw repositories de zojuist gepubliceerde repository staan.

    Om je wijzigen ook in de cloud op te slaan kun je commits `pushen` naar [github.com](https://github.com/) met de knop `Push origin`. Als je op een andere computer gaat werken kun je de laatste wijzigingen vanuit de cloud naar de computer halen door op `Fetch origin` te klikken en daarna op `Pull origin`.

??? meer-leren "Openbare code en samenwerken"

    Om makkelijk je Git repository te delen met vrienden, collega's en de rest van de wereld kun je er dus voor kiezen om deze op GitHub te zetten. Je kunt dan je commits pushen naar GitHub en wijzigingen die je vrienden hebben gemaakt pullen, zodat jij er ook weer aan verder kan werken. Van alle repositories die op GitHub staan én openbaar zijn kun je de broncode clonen en er zelf mee aan de slag! Laten we eens een kijkje nemen op GitHub.

    !!! opdracht-meer "Tailor"

        Als je nog nooit op GitHub bent geweest dan kunnen de pagina's nogal intimiderend overkomen. De informatiedichtheid is nogal hoog. Na een paar bezoeken weet je meestal wel waar je dingen kunt vinden. David heeft een data-analyse app geschreven dat Tailor heet. Deze app wordt gebruikt bij natuurkundepractica voor studenten Medische natuurwetenschappen en Science, business and innovation. Interessant om eens te kijken wat je hierover kunt vinden op GitHub.

        1. Zoek de repository {{github}}`/davidfokkema/tailor` op [github.com](https://github.com) op.
        2. Je komt nu terecht op de hoofdpagina. Hier zie je een mappenstructuur met een aantal bestanden. Rechts daarvan staat een korte beschrijving onder het kopje _About_. Een uitgebreidere beschrijving vind je als je naar beneden scrolt onder _README_.
        3. Linksboven zie je een aantal tabbladen (_Code_, _Issues_, _Pull requests_, enzovoorts). Het tabblad _Code_ is de hoofdpagina met de mappenstructuur. Navigeer door de mappen, wat staat er op regel 14 van {{file}}`plot_tab.py`?
        4. Ga terug naar de hoofdpagina. In de regel boven de mappenstructuur vind je onder andere informatie over de commits (onder de groene knop met _Code_). Hoeveel commits zijn er gemaakt? Klik op _Commits_ en daarna op een aantal commit messages. Hoeveel regels zijn er bij een commit message weggehaald of bijgekomen?
        5. Je kunt per bestand bekijken wanneer die is aangepast en wat er is aangepast. Ga naar het bestand {{file}}`pyproject.toml` en klik rechtsboven op _History_. Wat is er aangepast in {{file}}`pyproject.toml` bij de commit <q>Release v2.0.0</q>? Je ziet ook welke bestanden nog meer zijn gewijzigd in deze commit, welk bestand is nog meer gewijzigd bij de commit <q>Release v2.0.0</q>?
        6. Ga terug naar de hoofdpagina. Welke versie van Tailor is als laatste gereleased? Kijk hiervoor onder _Releases_ aan de rechterkant.
        7. Je kent het misschien wel, dat je een app gebruikt maar dat het niet helemaal goed werkt (_bug_), of je hebt een idee hoe het nog beter kan worden (_enhancement_). Daarvoor is op GitHub het tabblad `Issues`. Hoeveel bugs zijn er gerapporteerd? En hoeveel enhancements?
        8. Als het jou gelukt is om een bug te fixen, of je hebt een super handige feature ontworpen, dan kan je de eigenaren van de repository vragen om jouw code te implementeren door een pull request te sturen. Ga naar het tabblad _Pull requests_, klik op _Closed_ en bekijk welke pull requests zijn geïmplementeerd.
        9. Het meest tabblad _Insights_ geeft je, tegen alle verwachtingen in, inzicht. Je kan bijvoorbeeld zien door hoeveel mensen er aan het project gewerkt wordt (_Contributors_). En kijk eens bij _Code frequency_, in welke periode is er het meest aan de code veranderd?
        10. Als je een repository goed/handig/slim/fijn vindt, kun je dit aangeven met een ster. Klik daarvoor rechtsboven op {{star}} _Star_.
        11. Dan tot slot die ene, meest in het oogspringende groene _Code_-knop op de hoofdpagina. Met die knop kun je de repository als ZIP-bestand downloaden of openen met GitHub Desktop.

## DNA-replicatie

Een klusje is pas echt stom als je het heel vaak achter elkaar moet doen. Computers zijn dan superhandig: je hoeft het klusje maar één keer te schrijven en te vertellen hoe vaak hij het moet uitvoeren.

Jullie hebben al eerder, handmatig, in DNA gezocht naar een fout die is ontstaan tijdens DNA-replicatie waarbij in de nieuwe streng soms een foutje kan ontstaan. We gaan allereerst een script schrijven dat het proces van DNA-replicatie nabootst.

!!! opdracht-basis "Replicatie"
    
    Maak een nieuw bestand met de naam {{file}}`dna_replication.py.`

    1. We beginnen met een stukje `#!py strand1 = "ATATAGAGTC"`. Print de letters van de bijbehorende tweede streng (Engels: _strand_), volgens de regels van DNA-replicatie, los onder elkaar. Dus, voor iedere letter uit strand1, als de letter een A is, print een T, als de letter een C is, print een G, enz.
    2. Het is duidelijker om beide strengen naast elkaar te printen. Als de letter uit strand1 een A is, print `A -- T`, enz.
    3. Ga naar GitHub Desktop en commit de code van deze opdracht.

!!! opdracht-meer "Vereenvoudigen"
    Je hebt nu waarschijnlijk een verzameling print-statements. Als je de vorm van de output wilt veranderen, bijvoorbeeld `A == T` wilt printen in plaats van `A -- T`, dan moet je dat op vier plekken aanpassen. Dat kan beter. Pas het script aan zodat hij hetzelfde doet, maar slechts één print-statement bevat. Tip: maak een nieuwe variabele aan voor de letter uit strand2. Commit je wijzigingen.

Nu we het proces van DNA-replicatie een beetje doorhebben, kunnen we onze kennis van wat de tweede streng zou _moeten_ zijn gebruiken om op zoek te gaan naar de fout.

!!! opdracht-basis "Vind de fout"

    Maak een nieuw bestand met de naam {{file}}`find_DNA_mistake.py`.

    1. Neem weer `#!py strand1 = "ATATAGAGTC"`. Daarnaast is `#!py strand2 = "AATATCGCAA"`. We willen nu weer een for-loop schrijven, maar hierbij de eerste letter uit strand1 vergelijken met de eerste letter uit strand2, en vervolgens de tweede letter uit strand1 vergelijken met de tweede letter uit strand2, enz. Dit betekent dat we een specifieke vorm van for-loop nodig hebben. Overleg welke.
    2. Schrijf code dat op zoek gaat naar _alle_ fouten in strand2. Voor iedere gevonden fout: print de positie van de fout (tel de eerste base als 1), print wat de fout is, en print wat de correcte base zou moeten zijn. Controleer met de hand of de output van je script klopt.
    3. Ga naar GitHub Desktop en commit de code van deze opdracht.

Fijn dat het werkt, maar fouten zoeken in zo’n klein stukje DNA kan natuurlijk veel sneller gewoon met de hand. Programmeren is pas nuttig als het zoeken met de hand veel langer duurt dan het programmeren. Dat is bijvoorbeeld het geval wanneer we een fout zoeken in 10.000 baseparen.

!!! opdracht-basis "Alle tijd van de wereld"
    Maak een schatting van hoe lang je daar met de hand mee bezig zou zijn.

Je hebt al een script dat de fout kan zoeken in kleine stukjes DNA. Maar je hoeft niet veel aan te passen om te zoeken in 10.000 baseparen. Je hoeft alleen maar de regels `#!py strand1 = ...` en `#!py strand2 = ...` aan te passen. Het kopiëren en plakken van 10.000 baseparen per streng is niet handig in een script. Daarom is het makkelijker om de gegevens op te slaan in bestanden en die bestanden in te lezen in je script. Download de gegevens voor beiden strengen [hier](data/strand1.txt) en [hier](data/strand2.txt). Gebruik de volgende regel om de data van strand1 in te lezen en te bewaren in de variabele:
```py
import pathlib
strand1 = pathlib.Path("strand1.txt").read_text().
```

!!! opdracht-basis "Zoek de speld in de hooiberg"
    Pas je script aan door gebruik te maken van bovenstaande regel om data in te lezen voor strand1, en ook voor strand2 en zoek de fouten in de 10.000 baseparen. Commit je wijzigingen.

!!! opdracht-meer "Meer condities"
    Als je code geneste if-statements bevat, zoals:
    ```py
    if ...:
        if ...:
            ...
    ```
    pas je code dan aan met `and` of `or` zodat je in totaal maar vier if-statements nodig hebt (in plaats van acht).
    
!!! opdracht-meer "Repareer de mutatie"
    Bekijk de volgende code, waarbij een mutatie in de vierde base wordt gerepareerd door stukjes DNA aan elkaar te plakken:
    ```py
    # DNA with mutation in base 4
    strand = "ATCGGA"
    
    # print base 4
    print(strand[3])
    # 'G'

    # Built new strand with the original base T restored
    fixed_strand = strand[:3] + "T" + strand[4:]
    print(fixed_strand)
    # 'ATCTGA'
    ```
    Begrijp je wat er gebeurt in de code? Er is wel een tekortkoming: in deze code staat de positie van de mutatie (base 4) in het script. De correcte base (T) staat ook keihard in het script. Voeg functionaliteit aan jouw bestaande code toe zodat je ongeveer hetzelfde doet, maar dan op basis van wat je script gevonden heeft: welke base en wat zou de correcte base moeten zijn? De voorbeelcode werkt maar in één specifiek geval. Zorg dat jouw code in alle gevallen werkt.

## Even herhalen, maar dan anders

We hebben 10.000 baseparen gecontroleerd op mutaties. Dat was een kleine taak, die we _heel vaak_ hebben uitgevoerd. We wisten van tevoren _hoe_ vaak: namelijk één keer voor ieder basepaar in het stuk DNA dat we bekeken hebben. Soms wil je echter een taak uitvoeren _zonder_ dat je van tevoren weet hoe lang. Je wilt de taak _blijven uitvoeren terwijl ..._ De letterlijke vertaling van _terwijl_ is _while_ en we gaan in de volgende opdrachten aan de slag met `#!py while`-loops.

Om dit te oefenen gaan we voor het gemak even terug naar ons script {{file}}`name_and_age.py`.

!!! opdracht-basis "_Hoe_ oud ben je?"

    In het script {{file}}`name_and_age.py` vragen we naar de leeftijd van de gebruiker. Maar... wat als die een onzin-leeftijd geeft? Wat als de gebruiker vertelt dat zij $-20$ jaar oud is? Als dat gebeurt wil je graag nogmaals de leeftijd blijven vragen, en dat _blijven_ doen terwijl de leeftijd onder nul is. Is de leeftijd nul of hoger, dan gaat het programma door. Voeg een `#!py while`-loop toe aan je programma zodat je altijd een leeftijd krijgt die positief is. Zorg eerst dat het werkt, en denk dan na of er andere oplossingen mogelijk zijn en kies de handigste.

!!! opdracht-basis "Stop-conditie"

    Regelmatig heb je voor een taak input nodig van de gebruiker en wil je de taak blijven herhalen. Je wilt de taak _altijd_ blijven uitvoeren. Als je je laptop openklapt vul je je wachtwoord in en ga je aan het werk. Niet drie keer, niet vijf keer, maar _altijd_. Het zou raar zijn als je laptop na de vijfde keer besluit volledig uit te schakelen omdat het wel mooi is geweest voor vandaag.

    Je kunt een `#!py while`-loop gebruiken om iets altijd te blijven doen door een conditie te kiezen die altijd waar is.

    1. Pas je script {{file}}`name_and_age.py` aan zodat hij altijd blijft herhalen. Hij vraagt je naam, je leeftijd, geeft output en herhaalt door opnieuw je naam te vragen.
    1. Echt _voor altijd_ is niet handig. Breek de `#!py while`-loop af wanneer iemand als naam "STOP" intypt.

[^git]: GitHub is een gebruiksvriendelijke laag over Git, het eigenlijke versiebeheersysteem. Git wordt tegenwoordig door bijna iedereen gebruikt of ondersteund. Git is ontwikkeld door Linus Torvalds als alternatief voor het commerciële systeem dat gebruikt werd voor de ontwikkeling van de Linux kernel.[@git] Het begon als een zeer eenvoudig &mdash; en volkomen ongebruiksvriendelijk &mdash; programma. Later is het in een veel gebruiksvriendelijker jasje gestoken. Relatief dan: je moet nog steeds ingewikkelde commando's intypen om iets voor elkaar te krijgen.
[^branches]: Een branch is een splitsing in je versiegeschiedenis. Je kunt het gebruiken om over een langere tijd een grote wijziging uit te testen, terwijl je af en toe heen en weer springt tussen je main branch en de nieuwe branch. Commits in de verschillende branches blijven gescheiden. Later kun je ervoor kiezen om de wijzigingen in de nieuwe branch te _mergen_ met je main branch, maar dat hoeft niet.
[^pro-account]: [https://github.com/education/students](https://github.com/education/students)
[^kabouter]: Dit kan echt gebeuren en is dus geen grap. Zo worden de zaalcomputers om privacy- en efficiëntieredenen met enige regelmaat automatisch opgeschoond. Je bent dan alles kwijt. Ok, het zijn waarschijnlijk geen kabouters &mdash; dat is wel een grap, denken we.
[^venvs-sync]: Als je met Pythonprojecten werkt dan kun je helaas gemakkelijk in de situatie komen waar je problemen krijgt met de synchronisatie. Met de instructies in deze cursus kun je dat voorkomen.
[^vscode-submap]: Als je dat doet dan weet Visual Studio Code niet welke bestanden allemaal bij je project horen en draait hij de code niet in je projectmap, maar in de submap. Je code kan dan errors geven als die bestanden op een andere plek zoekt.
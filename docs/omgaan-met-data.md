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

## Versiebeheer

Zodra je scripts wat ingewikkelder worden, begin je tegen heel praktische problemen aan te lopen. Het werkt _nu_, maar je wilt een flinke aanpassing gaan doen. Werkt het dan straks nog wel? Hoe ingewikkelder het script, hoe ingewikkelder de wijzigingen en hoe minder het vertrouwen dat het in één keer gaat lukken. Misschien heb je wel eens de ervaring gehad dat een wijziging maar niet wilde werken en dat je niet goed meer wist wat je precies had veranderd ten opzichte van toen het nog _wel_ werkte. Veel mensen hebben daarom de neiging om naast een {{file}}`script.py` een {{file}}`script-v1.py`, {{file}}`script-v2.py`, enzovoorts aan te maken. Soms zelfs een {{file}}`script-eindversie.py` en met wat pech dan toch nog een {{file}}`script-eindversie-definitief.py`. Niet heel fijn. Je ziet dan nog steeds niet goed wat er veranderd is (dat blijft naast elkaar leggen en zoeken) en je map loopt vol met overbodige scripts. Dit kan beter&hellip;\ met versiebeheer!

Versiebeheer (Engels: _version control_) stelt je in staat om af en toe een momentopname te maken van al je bestanden in een bepaalde map, inclusief alle submappen. Dit doe je niet na iedere regel code, maar bijvoorbeeld wel als je een stukje code af hebt en na het testen weet dat het werkt. Zo'n momentopname heet een _commit_. Hoe vaak je commit is aan jou; maar wacht niet te lang &mdash; anders is het geen versiebeheer meer.

Je versiebeheersysteem geeft ondertussen duidelijk al je wijzigingen weer ten opzichte van de laatste commit. Ook kun je de wijzigingen tussen oudere versies bekijken. Alles is relatief: je kunt zien wat er veranderd is tussen twee weken terug en gisteren, of tussen gisteren en vandaag; iedere commit kun je vergelijken met willekeurig iedere andere commit. Heb je iets verprutst en wil je een oude versie terughalen? Prima! Commit die ook, dan kun je zelfs dat weer terugdraaien. Je verliest zo nooit meer je werk. En stukmaken mag![^stuk]

### Git

Ruim tien jaar geleden werden er nog vele concurrerende systemen gebruikt. Die tijd is grotendeels voorbij. Eén van de nieuwste systemen, Git,[^git_footnote] wordt tegenwoordig door bijna iedereen gebruikt of ondersteund. Git is ontwikkeld door Linus Torvalds als alternatief voor het commerciële systeem dat gebruikt werd voor de ontwikkeling van de Linux kernel.[@git] Het begon als een zeer eenvoudig &mdash; en volkomen ongebruiksvriendelijk &mdash; programma. Later is het in een veel gebruiksvriendelijker jasje gestoken.

Git werkt in principe via de command-line. Je geeft opdrachten in de map waar je broncode staat: toevoegen van wijzigingen aan de _staging area_, bekijken van de meest recente wijzigingen, committen van je code, teruggaan en werken met oudere versies, aanmaken van _branches_,[^branches] je wijzigingen uploaden naar internet, enzovoorts. Het geheel van de map met broncode en de versiegeschiedenis wordt een _repository_ genoemd.

In deze cursus zul je gebruik maken van een grafische applicatie die eenvoudiger werkt. Je kunt daarna &mdash; als je dat wilt &mdash; de stap maken naar de command-line, waarmee je veel meer mogelijkheden tot je beschikking krijgt. Zie het boek _Pro Git_[@gitpro] voor meer informatie over Git en het gebruik via de command-line.

### GitHub

Git is een _distributed version control system (DVCS)_, wat wil zeggen dat er geen centrale server hoeft te zijn. Je kunt volledig offline werken in je eigen repository en je wijzigingen af en toe committen. Als je daar zin in hebt kun je je wijzigingen naar een collega sturen (_pushen_) en je kunt een collega toestemming geven om de wijzigingen op te halen (_pullen_). Je bouwt dan aan één grote versiegeschiedenis met kopieën op meerdere computers. Je bent zo volledig onafhankelijk van bedrijven die servers in de lucht houden of bepalen wie er wel en niet toegang krijgt. Dat is fijn, maar een centrale plek om repositories neer te zetten heeft weer het grote voordeel dat je de wereld kunt laten zien wat voor moois je gemaakt hebt én het vermakkelijkt samenwerking. Daarnaast is iedereen uit je team up-to-date als iedereen regelmatig commits pusht naar een centrale server.

Er zijn tegenwoordig veel websites die een plek bieden voor Git repositories. De bekendste zijn GitHub, GitLab, Bitbucket en SourceForge. GitHub, aangekocht door Microsoft, is op dit moment het bekendste en grootste platform. Veel bekende softwareprojecten vinden daar hun thuis.

In deze cursus ga je werken met GitHub. Je moet hiervoor wel een (gratis) account aanmaken. Als student kom je ook nog in aanmerking voor een educatiekorting op een pro-account.[^pro-account] Je betaalt dan nog steeds niets.

!!! opdracht-basis "Account aanmaken"

    Ga naar [https://github.com/](https://github.com/) en klik op `Sign up for GitHub`. Maak een account aan onder je _privé-emailadres_. Op deze manier blijf je toegang houden tot je account ook nadat je afgestudeerd bent.

    !!! info

        Mogelijk heb je eerder al eens een account aangemaakt bij GitHub, bijvoorbeeld bij de cursus Project natuurkunde/sterrenkunde 1. Maak voor ECPC dan ook gebruik van dit account. Controleer wel nog even of je voor dit account je _privé-emailadres_ gebruikt.

### GitHub Desktop

Om het programmeurs makkelijker te maken met GitHub te werken heeft GitHub een desktopapplicatie ontwikkeld met de naam GitHub Desktop. Je gaat GitHub Desktop gebruiken om een repository te maken van de map met de oefenopdrachten.

!!! opdracht-basis "GitHub Desktop installeren"

    Ga naar [https://desktop.github.com/download/](https://desktop.github.com/download/) om GitHub Desktop te downloaden. Zoek daarna het gedownloade bestand op en installeer de applicatie. Log nu in met jouw account.

    !!! info

        Mogelijk heb je eerder al eens GitHub Desktop geïnstalleerd. Controleer dan of je met het juiste account ingelogd bent. Ga hiervoor naar **Accounts** via het dropdownmenu **File** > **Options**.

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

### Commit

Alle wijzigingen aan bestanden in de repository kun je vanaf nu bijhouden door regelmatig een commit te maken. Met een commit maak je als het ware een snapshot van alle bestanden en hang je daar een labeltje aan.
Dit kan in GitHub Desktop, maar ook direct vanuit Visual Studio Code. Elke commit geef je een begeleidend schrijven mee, een _commit message_. Je hoopt dat jij &mdash; maar ook je collega &mdash; na het lezen van de commit message snel begrijpt wat er veranderd is én waarom. Wanneer je bepaalde wijzigingen ongedaan wilt maken, kan je door het lezen van de commit messages snel vinden bij welke commit je dan moet zijn. En wanneer je je applicatie gaat uitbrengen op GitHub, kun je de commit messages gebruiken om snel op te sommen wat de nieuwste versie van jouw app kan!

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
    8. Onder de lijst met gewijzigde bestanden vind je twee invulvelden. Een smal veld voor een titel en een groot veld voor een uitgebreide beschrijving (_Description_). In het veld voor een titel staat in lichtgrijs een nietzeggende commit, bijvoorbeeld _Update test.py_. Schrijf daar een nuttige commit message. Dus niet: <q>opdracht: commit</q>. Maar meer zoiets als: <q>feat: lookup port name for device</q>. Houd de titel in de commit message kort en krachtig. Een uitgebreidere beschrijving kun je kwijt in het grote veld.
    9. Klik op _Commit to main_. Gefeliciteerd! {{feesttoeter}} Je hebt je eerste commit gedaan!

In GitHub Desktop zie je nu bij _History_ de commit staan, met in één oogopslag alle wijzigingen.

!!! info

    Als je wilt opzoeken hoe iets werkt bij GitHub Desktop, kijk dan in de documentatie: [https://docs.github.com/en/desktop](https://docs.github.com/en/desktop).

!!! opdracht-basis "Push en pull"

    De repository {{github}}`BiomedicalComputing` bestaat alleen nog maar op de computer. Het kan fijn zijn om de repository ook in de cloud te hebben op [github.com](https://github.com/). Het geeft de mogelijkheid je code op andere computers binnen te halen en te delen met anderen. Bovendien ben je dan beschermd tegen computerkabouters die 's nachts documenten verplaatsen of wissen.[^kabouter]

    In GitHub Desktop vind je een knop `Publish repository; Publish this repository to GitHub`. Als je daar op drukt kun je nog een andere naam aan de repository geven (deze naam bepaalt de url op [github.com](https://github.com/)), een beschrijving toevoegen en aangeven of de code privé moet zijn. Daarna klik je op de blauwe knop `Publish repository`. Als je nu naar [github.com](https://github.com) gaat zie je bij jouw repositories de zojuist gepubliceerde repository staan.

    Om je wijzigen ook in de cloud op te slaan kun je commits `pushen` naar [github.com](https://github.com/) met de knop `Push origin`. Als je op een andere computer gaat werken kun je de repository vanuit de cloud naar de computer halen door op `Fetch origin` te klikken en daarna op `Pull origin`.

### Repositories op GitHub

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

[^stuk]: Stukmaken mag, maar het terughalen van een oude versie is niet met één druk op de knop gebeurd. Vraag om hulp als je terug wilt naar een oude versie, wij helpen je graag!
[^git_footnote]: <https://initialcommit.com/blog/How-Did-Git-Get-Its-Name>
[^branches]: Een branch is een splitsing in je versiegeschiedenis. Je kunt het gebruiken om over een langere tijd een grote wijziging uit te testen, terwijl je af en toe heen en weer springt tussen je main branch en de nieuwe branch. Commits in de verschillende branches blijven gescheiden. Later kun je ervoor kiezen om de wijzigingen in de nieuwe branch te _mergen_ met je main branch, maar dat hoeft niet.

[^pro-account]: [https://github.com/education/students](https://github.com/education/students)

    [^kabouter]: Dit kan echt gebeuren en is dus geen grap. Zo worden de zaalcomputers om privacy- en efficiëntieredenen met enige regelmaat automatisch opgeschoond. Je bent dan alles kwijt. Ok, het zijn waarschijnlijk geen kabouters &mdash; dat is wel een grap, denken we.

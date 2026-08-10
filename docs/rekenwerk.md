# Rekenwerk

In de vorige sessie heb je al gemerkt dat een computer heel geschikt is om een eenvoudig klusje dat 10.000 keer herhaald moet worden uit te voeren zodat jij dat niet zelf hoeft te doen. Een ander groot voordeel is dat een computer kan rekenen. _To compute_ betekent niet voor niets _berekenen._ Rekenwerk kan natuurlijk ook met de hand, maar is niet altijd het leukste klusje om te doen. Daarnaast is het mogelijk dat er ergens een fout(je) insluipt. Zeker als bepaald rekenwerk meer dan eens gedaan moet worden, is het fijn om dit te programmeren.

Het belangrijkste wat je moet weten is hoe je in Python moet optellen, aftrekken, vermenigvuldigen, delen en machtsverheffen, en hoe je van strings een integer of een floating point number kunt maken met `#!py int()` en `#!py float()`.

## Stralingsveiligheid

Ioniserende straling is gevaarlijk, maar kan ook heel nuttig zijn bij de behandeling van tumoren of bij diagnostiek. Het is dan wel belangrijk om ervoor te zorgen dat patiënten en zorgpersoneel zo min mogelijk straling ontvangen. Daarom zal een tandarts(assistent) ook altijd kort de behandelruimte verlaten op het moment dat er een röntgenfoto van je gebit wordt gemaakt. Doen ze dat niet, dan ontvangen ze de straling van tientallen, zo niet honderden, röntgenfoto’s per jaar. Ook bij het produceren van radioactieve isotopen of bij het doen van wetenschappelijk onderzoek kunnen medewerkers blootgesteld worden aan straling. Bij alfa- en bètastraling is het niet heel ingewikkeld om de medewerkers af te schermen. Bij gammastraling is dat wél een probleem: deze straling heeft een groot doordringend vermogen en is moeilijk af te schermen. Daarom worden regelmatig berekeningen gemaakt om de ontvangen equivalente dosis (in Sievert) te bepalen. Op deze manier kan in de gaten gehouden of een medewerker niet teveel straling ontvangt.

Omdat de exacte hoeveelheid ontvangen straling wordt bijgehouden met badges die de medewerkers op hun lichaam dragen is het vaak voldoende om voor de berekeningen gebruik te maken van een vuistregel:

\begin{equation}
H = \gamma \frac{A t}{r^2},
\end{equation}

Met de ontvangen equivalente dosis $H$, de gammaconstante van de bron $\gamma$, de activiteit van de bron $A$, de blootstellingstijd $t$ en de afstand tot de bron $r$.

!!! opdracht-basis "Stralingsveiligheid"

    In deze opdracht ga je een rekentool ontwikkelen die stralingsmedewerkers kunnen gebruiken om in te schatten of ze veilig kunnen werken. Voor cesium-137, een veelgebruikte radioactieve isotoop, is de gammaconstante gelijk aan $0.084 \, \mu\text{Sv} \, \text{m}^2 \, \text{MBq}^{-1} \, \text{h}^{-1}$. Tip: als je in formule (1) de eenheden meter, megabecquerel en uur gebruikt vallen de eenheden weg en is je antwoord vanzelf in microsievert.

    1. Bereken de ontvangen stralingsdosis als je gedurende twee uur werkt met een bron met een activiteit van 2 MBq op een afstand van 4 m. Gebruik in de berekening de formule met letters en vul niet de getallen direct in. Bovenaan je script definieer je dan de waardes, bijvoorbeeld `#!py A = ...`. Print het resultaat van je berekening. Commit je code.

    2. Nadat je de dosis print doe je een aantal checks en print je, zonodig, nog wat meer informatie. Jaarlijks ontvang je via natuurlijke weg ongeveer 2 mSv aan straling. Als je volgens je berekening méér ontvangt wil je dat wel weten. Meer dan 2 Sv (dus 2000 mSv) is dodelijk. Minder dan 1 mSv mag je als veilig beschouwen. Commit.

    3. Pas nu je script aan zodat de getallen voor activiteit, afstand en verblijfsduur niet vast gedefinieerd zijn bovenaan je script, maar aan de gebruiker worden gevraagd. Commit.

!!! opdracht-meer "Gammaconstantes"

    Onze rekentool gaat nu altijd uit van cesium-137. Pas je script aan zodat de gebruiker gevraagd wordt naar de gammaconstante, maar zorg ervoor dat als de gebruiker niets invult dat het script dan uitgaat van de gammaconstante van cesium-137. Vertel ook aan de gebruiker dat de gammaconstante optioneel is en wat de standaardwaarde is.

## Nierfunctie

Je nieren zijn een belangrijk orgaan. Je hebt er twee, en kunt er één missen, maar kunt absoluut niet zonder. Dit orgaan haalt afvalstoffen uit het bloed die je vervolgens uitplast. Mensen die een heel slechte nierfunctie hebben moeten gedialyseerd worden waarbij een machine gedurende een aantal uur de afvalstoffen uit het bloed haalt. Dit moet dan vaak zo’n drie keer per week. Als een arts vermoedt dat er mogelijk iets mis is met je nieren, kan je nierfunctie worden gemeten.

De eGFR-meting (_estimated Glomerular Filtration Rate_) meet de hoeveelheid kreatine in je bloed. Kreatine is een afvalproduct van de spieren en je nieren filteren dat uit het bloed, tenzij ze niet goed meer functioneren. Hoeveel kreatine er normaal gesproken in het bloed zit (en dus mág zitten) verschilt per persoon afhankelijk van de hoeveelheid spiermassa. Dit kan geschat worden op basis van het biologisch geslacht en de leeftijd van de patiënt. Aan de hand van de meting van de kreatineconcentratie, geslacht en leeftijd kan de glomerulaire filtratiesnelheid als schatting worden berekend aan de hand van de volgende empirische formules:

\begin{equation}
\text{eGFR} = 144 \cdot \left( \frac{\text{cr.conc.}}{62} \right)^{-0.329} \cdot 0.993^{\text{age}} \quad (\text{vrouw, cr.conc. } \leq 62\, \mu\text{mol}/\text{L})
\end{equation}

\begin{equation}
\text{eGFR} = 144 \cdot \left( \frac{\text{cr.conc.}}{62} \right)^{-1.209} \cdot 0.993^{\text{age}} \quad (\text{vrouw, cr.conc. } \gt 62\, \mu\text{mol}/\text{L})
\end{equation}

\begin{equation}
\text{eGFR} = 141 \cdot \left( \frac{\text{cr.conc.}}{80} \right)^{-0.411} \cdot 0.993^{\text{age}} \quad (\text{man, cr.conc. } \leq 80\, \mu\text{mol}/\text{L})
\end{equation}

\begin{equation}
\text{eGFR} = 141 \cdot \left( \frac{\text{cr.conc.}}{80} \right)^{-1.209} \cdot 0.993^{\text{age}} \quad (\text{man, cr.conc. } \gt 80\, \mu\text{mol}/\text{L})
\end{equation}

Met bovenstaande factoren wordt de eenheid van de eGFR de mL/min/1,73 m$^2$. Een beetje vreemde eenheid waarbij het lichaamsoppervlak gestandaardiseerd wordt op 1,73 m$^2$, en dat vaak ook als percentage wordt gepresenteerd. Dus als je een eGFR vindt van 83 (mL/min/1,73 m$^2$) dan wordt vaak gezegd dat je nieren nog voor 83 % functioneren.

Artsen gebruiken verschillende categorieën (stadia) om de nierfunctie aan te geven:

| Stadium | Beschrijving                                                                         |
| ------- | ------------------------------------------------------------------------------------ |
| G1      | normale of hoge nierfunctie; de nieren werken voor meer dan 90%                      |
| G2      | mild afgenomen nierfunctie; de nieren werken voor 60 - 89%                           |
| G3a     | mild tot matig afgenomen nierfunctie; de nieren werken voor 45 - 59%                 |
| G3b     | matig tot ernstig afgenomen nierfunctie; de nieren werken voor 30 - 44%              |
| G4      | ernstig afgenomen nierfunctie; de nieren werken voor 15 - 29%                        |
| G5      | zeer ernstig afgenomen nierfunctie (nierfalen); de nieren werken voor minder dan 15% |

!!! opdracht-basis "Nierfunctie eGFR"

    1. Schrijf een script waarbij je bovenin je script variabelen definieert voor geslacht, leeftijd en de kreatineconcentratie. Bereken vervolgens de eGFR. Tip: gebruik `#!py if...else...`-statements om de goede formule te gebruiken. Print de gevonden waarde.
    2. Breid je script uit zodat ook het stadium (bijvoorbeeld G2), en een beschrijving van dat stadium (bijvoorbeeld "mild afgenomen nierfunctie") worden gegeven.
    3. Vraag de gebruiker om de waardes van de variabelen in plaats van dat je ze definieert in je script. Test met een paar verschillend inputs.

## UV-Vis spectroscopie

!!! info "Practicum bio-analytische chemie (jaar 1, periode 5)"

    _UV-Vis-spectroscopie is een veelgebruikte detectietechniek om de concentratie van opgeloste stoﬀen te bepalen. De methode berust op de absorptie van licht bij specifieke golflengten, die karakteristiek zijn voor een bepaalde stoﬀen. Volgens de wet van Lambert-Beer is deze absorptie recht evenredig met de concentratie, waardoor de concentratie van een stof in oplossing kan worden bepaald. In dit experiment wordt deze techniek toegepast om de hoeveelheid vitamine B12 in een vitaminepil te bepalen. Hiervoor wordt een kalibratielijn opgesteld met een standaardoplossing van vitamine B12, waarmee de concentratie in het monster kan worden berekend._

    -- Handleiding UV-Vis experiment, practicum bio-analytische chemie voor MNW, Vrije Universiteit

Naast bepalen hoeveel vitamine er écht zit in een voedingssupplement kun je met behulp van deze techniek ook vragen beaantwoorden als _Hoeveel cafeïne zit er in een energy drink?_, of _welke zonnebrand heeft een hogere spf-factor?_. Om nauwkeurig te kunnen bepalen wat de concentratie is van een bepaalde stof in een bepaald oplosmiddel moeten wel een paar stappen worden doorlopen.

In het experiment schijn je licht door je monster heen. De hoeveelheid licht die geabsorbeerd wordt is dan een maat voor de hoeveelheid stof. Daarvoor moet je wel weten hoeveel licht er normaal gesproken geabsorbeerd wordt door die stof. Daarvoor maak je heel nauwkeurig een oplossing met een bekende hoeveelheid stof (de _stockoplossing_) en die ga je vervolgens een aantal keer verdunnen zodat je veel verschillende concentraties hebt, van hoog naar laag, een _verdunningsreeks_. Die meet je allemaal door en zo kun je een ijklijn of kalibratiecurve maken. Als laatste meet je de onbekende hoeveelheid door en dan kun je op de ijklijn aflezen hoeveel stof er in de onbekende oplossing zit.

### Pipetteerschema voor een verdunningsreeks

Om een verdunningsreeks te maken moet je een aantal keer een bepaalde hoeveelheid stockoplossing vermengen met een bepaalde hoeveelheid oplosmiddel. Bepalen hoeveel dat precies moet zijn is een rekenwerkje dat je goed uit moet voeren. Omdat tijdens het verdunnen de _hoeveelheid stof_ niet verandert, en omdat de hoeveelheid gelijk is aan de concentratie maal het volume, kun je zeggen:
\begin{equation}
C_1 V_1 = C_2 V_2,
\end{equation}
met $C_1$ de concentratie in de stockoplossing, $V_1$ de hoeveelheid stockoplossing die je neemt, $C_2$ de concentratie in de verdunde oplossing en $V_2$ de hoeveelheid verdunde oplossing. Meestal wil je bepalen hoeveel stockoplossing $V_1$ je nodig hebt voor een bepaalde verdunning, en hoeveel oplosmiddel daar bij moet ($V_2 - V_1$). De _verdunningsfactor_ $D$ wordt dan gegeven door:
\begin{equation}
D = \frac{C_1}{C_2}.
\end{equation}

!!! opdracht-basis "Pipetteerschema"

    1. Stel je hebt een stockoplossing van 0.10 mol/L. Bereken, met de hand, hoeveel van deze oplossing je nodig hebt om 5.0 mL oplossing te maken die een concentratie heeft van 0.025 mol/L? Hoeveel verdund is dat? Hoeveel oplosmiddel heb je dan nog nodig?
    2. Schrijf nu een script die deze berekening voor je uitvoert. Denk er weer aan om de formule te programmeren met grootheden, niet direct met getallen. Definieer de waardes van de grootheden weer bovenaan je script. Vergeet niet om je antwoord duidelijk te printen: verdunningsfactor, benodigde hoeveelheid stockoplossing, benodigde hoeveelheid oplosmiddel.
    3. Pas je script aan zodat hij in één keer een hele verdunningsreeks maakt. Tip: definieer een lijst van concentraties en gebruik een for-loop om je berekening voor iedere concentratie uit te voeren. Bepaald de verdunningsreeks voor concentraties 0.025, 0.020, 0.015, 0.010, 0.005 en 0.000 mol/L.
    4. Het kan soms handig zijn om de resultaten van je berekeningen te bewaren voor later, en pas op een later moment de resultaten te printen, of op te slaan in een bestand, of op een andere manier te gebruiken. Om dat te oefenen passen we ons script aan zodat de resultaten eerst worden bewaard en pas later worden geprint. Maak een lijst aan voor iedere grootheid die je wilt berekenen en bewaar het resultaat in die lijst, maar print niets binnen de for-loop. Als allerlaatste onderdeel van je script print je in één keer de resultaten.
    
!!! opdracht-meer "Tabellen printen"

    Een mooie manier om de resultaten weer te geven is met een tabel. Je kunt als eerste een koptekst printen (`kolom 1  kolom 2`), vervolgens een lijn met streepjes (`-------`), en dan een for-loop waarbij je een index gebruikt om de eerste waarde voor kolom 1, de eerste waarde voor kolom 2, enz. te printen, regel voor regel. Om alles netjes te krijgen moet je dan wel zorgen dat de getallen netjes onder elkaar komen. Dat doe je door Python te vertellen hoeveel ruimte een getal moet innemen. Dat gaat veruit het makkelijkst met f-strings. De regel
    ``` py
    print(f"{number1:7.2f}  {number2:7.2f}")
    ```
    betekent dat de getallen in totaal zeven karakters mogen innemen (de lengte van de tekst `kolom #`) en dat je, binnen die zeven karakters, twee cijfers achter de komma wilt. De `f` betekent dat je wilt dat Python het getal behandelt als een floating point number, ofwel een kommagetal.

    Pas je script voor het pipetteerschema aan zodat de resultaten worden weergegeven in een tabel. Schrijf een goede koptekst, tel de breedte van de kolommen en maak een mooi print-statement zodat alles netjes wordt uitgelijnd.

!!! opdracht-meer "Ritsen"

    Loopen met een index voelt misschien een beetje omslachtig aangezien je in Python ook direct kunt loopen over de elementen in een lijst. Je kunt zeggen `#!py for element in my_list: ...` in plaats van `#!py for idx in range(len(my_list)): ...`. Best handig, maar hoe doe je dat wanneer je wilt loopen over de elementen uit meerdere lijsten tegelijk? Dat kan met `#!py zip()`, als volgt:
    ``` py
    fruits = ["apple", "pear", "melon"]
    prices = [0.99, 1.99, 2.99]
    amounts = [10, 5, 2]
    for fruit, price, amount in zip(fruits, prices, amounts):
        print(fruit, price, amount)
    # apple 0.99 10
    # pear 1.99 5
    # melon 2.99 2
    ```
    Pas het script voor je pipetteerschema aan zodat je de tabel print met gebruik van `#!py zip()`.

!!! opdracht-basis "Pipetteerschema met input"

    Ook hier kan het handig zijn om een mooi script te schrijven waar de gebruiker zelf de concentraties kan intypen. Vraag eerst hoeveel concentraties de gebruiker wil maken en schrijf dan een for-loop die de concentraties één voor één vraagt en toevoegt aan de lijst met concentraties. Vergeet niet ook de concentratie van de stockoplossing te vragen, en de hoeveelheid oplossing die je wilt maken in je pipet. Daarna voer je de rest van je script uit.

!!! opdracht-meer "Handiger input"

    Nóg handiger is als je de gebruiker niet van tevoren hoeft te vragen hoeveel concentraties die wil hebben. Vraag de gebruiker om alle concentraties in één keer in te typen, gescheiden door een komma. Dus bijvoorbeeld: `0.025, 0.020, 0.015, 0.010, 0.005, 0`. Net zoals een list in Python de method `#!py .append()` kent, kun je in Python voor een string `#!py split()` gebruiken. Geef tussen de haakjes aan wat het scheidingsteken is (de `#!py ","`) en Python splitst de string en geeft je een lijst van de verschillende waardes. Dit zijn wel dan nog strings en je moet nog een for-loop schrijven om die te vertalen naar floats. Als dat lukt heb je wel iets heel moois gemaakt!

### Kalibratiecurve

Als je de verdunningsreeks gemaakt en doorgemeten hebt, wil je de kalibratiecurve opstellen. Neem de volgende metingen:

| concentration | absorption |
|---------------|------------|
| 0.025         | 0.61       |
| 0.02          | 0.45       |
| 0.015         | 0.37       |
| 0.01          | 0.23       |
| 0.005         | 0.13       |
| 0.0           | 0.0        |

Aangezien de absorptie recht evenredig is met de hoeveelheid stof (en dus de concentratie) verwacht je een lineair verband, met mogelijk een correctie (asafsnijding):
\begin{equation}
S = ac_s + b,
\end{equation}
met het absorbtiesignaal $S$, de concentratie van het monster $c_s$, en met de helling $a$ en asafsnijding $b$ de kalibratieparameters.

!!! opdracht-basis "IJken van de UV-Vis spectrometer"

    1. Bepaal, met behulp van Tailor, de kalibratieparameters. Voer daartoe bovenstaande metingen in en fit aan formule (8). 
    2. Bepaal, met behulp van je ijking, de concentratie stof in een onbekend monster met een absorptiesignaal van 0.41.

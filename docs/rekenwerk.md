
# Rekenwerk

In de vorige sessie heb je al gemerkt dat een computer heel geschikt is om een eenvoudig klusje dat 10.000 keer herhaald moet worden uit te voeren zodat jij dat niet zelf hoeft te doen. Een ander groot voordeel is dat een computer kan rekenen. *To compute* betekent niet voor niets *berekenen.* Rekenwerk kan natuurlijk ook met de hand, maar is niet altijd het leukste klusje om te doen. Daarnaast is het mogelijk dat er ergens een fout(je) insluipt. Zeker als bepaald rekenwerk meer dan eens gedaan moet worden, is het fijn om dit te programmeren.

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

| Stadium | Beschrijving |
| --- | --- |
| G1 | normale of hoge nierfunctie; de nieren werken voor meer dan 90% |
| G2 | mild afgenomen nierfunctie; de nieren werken voor 60 - 89% |
| G3a | mild tot matig afgenomen nierfunctie; de nieren werken voor 45 - 59% |
| G3b | matig tot ernstig afgenomen nierfunctie; de nieren werken voor 30 - 44% |
| G4 | ernstig afgenomen nierfunctie; de nieren werken voor 15 - 29% |
| G5 | zeer ernstig afgenomen nierfunctie (nierfalen); de nieren werken voor minder dan 15% |    

!!! opdracht-basis "Nierfunctie eGFR"

    1. Schrijf een script waarbij je bovenin je script variabelen definieert voor geslacht, leeftijd en de kreatineconcentratie. Bereken vervolgens de eGFR. Tip: gebruik `#!py if...else...`-statements om de goede formule te gebruiken. Print de gevonden waarde.
    2. Breid je script uit zodat ook het stadium (bijvoorbeeld G2), en een beschrijving van dat stadium (bijvoorbeeld "mild afgenomen nierfunctie") worden gegeven.
    3. Vraag de gebruiker om de waardes van de variabelen in plaats van dat je ze definieert in je script. Test met een paar verschillend inputs.

## Pipetteerschema


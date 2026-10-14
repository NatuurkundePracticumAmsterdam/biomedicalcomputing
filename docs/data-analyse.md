# Data-analyse

In het hoofdstuk farmacokinetiek hebben we van twee medicijnen bekeken hoe ze worden opgenomen en afgebroken in het menselijk lichaam. We zijn ervan uitgegaan dat de medicijnen zich zeer snel verdeelden over het lichaam en vervolgens langzaam werden afgebroken volgens een envoudig exponentieel model met een halfwaardetijd. Als je wilt weten of dat klopt dan zul je metingen moeten doen van de concentratie van het medicijn in het bloed van een patiënt. Je moet dan op gezette tijden een buisje bloed afnemen en dat analyseren. En als je de concentraties hebt bepaald en uitgezet in een grafiek dan zul je moeten fitten aan het exponentiële model om te kijken of de datapunten en het model goed overeenkomen. Dit is dezelfde werkwijze als die je hebt toegepast op het natuurkundepracticum. Daar voerde je een experiment uit en fitte je de metingen aan een natuurkundig model om te kijken of die goed overeen kwamen en zo ja, wat de waardes van de modelparameters waren. Jullie hebben dat gedaan met Tailor. Maar dat kan natuurlijk ook met Python! Dat is meer typewerk maar geeft je veel meer vrijheid over wat je _precies_ gedaan wilt krijgen.

## Lidocaïne

Lidocaïne is een medicijn dat zenuwgeleiding tijdelijk vermindert of blokkeert en is vooral werkzaam op pijnprikkels. Het is daardoor zeer geschikt als middel om (lokaal) te verdoven, en wordt soms bij ernstige zenuwpijn direct in de bloedbaan ingebracht. In die situatie verspreidt het zich door het hele lichaam en wordt opgenomen door lichaamsweefsel. Om te controleren of het afbraakmodel waarmee je eerder gewerkt hebt ook op dit medicijn van toepassing is, hebben we een dosis van 100 mg lidocaïne direct in de bloedbaan gebracht van een volwassen patiënt. Daarna is op een aantal momenten bloed afgenomen om de concentratie van het medicijn in het bloed te bepalen. De metingen zijn hieronder weergegeven:

| Tijd (min) | Concentratie lidocaïne (mg/L) |
|-----------:|---------------------:|
| 2 | 2.28 |
| 4 | 2.31 |
| 6 | 2.16 |
| 8 | 1.73 |
| 10 | 1.46 |
| 15 | 1.30 |
| 20 | 1.13 |
| 30 | 0.90 |
| 45 | 0.59 |
| 60 | 0.50 |
| 90 | 0.47 |
| 120 | 0.38 |
| 180 | 0.266 |
| 240 | 0.168 |
| 360 | 0.067 |

De meetonzekerheid op de concentratie is 8 % van de meetwaarde.

!!! opdracht-basis "Plotten van de metingen"

    In de [appendix over matplotlib](package-matplotlib.md) kun je meer informatie vinden over het maken van grafieken, inclusief het gebruik van foutenvlaggen. Lees dat nog een keer goed door want dat maakt je leven een stuk makkelijker.

    1. Zet de data voor de tijd en de concentratie in je script.
    1. Maak een lege lijst voor de onzekerheid op de concentratie, en gebruik een loop om die te vullen met 8 % van iedere meetwaarde.
    1. Maak een grafiek van de meetwaardes, inclusief foutenvlaggen. Maak een scatter plot, en gebruik geen lijn. Maak de grafiek netjes met aslabels en laat de grafiek in de oorsprong beginnen.

In het hoofdstuk _farmacokinetiek_ [is besproken ](farmacokinetiek.md#hoeveelheid-paracetamol-in-het-lichaam) dat je lichaam een medicijn afbreekt en dat de concentratie medicijn in je lichaam gemodelleerd kan worden met de vergelijking:
\begin{equation}
C(t) = C_0 \cdot \frac{1}{2}^\frac{t}{t_{1/2}},
\end{equation}
met $C(t)$ de concentratie medicijn op tijdstip $t$, $C_0$ de beginconcentratie en $t_{1/2}$ de halfwaardetijd van het medicijn. We zullen zien dat dit model niet voor alle medicijnen toepasbaar is, waaronder lidocaïne. We doen dit door vergelijking (1) te fitten aan onze dataset en vast te stellen dat de fit niet heel goed is.

!!! opdracht-basis "Fitten van een (te) vereenvoudigd model"

    In de [appendix over lmfit](package-lmfit.md) kun je meer informatie vinden over het uitvoeren van een fit. Lees vooral ook het stukje over fitten met foutenvlaggen.

    1. Maak, voordat we de fit kunnen doen, een lege lijst voor de gewichten. Gebruik een loop om voor iedere meetwaarde het gewicht uit te rekenen en die toe te voegen aan de lijst. Tip: je hebt al een loop die je mogelijk kunt gebruiken.
    1. Gebruik lmfit om de data te fitten met het bovenstaande model (vergelijking 1) waarbij je gebruik maakt van de gewichten.
    1. Gebruik het fit-resultaat om de fitcurve te plotten in je bestaande grafiek. Plot de curve met een lijn, en zonder punten. Wat vind je van het resultaat?

Het is je vast opgevallen dat de fit niet goed past op de meetpunten. Dat komt omdat het model te eenvoudig is. Dat gaat er namelijk vanuit dat het medicijn zich snel verspreidt door je lichaam en dan langzaam wordt afgebroken door de lever. In werkelijkheid verspreidt het medicijn zich snel door je bloed (waarvan we de concentratie meten), wordt dan redelijk snel opgenomen door de weefsels in je lichaam (de snelle afname van de concentratie in het bloed) en langzaam afgebroken door de lever terwijl de concentratie in het bloed en de concentratie in de weefsels in evenwicht blijven (de langzame afname). We kunnen dus beter het volgende model gebruiken:
\begin{equation}
C(t) = C_1 \cdot \frac{1}{2}^\frac{t}{T_1} + C_2 \cdot \frac{1}{2}^\frac{t}{T_2},
\end{equation}
waarbij de concentraties $C_1$ en $C_2$ en de halfwaardetijden $T_1$ en $T_2$ nu gebaseerd zijn op twee zogeheten _compartimenten_: het bloed en het weefsel. Omdat dit een oplossing is van een gekoppelde differentiaalvergelijking kun je niet eenvoudig stellen dat $C_1$ de concentratie is in het bloed en $C_2$ de concentratie in het weefsel; de volledige uitdrukking is omwille van eenvoud omgeschreven. Dit technisch detail mag je buiten beschouwing laten.

!!! opdracht-basis "Fitten van het twee-compartimentenmodel"

    1. Gebruik lmift om de data te fitten met het verbeterde model uit vergelijking 2. Let op: haal de oude fit niet weg, maar plot _beide_ fits in dezelfde grafiek zodat je goed kunt vergelijken.
    1. Gebruik een legenda voor de twee curves zodat je goed kunt zien welke curve bij welk model hoort. Past het twee-compartimentenmodel beter?
    1. Print de waarde mét onzekerheid van de twee halfwaardetijden uit het verbeterde model, en geef de biologische betekenis van de twee waardes.

!!! opdracht-meer "Afronden"

    In de vorige opdracht heb je de waarde met onzekerheid weergegeven, maar waarschijnlijk _niet_ in het juiste aantal significante cijfers. Jullie kennen de functie `#!py round()` waarbij je een getal kunt afronden. Deze functie accepteert een extra parameter waarbij je aangeeft op hoeveel decimalen je het getal af wilt ronden:
    ```py
    from math import pi

    pi
    # 3.141592653589793
    round(pi)
    # 3
    round(pi, 1)
    # 3.1
    round(pi, 2)
    # 3.14
    ```
    Gebruik `#!py round()` om de halfwaardetijden volgens de richtlijnen van het natuurkundepracticum correct uit te printen.

!!! opdracht-meer "f-strings"

    Je kunt `#!py round()` gebruiken... maar makkelijker is om [f-strings](uv-vis-spectroscopie.md#opdr:tabellen-printen) te gebruiken! Als je alléén af wilt ronden kan dat met `#!py f"{value:.2f}"` om af te ronden op twee decimalen. Gebruik f-strings om de waardes met onzekerheden van de halfwaardetijden te printen. Zijn je print-statements nu korter geworden?

## Eigen data

Bij het natuurkundepracticum hebben jullie gebruik gemaakt van Tailor. Hierdoor hoefde je niet zelf te programmeren maar kon je met een applicatie je data analyseren en fitten met een model. Wel zo makkelijk! Misschien ben je tegen dingen aangelopen die Tailor _niet_ kon en die je daarom anders moest oplossen. Dat is één van de redenen dat leren programmeren handig is: als een programma iets niet kan, dan doe je het toch gewoon zelf? Op een manier die jij wilt? Verrassing: zo is Tailor ontstaan. Wij hebben Tailor geschreven omdat andere programma's te ingewikkeld waren of niet konden wat wij wilden: eenvoudig een dataset analyseren. [Tailor is geschreven in Python](https://github.com/davidfokkema/tailor) en maakt gebruikt van lmfit en matplotlib, zoals jullie hierboven gebruikt hebben. Jullie kunnen nu (bijna) net zoveel als Tailor kan!

!!! opdracht-basis "Analyseer je eigen dataset"

    Haal je labjournaal tevoorschijn en kies een dataset die je geanalyseerd hebt met Tailor, waarbij je gefit hebt aan een model. Kies wel een dataset met niet al te veel metingen zodat je ze kunt overtypen in een Python list.
    
    1. Neem de data over, fit aan hetzelfde model en maak een grafiek die overeenkomt met de grafiek in je labjournaal (of maak hem mooier!). Krijg je hetzelfde fitresultaat?
    1. Bewaar de data als PDF-bestand zodat je die zou kunnen gebruiken in een verslag of wetenschappelijk artikel.

# Analyse van (bio)medische meetgegevens

In het hoofdstuk _Farmacokinetiek_ hebben we van twee medicijnen bekeken hoe ze worden opgenomen en afgebroken in het menselijk lichaam. We zijn ervan uitgegaan dat de medicijnen zich zeer snel verdeelden over het lichaam en vervolgens langzaam werden afgebroken volgens een eenvoudig exponentieel model met een halfwaardetijd. Als je wilt weten of dat klopt, zul je de concentratie van het medicijn in het bloed van een patiënt op verschillende momenten moeten meten. Je neemt dan op gezette tijden een buisje bloed af en analyseert dat. Als je de concentraties hebt bepaald en uitgezet in een grafiek, zul je het exponentiële model aan de meetgegevens moeten fitten om te kijken of de datapunten en het model goed overeenkomen. Dit is dezelfde werkwijze als die je hebt toegepast op het natuurkundepracticum. Daar voerde je een experiment uit en fitte je de metingen aan een natuurkundig model om te kijken of die goed overeen kwamen en zo ja, wat de waardes van de modelparameters waren. Je hebt dat daar gedaan met Tailor. Maar dat kan natuurlijk ook met Python! Dat is meer typewerk maar geeft je veel meer vrijheid over wat je _precies_ gedaan wilt krijgen.

!!! info "Aansluiting MNW-programma"

    In deze sessie analyseren we meetgegevens en fitten we een model om te onderzoeken hoe goed het de metingen beschrijft. Dit is een belangrijke vaardigheid binnen (bio)medisch onderzoek. Je gebruikt deze vaardigheid onder meer bij de vakken _Practicum natuurkunde en informatica 1_ (jaar 1, periode 1) en _Practicum natuurkunde en informatica 2_ (jaar 2, periode 5), maar ook bij andere vakken binnen het MNW-programma.

## Lidocaïne

Lidocaïne is een medicijn dat zenuwgeleiding tijdelijk vermindert of blokkeert en is vooral werkzaam op pijnprikkels. Het is daardoor zeer geschikt als middel om (lokaal) te verdoven, en wordt soms bij ernstige zenuwpijn direct in de bloedbaan ingebracht. In die situatie verspreidt het zich door het hele lichaam en wordt opgenomen door lichaamsweefsel. Om te controleren of het afbraakmodel waarmee je eerder gewerkt hebt ook op dit medicijn van toepassing is, hebben we een dosis van 100 mg lidocaïne direct in de bloedbaan gebracht van een volwassen patiënt. Daarna is op een aantal momenten bloed afgenomen om de concentratie van het medicijn in het bloed te bepalen. De metingen zijn hieronder weergegeven:

| Tijd (min) | Concentratie lidocaïne (mg$\,$L$^{-1}$) |
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

!!! opdracht-basis "Plotten van de metingen"

    In de [appendix over matplotlib](package-matplotlib.md) kun je meer informatie vinden over het maken van grafieken. Gebruik de informatie uit deze appendix bij de komende opdrachten. 

    1. Maak een nieuw bestand aan met de naam {{new_file}}`lidocaine.py`. Zet de tijden en de bijbehorende concentraties lidocaïne in het bloed in twee aparte lijsten.
    2. De meetonzekerheid op de concentratie lidocaïne in het bloed is 8% van de meetwaarde. Maak hiervoor een lege lijst. Gebruik een loop om voor elke gemeten concentratie de meetonzekerheid uit te rekenen en deze toe te voegen aan de lijst.
    3. Maak een scatter plot[^scatter] van de concentratie lidocaïne tegen de tijd, met foutenvlaggen voor de meetonzekerheid. Geef beide assen een label en laat beide assen in de oorsprong beginnen. _Tips_: zoek in de [appendix](package-matplotlib.md) op welke `#!py matplotlib`-functie je kunt gebruiken om meetpunten met foutenvlaggen weer te geven. Gebruik verder `#!py marker=` en `#!py linestyle=` om de datapunten zichtbaar te maken en de lijn tussen de datapunten weg te halen.

    [^scatter]: Een scatter plot geeft datapunten weer als losse punten, zonder ze met een lijn te verbinden.

In het hoofdstuk _Farmacokinetiek_ [is besproken ](farmacokinetiek.md#hoeveelheid-paracetamol-in-het-lichaam) dat je lichaam een medicijn afbreekt en dat de concentratie van het medicijn in je lichaam gemodelleerd kan worden met de vergelijking
\begin{equation}
C(t) = C_0 \cdot \frac{1}{2}^\frac{t}{t_{1/2}},
\end{equation}
met $C(t)$ de concentratie van het medicijn op tijdstip $t$, $C_0$ de beginconcentratie en $t_{1/2}$ de halfwaardetijd van het medicijn. Dit model beschrijft niet voor alle medicijnen even goed hoe de concentratie in de tijd verandert. We onderzoeken daarom hoe goed het model past bij onze metingen van lidocaïne. Hiervoor fitten we vergelijking 1 aan de meetgegevens en bekijken we hoe goed de fitlijn overeenkomt met de datapunten.

<div id="opdr:vereenvoudigd-model"></div>
!!! opdracht-basis "Fitten van een (te) vereenvoudigd model"

    In de [appendix over lmfit](package-lmfit.md) kun je meer informatie vinden over het uitvoeren van een fit. Gebruik de informatie uit deze appendix bij de komende opdrachten. 

    1. Bij het fitten met meetonzekerheden worden gewichten gebruikt. Deze bepalen hoe zwaar elk meetpunt meetelt in de fit. Je berekent het gewicht uit de meetonzekerheid:
        ```python
        weight = 1 / uncertainty
        ```
    Maak een lege lijst voor de gewichten. Gebruik een loop om voor elke gemeten concentratie het gewicht te berekenen en deze toe te voegen aan de lijst. _Tip_: je kunt hiervoor je eerder geschreven loop uitbreiden.  
    2. Definieer met `#!py ExpressionModel` een model voor vergelijking 1. Gebruik hiervoor de uitleg in de [appendix](package-lmfit.md). _Tip_: bepaal welke variabele de tijd voorstelt en welke twee parameters tijdens het fitten worden bepaald. Geef de tijdvariabele op bij `#!py independent_vars=`.
    3. Fit het model aan de meetgegevens. Gebruik in de fit de gewichten die je eerder hebt berekend en geef startwaarden voor de twee parameters mee. _Tip_: gebruik de grafiek om de startwaarden af te schatten.
    4. Gebruik het fitresultaat om de fitcurve toe te voegen aan de bestaande grafiek. Geef de fitcurve weer als een lijn zonder punten. _Tip_: gebruik de [appendix over lmfit](package-lmfit.md) om de $y$-waarden van de fit te bepalen. Daarna kun je met informatie uit de [appendix over matplotlib](package-matplotlib.md) de fitcurve aan de grafiek toevoegen.
    5. Hoe goed beschrijft het model de meetgegevens? Licht je antwoord toe.

Het is je vast opgevallen dat de fit niet goed past bij de meetpunten. Dat komt doordat het model te eenvoudig is. Het gaat er namelijk van uit dat het medicijn zich snel verspreidt door het lichaam en daarna langzaam wordt afgebroken door de lever. In werkelijkheid verspreidt het medicijn zich snel door het bloed, waarin we de concentratie meten. Vervolgens wordt het medicijn relatief snel opgenomen door de weefsels in het lichaam. Daardoor neemt de concentratie in het bloed in eerste instantie snel af. De concentratie in het bloed neemt daarna langzamer af, vooral doordat de lever het medicijn afbreekt. Tijdens deze fase blijft de concentratie in het bloed en de concentratie in de weefsels in evenwicht. Om zowel de snelle als de langzame afname van de concentratie in het bloed te beschrijven, gebruiken we het volgende model:
\begin{equation}
C(t) = C_1 \cdot \frac{1}{2}^\frac{t}{T_1} + C_2 \cdot \frac{1}{2}^\frac{t}{T_2},
\end{equation}
waarbij de concentraties $C_1$ en $C_2$ en de halfwaardetijden $T_1$ en $T_2$ nu gebaseerd zijn op twee zogeheten _compartimenten_: het bloed en de weefsels. De twee termen beschrijven samen de concentratie van het medicijn in het bloed. Omdat dit een oplossing is van een gekoppelde differentiaalvergelijking kun je niet eenvoudig stellen dat $C_1$ de concentratie is in het bloed en $C_2$ de concentratie in het weefsel; de volledige uitdrukking is omwille van eenvoud omgeschreven. Dit technisch detail mag je buiten beschouwing laten.

!!! opdracht-basis "Fitten van het tweecompartimentenmodel"

    Je gaat zo _naast_ het vereenvoudigde model ook het tweecompartimentenmodel fitten. Je volgt hiervoor dezelfde stappen als in de [_opdracht Fitten van een (te) vereenvoudigd model_](#opdr:vereenvoudigd-model). Gebruik voor het tweecompartimentenmodel en het fitresultaat andere variabelenamen dan bij de eerdere fit, zodat je de resultaten van beide modellen naast elkaar kunt blijven gebruiken.

    1. Definieer met `#!py ExpressionModel` het tweecompartimentenmodel uit vergelijking 2 en fit het aan de meetgegevens. Gebruik in de fit de eerder berekende gewichten en geef startwaarden voor de vier parameters mee.
    2. Gebruik het fitresultaat om de nieuwe fitcurve als een lijn zonder punten toe te voegen aan de bestaande grafiek. Laat de eerdere fitcurve staan, zodat je beide modellen kunt vergelijken. Voeg een legenda toe die aangeeft welke curve bij welk model hoort.
    3. Vergelijk beide fitcurves met de meetpunten. Past het tweecompartimentenmodel beter dan het vereenvoudigde model? Licht je antwoord toe.
    4. Print de twee halfwaardetijden uit het tweecompartimentenmodel elk met de bijbehorende onzekerheid. Welke halfwaardetijd hoort bij de snelle afname en welke bij de langzame afname? Leg uit welke biologische processen vooral bijdragen aan de snelle en de langzame afname van de concentratie in het bloed.

!!! opdracht-meer "Afronden"

    In de vorige opdracht heb je de waarde met onzekerheid weergegeven, maar waarschijnlijk _niet_ in het juiste aantal significante cijfers. Je kent de functie `#!py round()` waarmee je een getal kunt afronden. Deze functie accepteert een extra parameter waarbij je aangeeft op hoeveel decimalen je het getal af wilt ronden:
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
    
    1. Gebruik `#!py round()` om de halfwaardetijden volgens de richtlijnen van het natuurkundepracticum correct uit te printen.

!!! opdracht-meer "f-strings"

    Je kunt `#!py round()` gebruiken, maar makkelijker is om [f-strings](uv-vis-spectroscopie.md#opdr:tabellen-printen) te gebruiken! Als je alléén af wilt ronden kan dat met `#!py f"{value:.2f}"` om af te ronden op twee decimalen. Gebruik f-strings om de waardes met onzekerheden van de halfwaardetijden te printen. Zijn je print-statements nu korter geworden?

## Eigen data

Bij het natuurkundepracticum heb je gebruikgemaakt van Tailor. Met deze applicatie kon je je data analyseren en fitten met een model, zonder zelf te hoeven programmeren. Wel zo makkelijk! Misschien ben je tegen dingen aangelopen die Tailor _niet_ kon en die je daarom anders moest oplossen. Dat is één van de redenen dat leren programmeren handig is: als een programma iets niet kan, kun je zelf programmeren wat je nodig hebt, op een manier die jij wilt. Verrassing: zo is Tailor ontstaan. Wij hebben Tailor geschreven omdat andere programma's te ingewikkeld waren of niet konden wat wij wilden: eenvoudig een dataset analyseren. [Tailor is geschreven in Python](https://github.com/davidfokkema/tailor) en maakt gebruikt van `#!py lmfit` en `#!py matplotlib`, net als jij in de eerdere opdrachten. Je kunt nu (bijna) net zoveel als Tailor!

!!! opdracht-basis "Analyseer een eigen dataset"

    Zoek de digitale versie van één van je labjournaals op Canvas op en kies een dataset die je met Tailor hebt geanalyseerd en met een model hebt gefit. Kies een dataset met niet al te veel metingen, zodat je de meetwaarden kunt overtypen in lijsten.

    1. Maak een nieuw Python-bestand aan. Kies zelf een geschikte naam voor dit bestand. Neem de meetgegevens over en fit het model dat je eerder hebt gebruikt aan de data. Maak een grafiek die overeenkomt met de grafiek in je labjournaal (of maak hem mooier!) Krijg je dezelfde fitresultaten als met Tailor?
    2. Sla de grafiek op als PDF-bestand, zodat je die zou kunnen gebruiken in een verslag of wetenschappelijk artikel. Zoek in de [appendix over matplotlib](package-matplotlib.md) op hoe je dit kunt doen.

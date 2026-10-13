# Data-analyse

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

    In de [appendix over lmfit](package-lmfit.md) kun je meer informatie vinden over het uitvoeren van een fit.

    1. Gebruik lmfit om de data te fitten met het bovenstaande model. Gebruik voor nu _geen_ foutenvlaggen!
    1. Gebruik het fit-resultaat om de fitcurve te plotten in je bestaande grafiek. Plot de curve met een lijn, en zonder punten. Wat vind je van het resultaat?
    1. Het is beter om wel foutenvlaggen te gebruiken. Maak, voordat je de fit doet, een lege lijst voor de gewichten. Gebruik een loop om voor iedere meetwaarde het gewicht uit te rekenen en die toe te voegen aan de lijst. Tip: je hebt al een loop die je mogelijk kunt gebruiken. Pas de fit aan zodat hij gebruik maakt van de foutenvlaggen en bekijk het nieuwe resultaat. Waarom is die zo anders dan het resultaat zonder foutenvlaggen?

Het is je vast opgevallen dat de fit niet goed past op de meetpunten. Dat komt omdat het model te eenvoudig is. Dat gaat er namelijk vanuit dat het medicijn zich snel verspreidt door je lichaam en dan langzaam wordt afgebroken door de lever. In werkelijkheid verspreid het medicijn zich snel door je bloed (waarvan we de concentratie meten), wordt dan redelijk snel opgenomen door de weefsels in je lichaam (de snelle afname van de concentratie in het bloed) en langzaam afgebroken door de lever terwijl de concentratie in het bloed en de concentratie in de weefsels in evenwicht blijven (de langzame afname). We kunnen dus beter het volgende model gebruiken:
\begin{equation}
C(t) = C_1 \cdot \frac{1}{2}^\frac{t}{T_1} + C_2 \cdot \frac{1}{2}^\frac{t}{T_2},
\end{equation}
waarbij de concentraties $C_1$ en $C_2$ en de halfwaardetijden $T_1$ en $T_2$ nu gebaseerd zijn op twee zogeheten _compartimenten_: het bloed en het weefsel. Omdat dit een oplossing is van een gekoppelde differentiaalvergelijking kun je niet eenvoudig stellen dat $C_1$ de concentratie is in het bloed en $C_2$ de concentratie in het weefsel; de volledige uitdrukking is omwille van eenvoud omgeschreven. Dit technisch detail mag je buiten beschouwing laten.

!!! opdracht-basis "Fitten van het twee-compartimentenmodel"

    1. Gebruik lmift om de data te fitten met het verbeterde model. Let op: haal de oude fit niet weg, maar plot _beide_ fits in dezelfde grafiek zodat je goed kunt vergelijken.
    1. Gebruik een legenda voor de twee curves zodat je goed kunt zien welke curve bij welk model hoort. Past het twee-compartimentenmodel beter?
    1. Print de waarde mét onzekerheid van de twee halfwaardetijden uit het verbeterde model, en geef de biologische betekenis van de twee waardes.

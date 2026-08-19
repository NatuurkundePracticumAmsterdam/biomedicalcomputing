# Sessie 5: epidemiologie

In de vorige sessie hebben we modellen gebouwd en de uitkomsten gevisualiseerd. Maar een model wordt pas echt krachtig als je het kunt gebruiken om te onderzoeken wat er gebeurt als de situatie verandert. We kunnen bijvoorbeeld onderzoeken wat er met een uitbraak van een infectieziekte gebeurt als een deel van de populatie is gevaccineerd. Of we kunnen berekenen hoeveel ziekenhuisbedden nodig zijn tijdens de piek van een uitbraak. Dit noemen we _simuleren_, een veelgebruikte aanpak in de (bio)medische wetenschappen. Simulaties worden gebruikt om verschillende scenario's door te rekenen en de uitkomsten te vergelijken. In deze sessie passen we dit toe op epidemiologie: de studie van hoe ziektes zich verspreiden in een populatie. 

!!! warning

    Onderstaand deel nog inbedden. 

    De halfwaardetijd van paracetamol kan verschillen tussen mensen. Dit kan bijvoorbeeld komen door verschillen in hoe snel het lichaam paracetamol afbreekt en uitscheidt. Leeftijd, de werking van de lever en nieren en het gebruik van andere medicijnen kunnen hierbij een rol spelen. 

    !!! opdracht-basis "Verschillende halfwaardetijd"
        Stel dat de halfwaardetijd van paracetamol bij drie verschillende patiënten 1, 2.5 en 4 uur is. 

        1. Hoe verwacht je dat de hoeveelheid paracetamol in het lichaam verschilt bij voor deze drie patiënten gedurende 24 uur? Schets je verwachting.
        2. Gebruik je numerieke model om de hoeveelheid paracetamol gedurende 24 uur te berekenen voor de drie verschillende halfwaardetijden. Gebruik steeds dezelfde beginhoeveelheid en hetzelfde doseerschema. Plot de drie verschillende situaties in één grafiek. Wat valt je op?

## Verspreiding van infectieziektes

Epidemiologie is het vakgebied dat zich bezighoudt met de verspreiding van ziektes in een populatie. Epidemiologen bestuderen vragen als: Hoe snel verspreidt een infectieziekte zich? Hoeveel mensen raken besmet? Wanneer dooft een uitbraak uit? Die vragen zijn niet alleen wetenschappelijk interessant, ze bepalen mede welke maatregelen een overheid neemt bij een uitbraak. Tijdens de COVID-19-pandemie waren dit soort voorspellingen dan ook bepalend voor het beleid. 

Om zulke vragen te beantwoorden, maken epidemiologen gebruik van wiskundige modellen. Zo'n model beschrijft in een stelsel van vergelijkingen hoe een ziekte zich door een populatie beweegt. Een besmet persoon komt in contact met gezonde mensen en kan die besmetten. Hoe besmettelijk de ziekte is en hoe lang iemand ziek blijft, bepalen samen hoe snel een uitbraak groeit of afneemt. Door die factoren in een model te stoppen, kun je simuleren hoe een uitbraak zich ontwikkelt en wat er gebeurt als je ingrijpt, bijvoorbeeld door vaccinatie of isolatie. 

!!! info "Aansluiting MNW-programma" 

    In dit deel van de sessie simuleren we de verspreiding van infectieziektes met behulp van het SIR-model. Daarmee sluit de sessie aan bij het vak _Mathematische methoden_ (jaar 1, periode 5), waarbinnen onder andere stelsels van differentiaalvergelijkingen aan bod komen. Het SIR-model bestaat uit zo'n stelsel.  

### SIR-model

Het SIR-model is een van de bekendste en meest gebruikte modellen in de epidemiologie. Het model werd in 1927 geïntroduceerd door Kermack en McKendrick[^SIR-model] en is sindsdien de basis van veel epidemiologische modellen. Het model verdeelt een populatie in drie compartimenten:

- $S$ (_susceptible_, vatbaar): personen die vatbaar zijn voor de ziekte, maar nog niet besmet;
  
- $I$ (_infectious_, besmettelijk): personen die besmet zijn met de ziekte en deze kunnen overdragen;
  
- $R$ (_recovered_, hersteld): personen die hersteld zijn van de ziekte en immuun zijn geworden.
  
Elke persoon bevindt zich op elk willekeurig tijdstip in precies één compartiment en beweegt uitsluitend in de richting $S \rightarrow I \rightarrow R$.

[^SIR-model]: William Ogilvy Kermack en Anderson Gray McKendrick. "A contribution to the mathematical theory of epidemics". In: _Proceedings of the Royal Society of London_, Series A, 115.772 (1927), p. 700–721. [https://doi.org/10.1098/rspa.1927.0118](https://doi.org/10.1098/rspa.1927.0118)

Voor dit model gelden een aantal aannames. De populatie is gesloten: er is geen geboorte, sterfte of migratie, waardoor de totale populatiegrootte $N = S + I + R$ constant blijft. Alle individuen zijn identiek: het model maakt geen onderscheid tussen individuen op basis van bijvoorbeeld leeftijd, gezondheid of gedrag. Verder gaat het model uit van homogene menging: elk individu heeft evenveel kans om in contact te komen met elk ander individu. Tot slot geldt dat wie besmet raakt direct besmettelijk is en wie herstelt direct en blijvend immuun is.

Het model bestaat uit een stelsel vergelijkingen dat beschrijft hoe de grootte van elk compartiment verandert in de tijd. De snelheid waarmee personen van $S$ naar $I$ overgaan, hangt af van het aantal besmette personen, het aantal personen dat nog vatbaar is en de besmettelijkheid van de ziekte. De verandering van $S$ in de tijd wordt gegeven door
\begin{equation}
\frac{dS}{dt} = - \beta \cdot \frac{S(t)}{N} \cdot I(t).
\end{equation}
Het minteken geeft aan dat het aantal vatbare personen door nieuwe besmettingen afneemt. De parameter $\beta$ bepaalt hoe makkelijk nieuwe besmettingen ontstaan door contacten tussen vatbare en besmette personen en geeft daarmee de besmettelijkheid van de ziekte weer. $I(t)$ geeft het aantal besmette personen op een bepaald tijdstip. In het model wordt aangenomen dat contacten willekeurig over de populatie plaatsvinden (homogene menging). De fractie $\frac{S(t)}{N}$ geeft dan de kans dat een willekeurig contact plaatsvindt met iemand die vatbaar is voor de ziekte. Samen bepalen deze factoren hoe snel het aantal vatbare personen afneemt.

De stroom van $I$ naar $R$ is eenvoudiger:
\begin{equation}
\frac{dR}{dt} = \gamma \cdot I(t).
\end{equation}
De parameter $\gamma$[^gamma] geeft aan hoe snel besmette personen herstellen. De herstelsnelheid is evenredig met $I(t)$, het aantal besmette personen op een bepaald tijdstip. $R$ neemt dus alleen toe.

[^gamma]: De herstelsnelheid $\gamma$ is te bepalen uit de gemiddelde besmettelijke periode. Als een persoon gemiddeld $d$ dagen besmettelijk is, geldt $\gamma = \frac{1}{d}$. 

Tot slot verandert $I$ door twee stromen tegelijk: $I$ ontvangt personen vanuit $S$ en verliest personen naar $R$. De verandering van $I$ is het verschil tussen die twee stromen:
\begin{equation}
\frac{dI}{dt} = \beta \cdot \frac{S(t)}{N} \cdot I(t) - \gamma \cdot I(t).
\end{equation} 

Het SIR-model met het stelsel van vergelijkingen is in onderstaand stroomdiagram visueel samengevat.

!!! warning

    Stroomdiagram toevoegen.

Tot nu toe hebben we het SIR-model beschreven met een stelsel differentiaalvergelijkingen. Die beschrijven de verandering op elk moment in de tijd. We hebben eerder gezien dat een numerieke aanpak goed werkt wanneer een analytische oplossing niet voorhanden is en dat is hier het geval. We berekenen elke tijdstap $\Delta t$ met 
\begin{equation}
S(t+\Delta t) = S(t) + \frac{dS}{dt} \cdot \Delta t.
\end{equation}
Door vergelijking 1 in te vullen voor $\frac{dS}{dt}$ krijgen we
\begin{equation}
S(t+\Delta t) = S(t) - \beta \cdot \frac{S(t)}{N} \cdot I(t) \cdot \Delta t.
\end{equation}
Voor $I$ en $R$ gebruik je dezelfde aanpak. En hoe kleiner $\Delta t$, hoe nauwkeuriger de benadering.

<div id="opdr:eerste-dagen"></div>
!!! opdracht-basis "De eerste dagen van de uitbraak"

    Het is goed om de numerieke aanpak eerst op papier uit te rekenen voor een aantal tijdstappen. Zo wordt duidelijk wat er per tijdstap gebeurt en kun je het voorbeeld later gebruiken om je programma te testen.

    We gaan uit van een populatie van 2000 personen, waarvan aan het begin 10 personen besmet zijn en nog geen personen hersteld zijn. De parameters zijn $\beta = 0.5$ en $\gamma = 0.2$. Als tijdstap nemen we $\Delta t = 1$ dag.

    1. Werk de eerste drie tijdstappen uit op papier. Maak een tabel met daarin $t$, $S$, $I$, $R$ en $N$. Begin bij $t=0$ en eindig bij $t=3$. Goed om te weten: het model behandelt de populatie als continu, ondanks dat een persoon in werkelijkheid niet deelbaar is. De waarden voor $S$, $I$ en $R$ kunnen daarom kommagetallen zijn. Rond voor deze opdracht de waarden af op één decimaal.
    2. Bekijk je tabel. Neemt $S$ af over de tijd? Neemt $I$ toe? Wat gebeurt er met $R$? En blijft $N$ constant? Controleer je berekeningen als de uitkomsten niet overeenkomen met je verwachting.

Nu je de eerste drie dagen met de hand hebt uitgerekend en je weet wat je voor elke tijdstap moet berekenen, gaan we het model programmeren. 

!!! opdracht-basis "Vijftig dagen later"

    1. Maak een nieuw bestand aan met de naam {{new_file}}`sir_model.py`. Definieer bovenaan in het bestand alle beginwaarden en parameters. Gebruik dezelfde beginwaarden en parameters als in de [_opdracht De eerste dagen van de uitbraak_](#opdr:eerste-dagen).
    2. Vertaal nu de berekeningen die je op papier hebt gedaan naar Python-code. Bereken de waarden van $S$, $I$ en $R$ voor de eerste 50 dagen. Bereken bij elke tijdstap ook $N$, zodat je kunt controleren of de populatie constant blijft. Zorg dat voor elke tijdstap het volgende geprint wordt:
        ```
        t = 0: S = 1990, I = 10, R = 0, N = 2000
        t = 1: S = ..., I = ..., R = ..., N = ...
        ```
    3. Controleer de eerste tijdstappen met de uitkomst van de [_opdracht De eerste dagen van de uitbraak_](#opdr:eerste-dagen). Komen de antwoorden overeen? Zo niet, zoek dan eerst uit waarom je andere waarden vindt. Commit.
 
!!! opdracht-meer "Waarden afgerond weergeven"

    In de [_opdracht De eerste dagen van de uitbraak_](#opdr:eerste-dagen) heb je de waarden afgerond op één decimaal. Je programma doet dat nu niet. Met f-strings kun je getallen afgerond weergeven. De regel
        ```py
        print(f"{number1:.1f}, {number2:.1f}")
        ```
    geeft de variabelen `number1` en `number2` weer op één decimaal.

    1. Zorg dat de waarden worden weergegeven op één decimaal. Commit.
    2. Je kunt de waarden ook weergeven in een tabel. Kijk daarvoor nog eens naar de [_opdracht Tabellen printen_](uv-vis-spectroscopie.md#opdr:tabellen-printen). Commit.
    
Eerder deze sessie heb je geleerd hoe je functies schrijft en kunt gebruiken. Die kennis passen we nu toe op de code die we aan het schrijven zijn.

!!! opdracht-basis "Een functie toevoegen"

    1. Schrijf in het bestand {{file}}`sir_model.py` de functie `#!py simulate_sir` met de volgende header: 
        ```py
        def simulate_sir(N, I0, R0, beta, gamma, days):
        ```
    Deze functie voert de simulatie uit en print de waarden voor elke tijdstap. Verplaats de `#!py for`-loop met de berekeningen en de printregels naar de functie en zorg voor de juiste indentatie. Je hoeft geen nieuwe code te schrijven. Let op: gebruik je andere variabelenamen dan de parameternamen in de header van de functie? Pas die dan wel aan zodat ze overeenkomen.
    2. De beginwaarden en parameters bovenaan in het bestand zijn nu overbodig, omdat de functie die waarden via de parameters verwacht te ontvangen. Verwijder ze daarom. Roep onderaan in het bestand de functie aan met de volgende waarden voor de parameters:
        ```py
        simulate_sir(N=2000, I0=10, R0=0, beta=0.5, gamma=0.2, days=50)
        ```
    Controleer de eerste tijdstappen met de uitkomst van de [_opdracht De eerste dagen van de uitbraak_](#opdr:eerste-dagen). Komen ze overeen? Zo niet, zoek dan eerst uit waarom je andere getallen vindt. Commit.

Tot nu toe het je de verschillende waarden laten printen in de terminal, maar een grafiek geeft meer inzicht over hoe de uitbraak zich in de tijd ontwikkelt. 

!!! opdracht-basis "De uitbraak gevisualiseerd"

    1. Voeg bovenaan in het bestand
        ```python
        import matplotlib.pyplot as plt
        ```
    toe.
    2. Pas de functie `simulate_sir` aan, zodat de functie de waarden voor $S$, $I$, $R$ en de tijd ook in lijsten opslaat. Geef deze lijsten aan het einde van de functie terug met `#!py return`. 
    3. Zorg dat je buiten de functie, daar waar je de functie aanroept, de lijsten opslaat in verschillende variabelen. Commit.
    4. Schrijf daarna onderaan in het bestand code om de waarden te plotten. Zet zowel $S$, $I$ als $R$ uit tegen de tijd in dezelfde plot. Voeg duidelijke aslabels en een legenda toe. Commit. 

!!! opdracht-meer "Plotten tegen de index"

    Als je met `matplotlib` plot, hoef je geen $x$-waardes mee te geven. De volgende regels code geven dus beide een plot:
        ```python
        plt.plot(x, y)
        plt.plot(y)
        ```
    In het eerste geval wordt $y$ tegen $x$ uitgezet. In het tweede geval wordt voor $x$ de index van de $y$-lijst gebruikt. Wanneer je $x$-waarden gelijk zijn aan de index, geven beide regels code hetzelfde resultaat. Maar zodra dat niet zo is, bijvoorbeeld als je alleen voor de dagen 20 tot 50 de berekeningen uitvoert, geeft `#!py plt.plot(y)` een verkeerd beeld.

    Op dit moment lopen de tijdstappen van 0 tot 50, wat gelijk is aan de index. Pas je code zo aan dat je voor het plotten alleen gebruikmaakt van de $y$-waarden en verwijder code die nu overbodig is geworden. Commit.

!!! opdracht-meer "Invoer via de terminal"

    De beginwaarden en parameters staan nu vast in het script. Met `#!py input()` kun je via de terminal opvragen wat deze waarden zijn.

    Pas je code aan zodat de beginwaarden en parameters via `#!py input()` worden opgevraagd. Zorg dat de invoer ook daadwerkelijk gebruikt wordt. Houd er rekening mee dat `#!py input()` altijd een string teruggeeft, zet de invoer dus om naar het juiste type. Commit. 

## Scenario's vergelijken

Nu het model geschreven is, kunnen we gaan simuleren. We leggen verschillende scenario's naast elkaar en kijken hoe een ziekte zich verspreidt door een populatie. 

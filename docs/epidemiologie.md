# Sessie 5: epidemiologie

In de vorige sessie hebben we modellen gebouwd, uitkomsten gevisualiseerd en al gekeken naar wat er verandert als we een parameter aanpassen. Juist die laatste stap maakt een model krachtig. We kunnen het model dan gebruiken om te onderzoeken wat er gebeurt als de situatie verandert. In deze sessie passen we dit toe op epidemiologie: de studie van hoe ziektes zich verspreiden in een populatie. We kunnen bijvoorbeeld onderzoeken wat er met een uitbraak van een infectieziekte gebeurt als een deel van de populatie is gevaccineerd. Of we kunnen berekenen hoeveel ziekenhuisbedden nodig zijn tijdens de piek van een uitbraak. Dit noemen we _simuleren_, een veelgebruikte aanpak in de (bio)medische wetenschappen. Simulaties worden gebruikt om verschillende scenario's door te rekenen en de uitkomsten te vergelijken. 

## Farmacokinetische simulaties vergelijken

In de vorige sessie hebben we een model gebouwd van de concentratie fenytoïne in het bloed. Met dit model hebben we onder andere de invloed van massa op de dagelijkse dosis bekeken en het effect van een vergeten dosis gesimuleerd. Elk scenario vroeg om een aanpassing in de code, waarna we het programma opnieuw uitvoerden. Dat werkte, maar vergelijken was daardoor lastig. We zagen telkens maar één grafiek. Om dit probleem op te lossen zouden we code kunnen dupliceren, maar dat leidt snel tot lange, onoverzichtelijke code. Functies bieden een elegante oplossing en daar gaan we in deze sessie mee aan de slag.

!!! opdracht-basis "Code ombouwen"

    Het is tijd om een functie te gaan gebruiken. Je gebruikt daarvoor de bestaande code in het bestand {{file}}`phenytoin.py` en geeft de dosis mee als parameter.

    1. Open het bestand {{file}}`phenytoin.py`. Voer het programma uit voor een patiënt met een massa van 80 kg en een dagelijkse dosis van 300 mg. Plot de concentratie gedurende 20 dagen. Maak een schets van deze plot, zodat je later kunt controleren of de code na het ombouwen dezelfde uitkomst geeft. Noteer de piek- en dalwaarden in de steady-state en hoe lang het ongeveer duurt om deze steady-state te bereiken.
    2. Maak een functie aan met de volgende header:
        ```python
        def simulate_concentration(dose):
        ```
    Deze functie voert de simulatie uit. Verplaats de lege lijst(en), de beginwaarden van variabelen die in de `#!py for`-loop worden bijgewerkt en de `#!py for`-loop met de berekeningen naar de functie en zorg voor de juiste indentatie. Voeg onderaan de functie een `#!py return`-regel toe die de gevulde lijst(en) teruggeeft. Behalve de functieheader en de `#!py return`-regel hoef je geen nieuwe code te schrijven. Let op: gebruik je een andere variabelenaam dan `dose`? Pas die dan aan, zodat de naam in de functieheader en in de rest van de functie overeenkomt.
    3. Roep de functie aan op de regel vóór `#!py plt.plot(...)` met
        ```py
        simulate_concentration(dose=300)
        ```
    Sla de uitkomst van de functie op in variabele(n) die je voor de plot kunt gebruiken. Staat de waarde voor `dose` ook nog los bovenin het bestand? Verwijder die dan, want de functie ontvangt deze waarde nu via de parameter.
    4.  Voer het programma uit en los eventuele fouten op. Controleer of de plot overeenkomt met de plot van voordat je de code ombouwde. Klopt alles? Commit.

Nu we een deel van de code in een functie hebben gezet, kunnen we makkelijker scenario's vergelijken. We kunnen de functie meerdere keren aanroepen met verschillende waarden voor `dose`. De uitkomsten slaan we elke keer op in aparte variabele(n). Deze variabelen gebruiken we daarna om meerdere lijnen in één plot te tekenen. 

!!! opdracht-basis "Verschillende doses vergelijken"

    De dagelijkse dosis voor fenytoïne ligt tussen de 200 mg en 400 mg. Voor een patiënt van 80 kg vergelijken we drie scenario's in één plot om te bepalen welke dagelijkse dosis het meest geschikt is. 

    1. Roep de functie `#!py simulate_concentration()` drie keer aan met een andere waarde voor `dose`: 200, 300 en 400 mg. Sla de uitkomsten van de functie elke keer op in aparte variabele(n). Voor de concentratie kun je bijvoorbeeld kiezen voor `concentration_200`, `concentration_300` en `concentration_400`.
    2. Geef alle drie de scenario's in dezelfde plot weer. Geef de verschillende lijnen in de plot duidelijke labels en voeg een legenda toe. Commit.
    3. Welke verschillen zie je tussen de scenario's? Welke dagelijkse dosis is voor deze patiënt het meest geschikt? Vergelijk je antwoord met dat van de [_opdracht Veilige dosis_](farmacokinetiek.md#opdr:dosis-fenytoine). Kom je tot hetzelfde antwoord? Wat voegt de visualisatie toe?

De functie `#!py simulate_concentration()` heeft nu één parameter: `dose`. Maar een functie kan ook meerdere parameters hebben. Zo kunnen we ook de massa van patiënten meegeven en scenario's vergelijken voor patiënten met een verschillend lichaamsgewicht. Of de halfwaardetijd, die sterk kan variëren &mdash; tussen de 7 en 42 uur[^farkompas-fenytoine] &mdash; en daardoor grote invloed heeft op de concentratie in het bloed. In de volgende opdracht voegen we deze parameters stap voor stap toe.

[^farkompas-fenytoine]: [https://www.farmacotherapeutischkompas.nl/bladeren/preparaatteksten/f/fenytoine](https://www.farmacotherapeutischkompas.nl/bladeren/preparaatteksten/f/fenytoine)

!!! opdracht-basis "Massa variëren"

    1. Voeg de massa toe als tweede parameter aan de functieheader, bijvoorbeeld met de naam `m`:
        ```python
        def simulate_concentration(dose, m):
        ```
    Staat de waarde voor de massa ook nog los bovenin het bestand? Verwijder die dan, want de functie ontvangt deze waarde nu ook via een parameter. Als je het programma uitvoert voor een patiënt van 80 kg, is de uitkomst dan gelijk aan wat je eerder had? Los eventuele fouten op. Commit.
    2. Roep de functie drie keer aan voor een patiënt van 60, 80 en 100 kg, steeds met een dagelijkse dosis van 300 mg. Bijvoorbeeld:
        ```python
        simulate_concentration(dose=300, m=60)
        ```
    Geef alle drie de scenario's in dezelfde plot weer met een duidelijke legenda. Commit. 
    3. Welke verschillen zie je tussen de scenario's? Bij welke massa blijft de concentratie binnen het therapeutisch venster?

!!! opdracht-basis "Halfwaardetijd variëren"

    1. Doe nu hetzelfde voor de halfwaardetijd. Voeg een parameter toe aan de functieheader met bijvoorbeeld de naam `half_life`. Staat de waarde van de halfwaardetijd ook nog los bovenin het bestand? Verwijder die dan. Voer het programma uit en los eventuele fouten op. Commit.
    2. Roep de functie drie keer aan met de halfwaardetijden van 7, 24 en 42 uur, voor een patiënt van 80 kg met een dagelijkse dosis van 300 mg. Geef alle drie de scenario's in dezelfde plot weer met een duidelijke legenda. Commit. 
    3. Welke verschillen zie je tussen de scenario's? Wat betekent een korte halfwaardetijd voor de piek- en dalwaarden in de steady-state? Bereiken alle scenario's de steady-state op hetzelfde moment?

???+ meer-leren "Keyword arguments versus positional arguments"

    Tot nu toe roep je de functie aan met parameternamen, bijvoorbeeld:
        ```python
        simulate_concentration(dose=300, m=80, half_life=24)
        ```
    Dit worden _keyword arguments_ genoemd. Je mag in dit geval de volgorde van de argumenten veranderen, omdat Python aan de naam ziet welke waarde bij welke parameter hoort. Het gebruik van keyword arguments maakt je code beter leesbaar. 

    Je mag de parameternamen ook weglaten. Maar je moet de argumenten dan in de juiste volgorde meegeven.
        ```python
        simulate_concentration(80, 24, 300)
        ```
    geeft een andere en hoogstwaarschijnlijk onverwachte uitkomst dan
        ```python
        simulate_concentration(300, 80, 24)
        ```
    Nu wordt het eerste argument aan `dose` gekoppeld, het tweede argument aan `m` en het derde argument aan `half_life`. Dit worden _positional arguments_ genoemd. Een functie op deze manier aanroepen is minder leesbaar en gevoeliger voor fouten, maar vergt wel minder typewerk.

    !!! opdracht-meer "Functie met positional arguments"

        1. Pas in het bestand {{file}}`phenytoin.py` de aanroepen van de functie aan zodat je geen parameternamen gebruikt. Controleer of de uitkomst gelijk blijft. Commit.
        2. Test uit wat er gebeurt als je de volgorde van de argumenten omdraait. Verklaar de uitkomst.

!!! opdracht-meer "Anti-epileptica"

    Valproïnezuur is een veelgebruikt medicijn dat bij epilepsie kan worden voorgeschreven. De farmacokinetische waarden van valproïnezuur verschillen sterk van fenytoïne. Door beide concentratiecurves naast elkaar te zetten, zie je direct hoe verschillen in de farmacokinetische waarden doorwerken in het concentratieverloop.

    De typische farmacokinetische waarden voor valproïnezuur zijn:

       * Dosering: 20-30 mg$\,$kg$^{-1} \,$dag$^{-1}$, tweemaal of vaker per dag[^farkompas-valproinezuur]
       * Halfwaardetijd: 10-15 uur[^farkompas-valproinezuur]
       * Verdelingsvolume: 0.1-0.4 L$\,$kg$^{-1}$[^tdm-valproinezuur]
       * Therapeutisch venster: 50-100 mg$\,$L$^{-1}$[^bepalingwijzer-vaproinezuur]
       * Toxische grens: > 120 mg$\,$L$^{-1}$[^bepalingwijzer-vaproinezuur]
  
    De dagelijkse dosis bereken je door het gewicht van de patiënt te vermenigvuldigen met de dosering. Deel dit getal vervolgens door het aantal doses per dag om de dosis per keer te krijgen.
  
    [^farkompas-valproinezuur]: [https://www.farmacotherapeutischkompas.nl/bladeren/preparaatteksten/v/valproinezuur](https://www.farmacotherapeutischkompas.nl/bladeren/preparaatteksten/v/valproinezuur) 
    [^tdm-valproinezuur]: [https://tdm-monografie.org/valproinezuur/](https://tdm-monografie.org/valproinezuur/)
    [^bepalingwijzer-vaproinezuur]:[https://www.umcutrecht.nl/bepalingenwijzer/valproinezuur](https://www.umcutrecht.nl/bepalingenwijzer/valproinezuur)
    
    1. Maak een nieuw bestand aan met de naam {{new_file}}`anti_epileptics.py`. Kopieer de code uit het bestand {{file}}`phenytoin.py` naar dit nieuwe bestand. 
    2. Pas de functie `#!py simulate_concentration()` aan zodat je naast de bestaande argumenten ook het verdelingsvolume en het doseringsinterval meegeeft als argumenten. Verwijder de vaste waarde voor het verdelingsvolume bovenin het bestand. Vervang ook de vaste waarde voor het doseringsinterval in de `#!py for`-loop. Gebruik het betreffende argument om te bepalen na hoeveel uur een volgende dosis wordt ingenomen.
    3. Roep de functie aan voor fenytoïne en plot de concentratiecurve. Controleer of de uitkomst overeenkomt met een uitkomst die je eerder gekregen hebt. Los eventuele fouten op. Commit.
    4. Roep nu ook de functie aan voor valproïnezuur. Kies zelf waarden die passen bij de farmacokinetische waarden die hierboven gegeven zijn. Let op: bereken eerst de dagelijkse dosis en deel deze door het aantal doses per dag om de waarde voor `dose` te bepalen. Geef beide medicijnen in dezelfde plot weer met een duidelijke legenda. Voeg ook het therapeutisch venster van valproïnezuur toe. Pas de $y$-as aan zodat beide therapeutische vensters goed zichtbaar zijn. Commit.
    5. Bekijk de twee concentratiecurves. Wat valt je op? Pas eens de massa aan en beschrijf wat er verandert in beide curves.

!!! opdracht-meer "Therapeutisch venster controleren"

    In de plot zie je aan de horizontale lijnen of de concentratie binnen het therapeutisch venster valt. Je moet de bijbehorende tijdstippen echter zelf aflezen. Schrijf daarom een functie die voor elk tijdstip waarop de concentratie buiten het therapeutisch venster valt een waarschuwing afgeeft. Gebruik voor deze opdracht het bestand {{file}}`phenytoin.py` of {{file}}`anti_epileptics.py`.

    1. Schrijf een nieuwe functie `#!py check_therapeutic_window()` die de tijdstippen, een lijst met concentraties en de onder- en bovengrens van het therapeutisch venster ontvangt. De functie controleert voor elke tijdstap of de concentratie binnen het therapeutisch venster valt. Valt de concentratie erbuiten? Print dan een waarschuwing met het bijbehorende tijdstip, de concentratie en de melding dat de concentratie onder of boven het therapeutisch venster ligt. Vergelijk de waarschuwingen met de concentratiecurve in de plot. Komt dit overeen? Commit.
    2. Roep de functie aan voor verschillende scenario's. Bij welk scenario komen de minste waarschuwingen voor? Bekijk ook of de waarschuwingen gaan over een te lage of juist een te hoge concentratie.

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

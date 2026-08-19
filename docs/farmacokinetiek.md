# Sessie 4: farmacokinetiek

In de voorgaande sessies hebben we al gezien dat programmeren handig kan zijn in bepaalde situaties. In deze sessie gaan we dieper in op iets dat je waarschijnlijk al kent: het modelleren van verschijnselen. Grote kans dat je op de middelbare school modellen gemaakt hebt in Coach.[^coach] En ook bij het huidige natuurkunde practicum gebruik je modellen om een verschijnsel te beschrijven, bijvoorbeeld om een verwachting op te stellen of je resultaten te interpreteren. 

[^coach]: [https://cma-science.nl/coach7_nl/](https://cma-science.nl/coach7_nl/)

Maar wat bedoelen we eigenlijk met het woord _model_? Een model is een vereenvoudigde weergave van de werkelijkheid. Je beschrijft een verschijnsel met formules, waarbij je keuzes maakt over wat je wel en niet meeneemt in het model. Een model dat alles probeert te beschrijven, wordt al snel te complex om mee te werken.[^aanname] Een computer is daarbij een handig hulpmiddel. Berekeningen die met de hand onpraktisch zijn[^Zuiderzee], voert een computer snel uit. En door resultaten te visualiseren, maken we de uitkomsten van het model inzichtelijk.

[^aanname]: Stel je modelleert een vallend voorwerp. In werkelijkheid speelt luchtwrijving een rol, maar die bijdrage is vaak verwaarloosbaar klein. In het model neem je daarom de luchtwrijving niet mee. Niet omdat je het effect vergeet, maar omdat het model anders onnodig ingewikkeld wordt.

[^Zuiderzee]: Een historisch voorbeeld: natuurkundige Hendrik Antoon Lorentz leidde van 1918 tot 1926 de Staatscommissie Zuiderzee, die de effecten van een afsluitdijk op de waterstanden moest berekenen.[^verslag] Dit gebeurde volledig met de hand, een enorme klus zonder computer!

[^verslag]: [https://www.lorentz.leidenuniv.nl/history/zuiderzee/zuiderzee.html](https://www.lorentz.leidenuniv.nl/history/zuiderzee/zuiderzee.html)

## Parachutesprong

In deze sessie modelleren en visualiseren we de concentratie van een medicijn in het lichaam. Maar eerst oefenen we met een kleinere opdracht: een parachutesprong. Daarbij gebruiken we een examenopgave uit 2005.[^champignon]

[^champignon]: [https://www.nvon.nl/examen/examen-2005-1-vwo-natuurkunde-12](https://www.nvon.nl/examen/examen-2005-1-vwo-natuurkunde-12)

!!! info "Aansluiting MNW-programma"

    De parachutesprong is een voorbeeld uit de klassieke mechanica. Dat is misschien niet het eerste onderwerp waar je aan denkt bij medische natuurwetenschappen, maar de onderliggende principes &mdash; krachten, beweging en weerstand &mdash; komen ook in de (bio)medische wereld voor. Bij het vak _Fysica: mechanica, electriciteit en magnetisme_ (jaar 1, periode 4 + 5) leer je onder andere meer over deze principes. En bij de module _Natuurkunde practicum_ (jaar 1, periode 1) kun je bij het experiment ultrasoondetector vallende objecten in meer detail bestuderen.

Hannes Arch is de eerste mens die een parachutesprong waagde van de Champignon, een 1800 meter hoge rots aan de noordwand van de Eiger in Zwitserland. We maken een model dat het verloop van zijn snelheid tijdens de sprong benadert. In dit model nemen we luchtweerstand mee. Voor de luchtweerstand geldt
\begin{equation}
    F_w = k \cdot A \cdot v^2.
\end{equation}
Hierin is $k$ een constante waarvan de waarde geschat wordt op $0.37 \text{ kg} \, \text{m}^{-3}$, $A$ het frontale oppervlak van de parachutist inclusief parachute in $\text{m}^2$ en $v$ de snelheid in $\text{m} \, \text{s}^{-1}$.

De massa van Hannes mét parachute is 91 kg. Zolang de parachute nog niet is geopend, is het frontale oppervlak $0.80 \text{ m}^2$. Na 13 s opent Hannes zijn parachute. De parachute ontvouwt zich geleidelijk in $3.8 \text{ s}$ tot een frontaal oppervlak van $42.6 \text{ m}^2$. Tijdens het openen van de parachute neemt het frontale oppervlak lineair toe in de tijd.

<div id="opdr:verken-probleem"></div>
!!! opdracht-basis "(Ver)ken je probleem"
    
    Voordat je gaat programmeren, is het handig om eerst het probleem te verkennen. Zo weet je welke grootheden en vergelijkingen je in het model nodig hebt. Werk op papier en overleg vooral ook met een buurmens.

    1. Maak een overzicht van alle constante grootheden en hun waarden.
    2. De parachutesprong bestaat uit drie fases. Beschrijf elke fase. Noteer per fase de tijdsgrenzen en het frontale oppervlak.
    3. Schrijf op welke vergelijkingen je nodig hebt om de snelheid op een tijdstip te berekenen. Gelden deze vergelijkingen in alle fases, of verschilt dit per fase? 

We programmeren het verloop van de snelheid tijdens de eerste $20 \text{ s}$ van de parachutesprong, met tijdstappen van $0.1 \text{ s}$. We bouwen het programma stap voor stap op en testen de code regelmatig. Zo blijven de stappen behapbaar en kun je controleren of het model het verwachte verloop geeft.

!!! opdracht-basis "Vrije val"

    1. Maak een nieuw bestand aan met de naam {{new_file}}`base_jumping.py`. Definieer bovenaan in het bestand alle constante grootheden, zie [_opdracht (Ver)ken je probleem_](#opdr:verken-probleem).
    2. Bereken de snelheid voor alle tijdstappen in de eerste fase, de fase waarin de parachute nog niet is geopend. Maak een plot waarin je de snelheid $v$ uitzet tegen de tijd $t$. Test je code. Komt de plot overeen met wat je verwacht? Commit.
    3. Bereken nu ook de snelheid voor alle tijdstappen in de tweede fase, de fase waarin de parachute zich geleidelijk ontvouwt. Breid de plot uit met deze fase. Test je code. Komt de plot overeen met wat je verwacht? Commit.
    4. Bereken nu ook de snelheid voor alle tijdstappen in de laatste fase, de fase waarin de parachute volledig geopend is. Maak een plot van alle fases. Test je code. Komt de plot overeen met wat je verwacht? Commit.

Volgens de examenopgave zou het $v,t$-diagram er als volgt uit moeten zien.[^champignon] Komt jouw plot met dit diagram overeen?
![$v,t$-diagram parachutesprong](figures/snelheid_tijd_diagram_parachutesprong.png){: style="width:60%"}

!!! opdracht-meer "Wat als?"
    
    Je hebt nu een model gemaakt van de parachutesprong. Onderzoek hoe het snelheidsverloop verandert wanneer je een parameter van het model aanpast. Kies één van de onderstaande situaties en plot verschillende scenario's in één grafiek. Geef de lijnen in de grafiek duidelijke labels.

    1. Hannes Arch heeft met parachute een massa van 91 kg. Hoe verandert het $v,t$-diagram voor een parachutespringer met meer of minder massa?
    2. Wat gebeurt er als de parachute zich niet volledig ontvouwt? Hoe verandert het $v,t$-diagram als het frontale oppervlak kleiner is? 
 
!!! warning
    Nog een meer leren opdracht nodig.

## Medicijnconcentratie in het lichaam

De aanpak die je zojuist toegepast hebt, kunnen we ook in andere situaties gebruiken. We kunnen bijvoorbeeld een model opzetten waarin we de hoeveelheid van een medicijn in het lichaam over de tijd bijhouden.

!!! opdracht-basis "Voorspellen"

    Paracetamol is een veelgebruikte pijnstiller. Stel je neemt een tablet paracetamol van 500 mg. De halfwaardetijd van paracetamol &mdash; de tijd die nodig is om de hoeveelheid in je lichaam te halveren &mdash; is gemiddeld genomen 2.5 uur.[^paracetamol-halfwaardetijd] 
    
    1. Hoe verwacht je dat de hoeveelheid paracetamol in je lichaam afneemt over de tijd? Schets een grafiek.
    2. Hoeveel procent van de paracetamol blijft er na elk uur over? Hoe bepaal je dit?

    [^paracetamol-halfwaardetijd]: [https://www.farmacotherapeutischkompas.nl/bladeren/preparaatteksten/p/paracetamol](https://www.farmacotherapeutischkompas.nl/bladeren/preparaatteksten/p/paracetamol)

Het antwoord op deze vragen laat twee verschillende manieren zien om naar hetzelfde probleem te kijken. Met een _analytische_ aanpak beschrijf je de hoeveelheid paracetamol in het lichaam met één formule. Daarmee kun je de hoeveelheid op elk willekeurig tijdstip direct berekenen. Met een _numerieke_ aanpak kijk je juist wat er per tijdstap gebeurt. Beide aanpakken beschrijven hetzelfde probleem, maar de ene aanpak kan handiger zijn dan de andere, afhankelijk van wat je met je model wilt doen. We kijken naar beide aanpakken in iets meer detail.

Bij een analytische aanpak beschrijf je de afname van de hoeveelheid paracetamol met de formule
\begin{equation}
    Q(t) = Q_0 \cdot \frac{1}{2}^{\frac{t}{t_{1/2}}}.
\end{equation}
Hierin is $Q$ de hoeveelheid op tijdstip $t$, $Q_0$ de beginhoeveelheid en $t_{1/2}$ de halfwaardetijd. Na één halfwaardetijd resteert de helft van de beginhoeveelheid: $Q=\frac{1}{2}Q_0$. Na twee halfwaardetijden resteert een kwart: $Q=\frac{1}{2}^2 \cdot Q_0 = \frac{1}{4} Q_0$. Voor paracetamol is de halfwaardetijd 2.5 uur. Na 2.5 uur is dus de helft van de beginhoeveelheid over en na 5 uur een kwart. 

Bij de numerieke aanpak bekijk je wat er per tijdstap gebeurt. Je berekent hoeveel paracetamol er na één tijdstap overblijft en gebruikt die hoeveelheid vervolgens als beginpunt voor de volgende tijdstap. De fractie $r$ die na één tijdstap $\Delta t$ overblijft, is 
\begin{equation}
    r = \frac{1}{2}^{\frac{\Delta t}{t_{1/2}}}.
\end{equation}
Voor paracetamol met een halfwaardetijd van 2.5 uur en een tijdstap van 1 uur geldt 
\begin{equation}
    r = \frac{1}{2}^{\frac{1}{2.5}} \approx 0.758.
\end{equation} 
Na elke tijdstap van 1 uur blijft dus ongeveer 75.8% van de hoeveelheid over. De hoeveelheid na de eerste tijdstap bereken je met 
\begin{equation}
    Q_1 = r \cdot Q_0
\end{equation}
en de hoeveelheid na de tweede tijdstap bereken je vervolgens met 
\begin{equation}
    Q_2 = r \cdot Q_1.
\end{equation}
Algemeen geldt:
\begin{equation}
    Q_{n+1} = r \cdot Q_n.
\end{equation}
Elke tijdstap bereken je dus aan de hand van de hoeveelheid in de vorige tijdstap. En dit is precies de manier waarop je bij de opdracht van de parachutesprong het verloop van de snelheid hebt berekend.

!!! opdracht-basis "Vergelijken"

    Leveren de twee aanpakken daadwerkelijk hetzelfde resultaat op? Je gaat dit onderzoeken door beide aanpakken te programmeren en de resultaten te vergelijken.

    1. Maak een nieuw bestand aan met de naam {{new_file}}`analytical_approach.py`. Definieer bovenaan in het bestand de beginhoeveelheid paracetamol en de halfwaardetijd. Bereken met de analytische formule, vergelijking 2, de hoeveelheid paracetamol in het lichaam voor elk uur gedurende de eerste 24 uur. Plot het resultaat. Commit.
    2. Maak een nieuw bestand aan met de naam {{new_file}}`numerical_approach.py`. Definieer bovenaan in het bestand de beginhoeveelheid paracetamol en de halfwaardetijd. Bereken de fractie $r$ met behulp van vergelijking 3. Gebruik deze fractie vervolgens om de hoeveelheid paracetamol in het lichaam stap voor stap te berekenen voor de eerste 24 uur, met tijdstappen van 1 uur. Plot het resultaat. Commit.
    3. Vergelijk beide grafieken. Komen de resultaten overeen?
    !!! warning 
        Nog een oplossing vinden om de beide grafieken echt te kunnen vergelijken (VS Code wil niet twee scripts draaien als er een grafiek open staat).

Je hebt gezien dat de analytische en numerieke aanpak voor één dosis paracetamol hetzelfde resultaat geven. Maar wat gebeurt er als we het model uitbreiden?

!!! opdracht-basis "Uitbreiden"

    Stel dat je na 6 uur een tweede tablet paracetamol van 500 mg inneemt. Bespreek met een buurmens onderstaande situaties. Je hoeft hiervoor je programma nog niet aan te passen.

    1. Kun je de analytische aanpak nog gebruiken om de hoeveelheid paracetamol in het lichaam te berekenen? Zo ja, hoe zou je dat aanpakken?
    2. Kun je de numerieke aanpak nog gebruiken om de hoeveelheid paracetamol in het lichaam te berekenen? Zo ja, hoe moet je het model aanpassen?
    3. Welke aanpak zou je kiezen als je een tweede tablet inneemt? En welke aanpak zou je kiezen als je vaker een nieuw tablet inneemt? Leg uit waarom.

De analytische aanpak is voor één dosis heel handig, je kunt voor ieder tijdstip direct berekenen hoeveel paracetamol er nog in het lichaam aanwezig is. Ook voor een tweede dosis is een analytische aanpak nog mogelijk, maar het wordt wel al wat meer gedoe. Maar hoe verder je het model uitbreidt, hoe ingewikkelder de analytische aanpak wordt. Wat als je meerdere doses inneemt? Wat als je een dosis vergeet of juist later inneemt? En wat als de snelheid waarmee paracetamol wordt verandert in de tijd? Bij de numerieke aanpak hoeven we voor deze uitbreidingen weinig te veranderen. Bij iedere tijdstap berekenen we hoeveel paracetamol er nog aanwezig is vanuit de vorige tijdstap en voegen we toe wat er tijdens die tijdstap wordt ingenomen. De berekening per tijdstap blijft hetzelfde. We kunnen daarom nieuwe situaties aan het model toevoegen zonder de hele berekening opnieuw te programmeren.

Een numerieke aanpak is dus niet per se beter dan een analytische aanpak. Voor eenvoudige problemen kan een analytische aanpak juist heel handig zijn. Een numerieke aanpak wordt vooral interessant wanneer je het model wilt uitbreiden of wanneer een analytische oplossing moeilijk of niet beschikbaar is, zoals bij de opdacht van de parachutesprong.

!!! opdracht-basis "Meerdere doses"

    Een patiënt in het ziekenhuis krijgt paracetamol als pijnstiller. De patiënt neemt elke 6 uur een tablet van 500 mg in, te beginnen op tijdstip $t=0$.

    1. Schets hoe je verwacht dat de hoeveelheid paracetamol in het lichaam gedurende de eerste 24 uur verloopt. Geef duidelijk de momenten aan waarop de patiënt een nieuwe tablet inneemt.
    2. Maak een nieuw bestand aan met de naam {{new_file}}`paracetamol.py`. Kopieer de code uit het bestand {{file}}`numerical_appraoch.py` naar dit nieuwe bestand. Pas het model aan zodat de patiënt elke 6 uur een tablet van 500 mg inneemt. Bereken de hoeveelheid paracetamol in het lichaam voor de eerste 24 uur en plot het resultaat. Commit.
    3. Vergelijk de plot met je voorspelling. Komt het verloop overeen met wat je verwachtte? Zo niet, waar zit het verschil?

!!! warning
    Informatie en opdrachten over therapeutisch venster nog toevoegen.

!!! warning
    Nieuwe Python constructen waarvoor (mogelijk) verwijzing naar appendix nodig is:

    1. Plotten
    2. Horizontale lijn in plot tekenen
    3. Importeren modules (of zit deze al in sessie 3?)
    4. ImportError (of zit deze al in sessie 3?)

    Nieuwe error constructen waarvoor (mogelijk) verwijzing naar appendix nodig is:

    5. Traceback
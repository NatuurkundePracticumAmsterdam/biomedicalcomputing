# Sessie 4: farmacokinetiek

In de voorgaande sessies hebben we al gezien dat programmeren handig kan zijn in bepaalde situaties. In deze sessie gaan we dieper in op iets dat je waarschijnlijk al kent: het modelleren van verschijnselen. Grote kans dat je op de middelbare school modellen gemaakt hebt in Coach.[^coach] En ook bij het huidige natuurkunde practicum gebruik je modellen om een verschijnsel te beschrijven, bijvoorbeeld om een verwachting op te stellen of je resultaten te interpreteren. 

[^coach]: [https://cma-science.nl/coach7_nl/](https://cma-science.nl/coach7_nl/)

Maar wat bedoelen we eigenlijk met het woord _model_? Een model is een vereenvoudigde weergave van de werkelijkheid. Je beschrijft een verschijnsel met formules, waarbij je keuzes maakt over wat je wel en niet meeneemt in het model. Een model dat alles probeert te beschrijven, wordt al snel te complex om mee te werken.[^aanname] Een computer is daarbij een handig hulpmiddel. Berekeningen die met de hand onpraktisch zijn[^Zuiderzee], voert een computer snel uit. En door resultaten te visualiseren, maken we de uitkomsten van het model inzichtelijk.

[^aanname]: Stel je modelleert een vallend voorwerp. In werkelijkheid speelt luchtwrijving een rol, maar die bijdrage is vaak verwaarloosbaar klein. In het model neem je daarom de luchtwrijving niet mee. Niet omdat je het effect vergeet, maar omdat het model anders onnodig ingewikkeld wordt.

[^Zuiderzee]: Een historisch voorbeeld: natuurkundige Hendrik Antoon Lorentz leidde van 1918 tot 1926 de Staatscommissie Zuiderzee, die de effecten van een afsluitdijk op de waterstanden moest berekenen.[^verslag] Dit gebeurde volledig met de hand, een enorme klus zonder computer!

[^verslag]: [https://www.lorentz.leidenuniv.nl/history/zuiderzee/zuiderzee.html](https://www.lorentz.leidenuniv.nl/history/zuiderzee/zuiderzee.html)

!!! opdracht-basis "Module `matplotlib` installeren"

    Voor het visualiseren van modellen gebruiken we de module `matplotlib`. Om deze module te kunnen gebruiken, moet je deze eerst installeren in de virtuele omgeving. Open in Visual Studio Code een terminal via het dropdownmenu **Terminal** en kies **New Terminal**. Installeer vervolgens de module met:
    ```
    uv pip install matplotlib
    ```

## Parachutesprong

In deze sessie modelleren en visualiseren we de concentratie van een medicijn in het lichaam. Maar eerst oefenen we met een kleinere opdracht: een parachutesprong. Daarbij gebruiken we een examenopgave uit 2005.[^champignon]

[^champignon]: [https://www.nvon.nl/examen/examen-2005-1-vwo-natuurkunde-12](https://www.nvon.nl/examen/examen-2005-1-vwo-natuurkunde-12)

!!! info "Aansluiting MNW-programma"

    De parachutesprong is een voorbeeld uit de klassieke mechanica. Dat is misschien niet het eerste onderwerp waar je aan denkt bij medische natuurwetenschappen, maar de onderliggende principes &mdash; krachten, beweging en weerstand &mdash; komen ook in de (bio)medische wereld voor. Bij het vak _Fysica: mechanica, electriciteit en magnetisme_ (jaar 1, periode 4 + 5) leer je onder andere meer over deze principes. En bij de module _Natuurkunde practicum_ (jaar 1, periode 1) kun je bij het experiment ultrasoondetector vallende objecten in meer detail bestuderen.

Hannes Arch is de eerste mens die een parachutesprong waagde van de Champignon, een 1800 meter hoge rots aan de noordwand van de Eiger in Zwitserland. We maken een model dat het verloop van zijn snelheid tijdens de sprong benadert. In dit model nemen we luchtweerstand mee. Voor de luchtweerstand geldt
\begin{equation}
    F_w = k \cdot A \cdot v^2.
\end{equation}
Hierin is $k$ een constante waarvan de waarde geschat wordt op 0.37 kg$\,$m$^{-3}$, $A$ het frontale oppervlak van de parachutist inclusief parachute in m$^2$ en $v$ de snelheid in m$\,$s$^{-1}$.

De massa van Hannes mét parachute is 91 kg. Zolang de parachute nog niet is geopend, is het frontale oppervlak 0.80 m$^2$. Na 13 s opent Hannes zijn parachute. De parachute ontvouwt zich geleidelijk in 3.8 s tot een frontaal oppervlak van 42.6 m$^2$. Tijdens het openen van de parachute neemt het frontale oppervlak lineair toe in de tijd.

<div id="opdr:verken-probleem"></div>
!!! opdracht-basis "(Ver)ken je probleem"
    
    Voordat je gaat programmeren, is het handig om eerst het probleem te verkennen. Zo weet je welke grootheden en formules je in het model nodig hebt. Werk op papier en overleg vooral ook met een buurmens.

    1. Maak een overzicht van alle constante grootheden en hun waarden.
    2. De parachutesprong bestaat uit drie fases. Beschrijf elke fase. Noteer per fase de tijdsgrenzen en het frontale oppervlak.
    3. Schrijf op welke formules je nodig hebt om de snelheid op een tijdstip te berekenen. Gelden deze formules in alle fases, of verschilt dit per fase? 

We programmeren het verloop van de snelheid tijdens de eerste 20 s van de parachutesprong, met tijdstappen van 0.1 s. We bouwen het programma stap voor stap op en testen de code regelmatig. Zo blijven de stappen behapbaar en kun je controleren of het model het verwachte verloop geeft.

!!! opdracht-basis "Parachutesprong"

    1. Maak een nieuw bestand aan met de naam {{new_file}}`base_jumping.py`. Definieer bovenaan in het bestand alle constante grootheden, zie [_opdracht (Ver)ken je probleem_](#opdr:verken-probleem).
    2. Bereken de snelheid voor alle tijdstappen in de eerste fase, de fase waarin de parachute nog niet is geopend. Maak een plot waarin je de snelheid $v$ uitzet tegen de tijd $t$. Test je code. Komt de plot overeen met wat je verwacht? Commit.
    3. Bereken nu ook de snelheid voor alle tijdstappen in de tweede fase, de fase waarin de parachute zich geleidelijk ontvouwt. Breid de plot uit met deze fase. Test je code. Komt de plot overeen met wat je verwacht? Commit.
    4. Bereken nu ook de snelheid voor alle tijdstappen in de laatste fase, de fase waarin de parachute volledig geopend is. Maak een plot van alle fases. Test je code. Komt de plot overeen met wat je verwacht? Commit.

Volgens de examenopgave zou het $v,t$-diagram er als volgt uit moeten zien.[^champignon] Komt jouw plot met dit diagram overeen?
![$v,t$-diagram parachutesprong](figures/snelheid_tijd_diagram_parachutesprong.png){: style="width:75%"}

!!! opdracht-meer "Wat als?"
    
    Je hebt nu een model gemaakt van de parachutesprong. Onderzoek hoe het snelheidsverloop verandert wanneer je een parameter van het model aanpast. Kies één van de onderstaande situaties en plot verschillende scenario's in één grafiek. Geef de lijnen in de grafiek duidelijke labels en voeg een legenda toe.

    1. Hannes Arch heeft met parachute een massa van 91 kg. Hoe verandert het $v,t$-diagram voor een parachutespringer met meer of minder massa?
    2. Wat gebeurt er als de parachute zich niet volledig ontvouwt? Hoe verandert het $v,t$-diagram als het frontale oppervlak kleiner is? 
 
???+ meer-leren "Van Hannes Arch naar Felix Baumgartner"

    Op 14 oktober 2012 sprong Felix Baumgartner uit een capsule op 38969 m hoogte, in de stratosfeer. Hij bereikte een maximale snelheid van 1357.6 km/h en doorbrak daarmee als eerste mens de geluidsbarrière in vrije val. Na 4 minuten en 19 seconden opende hij zijn parachute. De sprong is [op video vastgelegd](https://www.youtube.com/watch?v=dOoHArAzdug). 

    Voor deze sprong volstaat het model dat we voor Hannes Arch hebben opgesteld niet meer. We hebben in dat model namelijk twee aannames gedaan die dicht bij het aardoppervlak redelijk zijn, maar op bijna 39 km hoogte niet meer opgaan: de zwaartekracht is constant en de luchtdichtheid is constant. In deze opdracht modelleren we de vrije val van Felix Baumgartner en vervangen we deze aannames door betere modellen.

    We beginnen met de zwaartekracht. Hiervoor gebruiken we de gravitatiewet, die aangeeft hoe twee deeltjes elkaar aantrekken: 
    \begin{equation}
    F_z = G \cdot \frac{m \cdot M}{(R + h)^2}.
    \end{equation}
    In deze vergelijking is $F_z$ de zwaartekracht tussen twee massa's, $G$ de gravitatieconstante, $m$ de massa van Felix Baumgartner mét uitrusting (geschat op 120 kg), $M$ de massa van de Aarde, $R$ de straal van de Aarde en $h$ de hoogte boven het aardoppervlak. 

    !!! opdracht-meer "Zwaartekracht afhankelijk van hoogte"

        1. Maak een nieuw bestand aan met de naam {{new_file}}`stratos_jump.py`. 
        2. Bekijk de code in het bestand {{file}}`base_jumping.py` en kopieer de delen die je kunt hergebruiken naar {{file}}`stratos_jump.py`. Je modelleert alleen de vrije val, code die samenhangt met het openen van de parachute heb je hier niet nodig. 
        3. Zoek de waarden op van de gravitatieconstante $G$, de massa van de Aarde $M$ en de straal van de Aarde $R$, en definieer deze bovenaan in het bestand samen met de andere constante grootheden.
        4. Modelleer de eerste 250 s van de vrije val. Pas het model zo aan dat de zwaartekracht bij elke tijdstap opnieuw wordt berekend op basis van de huidige hoogte. Houd de luchtdichtheid en daarmee de luchtweerstand voor nu nog constant. _Tip_: de hoogte neemt bij elke tijdstap af. Commit.

    De luchtdichtheid verandert sterk met de hoogte. Om dit te modelleren gebruiken we het [atmosfeermodel van NASA](https://www.grc.nasa.gov/www/k-12/airplane/atmosmet.html) dat de atmosfeer in drie lagen verdeelt. In elke laag gelden andere formules voor de temperatuur en de luchtdruk. Als de luchtdruk bekend is, dan kan de luchtdichtheid berekend worden.

    In het model voor Hannes Arch gebruiken we voor de luchtweerstand
    $$
    F_w = k \cdot A \cdot v^2,
    $$
    waarbij $k$ een constante is die enkele eigenschappen van lucht en het voorwerp samenvoegt. Nu de luchtdichtheid varieert met de hoogte, moeten we deze expliciet meenemen. De volledige formule voor de luchtweerstand is:
    \begin{equation}
    F_w = \frac{1}{2} \cdot \rho(h) \cdot C_w \cdot A \cdot v^2.
    \end{equation}
    Hierin is $\rho$ de luchtdichtheid die varieert met de hoogte $h$ en $C_w$ de weerstandscoëfficiënt van het voorwerp. Voor Felix Baumgartner in vrije val schatten we $A = 1 \text{ m}^2$ en $C_w = 1$.
        
    !!! opdracht-meer "Luchtdichtheid afhankelijk van hoogte"

        5. Zoek op de [website van NASA](https://www.grc.nasa.gov/www/k-12/airplane/atmosmet.html) de formules op voor de temperatuur, de luchtdruk en de luchtdichtheid voor elk van de drie atmosfeerlagen.
        6. Voeg de drie lagen toe aan het model. Bereken bij elke tijdstap de temperatuur, de luchtdruk en de luchtdichtheid op basis van de huidige hoogte en gebruik de luchtdichtheid in de berekening van de luchtweerstand. _Tip_: gebruik `#!py from math import exp` om `#!py exp` te kunnen gebruiken bij de exponentiële functie. Commit.

    !!! opdracht-meer "Vrije val"

        Nu kun je het programma uitvoeren en zien wat de uitkomst is. Zorg dat je als uitkomst een $v,t$-diagram hebt. Vergelijk de maximale snelheid met de werkelijke waarde, 1357.6 km/h.
        
    !!! opdracht-meer "Model versus werkelijkheid"
       
        In een [video](https://www.redbull.com/int-en/fly-with-felix-red-bull-stratos-pov-video) van de sprong zijn de tijd en de snelheid zichtbaar, waardoor je het model direct kunt vergelijken met de werkelijke data. Kopieer onderstaande lijsten en zet ze bovenaan in het bestand {{file}}`stratos_jump.py`: 
            ```python
            t_real = [
                0,
                10,
                21,
                30,
                40,
                50,
                60,
                70,
                80,
                90,
                100,
                110,
                120,
                130,
                140,
                150,
                160,
                170,
                180,
                190,
                200,
                210,
                220,
                230,
                240,
                250,
            ]
            v_real = [
                0,
                364,
                749,
                1013,
                1260,
                1355,
                1196,
                917,
                726,
                611,
                500,
                440,
                386,
                375,
                359,
                347,
                312,
                286,
                285,
                271,
                229,
                221,
                219,
                213,
                210,
                199,
            ]
            ```
        Voeg de echte data toe aan je $v,t$-diagram. Hoe goed volgt het model de werkelijkheid? Waar wijkt het af en wat zou dat kunnen verklaren? Commit.
    
    !!! opdracht-meer "Geluidsbarrière" 
    
        De geluidssnelheid is afhankelijk van de temperatuur en dus van de hoogte. Bereken de geluidssnelheid op de hoogte waarop Felix Baumgartner de geluidsbarrière doorbrak en voeg deze als horizontale lijn toe aan het $v,t$-diagram. Commit.

## Hoeveelheid paracetamol in het lichaam

De aanpak die je zojuist toegepast hebt, kunnen we ook in andere situaties gebruiken. Een voorbeeld uit de klinische chemie is farmacokinetiek: het vakgebied dat beschrijft hoe het lichaam een medicijn opneemt, verdeelt, afbreekt en uitscheidt. We zetten een model op waarin we de hoeveelheid van een medicijn in het lichaam over de tijd bijhouden.

!!! info "Aansluiting MNW-programma"

    Farmacokinetiek sluit aan bij de MNW-leerlijn _Scheikunde en klinische chemie_. In het vak _Klinische en analytische chemie_ leer je analytische technieken toepassen om stoffen in geneesmiddelen en biologische monsters te meten. In het _Practicum bio-analytische chemie_ pas je die technieken toe. Het model dat we hier bouwen laat zien wat er met een medicijn in het lichaam gebeurt nadat het is ingenomen, een basis die je later in het lab kunt koppelen aan echte metingen.

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

    1. Maak een nieuw bestand aan met de naam {{new_file}}`analytical_approach.py`. Definieer bovenaan in het bestand de beginhoeveelheid paracetamol en de halfwaardetijd. Bereken met de analytische formule, vergelijking 4, de hoeveelheid paracetamol in het lichaam voor elk uur gedurende de eerste 24 uur. Plot het resultaat. Commit.
    2. Maak een nieuw bestand aan met de naam {{new_file}}`numerical_approach.py`. Definieer bovenaan in het bestand de beginhoeveelheid paracetamol en de halfwaardetijd. Bereken de fractie $r$ met behulp van vergelijking 5. Gebruik deze fractie vervolgens om de hoeveelheid paracetamol in het lichaam stap voor stap te berekenen voor de eerste 24 uur, met tijdstappen van 1 uur. Plot het resultaat. Commit.
    3. Vergelijk beide grafieken. Komen de resultaten overeen?
    !!! warning 
        Nog een oplossing vinden om de beide grafieken echt te kunnen vergelijken (VS Code wil niet twee scripts draaien als er een grafiek open staat).

Je hebt gezien dat de analytische en numerieke aanpak voor één dosis paracetamol hetzelfde resultaat geven. Maar wat gebeurt er als we het model uitbreiden?

!!! opdracht-basis "Uitbreiden"

    Stel dat je na 6 uur een tweede tablet paracetamol van 500 mg inneemt. Bespreek met een buurmens onderstaande situaties. Je hoeft hiervoor je programma nog niet aan te passen.

    1. Kun je de analytische aanpak gebruiken om de hoeveelheid paracetamol in het lichaam te berekenen? Zo ja, hoe zou je dat aanpakken?
    2. Kun je de numerieke aanpak gebruiken om de hoeveelheid paracetamol in het lichaam te berekenen? Zo ja, hoe zou je dat aanpakken?
    3. Welke aanpak zou je kiezen als je een tweede tablet inneemt? En welke aanpak zou je kiezen als je vaker een nieuw tablet inneemt? Leg uit waarom.

De analytische aanpak is voor één dosis heel handig, je kunt voor ieder tijdstip direct berekenen hoeveel paracetamol er nog in het lichaam aanwezig is. Ook voor een tweede dosis is een analytische aanpak nog mogelijk, maar het wordt wel al wat meer gedoe. Maar hoe verder je het model uitbreidt, hoe ingewikkelder de analytische aanpak wordt. Wat als je meerdere doses inneemt? Wat als je een dosis vergeet of juist later inneemt? En wat als de snelheid waarmee paracetamol wordt afgebroken verandert in de tijd? Bij de numerieke aanpak hoeven we voor deze uitbreidingen weinig te veranderen. Bij iedere tijdstap berekenen we hoeveel paracetamol er nog aanwezig is vanuit de vorige tijdstap en voegen we toe wat er tijdens die tijdstap wordt ingenomen. De berekening per tijdstap blijft hetzelfde. We kunnen daarom nieuwe situaties aan het model toevoegen zonder de hele berekening opnieuw te programmeren.

Een numerieke aanpak is dus niet per se beter dan een analytische aanpak. Voor eenvoudige problemen kan een analytische aanpak juist heel handig zijn. Een numerieke aanpak wordt vooral interessant wanneer je het model wilt uitbreiden of wanneer een analytische oplossing moeilijk of niet beschikbaar is, zoals bij de opdacht van de parachutesprong.

!!! opdracht-basis "Meerdere doses"

    Een patiënt in het ziekenhuis krijgt paracetamol als pijnstiller. De patiënt neemt elke 6 uur een tablet van 500 mg in, te beginnen op tijdstip $t=0$.

    1. Schets hoe je verwacht dat de hoeveelheid paracetamol in het lichaam gedurende de eerste 24 uur verloopt. Geef duidelijk de momenten aan waarop de patiënt een nieuwe tablet inneemt.
    2. Maak een nieuw bestand aan met de naam {{new_file}}`paracetamol.py`. Kopieer de code uit het bestand {{file}}`numerical_approach.py` naar dit nieuwe bestand. Pas het model aan zodat de patiënt elke 6 uur een tablet van 500 mg inneemt. Bereken de hoeveelheid paracetamol in het lichaam voor de eerste 24 uur en plot het resultaat. Commit.
    3. Vergelijk de plot met je voorspelling. Komt het verloop overeen met wat je verwachtte? Zo niet, waar zit het verschil?

### Therapeutisch venster

Tot nu toe hebben we de hoeveelheid paracetamol in het lichaam over de tijd berekend en geplot. Maar om te beoordelen of een medicijn ook daadwerkelijk werkt en niet schadelijk is, kijken we naar de concentratie van het medicijn in het bloed, niet naar de hoeveelheid in het lichaam. Die concentratie vergelijken we daarna met het therapeutisch venster: de zone waarbinnen een medicijn effectief is. De grenzen van het therapeutisch venster voor paracetamol verschillen iets per bron, sommige bronnen hanteren 5-20 mg/l[^venster-5-20], andere 10-20 mg/l[^venster-10-20] en weer andere 10-30 mg/l[^venster-10-30]. De ondergrens van 5 mg/l komt overeen met de minimale effectieve concentratie voor koortsvermindering, voor pijnstilling ligt de grens rond de 10 mg/l. In onze opdrachten werken we met een venster van 5-20 mg/l. 

[^venster-5-20]: I. A. Gibb en B.J.Anderson. "Paracetamol (acetaminophen) pharmacodynamics: interpreting the plasma concentration". In: _Archives of Disease in Childhood_ 2008.93 (2008), p. 241-247. 

[^venster-10-20]: [https://www.umcutrecht.nl/bepalingenwijzer/paracetamol](https://www.umcutrecht.nl/bepalingenwijzer/paracetamol)

[^venster-10-30]: [https://www.thepathologycentre.org/test/paracetamol-2/](https://www.thepathologycentre.org/test/paracetamol-2/)

!!! warning "Uitsluitend bedoeld als voorbeeld"

    De modellen in de opdrachten zijn sterk vereenvoudigd. Trek er geen conclusies uit over hoe jij paracetamol zou moeten gebruiken. Volg altijd de bijsluiter of het advies van een arts of apotheker.

Om van hoeveelheid naar concentratie te gaan, hebben we het verdelingsvolume $V_d$ nodig. Wanneer je een medicijn inneemt, verspreidt het zich over het lichaam. Een deel blijft in het bloed en een deel trekt weg naar lichaamsweefsels. De concentratie van het medicijn meten we in het bloed, maar die weerspiegelt niet de totale hoeveelheid in het lichaam. Het verdelingsvolume koppelt dit aan elkaar: het is het hypothetische volume waarin de totale hoeveelheid medicijn zich zou moeten bevinden om de gemeten bloedconcentratie te verklaren. 

Voor paracetamol is het verdelingsvolume 1 l$\,$kg$^{-1}$.[^verdelingsvolume-paracetamol] Voor het berekenen van de concentratie vermenigvuldigen we $V_d$ eerst met de lichaamsmassa $m$ om het totale verdelingsvolume in liters te krijgen. De concentratie berekenen we dan met 
\begin{equation}
C = \frac{Q}{V_d}.
\end{equation}
Voor een persoon van 80 kg en een dosis paracetamol van 500 mg geeft dat $C$ = 500 mg / (1 l$\,$kg$^{-1} \cdot$ 80 kg) = 6.25 mg/l.

[^verdelingsvolume-paracetamol]: [https://www.farmacotherapeutischkompas.nl/bladeren/preparaatteksten/p/paracetamol](https://www.farmacotherapeutischkompas.nl/bladeren/preparaatteksten/p/paracetamol)

Merk op dat dit model een vereenvoudiging is. We gaan ervan uit dat de volledige dosis direct beschikbaar is, terwijl in werkelijkheid een deel van het medicijn verloren gaat bij de eerste passage door de lever en de concentratie oploopt naar een piek. Nieuwsgierig naar wat er echt gebeurt? Op [https://trc-p.nl/23/](https://trc-p.nl/23/) lees je er meer over.

!!! opdracht-basis "Van concentratie naar therapeutisch venster"

    In het bestand {{file}}`paracetamol.py` heb je de hoeveelheid paracetamol in het lichaam over de tijd berekend en geplot, waarbij elke zes uur een nieuwe dosis wordt toegediend. We zetten de hoeveelheid nu om naar concentratie en vergelijken die met het therapeutisch venster. 

    1. Pas de code in het bestand {{file}}`paracetamol.py` aan zodat de concentratie tegen de tijd geplot wordt voor een persoon met een massa van 80 kg. Commit.
    2. Voeg het therapeutisch venster van 5-20 mg/l toe als horizontale lijnen met `#!py plt.axhline()`. Zorg voor duidelijke labels en een legenda. Commit.
    3. Ligt de concentratie paracetamol binnen het therapeutisch venster? Wat zou er gebeuren als deze persoon niet één maar twee tabletten per keer neemt?
    4. Wat verandert er als de persoon een massa van 60 kg heeft in plaats van 80 kg? En 120 kg? Dit verklaart waarom artsen de dosis van sommige medicijnen afstemmen op het lichaamsgewicht.

### Van paracetamol naar fenytoïne

Het model dat we voor paracetamol hebben gebeouwd beschrijft de concentratie in het bloed, maar de piekconcentratie ligt maar net boven de ondergrens. Het effect van een andere dosering of een vergeten dosis is daardoor moeilijker zichtbaar te maken. Om de kracht van farmacokinetische modellen beter te laten zien, kijken we naar een medicijn waarbij een vergeten dosis directe klinische gevolgen kan hebben.

Fenytoïne is een medicijn dat wordt gebruikt bij epilepsie. Het onderdrukt overmatige elektrische activiteit in de hersenen en voorkomt daarmee aanvallen. Wat fenytoïne bijzonder maakt vanuit farmacokinetisch oogpunt, is het therapeutisch venster. De concentratie in het bloek moet tussen de 8 mg/l en 20 mg/l liggen. Onder de 8 mg/l is het medicijn onvoldoende werkzaam en bestaat er het risico op een epileptische aanval. Boven de 20 mg/l treedt toxiciteit op, met bijwerkingen zoals nystagmus (onwillekeurige oogbewegingen), coördinatiestoornissen en verwardheid. De toxische grens valt hier samen met de bovengrens van het therapeutisch venster, er is dus geen veiligheidsmarge. 

De relevante parameters voor fenytoïne zijn:

* Dosering: 200-400 mg/dag[^farkompas-fenytoine]
* Halfwaardetijd: ongeveer 24 uur[^farkompas-fenytoine]
* Verdelingsvolume: ongeveer 0.65 l/kg[^farkompas-fenytoine]
* Therapeutisch venster: 8-20 mg/l[^bepalingwijzer-fenytoine]
* Toxische waarde: > 20 mg/l[^bepalingwijzer-fenytoine]

[^farkompas-fenytoine]: [https://www.farmacotherapeutischkompas.nl/bladeren/preparaatteksten/f/fenytoine](https://www.farmacotherapeutischkompas.nl/bladeren/preparaatteksten/f/fenytoine)

[^bepalingwijzer-fenytoine]: [https://www.umcutrecht.nl/bepalingenwijzer/fenytoine](https://www.umcutrecht.nl/bepalingenwijzer/fenytoine)]

Net als bij paracetamol maken we ook hier een vereenvoudigd model. We gaan er opnieuw vanuit dat de absorptie onmiddelijk en volledig plaatsvindt en dat het medicijn zich gelijkmatig verdeelt over het verdelingsvolume. De werkelijkheid is complexer.
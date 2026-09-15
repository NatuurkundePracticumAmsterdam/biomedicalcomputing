# Package: matplotlib

Met matplotlib kun je grafieken maken, zoals je dat op het natuurkundepracticum gewend bent met Tailor te doen. Alleen: Tailor is een grafische applicatie die je niet aan kunt sturen met een Pythonscript. Met matplotlib kan dat wel, en heb je veel meer vrijheid om je grafiek aan te passen.

We bespreken het gebruik van dit package stap voor stap. Als je dit al gelezen hebt en snel iets op wilt zoeken dan is de [samenvatting](#samenvattend) handig.

## Installatie

Om deze module te kunnen gebruiken, moet je deze eerst installeren in de virtuele omgeving. Open in Visual Studio Code een terminal via het dropdownmenu **Terminal** en kies **New Terminal**. Installeer vervolgens de module met:
```
uv pip install matplotlib
```

## Benodigdheden

Zet bovenaan je script:
```py
import matplotlib.pyplot as plt
```
en onderaan je script:
```py
plt.show()
```
om ervoor te zorgen dat de plot aan het eind van je script ook daadwerkelijk getoond wordt. Vergeet je deze regel, dan sluit je script af als hij klaar is en krijg je de grafiek niet te zien. Tussen deze twee regels kun je de rest van je script schrijven.

## Data invoeren

Als je een grafiek wilt maken met matplotlib dan moet je natuurlijk eerst de data definiëren. Dat kan door lists aan te maken. Je mag elke naam kiezen, maar voor dit voorbeeld nemen we `x_data` en `y_data`, en een tweede dataset `y2_data`.
```py
x_data = [0, 1, 2, 3, 4, 5]
y_data = [0, 2, 5, 8, 15, 27]
y2_data = [0, 1, 3, 5, 10, 20]
```

## Een dataset plotten

Om een dataset in de grafiek te plotten maak je gebruik van de `#!py plt.plot()` functie:
```py
plt.plot(x_data, y_data)
```
Als je meerdere datasets in dezelfde grafiek wilt weergeven dan mag je meerdere `#!py plt.plot()` aanroepen doen:
```py
plt.plot(x_data, y_data)
plt.plot(x_data, y2_data)
```

## Grootheden en eenheden langs de assen plaatsen

Het is belangrijk om in een grafiek te laten zien _wat_ je precies geplot hebt. Wat staat er langs de assen? Voeg aslabels toe met:
```py
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
```

## Het bereik van de assen

Matplotlib schaalt de assen automatisch zodat de alle metingen te zien zijn, maar laat ook wat extra ruimte over. Daardoor komt het vaak voor dat een grafiek niet in de oorsprong begint. Je kunt het bereik van de assen aanpassen met:
```py
plt.xlim(0, 5)
plt.ylim(0, 30)
```
Bovenstaande code past het bereik van de x-as aan zodat hij begint bij 0 en loopt tot 5, en de y-as van 0 tot 30.

## Een legenda toevoegen

Als je meerdere datasets plot dan is het handig om aan te geven welke dataset waarbij hoort. Je kunt dit doen met een legenda. Je moet dan wel bij je `#!py plt.plot()` aanroepen een label meegeven, en aan het eind van je plot-code een legenda maken. Doe dit pas nadat je alle datasets geplot hebt, anders is de legenda niet compleet:
```py
plt.plot(x_data, y_data, label="Fast car")
plt.plot(x_data, y2_data, label="Slow car")

...

plt.legend()
```

## Horizontale en verticale lijnen toevoegen

Het kan handig zijn om hulplijnen toe te voegen aan je grafiek die bijvoorbeeld een kritische waarde aangeven, of het bereik waarin je gegevens betrouwbaar zijn. Een verticale lijn maak je aan met `#!py plt.axvline()` en een horizontale met `#!py plt.axhline()`. Geef als argument de positie op de x-as of de y-as waar de lijn getekend moet worden, en eventueel een label als je wilt dat die verschijnt in de legenda:
```py
plt.axvline(3, label="3-second mark")
plt.axhline(15, label="15-meter line")
```

## Kleur, marker en lijnstijl, en volgorde van plotten

Om duidelijker onderscheid te maken tussen alle lijnen en datasets wil je wellicht de kleur aanpassen, of zelfs de lijnstijl. Op het natuurkundepracticum leer je bijvoorbeeld om je datapunten _niet_ te verbinden met een lijn, maar je metingen als losse punten weer te geven. Dat kan met de parameters `marker`, `linestyle` en `color`. De marker geeft het datapunt weer en is bijvoorbeeld een `o` (cirkel), `.` (punt), `s` (vierkant), enz. Zie [hier](https://matplotlib.org/stable/api/markers_api.html) voor een volledige lijst. Linestyle (de lijn die de punten verbindt) kan zijn `-` (`solid`), `:` (`dotted`), `--` (`dashed`) of `-.` (`dashdot`). Een volledige lijst staat [hier](https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html) verstopt in de code. De color kan een enkele letter zijn als `r` (rood), `g` (groen) of `b` (blauw), of een naam uit de lijst met zogeheten CSS kleuren. Die lijst vind je [hier](https://matplotlib.org/stable/gallery/color/named_colors.html#css-colors). Onze code wordt dan bijvoorbeeld:
```py
plt.axvline(3, color="orange", label="3-second mark")
plt.axhline(15, color="lightgrey", label="15-meter line")

plt.plot(x_data, y_data, color="r", marker="s", linestyle="", label="Fast car")
plt.plot(x_data, y2_data, color="seagreen", marker="o", linestyle=":", label="Slow car")
```
De eerste dataset heeft geen linestyle (`""`) dus er worden alleen punten weergegeven. Het valt je misschien op dat we de volgorde van aanroepen verandert hebben: éérst de horizontale en verticale lijnen en dan pas de datasets. Dit zorgt ervoor dat de datasets bovenop de lijnen geplot worden, met de lijnen op de achtergrond.

## Samenvattend

De code van bovenstaand voorbeeld is samengevoegd:
```py
import matplotlib.pyplot as plt

x_data = [0, 1, 2, 3, 4, 5]
y_data = [0, 2, 5, 8, 15, 27]
y2_data = [0, 1, 3, 5, 10, 20]

plt.axvline(3, color="orange", label="3-second mark")
plt.axhline(15, color="lightgrey", label="15-meter line")

plt.plot(x_data, y_data, color="r", marker="s", linestyle="", label="Fast car")
plt.plot(x_data, y2_data, color="seagreen", marker="o", linestyle=":", label="Slow car")

plt.xlabel("Time (s)")
plt.ylabel("Position (m)")

plt.xlim(0, 5)
plt.ylim(0, 30)

plt.legend()

plt.show()
```

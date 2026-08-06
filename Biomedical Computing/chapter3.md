
# 3. Rekenwerk

In de vorige sessie heb je al gemerkt dat een computer heel geschikt is om een eenvoudig klusje dat 10.000 keer herhaald moet worden uit te voeren zodat jij dat niet zelf hoeft te doen. Een ander groot voordeel is dat een computer kan rekenen. *To compute* betekent niet voor niets *berekenen.* Rekenwerk kan natuurlijk ook met de hand, maar is niet altijd het leukste klusje om te doen. Daarnaast is het mogelijk dat er ergens een fout(je) insluipt. Zeker als bepaald rekenwerk meer dan eens gedaan moet worden, is het fijn om dit te programmeren.

HERHALING: ACTIONS IN UNDERSTANDING?

### Het ene getal is het andere niet

Je hebt de vorige sessie al gemerkt dat als je Python vertelt hoe oud je bent, je het antwoord niet direct kunt gebruiken maar van de *tekst* “18” eerst het *getal* 18 moet maken met de functie int(). Dat is ook nodig als je wilt gaan rekenen. Blijkbaar kent Python verschillende *datatypes*.

Bekijk de code en voorspel wat iedere regel doet.

Code met strings: str + str, 4 \* str, str(12345). Int(“18”), int + int, int - int, int \* int, int \*\* int. Type(“18”), type(18). Type(18 / 2).

Float(“18.5”). Float \* float. 20 / 3. 20 // 3. 20 % 3.

List + list, int \* list.

A = 4, b = 5, c = 10, d = 8, (a + b) \* (c - d).

### Stralingsveiligheid

Ioniserende straling is gevaarlijk, maar kan ook heel nuttig zijn bij de behandeling van tumoren of bij diagnostiek. Het is dan wel belangrijk om ervoor te zorgen dat patiënten en zorgpersoneel  zo min mogelijk straling ontvangen. Daarom zal een tandarts(assistent) ook altijd kort de behandelruimte verlaten op het moment dat er een röntgenfoto van je gebit wordt gemaakt. Doen ze dat niet, dan ontvangen ze de straling van tientallen, zo niet honderden, röntgenfoto’s per jaar. Ook bij het produceren van radioactieve isotopen of bij het doen van wetenschappelijk onderzoek kunnen medewerkers blootgesteld worden aan straling. Bij alfa- en bètastraling is het niet heel ingewikkeld om de medewerkers af te schermen. Bij gammastraling is dat wél een probleem: deze straling heeft een groot doordringend vermogen en is moeilijk af te schermen. Daarom worden regelmatig berekeningen gemaakt om de ontvangen equivalente dosis (in Sievert) te bepalen. Op deze manier kan in de gaten gehouden of een medewerker niet teveel straling ontvangt.

Omdat de exacte hoeveelheid ontvangen straling wordt bijgehouden met badges die de medewerkers op hun lichaam dragen is het vaak voldoende om voor de berekeningen gebruik te maken van een vuistregel:

H = gamma \* A \* t / r\*\*2

Met de ontvangen equivalente dosis H, de gammaconstante van de bron gamma, de activiteit van de bron A, de blootstellingstijd t en de afstand tot de bron r. Voor cesium-137 is de gammaconstante gelijk aan 84 microsievert square meter per gigabecquerel per hour.

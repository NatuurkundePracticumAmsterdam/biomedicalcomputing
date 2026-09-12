# Package: lmfit

Met lmfit kun je een model fitten aan metingen, precies zoals je dat op het natuurkundepracticum gewend bent met Tailor te doen. Alleen: Tailor is een grafische applicatie die je niet aan kunt sturen met een Pythonscript. Met lmfit kan dat wel.

Tailor is handig als je snel verschillende dingen wil proberen en vergelijken en één of twee keer een set metingen wilt verwerken. Lmfit is handig als je een analyse vaker en op _precies dezelfde manier_ wilt herhalen. Run je script, en je weet _zeker_ dat je dezelfde fit doet als de vorige keer. Het is alleen wel meer typewerk en je moet je houden aan de 'spelregels'.

## Installatie

Om lmfit te installeren in je venv, open een terminal in Visual Studio Code en type in:
```
uv pip install lmfit
```

## Data invoeren

Als je een fit wilt uitvoeren met lmfit dan moet je natuurlijk eerst de data definiëren. Dat kan door lists aan te maken. Je mag elke naam kiezen, maar voor dit voorbeeld nemen we $x$ en $y$:
```py
x_data = [0, 1, 2, 3, 4, 5]
y_data = [0, 1, 5, 8, 15, 27]
```

## Een model definiëren

Je wilt je meetgegevens fitten aan een model. Zet bovenaan je script:
```py
from lmfit.models import ExpressionModel
```
Hiermee _importeer_ je de functionaliteit van het lmfit-package. Daarna kun je in je script een model definiëren in dezelfde notatie als waarmee je een berekening uitvoert. Stel dat we de data willen fitten aan:
\begin{equation}
y = a x^2 + b,
\end{equation}
een kwadratische vergelijking met parameters $a$ en $b$, dan zouden we dat uitrekenen in Python als
```py
y = a * x**2 + b
```
Als we met dit model de fit kunnen doen dan definieer je dat als volgt:
```py
model = ExpressionModel("a * x**2 + b", independent_vars=["x"])
```
Met `#!py independent_vars=["x"]` geef je lmfit een lijst van _onafhankelijke variabelen_. Dat is in ons geval altijd de variabele die je op de $x$-as uitzet. Die mag elke naam hebben, als je maar consequent bent.

## De fit uitvoeren

Het daadwerkelijk fitten van het model aan de metingen doe je als volgt:
```py
fit = model.fit(y_data, x=x_data, a=1, b=1)
```
De eerste parameter is de variabele met de metingen (in ons geval `y_data`). Met `x=x_data` geven we aan dat we voor de `x` uit ons model de waardes uit `x_data` gaan gebruiken. Met `a=1` en `b=1` geven we startwaardes voor de parameters. Daarna gaat lmfit de beste waardes proberen te vinden.

## Het fit-resultaat

Als de fit gelukt is zonder foutmelding, dan bevat de variabele `fit` alle informatie over de beste fit. De informatie over de parameters is opgeslagen in `fit.params`. Je kunt de parameter `a` benaderen met `#!py fit.params['a']`. De waarde is beschikbaar in `.value` en de onzekerheid in `.stderr` (afkorting van _standard error_), als volgt:
```py
a_value = fit.params['a'].value
a_uncertainty = fit.params['a'].stderr
```

## Samenvattend

De code van bovenstaand voorbeeld is samengevoegd:
```py
from lmfit.models import ExpressionModel

x_data = [0, 1, 2, 3, 4, 5]
y_data = [0, 1, 5, 8, 15, 27]

model = ExpressionModel("a * x**2 + b", independent_vars=["x"])
fit = model.fit(y_data, x=x_data, a=1, b=1)

a_value = fit.params['a'].value
a_uncertainty = fit.params['a'].stderr
```

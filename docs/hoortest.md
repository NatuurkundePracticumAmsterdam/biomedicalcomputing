# Sessie 6: audiologie

Tot nu toe hebben we Python-programma's geschreven voor het doorzoeken van data, het maken van berekeningen en het opstellen en simuleren van modellen. In deze sessie schrijven we een Python-programma voor het uitvoeren van een diagnostische test. Zo'n test zouden we ook met de hand kunnen uitvoeren, maar door hem te automatiseren wordt hij sneller, nauwkeuriger en betrouwbaarder. Natuurlijk kost het schrijven van een Python-programma tijd, maar daarna kunnen we hem wel steeds opnieuw gebruiken. 

!!! info "Aansluiting MNW-programma"

    In deze sessie ontwikkelen we een programma voor een eenvoudige hoortest. Daarmee sluit de sessie aan bij het vak _Natuurkunde en gezondheid_ (jaar 1, periode 5), waarbinnen onder andere het vakgebied audiologie aan bod komt. Audiologie richt zich op het gehoor en op gehoorproblemen. Een hoortest is één van de methoden om het gehoor te onderzoeken.
    
## Module `sounddevice`     

Voor het uitvoeren van een hoortest heb je geluid nodig. Daarvoor gebruiken we de Python-module `sounddevice`, waarmee we audio kunnen afspelen op een laptop. De basisstructuur van zo'n programma ziet er als volgt uit: 
```py
import sounddevice as sd

# create a sine wave
# store the sine wave values in a list called values
...

# play the tone and wait until it has finished
sd.play(values, samplerate=44100)
sd.wait()
```
Eerst importeren we de module. Daarna maken we een lijst aan met de waarden van de sinusgolf (dit deel programmeer je later zelf). Met `sd.play()` spelen we de toon af. We geven daarbij de lijst met de waarden van de sinusgolf en een bemonsteringsfrequentie (Engels: sample rate) mee. De bemonsteringsfrequentie geeft aan hoeveel waarden per seconde worden gebruikt bij het afspelen van het signaal. Wij gebruiken een bemonsteringsfrequentie van 44100 Hz, wat een standaardwaarde is in audio. De duur van de toon hangt af van de lengte van de lijst. Bij een bemonsteringsfrequentie van 44100 Hz en een lijst van 44100 elementen duurt de toon precies één seconde. Tot slot zorgt `sd.wait()` ervoor dat het programma wacht totdat de toon volledig is afgespeeld, voordat het verdergaat.

!!! warning "Gebruik een koptelefoon"

    Gebruik tijdens deze sessie een koptelefoon. Zo voorkom je dat verschillende geluiden in het lokaal elkaar verstoren. Bovendien kan een koptelefoon lage frequenties, en soms ook hoge frequenties, meestal beter afspelen dan de ingebouwde luidsprekers van een laptop. Daardoor kun je de grenzen van je gehoor beter bepalen. Houd er wel rekening mee dat ook koptelefoons een beperkt frequentiebereik kunnen hebben. Als je een lage of hoge toon niet hoort, zou dat dus aan de koptelefoon kunnen liggen.
    
!!! opdracht-basis "Toon afspelen"

    1. Maak een nieuw bestand aan met de naam {{new_file}}`play_tone.py`. Definieer bovenaan in het bestand de frequentie van 1000 Hz en maak een lege lijst `values` aan om de waarden van de sinusgolf in op te slaan. 
    2. Schrijf een for-loop om de lijst `values` te vullen met 44100 elementen, zodat de toon één seconde duurt. Commit.
    3. Speel de toon af en controleer of je de toon hoort. 
    4. Zorg ervoor dat het programma de frequentie print van de toon die wordt afgespeeld. Bijvoorbeeld: `Playing a tone of 1000 Hz.` Zet het print-statement vóór het afspelen van de toon. Controleer of je programma zowel print als de toon afspeelt. Commit.

!!! opdracht-basis "Spelen met geluid"

    1. Nu je een toon van 1000 Hz kunt afspelen, kun je ook andere tonen afspelen. Pas de frequentie aan en controleer of je een andere toonhoogte hoort. 
    2. De toon die je afspeelt duurt nu één seconde. Pas je code aan om een toon van twee seconden af te spelen. Doe dit daarna ook voor vijf seconden en voor tien seconden.

!!! opdracht-basis "Quick-'n-dirty hoortest"

    Probeer met behulp van je programma te achterhalen wat de laagste en de hoogste frequentie is die je nog kunt horen. 

!!! opdracht-meer "Fade out"

    Je kunt natuurlijk het volume van de toon aanpassen via de instellingen van je laptop. Maar je kunt de toon ook zachter of harder maken door de amplitude van het signaal aan te passen. 
    
    1. Maak een nieuw bestand aan met de naam {{new_file}}`fade_out.py` en kopieer je code uit het bestand {{file}}`play_tone.py` naar dit bestand. 
    2. Pas de code aan zodat de amplitude van de sinusgolf geleidelijk afneemt naar nul. Commit.

!!! opdracht-meer "Stereo panning"

    Bij een gehoortest wil je soms het linker- en het rechteroor apart testen. Met stereogeluid kun je een toon aan één oor aanbieden door het signaal alleen via de linker- of rechterluidspreker af te spelen. 

    De module `sounddevice` ondersteunt stereogeluid. Je geeft dan `sd.play()` een lijst mee waarin elk element bestaat uit twee waarden: één voor het linkerkanaal en één voor het rechterkanaal. Om het signaal alleen links af te spelen, zet je de rechterwaarde op nul: 
    ```python
    values_left.append([value, 0])
    ```
    Om het signaal alleen rechts af te spelen, zet je de linkerwaarde op nul. 

    1. Maak een nieuw bestand aan met de naam {{new_file}}`stereo_panning.py` en kopieer je code uit het bestand {{file}}`play_tone.py` naar dit bestand. 
    2. Maak nu twee aparte lijsten: één voor alleen links en één voor alleen rechts. Speel beide tonen daarna af. Print vóór het afspelen de frequentie en via welke luidspreker de toon wordt afgespeeld. Commit.

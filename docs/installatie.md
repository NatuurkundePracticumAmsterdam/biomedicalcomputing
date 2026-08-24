# Sessie 1: installatie van benodigde software

In deze sessie heb je al flink wat code gezien en gelezen, maar je hebt nog niet zelf code geschreven. Voordat je dat kunt, moet je een aantal programma's installeren. Je hebt het volgende nodig: 

* _Python_: de programmeertaal die we gebruiken
* _uv_: een tool om Python en losse pakketten te installeren
* _Visual Studio Code_: de editor waarin je straks code schrijft
* _GitHub Desktop_: een programma om je code online te kunnen bewaren

In de volgende opdracht vind je de installatie-instructies. Aangezien deze instructies afhankelijk zijn van het besturingssysteem zijn er specifieke instructies geschreven voor macOS en voor Windows. De instructies gaan ervan uit dat je Python, uv, Visual Studio Code én GitHub Desktop nog niet geïnstalleerd hebt. Heb je één of meer van deze programma's al geïnstalleerd, kijk dan even welke stappen je kunt overslaan.

!!! opdracht-basis "Benodigde programma's installeren"

    === "macOS"

        Hieronder staan de installatie-instructies voor **macOS**. Heb je Windows op je laptop staan, ga dan naar het tabblad Windows. 
        <br><br>

        **Stap 1: installeer Homebrew**

        We gebruiken Homebrew, een populaire package manager voor macOS, om de benodigde programma's te installeren.

        1. Open een terminal door op ++cmd+space++ te drukken en te zoeken op _Terminal_.
        2. Kopieer het volgende commando en plak het in de terminal:
            ```
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
            ```
        3. Sluit de terminal af.
        <br><br>

        **Stap 2: installeer uv, Visual Studio Code en GitHub Desktop**
        
        4. Open opnieuw een terminal door op ++cmd+space++ te drukken en te zoeken op _Terminal_.
        5. Kopieer de volgende commando's en plak deze in de terminal:
            ```
            brew install uv
            brew install visual-studio-code
            brew install github
            ```
        6. Sluit de terminal af.
        <br><br>

        **Stap 3: installeer Python**

        7. Open nogmaals een terminal door op ++cmd+space++ te drukken en te zoeken op _Terminal_.
        8. Kopieer het volgende commando en plak het in de terminal:
            ```
            uv python install 
            ```
        9. Sluit de terminal af.

    === "Windows"

        Hieronder staan de installatie-instructies voor **Windows**. Heb je macOS op je laptop staan, ga dan naar het tabblad macOS. 
        <br><br>

        **Stap 1: installeer uv, Visual Studio Code en GitHub Desktop**
   
        We gebruiken Winget, een package manager die standaard beschikbaar is op Windows, om de benodigde programma's te installeren.

        10. Open een terminal door in het zoekveld van de taakbalk te zoeken op _Windows PowerShell_.
        11. Kopieer de volgende commando's en plak deze in de terminal:
            ```
            winget install astral-sh.uv
            winget install microsoft.visualstudiocode
            winget install github.githubdesktop
            winget install git.git
            ```
        12. Sluit de terminal nog niet af.
        <br><br>

        **Stap 2: sta het uitvoeren van scripts toe**

        In de PowerShell, de terminal die Visual Studio Code gebruikt, is het standaard niet toegestaan om scripts uit te voeren. Het volgende commando staat dat toe voor de huidige gebruiker, maar alleen voor scripts van vertrouwde partijen, zoals Microsoft. Willekeurige of onbekende scripts worden ook na dit commando nog steeds geblokkeerd. 

        13. Kopieer het volgende commando en plak het in de terminal:
            ```
            Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
            ```
        14. Sluit de terminal af.
        <br><br>

         **Stap 3: installeer Python**

        15. Open opnieuw een terminal door in het zoekveld van de taakbalk te zoeken op _Windows PowerShell_.
        16. Kopieer het volgende commando en plak het in de terminal:
            ```
            uv python install 
            ```
        17. Sluit de terminal af.

Nu de programma's zijn geïnstalleerd, installeren we twee extensies voor Visual Studio Code.[^installatie-extensies] Met extensies voeg je aan Visual Studio Code extra functionaliteiten toe, in ons geval ondersteuning voor Python en een tool die je code automatisch netjes maakt. 

[^installatie-extensies]: We kiezen er voor om nu de extensies via de terminal te installeren. Maar je kunt ze ook installeren via Visual Studio Code zelf. Klik daarvoor op het blokjes-icoon in de linkerbalk, zoek op de naam van de extensie en klik op _Install_.

!!! opdracht-basis "Benodigde extensies installeren"

    === "macOS"

        Hieronder staan de installatie-instructies voor **macOS**. Heb je Windows op je laptop staan, ga dan naar het tabblad Windows. 
        <br><br>
        
        1. Open een terminal door op ++cmd+space++ te drukken en te zoeken op _Terminal_.
        2. Kopieer de volgende commando's en plak deze in de terminal:
            ```
            code --install-extension ms-python.python
            code --install-extension charliermarsh.ruff
            ```
        3. Sluit de terminal af.
    
    === "Windows"

        Hieronder staan de installatie-instructies voor **Windows**. Heb je macOS op je laptop staan, ga dan naar het tabblad macOS. 
        <br><br>

        1. Open een terminal door in het zoekveld van de taakbalk te zoeken op _Windows PowerShell_.   
        2. Kopieer de volgende commando's en plak deze in de terminal:
            ```
            code --install-extension ms-python.python
            code --install-extension charliermarsh.ruff
            ```
        3. Sluit de terminal af. 

Bijna klaar &mdash; nu de programma's en extensies zijn geïnstalleerd, passen we nog een aantal instellingen aan in Visual Studio Code, onder andere om te zorgen dat de extensies ook echt hun werk kunnen doen. Zo stellen we in dat elke keer als je een bestand opslaat met ++cmd+s++ (macOS)/++ctrl+s++ (Windows) de tool Ruff aan het werk gaat: je code wordt opgeschoond en import statements worden gesorteerd. Daardoor hoef je je veel minder druk te maken over hoe netjes je code eruitziet.

!!! opdracht-basis "Instellingen Visual Studio Code"

    Onderstaande stappen zijn gelijk voor macOS en Windows.

    1. Open Visual Studio Code.
    2. Kies via het dropdownmenu **File** voor **Preferences > Settings**. 
    3. Typ in het zoekvenster _chat: disable AI features_ en vink de instelling aan.
    4. Typ in het zoekvenster _format on save_ en vink de bovenste instelling aan.
    5. Typ in het zoekvenster _@lang:python default formatter_ en kies _Ruff_.
    6. Typ in het zoekvenster _@lang:python code actions on save_, kies _Edit in settings.json_ en selecteer _source.organizeImports.ruff_. Zet de waarde op _explicit_. De volledige regel luidt dan: ```"source.organizeImports.ruff": "explicit"```. Sla de wijzigingen op via het dropdownmenu **File** en kies **Save** of met ++cmd+s++ (macOS)/++ctrl+s++ (Windows).
    7. Sluit de tabbladen met de instellingen.

Dat was het voor sessie 1: de programma's staan klaar en de instellingen zijn goed. Je bent klaar voor sessie 2 {{feesttoeter}} We gaan in sessie 2 de eerste regels Python-code schrijven in Visual Studio Code. Hoe dat precies werkt leggen we dan stap voor stap uit.

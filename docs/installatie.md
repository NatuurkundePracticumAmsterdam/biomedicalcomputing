# Sessie 1: installatie van benodigde software

## Introductie

We beschrijven hier de installatie van een ontwikkelomgeving voor Python. De instructies gaan er vanuit dat je een _schone_ omgeving hebt, dus zonder Python en Visual Studio Code bijvoorbeeld. Kijk dus zelf welke instructies je precies nodig hebt. Eerst volgen instructies die voor Windows en MacOS verschillend zijn. Daarna volgen nog algemene instructies. _Lees die ook!_

## Installatie &mdash; Windows

We gebruiken uv, Visual Studio Code en GitHub Desktop. Je kunt die via de verschillende websites downloaden en installeren, maar het kan ook vanuit een terminal met Winget, een populaire package manager. Doe vooral wat je fijn vindt. Als je Winget wilt gebruiken: open een _Terminal_ en type in:

```
winget install astral-sh.uv
winget install microsoft.visualstudiocode
winget install github.githubdesktop
winget install git.git
```

In de PowerShell (de standaard shell) is het nodig om toestemming te geven om scripts uit te voeren. Het volgende commando staat dat toe voor de huidige gebruiker (jijzelf) voor scripts die digitaal zijn ondertekend waardoor Microsoft ze kan blokkeren als dat nodig is. Dit is dus een veilige optie. Type in:

```
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Open een _nieuwe_ Terminal en installeer Python:

```
uv python install
```

## Installatie &mdash; macOS

We gebruiken uv, Visual Studio Code en GitHub Desktop. Je kunt die via de verschillende websites downloaden en installeren, maar het kan ook vanuit een terminal met Homebrew, een populaire package manager. Doe vooral wat je fijn vindt. Installeer de package manager _Homebrew_ als volgt. Open een _terminal_ en type in (of kopieer van [https://brew.sh](https://brew.sh)):

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Sluit de terminal af en open een _nieuwe_ terminal. We installeren de ontwikkelomgeving met:

```
brew install uv
brew install visual-studio-code
brew install github
```

Open opnieuw een _nieuwe_ terminal en installeer Python:

```
uv python install
```

Zie voor verdere instructies de volgende secties.

## VS Code extensions &mdash; Alle OSes

Sluit de terminal of prompt af. Je kunt in Visual Studio Code zelf extensies zoeken en installeren door te klikken op het 'blokjes' icoon in de linkerbalk. De namen van de extenties staan hieronder. Je kunt ze ook in een terminal of prompt installeren. Open dan een _nieuwe_ terminal of prompt. We installeren de extensions voor Visual Studio Code in één keer met:

```
code --install-extension ms-python.python
code --install-extension charliermarsh.ruff
code --install-extension tamasfe.even-better-toml
code --install-extension njpwerner.autodocstring
```

## Instellingen VS Code &mdash; Alle OSes

Er zijn drie instellingen om je code automatisch wat op te schonen en import statements te sorteren. Op die manier hoef je je veel minder druk te maken over hoe netjes je code eruitziet. Elke keer als je je bestand opslaat gaat de tool _ruff_ aan het werk.

1. Open de app "Visual Studio Code".
2. Kies **File>Preferences>Settings** of druk op ++ctrl+comma++ (control-komma).
3. Type nu in het zoekvenster: `chat: disable AI features` en vink de instelling aan.
4. Type nu in het zoekvenster: `format on save` en vink de bovenste instelling aan.
5. Type nu in het zoekvenster: `@lang:python default formatter` en kies `Ruff`
6. Type nu in het zoekvenster: `@lang:python code actions on save` en kies `Edit in settings.json` en kies dan in het menuutje `source.organizeImports.ruff` en dan `explicit`.
7. Sla dan het bestand op met **File>Save** of ++ctrl+s++.
8. Sluit de settingstabbladen.

Zodra je een Pythonbestand hebt geopend kun je rechts onderin bij `Select interpreter` het juiste environment kiezen.

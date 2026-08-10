# Het ene getal is het andere niet

Je hebt de vorige sessie al gemerkt dat als je Python vertelt hoe oud je bent, je het antwoord niet direct kunt gebruiken maar van de *tekst* “18” eerst het *getal* 18 moet maken met de functie int(). Dat is ook nodig als je wilt gaan rekenen. Blijkbaar kent Python verschillende *datatypes*.

Bekijk de code en voorspel wat iedere regel doet, vóórdat je het uitprobeert.

```py linenums="1"
# Strings
text1 = "Hoi" + "Alice"
text2 = 40 * '='
text3 = str(12345)

# Integers
number1 = int("42")
number2 = 14 + 12
number3 = 14 - 12
number4 = 12 * 12
number5 = 16**2

# Check datatypes
print(type("42"))
print(type(42))

# Floating point numbers
number6 = float("18.2")
number7 = 1.1 * 2.2
number8 = 20 / 3
number9 = 20 // 3
number10 = 20 % 3

# Lists
newlist1 = [1, 2, 3] + [4, 5, 6]
newlist2 = 10 * [1, 2, 3]

# Order of calculation
a = 4
b = 5
c = 10
d = 8
result = (a + b) * (c - d)
```
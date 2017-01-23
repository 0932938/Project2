import random

class vragen:
    def __init__(self, vraagafbeelding, Antwoord):
        self.vraag = vraagafbeelding
        self.Antwoord = Antwoord

#sportvragen
a1 = vragen("Hoe lang is Jay?","180")
a2 = vragen("Hoe lang is Jawed","164")

#historyvragen
b1 = vragen("Welk jaar werd Rotterdam gebombardeerd door de Duitsers?", "1940")
b2 = vragen("Hoe heet de oudste tunnel van Rotterdam?", "Maastunnel")

#entertainmentvragen
c1 =  vragen("Wat is de beste film ooit gemaakt?","Bee movie")

#testvragen
d1 = "miauw"
d2 = "woof"

testvragen = [d1, d2]

sportvragen = [a1, a2]
historyvragen = [b1, b2]
entertainmentvragen = [c1]


print(random.choice(historyvragen))

#print(str(c1.vraag))
userinput = str(input("Zet hier je input \n"))
if userinput == c1.Antwoord:
    print("correct")
else:
    print("incorrect")


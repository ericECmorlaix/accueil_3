# Dépendances
from microbit import *

# Définitions
a = Image("00000:00000:00900:00000:00000")
b = Image("09090:90009:00000:90009:09090")
c = Image("90009:00000:00000:00000:90009")
l = Image("00900:09090:90009:09090:00900")
s = Image("00000:00000:00000:00000:00900")
t = Image("00000:00900:09090:00900:00000")
v = Image("00000:00000:00000:00900:00000")

# Boucle de répétition infinie
while True:
    display.show(a)
    sleep(500)
    display.show(b)
    sleep(500)
    display.show(c)
    sleep(500)
    display.show(l)
    sleep(500)
    display.show(s)
    sleep(500)
    display.show(t)
    sleep(500)
    display.show(v)
    sleep(500)
    display.clear()
    sleep(1000)
        

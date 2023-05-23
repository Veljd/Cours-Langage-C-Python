h2sec = 3600
m2sec = 60

nbseconde = int(input("Entrez un nombre de seconde(s)\n"))

heure = nbseconde // h2sec
minute = nbseconde // m2sec % m2sec
seconde = nbseconde % m2sec

print("Ce nombre de secondes correspond à :", heure, "heure(s) et", minute, "minute(s) et", seconde, "seconde(s)")
wordlist = []
#Bayes Rule

# chance = 2/6 NOT = 4/6 mit 5 Würfeln also 1- (4/6)^5

x = (5/6)**4
y= 625/1296

print(x)
print(y)

# 5 Würfe
# mindestens 3 Davon eine 1 oder 2
# Also Chance 3 mal (1 oder 2) = 2/6
# + 4mal + 5mal

#=> 2/6^3 * 4/6^2 // 3 Würfe mit Ja und 2 mit Nein
#=> 2/6^4 * 4/6^1
#=> 2/6^5 * 4/6^0

# Wie oft das gewünschte Event auftritt
rmin = 3  # 2
rmax = 5  # 4
# Maxmimale Würfe
max = 5  # 4
# Anzahl an Rechnungen
iterations = rmax - rmin + 1
# Chances of Yes und No (Yes = wollen wir, No = nicht)
Yep = 2/6  # 1/6
Nope = 4/6  # 5/6

chance = 0
for i in range(iterations):
    chance += (Yep**(rmin+i) * Nope**((max-rmin)-i))
print("chance is:")
print(chance)
print("\n")
## TODO die rechnung oben als ALgorithmus/Function




###############
chance2 = 0
for i in range(3):
    chance2 += ((1/6)**(2+i) * (5/6)**(2-i))
    print(chance2)

print("der Test: ", chance2)
print(171/1296)
print("----")
print( ((1/6)**2) * ((5/6)**2) )
print("##")
print(150/1296)
print(20/1296)
print(1/1296)

# Test Lösung = 171/1296 TODO JUnit Test machen nachm Programm https://www.quora.com/What-is-the-probability-of-getting-6-at-least-two-times-in-throwing-a-fair-die-4-times
#  binomial probability problem where  n=4, k=2, 3, 4,   p=16  and  q=56.

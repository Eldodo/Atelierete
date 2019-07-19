import random

file = "liste_mots_fra.txt"
liste = [line.rstrip('\n').lower() for line in open(file)]

tries = 10

choix = liste[random.randrange(0,len(liste))]
stars = ['*' for i in range(0,len(choix)-1)]
myst = choix[0]+''.join(stars)
print("Vous avez "+str(tries)+" essaies")
ans = input("Devinez le mot mystère: " + myst+"\n")
while(ans != choix and tries>0):
    tries = tries - 1
    print("Il vous reste "+str(tries)+" essaies")
    stop = 0
    if(len(myst)>len(ans)):
        stop = len(ans)
    else:
        stop = len(myst)
    for i in range(0, stop):
        mystcpy = list(myst)
        if(ans[i] == choix[i]):
            mystcpy[i] = choix[i]
        myst = ''.join(mystcpy)
    ans = input("Devinez le mot mystère: " + myst + "\n")

if(tries > 0):
    print("Bravo vous avez trouvé le mot mystère!")
else:
    print("Perdu! Le mot mystère était "+ choix)
    

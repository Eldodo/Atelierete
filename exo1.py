continuer = True
noms = []
ages = []
while(continuer):
    nom = input("Entrez un nom : ")
    noms.append(nom)
    age = input("Entrez l'âge de la personne : ")
    ages.append(int(age))

    ans = input("Voulez vous encore entrer un nom? (O/N)")
    if(ans == 'n' or ans == 'N'):
        continuer = False
print("Vous avez entré "+ str(len(noms))+ " noms. Les voici:")
for i in range(0, len(noms)):
    if(ages[i] >= 18):
        print(noms[i] + " a " + str(ages[i]) + " ans, il est majeur.")
    else:
        print(noms[i] + " a " + str(ages[i]) + " ans, il est mineur.")

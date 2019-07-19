import random
continuer = True

while(continuer):
    a = random.randrange(0,100)
    b = random.randrange(0,100)
    c = random.randrange(0,3)
    res = ans = None

    if(c == 0):
        ans = input(str(a)+"+"+str(b)+"=?\n")
        res = a+b
    elif(c == 1):
        ans=input(str(a)+"-"+str(b)+"=?\n")
        res = a-b
    elif(c == 2):
        ans = input(str(a)+"*"+str(b)+"=?\n")
        res = a*b
    else:
        while(a==0):
            a = random.randrange(0,100)
        ans = input(str(a)+"/"+str(b)+"=?\n")
        res = a//b
        
    if(int(ans) == res):
        print("Bravo vous avez trouvé la bonne réponse!")
    else:
        print("Ce n'est pas la bonne réponse, la bonne réponse était "+str(res))
    ans = input("Voulez vous continuer? O/N\n")
    if(ans == 'n' or ans == 'N'):
        continuer = False

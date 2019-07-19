def factorielle(a):
    if(a == 0 or a == 1):
        return 1
    i = 2
    fact = 2
    while(i < a):
        i = i+1
        fact = i*fact
    return fact

def failure():
    exit()

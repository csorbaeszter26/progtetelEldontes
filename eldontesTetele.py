import math

n = int(input("\nszám: "))
prim = bool

if n < 2:
    prim = False
    print("Prím")
else:
    i = 2
    while (i <= math.sqrt(n)) and (n % i != 0):
        i += 1
    if i > math.sqrt(n):
        prim = True
        print("Prím")
    else:
        print("Nem prím")


#sorozathoz értéket rendel
#eldöntendő kérdés: igen v nem, igaz v hamis választ ad
#mi a sorozat?
# itt az i mit reprezentál? -> számnak az osztói
# i = osztó
# sorozat elemei a szám osztói
# mi a kérdés? mit akarunk eldöteni? -> 

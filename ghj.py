try:
    r=input()
    g=input()
    j=int(r)+int(g)
    print(j)
except ValueError:
    print (str(r)+str(g))
    
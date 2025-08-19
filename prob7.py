#Problema 7 – Criba lui Eratostene (10p)
#Scrie o funcție care generează toate numerele prime ≤ n folosind Criba lui Eratostene.

def criba(n):
    prim = [True for _ in range(n+1)]
    prim[0], prim[1] = False, False
    p = 2
    while p*p <= n:
        if prim[p]:
            for i in range(p* p,n+1,p):
                prim[i] = False
        p+= 1
    return [i for i, is_prim in enumerate(prim) if is_prim]

print("Numere prime până la 45:", criba(45))

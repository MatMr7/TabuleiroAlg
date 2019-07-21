
def swap(a):
     swp = a[r1][c1]
     a[r1][c1] = a[r2][c2]
     a[r2][c2] = swp



def createBoard(a,b,c):
    
    lista = [ [] for i in range(a)]

    print(lista)

    for k in range(a):
        for i in range(b):
            peca = random.randrange(0,c)
            lista[k].append(peca)

    return lista



def clearAll(a,sym):
    for k in range(len(a)):
        for i in range(len(a[k])):
            if a[k][i] == sym:
                a[k][i] = -1

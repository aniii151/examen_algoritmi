#prob 3 cautare in matrice SORTATA
matrice = [
        [1, 4, 7],
        [2, 5, 9],
        [3, 6, 10] ]
def cauta_matrice(matrice, target):
    if not matrice:   #verifica daca matricea e goala
        return False
    rows,cols = len(matrice), len(matrice[0])    #aflam ce dimensiuni are
    row, col = 0, cols-1  #pornim de la randul 0 pana la ultima coloana
    while row<rows and col>=0:
        if matrice[row][col] == target:
            return True   #daca am gasit targetul return true
        elif matrice[row][col] > target:  #daca val gasita e mai mare decat target, cautam in stanga
            col-=1
        else:   #daca val e mai mica decat targetul mergem pe randul urm
            row+=1
    return False


print(cauta_matrice(matrice, 5))

#prob 2-cautare liniara

def cautare_liniara(arg, target):
    for i in range(len(arg)):
        if arg[i] == target:
            return i
    return False

if __name__ == "__main__":
    arg = [4, 7, 1, 9]
    print(cautare_liniara(ar, 7))
# Problema 4 – Stivă (20p)
  #stiva   principiul lifo


class stiva:
    def __init__(self):
        self.elemente= []
    def push(self,element):  #adaug un elem
        self.elemente.append(element)
    def pop(self):
        return self.elemente.pop()


if __name__ == "__main__":
    s = stiva()
    s.push(5)
    s.push(7)
    s.pop()
    s.push(9)
    print(s)

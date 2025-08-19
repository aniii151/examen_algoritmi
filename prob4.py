
class stiva:
    def __init__(self):
        self.elemente = []

    def push(self, element):  # adaug un elem
        self.elemente.append(element)

    def pop(self):
        return self.elemente.pop()
    def  peek(self):
        return self.elemente[-1]


if __name__ == "__main__":
    s = stiva()
    s.push(5)
    s.push(7)
    s.pop()
    s.push(9)
    s.peek()

print(s)
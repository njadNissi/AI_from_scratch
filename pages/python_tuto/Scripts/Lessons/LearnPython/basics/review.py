
class Pen:
    def __init__(self, name, length) -> None:
        self.name = name
        self.length = length

    def __repr__(self) -> str:
        return self.name + ", " + str(self.length)


pens = [
    Pen('Bic', 1.25),
    Pen('Stylo', 1.6)
]

for pen in pens:
    print(pen)

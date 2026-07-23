class TwoDvector:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def show(self):
        print(f"the vector is {self.x}, {self.y}")

class ThreeDvector(TwoDvector):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z


    def show(self):
        print(f"the vector is{self.x}, {self.y}, {self.z}")
a = TwoDvector(3, 4)
a.show()
b = ThreeDvector(5, 6, 7)
b.show()

class Rabbit:

    def __init__(self, size, danger):  # constructor, passed self
        self._size = size
        self._danger = danger
        self._victims = []

    def threaten(self):  # instance method, passed self
        print("I am a {} bunny with {}!".format(self._size, self._danger))


r1 = Rabbit('large', "sharp, pointy teeth")  # pass parameters to constructor
r1.threaten()  # instance method has access to variables via self

r2 = Rabbit('small', 'fluffy fur')
r2.threaten()

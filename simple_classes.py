x = list()  #  List x = new List();

x.append('spam')
x.append('ham')
x.append('toast')
x.insert(1, 'bacon')
print(f"x: {x}")

m = 5   #   m = int(5)         Integer m = new Integer(5);
print(f"type(m): {type(m)}")

class Dog:
    def bark(self):
        print("woof! woof!")

d = Dog()   # create instance of Dog class

d.bark()

d2 = Dog()
d3 = Dog()
d3.bark()


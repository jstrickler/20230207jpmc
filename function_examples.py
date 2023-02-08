
def spam():
    print("Hello from spam()")

spam()

def hello(whom="world"):
    print("Hello,", whom)

hello("Mom")
hello("Dad")
hello()

#  pos-only required-pos optional-pos required-named opt-named

def sum_values(size, *values):
    print(f"values: {values}")
    return sum(values)

print(f"sum_values(1, 2, 3): {sum_values(1, 2, 3)}")
print(f"sum_values(8, 9, 10, 47, 6, 1): {sum_values(8, 9, 10, 47, 6, 1)}")


def wacky(p1, /, p2, p3, *p4, p5, p6, **p7):
    print(p1, p2, p3, p4, p5, p6, p7)

def search(search_term, *, ignore_case=False, encoding="utf-8"):
    pass

#  search('foo')
#  search('bar', ignore_case=True)

#  pos, pos, *, named=value, named=value



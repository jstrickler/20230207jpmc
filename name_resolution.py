
x = 10

print(x)

#  function local -> nonlocal -> file global -> builtin

def spam():
    print(f"x: {x}")

    animal = "wombat"  # local variable

spam()

# print(f"animal: {animal}")
print(f"x: {x}")

def foo(a):
    m = "mongoose"  # nonlocal
    def bar():
        print("a is", a)

    return bar

b = foo(35)
b()


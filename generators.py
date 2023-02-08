fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

fr = reversed(fruits)
print(f"fr: {fr}")

for fruit in fr:
    print(fruit)
print()

fruit_enum = enumerate(fruits)
print(f"fruit_enum: {fruit_enum}\n")
for i, fruit in fruit_enum:
    print(i, fruit)
print()

fruits_upper_gen = (f.upper() for f in fruits)
print(f"fruits_upper_gen: {fruits_upper_gen}\n")
for fruit in fruits_upper_gen:
    print(fruit)
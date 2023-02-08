fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

def ignore_case(fruit):
    compare_value = fruit.lower()
    print(f"comparing {fruit} as {compare_value}")
    return compare_value

f1 = sorted(fruits, key=ignore_case)
print(f"f1: {f1}\n")

def weird_sort(f):
    return f[-1].lower()

f2 = sorted(fruits, key=weird_sort)
print(f"f2: {f2}\n")

f3 = sorted(fruits, key=str.lower)
print(f"f3: {f3}\n")

f4 = sorted(fruits, key=len)
print(f"f4: {f4}\n")

def len_and_name(f):
    return len(f), f.lower()

f5 = sorted(fruits, key=len_and_name)
print(f"f5: {f5}\n")


people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

def by_dob(p):
    return p[3]  # or p[-1]

for person in sorted(people, key=by_dob):
    print(person)
print()

def last_name_first_name(p):
    return p[1], p[0]

for person in sorted(people, key=last_name_first_name):
    print(person)
print()

f4 = sorted(fruits, key=str.lower, reverse=True)
print(f"f4: {f4}\n")

for person in sorted(people, key=lambda p: (p[2], p[1])):
    print(person)
print()




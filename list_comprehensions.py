fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    new_item = f.upper()
    f0.append(new_item)
print(f"f0: {f0}\n")

#     [EXPR-USING-VAR for VAR in ITERABLE]
f1 = [f.upper() for f in fruits]
print(f"f1: {f1}\n")

f2 = [f.upper() for f in fruits if f.startswith('p')]
print(f"f2: {f2}\n")

f3 = [f for f in fruits if f.startswith('p')]
print(f"f3: {f3}\n")

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
    ('Guido', 'van Rossum', 'Python', '1956-01-31'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

oldsters = [p for p in people if p[3] < '1960']
for oldster in oldsters:
    print(oldster)
print()

dobs = [p[3] for p in people]
print(f"dobs: {dobs}\n")


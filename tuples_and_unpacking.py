
data = ['a', 'b', 'c']   # list

# a collection of related data
# AKA a STRUCTURE or RECORD
person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'

print(type(data), type(person))

print(f"person[0]: {person[0]}")
print(f"person[-1]: {person[-1]}")

#  storing fielded data
# tuple   namedtuple  dataclass dictionary
#  ro        ro          r/w      r/w
#     immutable             mutable
person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'


first_name, last_name, product, dob = person   # unpack the iterable


print(first_name, last_name, dob)

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'git', '1969-12-28'),
    ('John', 'Strickler', '1956-10-31'),
]

print(f"people[0]: {people[0]}")
print(f"people[0][0]: {people[0][0]}")
print(f"people[-1][-1]: {people[-1][-1]}")
print()

for first_name, last_name, *product, dob in people:
    print(f"{last_name:12} {product}")
print()

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'LTN': 'London',  # (Luton)
    'LGW': 'London',  # (Gatwick)
    'LHR': 'London',  # (Heathrow)
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

for code, city in airports.items():
    print(code, city)
print()

print(airports.items())

cats = ['jaguar', 'leopard', 'tiger', 'lion', 'ocelot', 'panther', 'lynx']

for i, cat in enumerate(cats):
    print(i, cat)
print()

states = ['NC', 'CA', 'GA', 'MA']
capitals = ['Raleigh', 'Sacramento', 'Atlanta', 'Boston']

for state, capital in zip(states, capitals):
    print(state, capital)
print()







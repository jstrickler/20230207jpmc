from johnstuff.misc import geometry
import sys

result = geometry.circle_area(47)
print(f"result: {result}")

result = geometry.rectangle_area(18, 4.7)
print(f"result: {result}")

s = geometry.Spam()
print(f"s: {s}")

# module search strategy
# 1. current folder
# 2. folders in PYTHONPATH env variable
# 3. Python installation lib folders
print(f"sys.prefix: {sys.prefix}")
print()
for path in sys.path:
    print(path)

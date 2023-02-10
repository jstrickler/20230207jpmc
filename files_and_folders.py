import os
from datetime import datetime

FOLDER = 'DATA'
FILE_NAME = 'alice.txt'

file_path = os.path.join(FOLDER, FILE_NAME)

print(f"file_path: {file_path}")

with open(file_path) as file_in:
    data = file_in.read()

file_size = os.path.getsize(file_path)
print(f"file_size: {file_size}")

file_raw_timestamp = os.path.getmtime(file_path)
print(f"file_raw_timestamp: {file_raw_timestamp}")

file_timestamp = datetime.fromtimestamp(file_raw_timestamp)
print(f"file_timestamp: {file_timestamp}")

# os.path.getmtime()  .getatime()  .getctime()

abs_path = os.path.abspath(file_path)
print(f"abs_path: {abs_path}")
path, ext = os.path.splitext(file_path)
print(f"path: {path}")
print(f"ext: {ext}")

print(f"os.path.splitdrive(abs_path): {os.path.splitdrive(abs_path)}")

some_path = "foo/bar"
some_file_name = "blah.txt"
some_file_path = os.path.join(some_path, some_file_name)
print(f"some_file_path: {some_file_path}")
good_file_path = os.path.normcase(some_file_path)
print(f"good_file_path: {good_file_path}")

terrible_file_name = "foo bar.txt"
with open(terrible_file_name) as terrible_in:
    print(terrible_in.read())
print()

for thing in FOLDER, file_path, FILE_NAME:
    print(thing, os.path.isfile(thing), os.path.isdir(thing), os.path.exists(thing))
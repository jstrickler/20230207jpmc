import os
# absolute paths (Windows)
#  c:\foo\bar\blah.txt
#  \\spam\ham\eggs.txt

# relative paths (Windows)
#  bar\blah.txt
#  blah.txt
#  ..\foo\bar\blah.txt
#  ..\..\..\myfile.docx

# good
file_path = r"C:\foo\bar\blah.txt"

# better
file_path = "C:/foo/bar/blah.txt"

# absolute paths (Mac, Linux)
#  /foo/bar/blah.txt

# relative paths (Mac, Linux)
#  bar/blah.txt
#  ../../blah.txt

print(f"__file__: {__file__}")

abs_path = os.path.abspath(__file__)
print(f"abs_path: {abs_path}")

folder = os.path.dirname(__file__)
print(f"folder: {folder}")

file_name = os.path.basename(__file__)
print(f"file_name: {file_name}")

print(f"os.path.split(__file__): {os.path.split(__file__)}")

my_path = "foo/bar/blah"
print(f"os.path.dirname(my_path): {os.path.dirname(my_path)}")
print(f"os.path.basename(my_path): {os.path.basename(my_path)}")








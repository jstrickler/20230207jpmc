
import fileinput

for line in fileinput.input():  # fileinput.input() is a generator of all lines in all files in sys.argv[1:]
    if 'bird' in line:
        print('{}: {}'.format(fileinput.filename(), line), end=' ')  # fileinput.filename() has the name of the current file

import sys

#  sys.argv           [                       ]
#  sys.argv[1]                -----
# cmd line =  "python spam.py alpha.txt beta.txt gamma.txt"

for file_path in sys.argv[1:]:
    with open(file_path) as file_in:
        for raw_line in file_in:
            pass



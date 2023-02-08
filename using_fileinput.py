import fileinput
import re
from argparse import ArgumentParser
import logging



parser = ArgumentParser(description="Fake version of grep")

parser.add_argument("-i", dest="ignore_case", action="store_true", help="Ignore case")
parser.add_argument("-f", dest="show_file_name", action="store_true", help="Display file name")
parser.add_argument("-d", dest="debug", action="store_true", help="show debugging messages")
parser.add_argument("search_term", help="Search term")
parser.add_argument("files", nargs="*", help="files to search")

args = parser.parse_args()   # parses sys.argv

if args.debug:
    level = logging.DEBUG
else:
    level = logging.WARNING

logging.basicConfig(
    filename="fakegrep.log",
    level=level,  # level threshold
    format="%(levelname)s %(asctime)s %(message)s",
    datefmt="%x-%X",
)


logging.info(f"search term: {args.search_term}")

logging.debug(f"args: {args}")

if args.ignore_case:
    re_options = re.IGNORECASE
else:
    re_options = 0  # no flags

rx_search_term = re.compile(args.search_term, re_options)

for raw_line in fileinput.input(args.files):
    if rx_search_term.search(raw_line):
        line = raw_line.rstrip()
        if args.show_file_name:
            print(fileinput.filename(), end=": ")
        print(line)

import csv
import pandas as pd
from dateutil.parser import parse
from datetime import date

INPUT_FILE = 'system.log'
OUTPUT_FILE = 'syslog.csv'

current_year = date.today().year

with open(INPUT_FILE) as file_in:
    with open(OUTPUT_FILE, "w") as file_out:
        wtr = csv.writer(file_out, lineterminator="\n")
        for raw_line in file_in:
            # in real life, concatenate lines starting with tab to the previous line
            if raw_line.startswith('\t'):
                continue
            line = raw_line.rstrip()   # remove \n
            month, day, time, source, logger, *message_words = line.split()
            date = parse(f"{month} {day}, {current_year}")
            message = ' '.join(message_words)
            wtr.writerow([date, source, message])

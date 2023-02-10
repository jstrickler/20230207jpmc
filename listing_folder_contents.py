import os
from glob import glob

DATA_FOLDER = "DATA"

all_files = os.listdir(DATA_FOLDER)
print(f"all_files: {all_files}\n")


files_in_data = [file_name for file_name in all_files if os.path.isfile(os.path.join(DATA_FOLDER, file_name))]
print(f"file_in_data: {files_in_data}\n")

all_text_files = glob('DATA/*.txt')
print(f"all_text_files: {all_text_files}\n")

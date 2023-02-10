import os

START_DIR = "."

#  os.walk(START_DIR)
for current_dir, sub_directories, file_names in os.walk(START_DIR):
    if ".git" in sub_directories:
        sub_directories.remove(".git")
    print(current_dir)
    for file_name in file_names:
        if file_name.endswith('.py'):
            file_path = os.path.join(current_dir, file_name)
            file_size = os.path.getsize(file_path)
            print(f"    {file_size:6d} {file_name}")

import os


os.mkdir('test_files')
file_path = "test_files"

if os.path.exists(file_path):
    print(f"The file {file_path} exists.")
else:
    print(f"The file {file_path} does not exist.")


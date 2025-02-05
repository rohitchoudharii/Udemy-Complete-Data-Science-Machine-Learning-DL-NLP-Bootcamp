import os

current_dir = os.path.join(os.getcwd(), "Section 9 File Handling in Python")

new_dir_path = os.path.join(current_dir, "package")
if not os.path.exists(new_dir_path):
    os.mkdir(new_dir_path)
print(f"new dir created {new_dir_path}")

items = os.listdir(current_dir)
print(items)

new_file_path = os.path.join(new_dir_path, "new_file.txt")
print(new_file_path)

check_path = "example.txt"
if os.path.exists(check_path):
    print("Path already exist", check_path)
else:
    print("Path doesnt exist", check_path)

if os.path.isfile(check_path):
    print("Path is a file. Path: ", check_path)
elif os.path.isdir(check_path):
    print("Path is a dir. Path: ", check_path)
else:
    print("Path is neither a file or dir. Path: ", check_path)

relative_path = "new_file.txt"
abs_path = os.path.abspath(relative_path)
print(abs_path)

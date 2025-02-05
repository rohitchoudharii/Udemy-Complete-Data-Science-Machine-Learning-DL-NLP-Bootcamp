base_file_path = "Section 9 File Handling in Python/files"
example_file_path = f"{base_file_path}/example.txt"
with open(example_file_path, "r") as file:
    print(file.read())

with open(example_file_path, "r") as file:
    for line in file:
        print(line.strip())  # strip is used to remove the extra spaces

# File over writing
with open(example_file_path, "w") as file:
    file.write("Hello World\n")
    file.write("This is a new line\n")
    file.write("This is the last line\n")

# File data appending
with open(example_file_path, "a") as file:
    file.write("This is the appended line\n")

lines = ["New line 1\n", "New line 2\n", "New line 3\n"]
with open(example_file_path, "a") as file:
    file.writelines(lines)

bin_data = b"\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21"
with open(f"{base_file_path}/example.bin", "wb") as file:
    file.write(bin_data)

with open(f"{base_file_path}/example.bin", "rb") as file:
    print(file.read())


# Read from one file and write to another file
with open(f"{base_file_path}/example.txt", "r") as file:
    contents = file.read()

with open(f"{base_file_path}/example_copy.txt", "w") as file_copy:
    file_copy.write(contents)


# Writing and reading from a file
with open(f"{base_file_path}/example.txt", "w+") as file:
    file.write("This is a new line\n")
    file.write("This is a new line 2\n")
    file.write("This is a new line 3\n")
    file.seek(0)
    print(file.read())

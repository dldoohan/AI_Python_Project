# Writing to a file
with open("sample_data.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a sample text file.\n")
    file.write("It contains multiple lines of text.\n")

# Reading from a file
with open("sample_data.text", "r") as file:
    content = file.read()
    print("Content of the file:")
    print(content)

    # Move the file pointer to the beginning
    file.seek(0)

    print("Reading line by line:")
    for line in file:
        print(line.strip())
def write_name_file(name):
    with open("name.txt", "w") as f:
        f.write(name)
    print("Name file written successfully!")

write_name_file("Dinh Quy Pham")
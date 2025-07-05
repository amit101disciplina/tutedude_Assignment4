filename = "output.txt"
with open(filename, "w") as file:
    write = input("Enter text to write to the file: ")
    file.write(write + "\n")
    print(f"Data successfully written to {filename}")
    print("\n")
with open(filename, "a") as file:
    append = input("Enter additional text to append: ")
    file.write(append + "\n")
    print("Data successfully appended.")
    print("\n")
with open(filename, "r") as file:
    print(f"Final content of {filename}:")
    read=file.read()
    print(read)

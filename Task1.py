try:
    line_number = 1
    filename = "sample.txt"
    with open(filename, "r") as file:
        print("Reading file content:")
        for line in file:
            print(f"Line {line_number}: {line.strip()}")
            line_number += 1
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")

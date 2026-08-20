try:
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The specified file was not found.")
finally:
    print("This block is always executed.")
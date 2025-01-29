import sys
import os

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a python file")
    elif not os.path.exists(sys.argv[1]):
        sys.exit("File not found")

    file_name = sys.argv[1]
    line_count = 0
    lines = []
    with open(file_name) as file:
        for line in file:
            if line.strip():
                lines.append(line.strip())
    for line in lines:
        if not line.startswith("#"):
            line_count += 1

    print(line_count)

if __name__ == "__main__":
    main()




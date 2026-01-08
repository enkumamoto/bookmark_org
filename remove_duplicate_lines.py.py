import sys

def remove_duplicate_lines(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()

    unique_lines = []
    for line in lines:
        if line not in unique_lines:
            unique_lines.append(line)

    with open(file_name, "w") as f:
        f.writelines(unique_lines)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python remove_duplicate_lines.py bookmarks.html")
        sys.exit(1)

    file_name = sys.argv[1]
    remove_duplicate_lines(file_name)

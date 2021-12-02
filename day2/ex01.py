
def main():
    horizontal = 0
    depth = 0
    file = open("input.txt")
    for line in file:
        if line[0] == 'f':
            horizontal = horizontal + int(line[8])
        if line[0] == 'd':
            depth = depth + int(line[5])
        if line[0] == 'u':
            depth = depth - int(line[3])
    print(horizontal * depth)
if __name__ == "__main__":
    main()
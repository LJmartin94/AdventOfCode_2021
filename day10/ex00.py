def main():
    file = open("input.txt")

    error = 0
    line_number = 0
    for line in file:
        line_number += 1
        parsed_line = []
        for char in line:
            if char == '(' or char == '[' or char == '{' or char == '<':
                parsed_line.append(char)
            i = len(parsed_line) - 1
            if char == ')' or char == ']' or char == '}' or char == '>':
                if char == ')' and parsed_line[i] != '(':
                    error += 3
                    break
                elif char == ']' and parsed_line[i] != '[':
                    error += 57
                    break
                elif char == '}' and parsed_line[i] != '{':
                    error += 1197
                    break
                elif char == '>' and parsed_line[i] != '<':
                    error += 25137
                    break
                else:
                    parsed_line.pop(i)
    answer = error
    print("Answer to 10.0:")
    print(answer)


if __name__ == "__main__":
    main()
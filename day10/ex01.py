def main():
    file = open("input.txt")

    solvable_lines = []
    line_number = 0
    for line in file:
        error = 0
        line_number += 1
        parsed_line = []
        for char in line:
            if char == '(' or char == '[' or char == '{' or char == '<':
                parsed_line.append(char)
            i = len(parsed_line) - 1
            if char == ')' or char == ']' or char == '}' or char == '>':
                if char == ')' and parsed_line[i] != '(':
                    error = 1
                    break
                elif char == ']' and parsed_line[i] != '[':
                    error = 1
                    break
                elif char == '}' and parsed_line[i] != '{':
                    error = 1
                    break
                elif char == '>' and parsed_line[i] != '<':
                    error = 1
                    break
                else:
                    parsed_line.pop(i)
        if error == 0:
            solvable_lines.append(parsed_line)

    line_scores = []
    for i in range(len(solvable_lines)):
        score = 0
        while len(solvable_lines[i]) > 0:
            c = len(solvable_lines[i]) - 1
            score *= 5
            if solvable_lines[i][c] == '(':
                score += 1
            if solvable_lines[i][c] == '[':
                score += 2
            if solvable_lines[i][c] == '{':
                score += 3
            if solvable_lines[i][c] == '<':
                score += 4
            # print(str(solvable_lines[i]) + str(score))
            solvable_lines[i].pop(c)
        line_scores.append(score)

    line_scores.sort()
    answer = line_scores[int(len(line_scores)/2)]
    print("Answer to 10.1:")
    print(answer)


if __name__ == "__main__":
    main()
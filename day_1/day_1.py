import os

def get_input_as_int(input_path):
    numbers = []
    with open(file_path, 'r') as fin:
        for line in fin:
            numbers.append(int(line))
    fin.close()
    return numbers


def problem_1(lines):
    for i in range(0, len(lines)):
        for j in range(i+1, len(lines)-1):
            if lines[i] + lines[j] == 2020:
                return lines[i] * lines[j]


def problem_2(lines):
    for i in range(0, len(lines)):
        for j in range(i+1, len(lines)-1):
            for k in range(i+2, len(lines)-1):
                if lines[i] + lines[j] + lines[k] == 2020:
                    return lines[i] * lines[j] * lines[k]

file_path = os.path.join(r'C:\Users\chris\PycharmProjects\advent_2020\day_1', 'input')

finput = get_input_as_int(file_path)

answer_1 = problem_1(finput)

answer_2 = problem_2(finput)

print(answer_1)
print(answer_2)
import os


def get_input(input_path):
    with open(file_path, 'r') as fin:
        lines = fin.readlines()
    fin.close()
    return lines


def problem_1(lines):
    correct = 0
    wrong = 0
    for line in lines:
        min_amount = line['letter_req'].start
        max_amount = line['letter_req'].stop
        char = line['char']
        password = line['password']
        char_count = password.count(char)
        if char_count >= min_amount and char_count <= max_amount:
            correct += 1
        else:
            wrong += 1
    return (correct, wrong)


def problem_2(lines):
    correct = 0
    wrong = 0
    for line in lines:
        start_pos = line['letter_req'].start - 1
        end_pos = line['letter_req'].stop - 1
        char = line['char']
        password = line['password']
        if password[start_pos] == char and password[end_pos] == char:
            wrong += 1
        elif password[start_pos] == char or password[end_pos] == char:
            correct += 1
        else:
            wrong += 1
    return (correct, wrong)


def get_range(string_range):
    split_range = string_range.split('-')
    start = split_range[0]
    start = int(start)
    stop = split_range[1]
    stop = int(stop)
    return range(start, stop)


def create_dictionary(line):
    split_line = line.split(' ')
    letter_requirements = get_range(split_line[0])
    char = split_line[1].split(':')[0]
    password = split_line[-1]
    user = {'letter_req': letter_requirements, 'char': char, 'password': password}
    return user


file_path = os.path.join(r'C:\Users\chris\PycharmProjects\advent_2020\day_3', 'input')

flines = get_input(file_path)

answer_1 = problem_1(flines)
answer_2 = problem_2(flines)

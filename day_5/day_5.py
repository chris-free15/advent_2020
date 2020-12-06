import os
import math


def binary_part_col(col, index, values):
    if index == 2:
        if col[-1] == 'R':
            return values[1]
        else:
            return values[0]
    else:
        if col[index] == 'L':
            last_col = len(values) // 2
            values = values[0:(last_col)]
            return binary_part_col(col, index + 1, values)
        else:
            last_col = len(values) // 2
            values = values[last_col:]
            return binary_part_col(col, index + 1, values)


def binary_part_row(row, index, values):
    if index == 6:
        if row[-1] == 'F':
            return values[0]
        else:
            return values[1]
    else:
        if row[index] == 'F':
            last_row = len(values) // 2
            values = values[0:(last_row)]
            return binary_part_row(row, index + 1, values)
        else:
            last_row = len(values) // 2
            values = values[last_row:]
            return binary_part_row(row, index + 1, values)


def binary_boarding_part_1(lines):
    boarding_pass_ids = []
    for line in lines:
        line = line.rstrip()
        row_chars = line[0:7]
        column_chars = line[7::]
        row_id = binary_part_row(row_chars, 0, list(range(0, 128)))
        row_id = row_id * 8
        col_id = binary_part_col(column_chars, 0, list(range(0, 8)))
        boarding_pass_ids.append(row_id + col_id)
    return boarding_pass_ids


def fill_binary_boarding_pass(lines):
    col = 8
    row = 128
    mat = [[0 for x in range(col)] for y in range(row)]
    for line in lines:
        line = line.rstrip()
        row_chars = line[0:7]
        column_chars = line[7::]
        row_id = binary_part_row(row_chars, 0, list(range(0, 128)))
        col_id = binary_part_col(column_chars, 0, list(range(0, 8)))
        mat[row_id][col_id] = 1
    return mat


def valid_positioning(line):
    missing_seat_sequence = "101"
    digit_str = ''
    for ele in line:
        digit_str += str(ele)
    if missing_seat_sequence in digit_str:
        return True
    return False


def find_col(line):
    return line.index(0)


def find_my_seat_id(matrix):
    row = 0
    for line in matrix:
        if valid_positioning(line):
            print("line: {}".format(line))
            col = find_col(line)
            return row * 8 + col
        row += 1


def get_input(input_path):
    with open(file_path, 'r') as fin:
        lines = fin.readlines()
    fin.close()
    return lines


file_path = os.path.join(r'C:\Users\chris\PycharmProjects\advent_2020\day_5', 'input')
finput = get_input(file_path)

max_id = max(binary_boarding_part_1(finput))  # part 1

filled_mat = fill_binary_boarding_pass(finput)
my_id = find_my_seat_id(filled_mat) # part 2


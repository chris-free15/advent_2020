import os


def get_input(input_path):
    with open(file_path, 'r') as fin:
        lines = fin.readlines()
    fin.close()
    return lines


def find_trees_in_slope(lines, shift_right_amount, shift_down_amount=1):
    trees = 0
    current_pos = 0
    for i in range(0, len(lines), shift_down_amount):
        current_line = lines[i].rstrip()
        if current_pos > 30:
            new_line = current_line
            while len(new_line) <= current_pos:
                new_line += current_line
            if new_line[current_pos] == '#':
                trees += 1
            current_pos += shift_right_amount
            continue
        if current_line[current_pos] == '#':
            trees += 1
        current_pos += shift_right_amount
    return trees


file_path = os.path.join(r'C:\Users\chris\PycharmProjects\advent_2020\day_3', 'input')

finput = get_input(file_path)

problem_1 = find_trees_in_slope(finput, 3, 1)

dxs = [1, 3, 5, 7]
product = 1
for dx in dxs:
    product *= find_trees_in_slope(finput, dx)

no_dy_change = product
final_product = find_trees_in_slope(finput, 1, 2) * no_dy_change

import os
import string
import collections

def count_yes_for_group(declaration_form):
    selected_answers = []
    for answers in declaration_form:
        for char in answers:
            selected_answers.append(char)
    return len(set(selected_answers))


def count_yes_for_same_questions(group_form):
    answer_dict = collections.defaultdict(list)
    set_list = []
    for answer in group_form:
        set_list.append(set(answer))
    u = set.intersection(*set_list)
    return len(u)


def get_numbers_of_yes(form):
    yes = 0
    current_group = []
    for line in form:
        if line == '\n':
            # yes += count_yes_for_group(current_group) part 1
            yes += count_yes_for_same_questions(current_group)
            # count_yes_for_same_questions(current_group)
            current_group = []
        else:
            line = line.rstrip()
            current_group.append(line)
    return yes


def get_input(input_path):
    with open(file_path, 'r') as fin:
        lines = fin.readlines()
    fin.close()
    return lines


file_path = os.path.join(r'C:\Users\chris\PycharmProjects\advent_2020\day_6', 'input')
custom_declaration_form = get_input(file_path)

# yes = get_numbers_of_yes(custom_declaration_form)
same = get_numbers_of_yes(custom_declaration_form)
print(same)
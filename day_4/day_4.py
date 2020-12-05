import os


def birth_year_check(birth_year):
    return (len(birth_year) == 4) and 1920 <= int(birth_year) <= 2002


def issue_year_check(issued_year):
    return (len(issued_year) == 4) and (2010 <= int(issued_year) <= 2020)


def expiration_year_check(expiration_year):
    return (len(expiration_year) == 4) and (2020 <= int(expiration_year) <= 2030)


def height_check(height):
    unit = height[-2::]
    res = ''.join(filter(lambda i: i.isdigit(), height))
    numb = int(res)
    if unit == 'in':
        valid = 59 <= numb <= 76
        return valid
    elif unit == 'cm':
        valid = 150 <= numb <= 193
        return valid
    else:
        return False


def hair_color_check(hair_color):
    if len(hair_color) != 7:
        return False
    if hair_color[0] != '#':
        return False
    chars = hair_color[1::]
    valid_characters = ['a', 'b', 'c', 'd', 'e', 'f']
    for i in range(0, len(chars)):
        test_char = chars[i]
        if test_char not in valid_characters and not test_char.isdigit():
            return False
    return True


def eye_color_check(eye_color):
    valid_colors = ['amb', 'blu', 'brn', 'grn', 'gry', 'hzl', 'oth']
    if eye_color in valid_colors:
        return True
    return False


def passport_id_check(passport_id):
    return len(passport_id) == 9


def passport_check(passport):
    keys = set(['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'])
    if not keys.issubset(passport.keys()):
        return False
    else:
        return True


def get_valid_passports(lines):
    valid_passports = []
    current_batch = []
    for line in lines:
        if line == '\n':
            # do stuff
            passport = {}
            for parsed_line in current_batch:
                pairs = parsed_line.split(' ')
                for pair in pairs:
                    kv = pair.split(':')
                    passport[kv[0]] = kv[1]
            if passport_check(passport):
                valid_passports.append(passport)
            current_batch = []
        else:
            info = line.rstrip()
            current_batch.append(info)
    return valid_passports


def get_input(input_path):
    with open(file_path, 'r') as fin:
        lines = fin.readlines()
    fin.close()
    return lines


file_path = os.path.join(r'C:\Users\chris\PycharmProjects\advent_2020\day_4', 'input')

finput = get_input(file_path)
valid_ports = get_valid_passports(finput)
print(len(valid_ports))  # part 1 solution
valid_passports = 0

for passport in valid_ports:
    check = []
    check.append(birth_year_check(passport['byr']))
    check.append(issue_year_check(passport['iyr']))
    check.append(expiration_year_check(passport['eyr']))
    check.append(height_check(passport['hgt']))
    check.append(hair_color_check(passport['hcl']))
    check.append(eye_color_check(passport['ecl']))
    check.append(passport_id_check(passport['pid']))
    if all(check):
        valid_passports += 1

print(valid_passports) # part 2 solution

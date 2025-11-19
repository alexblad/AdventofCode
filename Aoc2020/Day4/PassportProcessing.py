## Part 1: Find the number of valid passports
passports = (x.replace('\n', ' ') for x in open("input.txt").read().split('\n\n'))

passport_dict = []
for passport in passports:
    fields = passport.strip().split(' ')
    passport_data = {}
    for field in fields:
        key, value = field.split(':')
        passport_data[key] = value
    passport_dict.append(passport_data)

valid_count = 0
for passport in passport_dict:
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    if all(field in passport for field in required_fields):
        valid_count += 1

print (valid_count)

## Part 2: Find the number of valid passports with stricter rules
valid_count = 0
for passport in passport_dict:
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    req_1 = False
    if all(field in passport for field in required_fields):
        req_1 = True

    if req_1:
        byr_valid = 1920 <= int(passport['byr']) <= 2002
        iyr_valid = 2010 <= int(passport['iyr']) <= 2020
        eyr_valid = 2020 <= int(passport['eyr']) <= 2030

        hgt = passport['hgt']
        if hgt.endswith('cm'):
            hgt_valid = 150 <= int(hgt[:-2]) <= 193
        elif hgt.endswith('in'):
            hgt_valid = 59 <= int(hgt[:-2]) <= 76
        else:
            hgt_valid = False

        hcl = passport['hcl']
        hcl_valid = (hcl[0] == '#' and len(hcl) == 7 and all(c in '0123456789abcdef' for c in hcl[1:]))

        ecl_valid = passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

        pid_valid = (len(passport['pid']) == 9 and passport['pid'].isdigit())

        if all([byr_valid, iyr_valid, eyr_valid, hgt_valid, hcl_valid, ecl_valid, pid_valid]):
            valid_count += 1

print (valid_count)

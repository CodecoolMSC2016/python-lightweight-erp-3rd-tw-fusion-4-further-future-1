# implement commonly used functions here

import random
# A -Z 65-90  a -z 97 122 spec 33-38

# generate and return a unique and random string
# other expectation:
# - at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of list
# @generated: string - generated random string (unique in the @table)


def generate_random(table):
    flag = 1
    while flag == 1:
        generated = ('' + gen_random_lower() + gen_random_upper() +
                     gen_random_number() + gen_random_number())
        generated = (generated + gen_random_upper() +
                     gen_random_lower() + gen_random_spec() + gen_random_spec())
        for i in table:
            if generated in i:
                flag = 1
            if generated not in i:
                flag = 0
        return generated


def gen_random_number():
    gen_random_number = random.randint(0, 9)
    return str(gen_random_number)


def gen_random_lower():
    gen_random_lower_utf = random.randint(97, 122)
    gen_random_lower = chr(gen_random_lower_utf)
    return gen_random_lower


def gen_random_upper():
    gen_random_upper_utf = random.randint(65, 90)
    gen_random_upper = chr(gen_random_upper_utf)
    return gen_random_upper


def gen_random_spec():
    gen_random_spec_utf = random.randint(33, 38)
    gen_random_spec = chr(gen_random_spec_utf)
    return gen_random_spec


def universal_add(file_name, args):
    print(args)
    get_table_from_file(table)

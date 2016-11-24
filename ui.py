

# This function needs to print outputs like this:
# /-----------------------------------\
# |   id   |      title     |  type   |
# |--------|----------------|---------|
# |   0    | Counter strike |    fps  |
# |--------|----------------|---------|
# |   1    |       fo       |    fps  |
# \-----------------------------------/
#
# @table: list of lists - the table to print out
# @title_list: list of strings - the head of the table
def print_table(table, title_list):
    # max_length = [[0] * (len(title_list) - 1)]
    max_length = [len(title) for title in title_list]
    for row in table:
        for i in range(len(max_length)):
            if len(row[i]) > max_length[i]:
                max_length[i] = len(row[i])
    for item in range(len(max_length)):
        max_length[item] += 2
    print(max_length)
    max_length_sum = 0
    for num in max_length:
        max_length_sum += num
    print(max_length_sum)
    print("/" + ("-" * (max_length_sum + (len(max_length) - 1))) + chr(92))
    for i in range(len(max_length)):
        print("|" + title_list[i].center(max_length[i]), end="")
    print("|")
    for row in table:

        for i in range(len(max_length)):
            print("|" + "-" * (max_length[i]), end="")
        print("|")
        for i in range(len(max_length)):
            print("|" + row[i].center(max_length[i]), end="")
        print("|")
    print(chr(92) + ("-" * (max_length_sum + (len(max_length) - 1))) + "/")
# This function needs to print result of the special functions
#
# @result: string or list or dictionary - result of the special function
# @label: string - label of the result


def print_result(result, label):

    print(label)
    if type(result) == dict:
        for k in result.items():
            print(k)
    else:
        print(result)


# This function needs to generate outputs like this:
# Main menu:
# (1) Store manager
# (2) Human resources manager
# (3) Inventory manager
# (4) Accounting manager
# (5) Selling manager
# (6) Customer relationship management (CRM)
# (0) Exit program
#
# @title: string - title of the menu
# @list_options: list of strings - the options in the menu
# @exit_message: string - the last option with (0) (example: "Back to main menu")
def print_menu(title, list_options, exit_message):
    print(title, "\n")
    for option in range(len(list_options)):
        print("({}) {}".format(option + 1, list_options[option]))

    print("(0)", exit_message)


# This function gets a list of inputs from the user by the terminal
#
# @list_labels: list of strings - the labels of the inputs
# @title: string - title of the "input section"
# @inputs: list of string - list of the received values from the user
def get_inputs(list_labels, title):

    print(list_labels, title)
    inputs = input()

    return inputs


# This function needs to print an error message. (example: Error: @message)
#
# @message: string - the error message
def print_error_message(message):

    print(message)

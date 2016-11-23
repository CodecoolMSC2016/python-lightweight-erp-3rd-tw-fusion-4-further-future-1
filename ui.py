

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
    ma = 0
    for num in max_length:
        ma = ma + num
    print(ma)
    print("/" + ("-" * (ma + (len(max_length) - 1))) + chr(92))
    for mb in range(len(max_length)):
        print("|" + title_list[mb].center(max_length[mb]), end="")
    print("|")
    for mc in range(len(max_length)):
        print("|" + "-" * (max_length[mc]), end="")
    print("|")

# This function needs to print result of the special functions
#
# @result: string or list or dictionary - result of the special function
# @label: string - label of the result


def print_result(result, label):

    # your code

    pass


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
    for option in list_options:
        print(list_options.index(option) + 1, option)

    print("0", exit_message)


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

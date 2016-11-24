# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


# importing everything you need
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader(
    "data_manager", current_file_path + "/../data_manager.py").load_module()
# common module
common = SourceFileLoader(
    "common", current_file_path + "/../common.py").load_module()


# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
#
def start_module():
    list_options = ["Show",
                    "Add",
                    "Remove ",
                    "Update"]

    ui.print_menu("Human Resources menu", list_options,
                  "Exit to the main menu")
    decide = ui.get_inputs("", "")
    if decide == "1":
        show_table(data_manager.get_table_from_file('hr/persons.csv'))
    elif decide == "2":
        current_table = data_manager.get_table_from_file('hr/persons.csv')
        data_manager.write_table_to_file('hr/persons.csv', add(current_table))
    elif decide == "3":
        current_table = data_manager.get_table_from_file('hr/persons.csv')
        identificator = ui.get_inputs("Enter an ID to delete", "")
        data_manager.write_table_to_file(
            'hr/persons.csv', remove(current_table, identificator))
    elif decide == "4":
        current_table = data_manager.get_table_from_file('hr/persons.csv')
        identificator = ui.get_inputs("Enter an ID to update", "")
        data_manager.write_table_to_file(
            'hr/persons.csv', update(current_table, identificator))
    elif decide == "0":
        pass

        # print the default table of records from the file
        #
        # @table: list of lists


def show_table(table):
    title_list = ["id", "name", "birth date"]
    ui.print_table(table, title_list)


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):

    title_list = ["name", "birth year"]
    args = []
    args.append(common.generate_random(table))
    for arg in range(len(title_list)):
        args.append(ui.get_inputs(("Please enter the " + title_list[arg]), ""))
    table.append(args)
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):

    for row in range(len(table)):
        if table[row][0] == id_:
            table.remove(table[row])
            return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):

    title_list = ["name", "birth year"]
    args = []
    args.append(id_)
    for arg in range(len(title_list)):
        args.append(ui.get_inputs(("Please enter the " + title_list[arg]), ""))

    for row in range(len(table)):
        if table[row][0] == id_:
            table[row] = args
            return table


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with
# the same value)
def get_oldest_person(table):

    # your code

    pass


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with
# the same value)
def get_persons_closest_to_average(table):

    # your code

    pass

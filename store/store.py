# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# manufacturer: string
# price: number (dollar)
# in_stock: number


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

    ui.print_menu("Store menu", list_options, "Exit to the main menu")
    decide = ui.get_inputs("", "")
    if decide == "1":
        show_table(data_manager.get_table_from_file("store/games_test.csv"))
    elif decide == "2":
        data_manager.write_table_to_file(
            'games_test.csv', add('games_test.csv'))
    elif decide == "3":
        remove()
    elif decide == "4":
        update()
    elif decide == "0":
        pass


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ["id", "title", "manufacturer", "price", "in stock"]
    ui.print_table(table, title_list)


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):

    args = ['id', 'title', 'manufacturer', 'price', 'in_stock']

    common.universal_add(table, args)

    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):

    # your code

    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):

    # your code

    return table


# special functions:
# ------------------

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):

    # your code

    pass


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_average_by_manufacturer(table, manufacturer):

    # your code

    pass

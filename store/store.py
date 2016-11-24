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
                    "Update",
                    "Count games all by manufacturers",
                    "Average of games in stock"]

    ui.print_menu("Store menu", list_options, "Exit to the main menu")
    decide = ui.get_inputs("", "")
    if decide == "1":
        show_table(data_manager.get_table_from_file('store/games.csv'))
    elif decide == "2":
        current_table = data_manager.get_table_from_file('store/games.csv')
        data_manager.write_table_to_file('store/games.csv', add(current_table))
    elif decide == "3":
        current_table = data_manager.get_table_from_file('store/games.csv')
        identificator = ui.get_inputs("Enter an ID to delete", "")
        data_manager.write_table_to_file(
            'store/games.csv', remove(current_table, identificator))
    elif decide == "4":
        current_table = data_manager.get_table_from_file('store/games.csv')
        identificator = ui.get_inputs("Enter an ID to update", "")
        data_manager.write_table_to_file(
            'store/games.csv', update(current_table, identificator))
    elif decide == "5":
        current_table = data_manager.get_table_from_file('store/games.csv')
        ui.print_result(get_counts_by_manufacturers(current_table), "Number of games by manufacturers: ")
    elif decide == "6":
        current_table = data_manager.get_table_from_file('store/games.csv')
        ui.print_result(get_average_by_manufacturer(current_table, ui.get_inputs(
            "Enter the manufacturer", "")), "Average of games: ")
    elif decide == "0":
        pass


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ["id", "title", "manufacturer", "price", "in stock"]
    ui.print_table(table, title_list)


# Ask a new record as an input from the user than add it to @table, sthan return @table
#
# @table: list of lists
def add(current_table):

    title_list = ["title", "manufacturer", "price", "in stock"]
    args = []
    args.append(common.generate_random(current_table))
    for arg in range(len(title_list)):
        args.append(ui.get_inputs(("Please enter the " + title_list[arg]), ""))
    current_table.append(args)
    return current_table


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
    title_list = ["title", "manufacturer", "price", "in stock"]
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

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):
    manufacturers = {}
    for row in table:
        if not row[2] in manufacturers:
            manufacturers[row[2]] = 1
        else:
            manufacturers[row[2]] += 1

    return manufacturers


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_average_by_manufacturer(table, manufacturer):
    sum_games = 0
    counter = 0
    for row in table:
        if row[2] == manufacturer:
            counter += 1
            sum_games += int(row[4])
    return sum_games / counter

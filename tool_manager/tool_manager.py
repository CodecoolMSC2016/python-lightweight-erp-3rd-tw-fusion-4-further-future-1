# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# manufacturer: string
# purchase_date: number (year)
# durability: number (year)


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
                    "Get available tools",
                    "Get average durability by manufacturer"]

    ui.print_menu("Tools menu", list_options, "Exit to the main menu")
    decide = ui.get_inputs("", "")
    if decide == "1":
        show_table(data_manager.get_table_from_file('tool_manager/tools.csv'))
    elif decide == "2":
        current_table = data_manager.get_table_from_file(
            'tool_manager/tools.csv')
        data_manager.write_table_to_file(
            'tool_manager/tools.csv', add(current_table))
    elif decide == "3":
        current_table = data_manager.get_table_from_file(
            'tool_manager/tools.csv')
        identificator = ui.get_inputs("Enter an ID to delete", "")
        data_manager.write_table_to_file(
            'tool_manager/tools.csv', remove(current_table, identificator))
    elif decide == "4":
        current_table = data_manager.get_table_from_file(
            'tool_manager/tools.csv')
        identificator = ui.get_inputs("Enter an ID to update", "")
        data_manager.write_table_to_file(
            'tool_manager/tools.csv', update(current_table, identificator))
    elif decide == "5":
        current_table = data_manager.get_table_from_file(
            'tool_manager/tools.csv')
        ui.print_result(get_available_tools(current_table), "Available tools by manufacturer: ")
    elif decide == "6":
        current_table = data_manager.get_table_from_file('tool_manager/tools.csv')
        ui.print_result(get_average_durability_by_manufacturers(current_table),
                        "Average of durability tools by manufacturer: ")
    elif decide == "0":
        pass


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ["id", "name", "manufacturer", "purchase_date", "durability"]
    ui.print_table(table, title_list)
    # your code

    pass


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):

    title_list = ["id", "name", "manufacturer", "purchase_date", "durability"]
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

    title_list = ["id", "name", "manufacturer", "purchase_date", "durability"]
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

# the question: Which items has not yet exceeded their durability ?
# return type: list of lists (the inner list contains the whole row with their actual data types)
#
# @table: list of lists
def get_available_tools(table):
    year = 2016
    list_of_available_tools = []
    for row in table:
        row_year = int(row[3])
        row_durab = int(row[4])
        if row_year + row_durab >= year:
            list_of_available_tools.append(row)
    return list_of_available_tools

# the question: What are the average durability time for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
#
# @table: list of lists


def get_average_durability_by_manufacturers(table):
    durabilty = {}
    for row in range(len(table)):
        counter = 0
        sum_of_durability = 0
        result = 0
        for manufacturer in range(len(table)):
            if table[manufacturer][2] == table[row][2]:
                sum_of_durability += int(table[manufacturer][4])
                counter += 1
        result = sum_of_durability / counter
        durabilty.update({table[row][2]: result})
    return durabilty

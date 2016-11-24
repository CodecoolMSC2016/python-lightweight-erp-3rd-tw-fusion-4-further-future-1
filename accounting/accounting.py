# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string (in = income, out = outcome)
# amount: number (dollar)


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
                    "Highest profitting year",
                    "Average profit per year"]

    ui.print_menu("Accounting menu", list_options, "Exit to the main menu")
    decide = ui.get_inputs("", "")
    if decide == "1":
        show_table(data_manager.get_table_from_file('accounting/items.csv'))
    elif decide == "2":
        current_table = data_manager.get_table_from_file(
            'accounting/items.csv')
        data_manager.write_table_to_file(
            'accounting/items.csv', add(current_table))
    elif decide == "3":
        current_table = data_manager.get_table_from_file(
            'accounting/items.csv')
        identificator = ui.get_inputs("Enter an ID to delete", "")
        data_manager.write_table_to_file(
            'accounting/items.csv', remove(current_table, identificator))
    elif decide == "4":
        current_table = data_manager.get_table_from_file(
            'accounting/items.csv')
        identificator = ui.get_inputs("Enter an ID to update", "")
        data_manager.write_table_to_file(
            'accounting/items.csv', update(current_table, identificator))
    elif decide == "5":
        current_table = data_manager.get_table_from_file(
            'accounting/items.csv')
        ui.print_result(which_year_max(current_table), "Highest profitting year: ")
    elif decide == "6":
        current_table = data_manager.get_table_from_file(
            'accounting/items.csv')
        ui.print_result(avg_amount(current_table), "Average profit per year: ")
    elif decide == "0":
        pass


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ["month", "year", "day", "year", "type", "amount"]
    ui.print_table(table, title_list)


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):

    title_list = ["month", "day", "year", "type: in or out(come)", "amount"]
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

    title_list = ["month", "day", "year", "type: in or out(come)", "amount"]
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

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):

    maximum = 0
    years_dict = {}
    most_profitable_year = 0
    for row in table:
        if row[3] not in years_dict:
            years_dict.update({row[3]: int(row[5])})
        else:
            if row[4] == "out":
                years_dict[row[3]] -= int(row[5])
            if row[3] in years_dict:
                years_dict[row[3]] += int(row[5])
    for value in years_dict.values():
        if int(value) > maximum:
            maximum = int(value)
    for key, value in years_dict.items():
        if value == maximum:
            key = int(key)
            return key

    # the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
    # return the answer (number)


def avg_amount(table, year):

    year_given = int(year)
    sum_of_amount = 0
    counter = 0
    for row in table:
        year = int(row[3])
        value = int(row[5])
        if year == year_given:
            if row[4] == "out":
                sum_of_amount -= value
            else:
                sum_of_amount += value
            counter += 1
    return sum_of_amount / counter

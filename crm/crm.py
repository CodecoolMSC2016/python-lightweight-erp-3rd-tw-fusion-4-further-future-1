# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# email: string
# subscribed: boolean (Is she/he subscribed to the newsletter? 1/0 = yes/not)


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
                    "Longest name ID",
                    "List of subscribed emails"]

    ui.print_menu("Customers menu", list_options, "Exit to the main menu")
    decide = ui.get_inputs("", "")
    if decide == "1":
        show_table(data_manager.get_table_from_file('crm/customers.csv'))
    elif decide == "2":
        current_table = data_manager.get_table_from_file('crm/customers.csv')
        data_manager.write_table_to_file(
            'crm/customers.csv', add(current_table))
    elif decide == "3":
        current_table = data_manager.get_table_from_file('crm/customers.csv')
        identificator = ui.get_inputs("Enter an ID to delete", "")
        data_manager.write_table_to_file(
            'crm/customers.csv', remove(current_table, identificator))
    elif decide == "4":
        current_table = data_manager.get_table_from_file('crm/customers.csv')
        identificator = ui.get_inputs("Enter an ID to update", "")
        data_manager.write_table_to_file(
            'crm/customers.csv', update(current_table, identificator))
    elif decide == "5":
        current_table = data_manager.get_table_from_file('crm/customers.csv')
        ui.print_result(get_longest_name_id(current_table), "Longest name ID: ")
    elif decide == "6":
        current_table = data_manager.get_table_from_file('crm/customers.csv')
        ui.print_result(get_subscribed_emails(current_table), "List of subscribed e-mails: ")
    elif decide == "0":
        pass


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ["id", "name", "e-mail", "subscribed"]
    ui.print_table(table, title_list)
    # your code

    pass


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):

    title_list = ["name", "e-mail", "subscribed"]
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

    title_list = ["name", "e-mail", "subscribed"]
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


# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name,
# return the first of descending alphabetical order
def get_longest_name_id(table):

    longest_name = 0
    sorted_list = []
    for row in table:
        name = row[1]
        if len(name) > longest_name:
            longest_name = len(name)
    for row in table:
        name = row[1]
        if len(name) == longest_name:
            sorted_list.append(row)
        list_length = len(sorted_list)
        while list_length > 1:
            list_length -= 1
            for row in range(len(sorted_list) - 1):
                if sorted_list[row][1].lower() > sorted_list[row + 1][1].lower():
                    sorted_list[row], sorted_list[row + 1] = sorted_list[row + 1], sorted_list[row]
    return sorted_list[0][0]


# the question: Which customers has subscribed to the newsletter?
# return type: list of string (where string is like email+separator+name,
# separator=";")
def get_subscribed_emails(table):

    list_of_subscribed = []
    for row in table:
        subscribed = row[3]
        if subscribed == "1":
            email = row[2]
            name = row[1]
            result_row = email + ";" + name
            list_of_subscribed.append(result_row)
    return list_of_subscribed

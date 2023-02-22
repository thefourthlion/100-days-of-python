from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Colors", ["red","white","blue"])
table.add_column("Index", ["First", "Second", "Third"])
print(table)
'''
This code is to get familiar with working with OOP and python packages.
I am using prettytable package to get familiar with OOP in python.
'''
from prettytable import PrettyTable

table = PrettyTable(["Pokemon", "Type"])

table.add_row(["Chespin","Grass"])
table.add_row(["Quilladin","Grass"])
table.add_row(["Chesnaught","Grass, Fighting"])
table.add_row(["Spewa","Bug"])
table.add_row(["Vivillon","Bug, Flying"])
table.add_row(["Caterpie","Bug"])
table.add_row(["Metapod","Bug"])
table.add_row(["Butterfree","Bug, Flying"])
table.add_row(["Weedle","Bug, Poison"])
table.add_row(["Kakuna","Bug, Poison"])
table.add_row(["Beedrill","Bug, Poison"])
table.add_row(["Pansage", "Grass"])
table.add_row(["Simisage","Grass"])
print(table)

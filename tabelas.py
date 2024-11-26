from tabulate import tabulate

table = [['Firs Name', 'Last Name', 'Age'],
         ['John', 'Smith', 39],
         ['Mary', 'Jane', 25],
         ['Jennyfer', 'Doe', 28]
         ]

print(tabulate(table))
print(tabulate(table, headers='firstrow', tablefmt='grid'))
print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
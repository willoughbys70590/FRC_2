# Get variable costs...
variable_costs = [
    ['Plain white Mug', 1.0],
    ['Printing', 0.75],
    ['Packaging', 0.5]
]

# main routine goes here ...

variable_name = input( "what will you be making?")
how_many = input("how many items will you be making?")
# varible_costs = input ("please enter variable costs")

subtotal = 0
for item in variable_costs:
    print("{}: ${:.2f}".format(item[0], item[1]))
    subtotal += item[1]

print(subtotal)
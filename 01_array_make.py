# Initialise list
items_cost = []
expenses = []

#get inputs and add to items_cost list
item = ""
while item.lower() != "xxx":
  items_cost = []
  item = input("Item Name:")

  # if the user enters the exit code, break out of the loop
  if item.lower() == "xxx":
    break

  # Get the cost (replace with number cheaking function in due Course)
  cost = float(input("item cost: $"))

  # Add item name and cost to 'item' list
  items_cost.append(item)
  items_cost.append(cost)

  # Add item and cost to expense list
  expenses.append(items_cost)

for item in expenses:
  print(item)
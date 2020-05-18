expense_list = [['white Mug', 1.0], ['printing', 0.75], ['packaging', 0.5]]

#sort from lowest to highest.
expense_list.sort(key=lambda x: x[1]), reverse=1

# output...
print("**** Items by cost <Most Expensive to least expensive> *******")
for item in expense_list:
    print("{}: ${:.2f}".format(item[0], Item[1]))
    
 print()

 # sort alphabetically
 expense_list.sort(key=lambda x: x[0])

print("**** items ,Alphabetical. *******")
for item in expense_list:
    print("{}: ${:.2f}".format(items[0], item[1]))


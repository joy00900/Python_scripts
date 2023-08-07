my_list = [] # create empty list
print("Empty list creation: ", my_list)

my_list = [1, 2, 3, 'Harsh', 3.132] # creating list with data
print("Creating list: ", my_list)

my_list.append([555, 12]) # add as a single element
print("Appended list: ", my_list)

my_list.extend([234, 'Mudit']) # add as different elements
print("Extending the list: ", my_list)

my_list.insert(1, 'Start') # add element at index 1
print("Inserting an element in a position: ", my_list)

count_occurrence = my_list.count(2)  # count the occurrence in the list
print("Counting the occurrence: ", count_occurrence)

del my_list[5] # delete element at index 5
print("Deleting an element at an index: ", my_list)

my_list.remove('Mudit') # remove element with value
print("Removing an element: ", my_list)

a = my_list.pop(1) # pop element from list
print("Popping an element: ", my_list)

my_list.clear() # empty the list
print("Emptying the list: ", my_list)


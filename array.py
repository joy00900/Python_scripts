cars = ["Ford", "Volvo", "BMW", "Volvo"]

print(cars[2])  # Accessing the element at index 2
print(len(cars))  # Getting the length of the list

for x in cars:  # Iterating and printing all elements in the list
    print(x)

cars.append("Honda")  # Adding one more element to the list
print(cars)

cars.count("Volvo")  # Counting the number of occurrences of "Volvo" in the list
print(cars)

cars.pop(1)  # Deleting the second element from the list
print(cars)

cars.remove("BMW")  # Deleting the element that has the value "BMW"
print(cars)

cars.clear()  # Removing all the elements from the list
print(cars)


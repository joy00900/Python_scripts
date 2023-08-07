x = {'Harsh': 7, 'Mudit': 10}

x['Harsh'] = 3  # updating the value
print(x)  # All the key-value in the dictionary

print(x['Harsh'])  # get the value of a key

del x['Mudit']  # delete a key
print(x)

x['Deepak'] = 9  # Adding a key value pair
print(list(x))  # Listing all the keys
print(sorted(x))  # Sorting the keys

'Harsh' in x  # Checking if the key is available in the dictionary
'Paul' not in x  # Checking if the key is not there


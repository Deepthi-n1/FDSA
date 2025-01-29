array = [10, 89, 9, 56, 4, 80, 8]

largest = array[0]
smallest = array[0]

for element in array:
    if element > largest:
        largest = element
    if element < smallest:
        smallest = element

print("largest element:", largest)
print("smallest element:", smallest)







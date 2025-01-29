array = [10, 89, 9, 56, 4, 80, 8]

largest = array[0]
second_largest = None
smallest = array[0]
second_smallest = None

for element in array:
    if element > largest:
        second_largest = largest
        largest = element
    elif second_largest is None or element > second_largest:
        second_largest = element
    
    if element < smallest:
        second_smallest = smallest
        smallest = element
    elif second_smallest is None or element < second_smallest:
        second_smallest = element

print("largest element:", largest)
print("second largest element:", second_largest)
print("smallest element:", smallest)
print("second smallest element:", second_smallest)
S
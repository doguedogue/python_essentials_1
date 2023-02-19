array = [8, 10, 6, 2, 4]

print (array)

for c in range (len(array)):    
    print ("Ciclo:", c)
    swapped = False
    for i in range(len(array)-1-c):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
            swapped = True
        print (array)
    if not swapped:
        break
print("Sorted: ", array)
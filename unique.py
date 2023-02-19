my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

my_list.sort()
print ("sorted: ",my_list)
i = 0
while True:
    print("i",i)
    if my_list[i] == my_list[i+1]:
        del my_list[i+1]
    else:
        i += 1
    print("i",i,"list=", my_list)
    if i > len(my_list)-2:
        break

print("The list with unique elements only:")
print(my_list)
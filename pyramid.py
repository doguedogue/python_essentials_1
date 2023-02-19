blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#
misbloques, height = 0, 0
while blocks:
    height += 1
    misbloques += height 
    print("Ciclo", height, "misbloques", misbloques)
    if misbloques == blocks:
        break
    elif misbloques > blocks:
        height -= 1
        break
    
else:
    height = 0


print("The height of the pyramid:", height)


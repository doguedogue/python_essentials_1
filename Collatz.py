c0 = int(input("Enter c0: "))

if c0 > 1:
    steps = 0
    while c0 != 1:
        #ODD impar
        if c0 %2 != 0:
            cnew = 3 * c0 + 1
        #EVEN par        
        else:
            cnew = c0 // 2
        c0 = cnew
        print("c0 = ",c0)        
        steps += 1
        if c0 == 1:
            break
    print("steps =",steps)
else:
    print("Bad c0 value")

def is_a_triangle(a, b, c):
    #if a + b <= c or b + c <= a or c + a <= b:
    #    return False
    #return True
    return a + b > c and b + c > a and c + a > b


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))


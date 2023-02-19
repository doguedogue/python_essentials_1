def is_prime(num):
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True

for i in range(1, 1000):
    if is_prime(i + 1):
        print(i + 1, end=" ")       
print()

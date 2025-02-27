#ex9:
def prime(x):
    for i in range(2,x//2):
        if (x%i==0):
            return False
    return True
print(prime(7))
print(prime(10))
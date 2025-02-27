#ex5 
def find_factorial(x):
    if(x==1):
        return 1
    return x*find_factorial(x-1)
print(find_factorial(5))
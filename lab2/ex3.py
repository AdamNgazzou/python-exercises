#ex3
def calculate_average(t,n):
    summ=0
    for i in range(n):
        summ=summ+t[i]
    return summ/n

print(calculate_average([1,2,3,4,5],5))
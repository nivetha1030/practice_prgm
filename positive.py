#the sum of all positive numbers in an array.
def sum_positive(arr):
    tot = 0
    for i in arr:
        if i > 0 :
          tot  += i
    return tot
arr = [1,-7,-6,5,-3,3]
result = sum_positive(arr)
print("The sum of all positive numbers is:",result)

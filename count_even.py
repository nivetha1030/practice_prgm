#Counting the number of even numbers in an array.
arr = [34,545,23,76,45,77,44,109]
count = 0
for i in arr:
    if i % 2 == 0:
        count += 1
print("The  count of even num is:", count)

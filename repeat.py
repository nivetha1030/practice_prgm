# 1st repeative character in string
a = "Apple"
a = a.lower()  

for i in range(len(a)):
    count = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            count += 1
    if count > 1 and a[i] not in a[:i]:
        print(a[i])

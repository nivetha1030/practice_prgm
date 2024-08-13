# maximum element in an array.
 def max_ele(arr):
 max_num = arr[0]
 for i in range(1,len(arr)):
   if arr[i] > max_num:
       max_num = arr[i]
 return max_num      
 
arr = [2,9,5,100,35,57]
print("The max num is: ",max_ele(arr))

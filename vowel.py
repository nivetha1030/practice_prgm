#Count the number of vowels in a string.
def count_vowels(string):
 vowels = "aeiouAEIOU"
 count = 0
 for char in string:
     if char in vowels:
         count+= 1
 return count
input_string = "Elephant"
result = count_vowels(input_string)
print("Number of vowels in the string:", result)
 

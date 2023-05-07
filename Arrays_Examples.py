#Document Strings for Methods and Classes
#
# For comments
/*
* Multi line comments
*/
"""
Using List as Array
"""

#initializing the array
sample = []
firstName = "Naidu" #its an array. Strings (or String Arrays) are immutable

#Creating Array
sample = [1,2,4]

#printing Array
sample

#Accessing the Element..Random Access ... O(1)
sample[0]

#iterating the elements
for i in sample:
    pront i

sample[::1]

#Searching the Element ... is it O(n) in python?

if 20 in sample:
    print("the number is present in the Array")
    
#Adding Element at the end ...O(1)
sample.append(5)

#Inserting the element in the order --- 0(n)

#Updating element --- O(1)
sample[1] = 4

#Popping the element at the end ...O(1)
sample[-1]

#Deleting the Element ..... is it O(n) in python?
del sample[0]

#sorting the elements
sorted(sample)

#revering the String
firstName[::-1]

#Palindrome example
#Example to check the output
#racecar
#abcba
#abba

def isPalindrome(s:str) -> bool :
    i=0
    j=len(s)-1 #Since index follows 0-notation for the first element

    while(i<j):    #We dont need to check for the equal sign...equal sign indicates a case where the letter will be same in either order.
        if (s[i] != s[j]):
            flag=False
            return False
        i+=1
        j-=1
         
    return True

isPalindrome('racecar')

isPalindrome('check')



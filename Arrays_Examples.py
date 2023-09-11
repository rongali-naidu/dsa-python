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

#Palindrome example...Time Complexity : O(n)
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

from typing import List
def sortedSquares(nums:List[int]) -> List[int]:
    return sorted(map(lambda num:num*num,nums))
    
    
def sortedSquares2(nums:List[int]) -> List[int]:
    nsnum = []
    psnum = []
    snum = []
    for num in nums:
        if num<0:
            nsnum.append(num*num)
        else :
            psnum.append(num*num)
    #merge the two arrays. nsnum merge from the right most number.
    nlen = len(nsnum)
    plen = len(psnum)
    pindx = 0
    nindx = nlen - 1
    while (nindx>-1 or pindx < plen):
        
        if (pindx >= plen):
            snum.append(nsnum[nindx])
            nindx -= 1
        elif (nindx <= -1):
            snum.append(psnum[pindx])  
            pindx += 1
        elif (nsnum[nindx] < psnum[pindx]):
            snum.append(nsnum[nindx])
            nindx -= 1
        else:
            snum.append(psnum[pindx])  
            pindx += 1
    
    return snum
    
def sortedSquares3(nums:List[int]) -> List[int]:
    #keep two pointets...one at the left and second one at right
    #keep populating biggest numbers , next biggest so on
    lindx = 0
    nums_length = len(nums)
    rindx = nums_length-1
    snum = [0]*nums_length
    sindx = nums_length-1
    while (lindx<=rindx):
        if (nums[lindx]*nums[lindx] > nums[rindx]*nums[rindx]):
            snum[sindx] = nums[lindx]*nums[lindx]
            sindx -= 1
            lindx += 1
        else:
            snum[sindx] = nums[rindx]*nums[rindx]
            sindx -= 1
            rindx -= 1     
               
    return snum

nums = [-4,-1,1,3,10]
sortedSquares3(nums)

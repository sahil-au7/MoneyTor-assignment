# Implement a program which will take an array as an input and remove the duplicates from it.
#  Eg. If [1,2,3,4,4,2,1,5,1,4,5] is the input, then the output should be [1,2,3,4,5]. 
# Bonus - Implement this function in O(nlogn) time complexity and O(1) space complexity. Constraints: 1 <= array length <= 1000000

# creating an empty list
inputList = []

# number of elements as input
n = int(input("Enter number of elements : ")) 

# Taking input
for i in range(0, n):
    ele = int(input())
    inputList.append(ele)

noDupicateList = []
for e in inputList:
    if e in noDupicateList:
        continue
    noDupicateList.append(e)

print(noDupicateList)
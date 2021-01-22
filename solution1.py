# // Implement a program which will take 2 parameters as input 'a' and 'b' and return a^b as output.
# // Eg.If a is 5 and b is 3, then the output will be 5 ^ 3 = 125. Bonus - Implement this program using recursion.Constraints: 1 <= a, b <= 10

# Power Function
def noPower(num,idx):
    if(idx==1):
       return(num)
    else:
       return (num * noPower(num, idx - 1))

# Taking Inputs
base=int(input("Enter number: "))
exp = int(input("Enter index: "))

result=noPower(base,exp)
print("{} raised to {}: {}".format(base,exp,result))

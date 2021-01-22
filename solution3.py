# Implement a program which will take 1 parameter as input and print fibonacci numbers upto that input. Constraints: 1 <= n <= 1000000


nTerms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nTerms <= 0:
   print("Please enter a positive integer")
elif nTerms == 1:
   print("Fibonacci sequence upto",nTerms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nTerms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

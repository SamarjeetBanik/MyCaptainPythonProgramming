# Program to display the Fibonacci sequence up to nth term

n = int(input("Enter the number of terms: "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(n1)
else:
   print("Fibonacci sequence upto",n,"terms: ")
   while count < n:
       print(n1, end = " ")
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
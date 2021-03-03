# Python program to print positive Numbers in a List 

# an empty list 
lst = []

# number of elemetns as input 
n = int(input("Enter number of elements : "))

# iterating till the range 
print("Enter the elements into the list:")
for i in range(0, n): 
    ele = int(input()) 
    lst.append(ele) # adding the element 
    
print("Positive elements from list:")
# iterating each number in list 
for num in lst: 
	
	# checking condition 
	if num >= 0: 
		print(num, end = " ") 

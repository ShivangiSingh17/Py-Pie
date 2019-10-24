# creating an empty list
array=[]
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
# iterating till the range
for i in range(0, n): 
    a = int(input())   
    array.append(a) # adding the element 
    # to get first and last element of list 
nlist = [ array[0], array[-1] ] 
 
print ("The first and last element of list are : " +  str(nlist)) 
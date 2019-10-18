nums= int(input("Enter the number of elements in the list: "))
a=[]
for i in range(0,nums):
	x= int(input("Enter the numbers: "))
	a.append(x)
b=[]
elem= (a[0], a[-1])
b.append(elem)
print(b)

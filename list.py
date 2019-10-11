n=int(input("Enter the array length"))
a=[]
l=[]
for i in range (n) :
   x=int(input("Enter the array elements"))
   a.append(x)
l.append(a[0])
l.append(a[n-1])
print(l)

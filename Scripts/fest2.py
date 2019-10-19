def reverse(sent):
	list1=[]
	list1= sent.split()
	list2=[]
	for i in list1:
		list2.insert(0,i)
	return list2
		
def main():
	sent= raw_input("Enter the sentence: ")
	k=[]
	k= reverse(sent)
	print ' '.join(str(p) for p in k)
main()

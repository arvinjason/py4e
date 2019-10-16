file = input('Enter file name: ')
fh = open(file)
lst = list()
for line in fh:
	temp1 = line.split()
	lst = lst + temp1
lst = list(dict.fromkeys(lst))
lst.sort()
print(lst)

file = input('Enter file name: ')
fh = open(file)
domain = dict()
for line in fh:
	if line.startswith("From "):
		lst = line.split()
		lst2 = lst[1].split('@')
		if lst2[1] not in domain:
			domain[lst2[1]] = 1
		else:
			domain[lst2[1]] = domain[lst2[1]] + 1
print(domain) 

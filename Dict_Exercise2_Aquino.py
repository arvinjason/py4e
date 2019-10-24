file = input('Enter file name: ')
fh = open(file)
email = dict()
for line in fh:
	if line.startswith("From "):
		lst = line.split()
		if lst[1] not in email:
			email[lst[1]] = 1
		else:
			email[lst[1]] = email[lst[1]] + 1
print(email) 

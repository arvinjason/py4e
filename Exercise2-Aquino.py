hours = input('Enter Hours: ')
try:
	h = int(hours)
except:
	h = -1

if h>0:
	rate = input('Enter Rate: ')
	try:
		r = int(rate)
	except:
		r = -1
	if r>0:
		if h > 40:
			h2 = h - 40
			h = 40
			pay = (h*r)+(h2*(r*1.5))
			print('Pay: ', pay)
		else:
			pay = (h*r)
			print('Pay: ', pay)
	else:
		print('Error please enter numerical input')
else:
	print('Error please enter numerical input')	



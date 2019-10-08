hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
h = float(hours)
r = float(rate)
pay = 0
if h > 40:
	h2 = h - 40
	h = 40
	pay = (h*r)+(h2*(r*1.5))
	print('Pay: ', pay)
else:
	pay = (h*r)
	print('Pay: ', pay)
	
import csv

with open('Export.csv', 'rb') as f:
	reader = csv.reader(f)
	debitList = list(reader)

total = 0.0

for each in debitList[4:]:
	if len(each)>=5:
		splitValue = (each[4].split('.'))
		if len(splitValue[-1]) > 0:
			remainder = splitValue[-1]
			print(remainder)
			amountToAdd = 100-float(remainder)
			print(str(total) + " + " + str(amountToAdd))
			total = total + amountToAdd

total=int(total)
strTotal=str(total)
print('$' + strTotal[:-2] + '.' + strTotal[-2:])

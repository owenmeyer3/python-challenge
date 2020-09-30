import csv

readPath = '/Users/Owen/Desktop/DSV/_HW_Repos/python_challenge/PyBank/Resources/budget_data.csv'

with open(readPath, 'r', newline = '') as csvFile:
	csvReader = csv.reader(csvFile, delimiter = ',')


	monthCount = 0
	for row in csvReader:
		if row[0] != '':
			monthCount += 1
		else:
			break
        
#header is not a month
monthCount -= 1

print('monthCount = ' + str(monthCount))
	

#import libraries
import csv

#define csv read and txt write paths
readPath = '/Users/Owen/Desktop/DSV/_HW_Repos/python_challenge/PyBank/Resources/budget_data.csv'
writePath = '/Users/Owen/Desktop/DSV/_HW_Repos/python_challenge/PyBank/Analysis/results.txt'

#initializa variables and arrays
monthCount = 0
isHeader = True
runningProfit = 0.00
lastProfit = 0.00
profits = []
profitChanges = []
maxProfit = 0.00
maxProfitMonth = ''
minProfit = 0.00
minProfitMonth = ''

with open(readPath, 'r', newline = '') as csvFile:
    csvReader = csv.reader(csvFile, delimiter = ',')

    for row in csvReader:
        #do not calculate on header row
        if isHeader:
            isHeader = False
            continue
        #calculate for-non blank rows
        if row[0] != '':
            #store month and profits from csv
            month = row[0]
            profit = float(row[1])
            
            #count months
            monthCount += 1
            
            #accumulate profits
            runningProfit += profit
            
            #create array of changes in profit (to average later)
            profitChange = profit - lastProfit
            profitChanges.append(profitChange)
            
            #find maximum profit with month
            if profit > maxProfit:
                maxProfit = profit
                maxProfitMonth = month
                
            #find minimum prifit with month
            if profit < minProfit:
                minProfit = profit
                minProfitMonth = month
                
            #store profit to use in profit change calculation for the next row
            lastProfit = profit
        else:
            break
        
#print result to console
print('\nFinancial Analysis\n-------------------------------')
print('\nmonthCount = ' + str(monthCount) + '\n')
print('runningProfit = ' + "${:,.2f}".format(runningProfit) + '\n')
print('avgProfitChange = ' + "${:,.2f}".format(runningProfit/monthCount) + '\n')
print('maxProfit = ' + maxProfitMonth + ': ' + "${:,.2f}".format(maxProfit) + '\n')
print('maxlosses = ' + minProfitMonth + ': ' + "${:,.2f}".format(minProfit) + '\n')

#print result to txt
with open(writePath, 'w') as result:
    result.write('Financial Analysis\n-------------------------------\n\n')
    result.write('monthCount = ' + str(monthCount) + '\n\n')
    result.write('runningProfit = ' + "${:,.2f}".format(runningProfit) + '\n\n')
    result.write('avgProfitChange = ' + "${:,.2f}".format(runningProfit/monthCount) + '\n\n')
    result.write('maxProfit = ' + maxProfitMonth + ': ' + "${:,.2f}".format(maxProfit) + '\n\n')
    result.write('maxlosses = ' + minProfitMonth + ': ' + "${:,.2f}".format(minProfit) + '\n\n')

	

#import libraries
import csv

#define csv read and txt write paths
readPath = '/Users/Owen/Desktop/DSV/_HW_Repos/python_challenge/PyPoll/Resources/election_data.csv'
writePath = '/Users/Owen/Desktop/DSV/_HW_Repos/python_challenge/PyPoll/Analysis/results.txt'

#initializa variables and arrays
voteCount = 0
isHeader = True
votesByCandidate = {}
percentByCandidate = {}


with open(readPath, 'r', newline = '') as csvFile:
    csvReader = csv.reader(csvFile, delimiter = ',')

    for row in csvReader:
        #stores but does not calculate on header row
        if isHeader:
            headerRow = row
            isHeader = False
            continue
        #calculate for-non blank rows
        if row[0] != '':
            #store votedId, county and candidate from csv
            voterID = int(row[0])
            candidate = row[2]
            
            #count votes
            voteCount += 1
            
            #add unique candidates to candidates list with 1 vote
            if candidate not in list(votesByCandidate.keys()):
                votesByCandidate.update({candidate: 1})
            else:
                #add one vote to candidate
                votesByCandidate[candidate] += 1
        else:
            break

#create dictionary for vote percentages. Get max votes with candidate
maxPercent = 0.0
percentByCandidate = votesByCandidate.copy()
for can, votes in percentByCandidate.items():
    percentByCandidate.update({can: votes / voteCount})
    if votes/voteCount > maxPercent:
        maxPercent = votes / voteCount
        maxCandidate = can
        
#print result to console
print('\nElection Results\n-------------------------------')
print('Total Votes: ' + str(voteCount) + '\n-------------------------------')
for can, percent in percentByCandidate.items():
    print(str(can) + ': ' + 
          '{:,.3f}%'.format(float(percent)*100) + ' (' +
          str(votesByCandidate[can]) + ')')
print('-------------------------------')
print('Winner: ' + maxCandidate)


#print result to txt
with open(writePath, 'w') as result:
    result.write('Election Results\n-------------------------------\n')
    result.write('Total Votes: ' + str(voteCount) + '\n-------------------------------\n')
    for can, percent in percentByCandidate.items():
        result.write(str(can) + ': ' + 
          '{:,.3f}%'.format(float(percent)*100) + ' (' +
          str(votesByCandidate[can]) + ')\n')
    result.write('-------------------------------\n')
    result.write('Winner: ' + maxCandidate)




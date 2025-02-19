#As you can tell, I had a lot of trouble with both exercises but am submitting anyway in hopes of getting partial credit for my code

# Import the os module to allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Set path for file
csvpath = os.path.join('Resources', '02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')

#Create lists to store data
count_votes = 0
votes = []
candidate = []
vote_percent = []

# Open and read the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # skip the first row of the CSV file
    header = next(csvreader)
#Begin loop
#Count total number of votes cast [Sum of votes]
    for row in csvreader:
    #count total number of votes cast
        count_votes = count_votes + 1

#list of candidates who received votes [Unique names in Column 2]
#This portion of code from https://www.geeksforgeeks.org/python-get-unique-values-list/
#check if candidate exists in list and add to their vote count
    if row[2] not in candidate:
        count_votes = count_votes + 1
        candidate.append(row[2])
    #if in list, add to vote count
    else:
        count_votes = count_votes + 1

#Total number of votes each candidate won
for i in range(len(candidate)):
    if row[2] == candidate

#percentage of votes each candidate won [Total number of votes per candidate / sum of votes]
    vote_percent = (candidate/count_votes) * 100
    
#Election winner based on popular vote [max value]
winner = max(vote)


#Print Findings
print("Election Results")
print("--------------------------------")
print(f"Total Votes:" + str(votes))
print("--------------------------------")
print(f"{candidate} {vote_percent}% ({votes})")
print("--------------------------------")
print(f"Winner: {winner}"")
print("--------------------------------")
# Specify the file to write to (txt file in the Analysis folder)

output_path = os.path.join("..", "Analysis", "new_pypoll.txt")

with open(output_path, "w", newline= '', encoding ='utf8') as datafile:
    writer = csv.writer(datafile)

    #write output file
    writer.writerow([
        ["Election Results"]
        ["--------------------------------"]
        [f"Total Votes:" + str(votes)]
        ["--------------------------------"]
        [f"{candidate} {vote_percent}% ({votes})"]
        ["--------------------------------"]
        [f"Winner: {winner}"]
        ["--------------------------------"]
    ])

        
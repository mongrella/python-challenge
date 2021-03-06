# Import the os module to allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Set path for file
csvpath = os.path.join('..', 'Resources', '02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')


# Open and read the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # skip the first row of the CSV file
    header = next(csvreader)

#Create lists to store data
count_votes = 0
total_votes = []
candidates = []
unique_candidate =[]
vote_percent = []

#Count total number of votes cast [Sum of votes]


#list of candidates who received votes [Unique names in Column 2]

#percentage of votes each candidate won [Total number of votes per candidate / sum of votes]


#Total number of votes each candidate won

#Election winner based on popular vote [max value]

# Specify the file to write to (txt file in the Analysis folder)

output_path = os.path.join("..", "Analysis", "new_pypoll.txt")

with open(output_path, "w", newline= '', encoding ='utf8') as datafile:
    writer = csv.writer(datafile)

    #write output file
    writer.writerow([
        
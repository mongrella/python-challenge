# Import the os module to allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Set path for file
csvpath = os.path.join('..', 'Resources', '02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

#Create lists to store data
output_rows = []
date = []
profit []
total_profit_change = []
average_profit_change = []

# Open and read the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # skip the first row of the CSV file
    header = next(csvreader)


#Total number of votes cast

#list of candidates who received votes

#percentage of votes each candidate won


#Total number of votes each candidate won

#Election winner based on popular vote

# Specify the file to write to (txt file in the Analysis folder)

output_path = os.path.join("..", "Analysis", "new_pybank.txt")

with open(output_path, "w", newline= '', encoding ='utf8') as datafile:
    writer = csv.writer(datafile)

    #write output file
    writer.writerow([
        
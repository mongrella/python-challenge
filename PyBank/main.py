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


#CSV file has to have two columns: Date and Profit/Losses

#iterate through rows after first row (header)
for row in csvreader:
    #apppend to column extractions
    date.append(row[0])
    profit.append(row[1])


# Calculate the total number of months included in the dataset
total_date = len(date)

# Calculate the net total amount of "Profit/Losses" over the entire period
#Iterate through rows to get average changes
for i in range(len(profit)):
    total_profit_change.append(profit[i+1]-profit[i])
    

#Calculate the average of the changes in "Profit/Losses" over the entire period
average_profit_change = sum(total_profit_change) / len(total_profit_change)

#Calculate the greatest increase in profits (date/index and amount) over the entire period
greatest_increase = max(average_profit_change)
greatest_increase_month = average.profit.change.index(max(average_profit_change))

#Calculate The greatest decrease in losses (date/index and amount) over the entire period
greatest_decrease = min(average_profit_change)
greatest_decrease_month = average.profit.change.index(min(average_profit_change))

#Print Findings
print("Financial Analysis")
print("--------------------------------")
print("Total Months:" + str(total_date))
print("Total Revenue: $" + str(profit))
print("Average Revenue Change: $" + str(average_profit_change))
print("Greatest Increase in Profit:" + str(greatest_increase_month) + "($ " + str(greatest_increase) + ")")
print("Greatest Decrease in Profit:" + str(greatest_decrease_month) + "($ " + str(greatest_decrease) + ")")


# Specify the file to write to (txt file in the Analysis folder)

output_path = os.path.join("..", "Analysis", "new_pybank.txt")

with open(output_path, "w", newline= '', encoding ='utf8') as datafile:
    writer = csv.writer(datafile)

    #write output file
    writer.writerow([
        ["Financial Analysis"],
        ["--------------------------------"],
        ["Total Months:" + str(total_date)],
        ["Total Revenue: $" + str(profit)],
        ["Average Revenue Change: $" + str(average_profit_change)],
        ["Greatest Increase in Profit:" + str(greatest_increase_month) + "($ " + str(greatest_increase) + ")"],
        ["Greatest Decrease in Profit:" + str(greatest_decrease_month) + "($ " + str(greatest_decrease) + ")"]
    ])


# Final script should both print the analysis to the terminal and export a text file with the results.
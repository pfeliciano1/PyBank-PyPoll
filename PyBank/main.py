# Your task is to create a Python script that analyzes the records to calculate each of the following:

# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

# Import modules (os,csv)
import os
import csv

# Setting path for data
csvpath = os.path.join( "..", "Resources", "budget_data.csv")
# Specify the file to write to
output_path = os.path.join("..", "analysis", "financial_analysis.txt")

# Naming the lists and variables
date = []
prof_loss = []
total = 0
changes = 0
total_changes = 0
previous = 0
grt_inc = 0
grt_dec = 0

# Opening the path using "reader" mode.
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    for row in csvreader:
        # Add date by month
        date.append(row[0])
        # Add profit and losses
        prof_loss.append(row[1])

# The total number of months included in the dataset
        # num_months += 1
# The net total amount of "Profit/Losses" over the entire period
        total += int(row[1])
# Calculate the changes in "Profit/Losses" over the entire period, 
        changes = int(row[1]) - previous
        if previous == 0:
            changes = 0
        previous = int(row[1])
        total_changes += changes
        
# then find the average of those changes
        avg_changes = total_changes / (len(date))
    
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period
    # increase = max(changes)
    # decrease = min(changes)
    # grt_inc = changes.index(max(changes))+1
    # grt_dec = changes.index(min(changes))+1


    print("Financial Analysis")
    print("------------------------------------")
    print(f'Total Months: {len(date)}')
    print(f'Total: ${total}')
    print(f'Average Change: ${avg_changes:.2f}')
    # print(f'Greatest Increase in Profits: {grt_inc} ({increase})')
    # print(f'Greatest Decrease in Profits: {grt_dec} ({decrease})')

# Open the file using "write" mode. 
# with open(output_path, 'w', newline='') as text:

#     # Initialize csv.writer
#     csvwriter = csv.writer(csvfile, delimiter=',')
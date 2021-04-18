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

# Naming the variables
num_months = 0
total = 0
changes = 0
avg_changes = 0
date = []

# Opening the path using "reader" mode.
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    




# Open the file using "write" mode. 
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
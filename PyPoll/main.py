# You will be give a set of poll data called election_data.csv. 
# The dataset is composed of three columns: Voter ID, County, and Candidate. 
# Your task is to create a Python script that analyzes the votes and calculates each of the following:

# Import modules (os,csv)
import os
import csv

# Setting path for data
csvpath = os.path.join( "..", "Resources", "election_data.csv")
# Specify the file to write to
output_path = os.path.join("..", "analysis", "election_results.txt")

votes = []
county = []
candidates = []
Correycount = 0
Khancount = 0
Licount = 0
OTooleycount = 0
total = 0

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    for row in csvreader:
        # Add votes to list
        votes.append(row[0])
        # Add county to list
        county.append(row[1])
        # Add candidates to list
        candidates.append(row[2])
# The total number of votes cast
        candidate = row[2]
        total += 1

        if (candidate == "Correy"):
            Correycount +=1
        elif (candidate == "Khan"):
            Khancount +=1
        elif (candidate == "Li"):
            Licount +=1
        elif (candidate == "O'Tooley"):
            OTooleycount +=1
# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.
# print(f"Total votes: {}")
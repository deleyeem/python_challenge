import os
import csv

#changedirectory path to the realpath of the file
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#Paths
CSV_PATH = os.path.join("Resources", "election_data.csv")
OUTPUT_PATH = os.path.join("Analysis", "Election_Analysis.txt")

#Indexes to create a reference for a single update if format/column changes
ID_INDEX=0
COUNTY_INDEX=1
CANDIDATE_INDEX=2

#variables
previous_candidate = None
tot_votes = 0

#dictionary
results = {}

#list
candidates = []

#open file using path
with open(CSV_PATH) as csv_file:
    #read file
    csvreader = csv.reader(csv_file)
    #skip header
    next(csvreader)

    for row in csvreader:
        # The total number of votes cast
        tot_votes+= 1

        # A complete list of candidates who received votes. Including this step for instructions to use a list.
        current_candidate=row[CANDIDATE_INDEX]
        if current_candidate not in candidates:
            candidates.append(current_candidate)

        #doing this an alternative way via dictionary
        # The total number of votes each candidate won
        if current_candidate in results:
            results[current_candidate] += 1
        else:
            results[current_candidate] = 1

#The percentage of votes each candidate won
#when writing a loop like this it will always assume the key from the dictionary
winning_count= 0

    
#open file to write
with open(OUTPUT_PATH, "w") as output_file:
    output1= ("Election Results\n"
        "-------------------------\n"
        f"Total Votes: {tot_votes}\n"
        "-------------------------\n")  
    
    output_file.write(output1)
    print(output1)

    for candidate in results:
        votes=results[candidate]
        percentages = "{:.3f}".format((votes/tot_votes) *100)

        #The winner of the election based on popular vote
        if votes > winning_count:
            winner = candidate
            winning_count = votes
        
        output2= f"{candidate}: {percentages}% ({votes})\n"
        
        output_file.write(output2)
        print(output2)
    output3= ("-------------------------\n"
            f"Winner: {winner}\n"
            "-------------------------\n")
    
    output_file.write(output3)
    print(output3)
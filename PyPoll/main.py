import os
import csv

#changedirectory path to the realpath of the file
#os.chdir(os.path.dirname(os.path.realpath(__file__)))

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
candidate_votes = {}

#list
candidates = []
vote_per_candidate = []
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
        if current_candidate in candidate_votes:
            candidate_votes[current_candidate] += 1
        else:
            candidate_votes[current_candidate] = 1

        # The percentage of votes each candidate won
        for candidate in candidate_votes:
            votes=candidate_votes[candidate]
            percentages = (votes/tot_votes) *100
            #how to add to dictionary?
        
        # The winner of the election based on popular vote
        #for vote_count in 
    print(candidate_votes)

output = ("Election Results\n"
          "-------------------------\n"
          f"Total Votes: {tot_votes}\n"
          "-------------------------\n"
          fCharles Casper Stockham: 23.049% (85213)
          Diana DeGette: 73.812% (272892)
          Raymon Anthony Doane: 3.139% (11606)
          "-------------------------\n"
          f"Winner: {winner}\n"
          "-------------------------\n")

# #open file to write
# with open(OUTPUT_PATH, "w") as output_file:
#     output_file.write(output)

# #print to terminal
# print(output)

#dictionary with candidate names as key and value
#import to use csv
import csv

#import to path compatible with windows
import os

#save the path for the csv file
csv_path = os.path.join("Resources","budget_data.csv")

#variables
row_count = 0
tot_months = 0
tot_PL = 0
changes_PL = [] #
avg_PL = [] #avg=tot_PL/tot_month
increase_max = [] #max
decrease_max = [] #min

#open file using path
with open (csv_path, "r") as csvfile:

    #read file
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader, None)  # Skip the header

    #loop through data row by row
    for row in csvreader:
        #count rows for month. Note this gives total of rows.  
        ######DOES LEN FUNCTION OF CSVREADER GET SAME OUTPUT?
        tot_months += 1

        #add column [1] to itself
        tot_PL += int(row[1])

        #evaluate change in  PL??????

        #
        increase_max = max(row[1])
        decrease_max = min(row[1])

avg_PL = int(tot_PL)/int(tot_months)

#save output path to write
output_path = os.path.join("..", "Analysis", "PyBankAnalysis.csv")

#open file to write
with open(output_path, "w", newline= '') as output_file:

    #initialize writer
    csvwriter = csv.writer(output_file, delimiter=",")

    #write rows
    #need to use brackets between ( and " to make it a tuple. The writer function expects iteration????
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["------------------------------"])
    csvwriter.writerow([tot_months])
 
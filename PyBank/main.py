#import to use csv
import csv

#import to path compatible with windows
import os

#save the path for the csv file
csv_path = os.path.join("Resources","budget_data.csv")

#variables
tot_months = 0
tot_PL = 0
changes_PL = [] #

#open file using path
with open (csv_path, "r") as csvfile:
    #read file
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip the header
    next(csvreader, None)

    #loop through data row by row
    for row in csvreader:
        #count rows for month. Note this gives total of rows.  
        ######DOES LEN FUNCTION OF CSVREADER GET SAME OUTPUT?
        tot_months += 1

        #add column [1] to itself
        tot_PL += int(row[1])

        #???? changed_PL

    increase_max = max(row[1])
    decrease_max = min(row[1])

avg_PL = int(tot_PL)/int(tot_months)

#save output path to write
output_path = os.path.join("..", "Analysis", "PyBankAnalysis.txt")

#open file to write
with open(output_path, "w") as output_file:

    #initialize writer - do you need to initialize 
    ##txtwriter = txtwriter.writer(output_file)

    #write rows
    #need to use brackets between ( and " to make it a tuple. The writer function expects iteration????
    #does this have to be line by line
    output_file.write("Financial Analysis\n")
    output_file.write("------------------------------\n")
    output_file.write(f"Total Months: {tot_months}\n")
    output_file.write(f"Total: ${tot_PL}\n")
    #output_file.write(f"Average Change: ${avg_PLs}\n")
    output_file.write(f"Greatest Increase in Profits: {increase_max}\n")
    output_file.write(f"Greatest Decrease in Profits: {decrease_max}\n")
 
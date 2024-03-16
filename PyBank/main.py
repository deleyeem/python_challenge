#import to use csv
import csv

#import to path compatible with windows
import os

#changedirectory path to the realpath of the file
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#Paths
CSV_PATH = os.path.join("Resources","budget_data.csv")
OUTPUT_PATH = os.path.join("Analysis", "PyBankAnalysis.txt")

#Indexes to create a reference for a single update if format/column changes
PL_INDEX = 1
MONTH_INDEX = 0

#variables
tot_months = 0
tot_PL = 0
tot_changes_PL = 0 #
previous_PL = None
increase_max_value = -99999999
decrease_max_value = 100000000

#open file using path
with open(CSV_PATH) as csvfile:
    #read file
    csvreader = csv.reader(csvfile)
    #Skip header
    next(csvreader)

    #loop through data row by row
    for row in csvreader:
        #count number of rows for month
        tot_months+= 1

        #capture current change for profit/loss
        current_PL= int(row[PL_INDEX])

        tot_PL+=current_PL

        #there will be no change for the first. Need this if statement to skip first
        if previous_PL is not None:
            #calculate current change
            current_change_PL = current_PL - previous_PL
            tot_changes_PL += current_change_PL
            #calculate and identify greatest increase value and month
            if current_change_PL >increase_max_value:
                increase_max_value = current_change_PL
                increase_max_month = row[MONTH_INDEX]
            #calculate and identify greatest decrease value and month
            if current_change_PL <decrease_max_value:
                decrease_max_value = current_change_PL
                decrease_max_month = row[MONTH_INDEX] 
        #prepare for next month
        previous_PL = current_PL
        #
        avg_PL = int(tot_changes_PL)/int(tot_months)

output = ("Financial Analysis\n"
          "---------------------------------------------------\n"
          f"Total Months: {tot_months}\n"
          f"Total: ${tot_PL}\n"
          f"Average Change: ${round(avg_PL, 2)}\n"
          f"Greatest Increase in Profits: {increase_max_month} (${increase_max_value})\n"
          f"Greatest Decrease in Profits: {decrease_max_month} (${decrease_max_value})\n")

#open file to write
with open(OUTPUT_PATH, "w") as output_file:
    output_file.write(output)
    print(output)  

#print on terminal
print(output)
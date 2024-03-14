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

    #loop through data row by row
    for row in csvreader:
        #count rows for month. Note this gives total of rows. Will need to subtract by one for headers later.
        row_count += 1

        for row in row[1]:
            #add column [1] to itself
            tot_PL = tot_PL + int(row)

tot_months = row_count - 1
#save output path to write
output_path = os.path.join("..", "Analysis", "PyBankAnalysis.csv")

#open file to write
with open(output_path, "w") as output_file:

    #initialize writer
    csvwriter = csv.writer(output_file, delimiter=",")

    #write first row
    csvwriter.writerow("Financial Analysis")
    csvwriter.writerow("------------------------------")
    csvwriter.writerow("Total Months: {tot_months}")

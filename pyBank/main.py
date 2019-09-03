# Import required packages
import csv
import os

# Files to load and output 
budget_data = "budget_data.csv"

with open(budget_data, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    month = []
    P_and_L = []

    # Read each row of data after the header
    for row in csvreader:
        month.append(row[0])
        P_and_L.append(int(row[1]))
        
    print("Financial Analysis")
    print("--------------------")
    print (f"Total Months: {len(month)}")
    print (f"Total: ${sum(P_and_L)}")
    
    budget_change = []
    
    for x in range(1,len(P_and_L)):
        budget_change.append((int(P_and_L[x]) - int(P_and_L[x-1])))
    
    average_change = sum(budget_change) / len(budget_change)
    print(f"Average  Change: ${round(average_change,2)}")
    
    greatest_increase = max(budget_change)
    print(f"Greatest Increase in Profits: ${greatest_increase} on {month[budget_change.index(greatest_increase)+1]}")

    greatest_decrease = min(budget_change)
    print(f"Greatest Decrease in Profits: ${greatest_decrease} on {month[budget_change.index(greatest_decrease)+1]}")

    #output file
    file = open("output.txt","w")

    file.write("Financial Analysis" + "\n")

    file.write("-------------------" + "\n")

    file.write(f"Total Months: {len(month)} \n")

    file.write(f"Total: ${sum(P_and_L)} \n")

    file.write(f"Average  Change: ${round(average_change,2)} \n")

    file.write(f"Greatest Increase in Profits: ${greatest_increase} on {month[budget_change.index(greatest_increase)+1]} \n")

    file.write(f"Greatest Decrease in Profits: ${greatest_decrease} on {month[budget_change.index(greatest_decrease)+1]} \n")

    file.close()
    

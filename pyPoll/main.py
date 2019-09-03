# Import required packages
import csv
import os

# Files to load and output 
election_data = "election_data.csv"
with open(election_data, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    votes = []
    candidates = []

    # Read each row of data after the header
    for row in csvreader:
        votes.append(row[0])
        candidates.append(row[2])
        
    print("Election Results")
    print("----------------------------")
    print (f"Total Votes: {len(votes)}")
    
    kcount = candidates.count("Khan")
    kpercentage = round((kcount / len(votes))*100, 2)
    ccount = candidates.count("Correy")
    cpercentage = round((ccount / len(votes))*100, 2)
    lcount = candidates.count("Li")
    lpercentage = round((lcount / len(votes))*100, 2)
    ocount = candidates.count("O'Tooley")
    opercentage = round((ocount / len(votes))*100, 2)
    print (f"Khan: {kcount} with {kpercentage}%")
    print (f"Correy: {ccount} with {cpercentage}%")
    print (f"Li: {lcount} with {lpercentage}%")
    print (f"O'Tooley: {ocount} with {opercentage}%")
    print("----------------------------")
    
    print(f"Winner: {max(set(candidates), key=candidates.count)}")
    
    #output file
    file = open("output.txt","w")

    file.write("Election Results" + "\n")

    file.write("----------------------------" + "\n")

    file.write(f"Total Votes: {len(votes)} \n")

    file.write(f"Khan: {kcount} with {kpercentage}% \n")

    file.write(f"Correy: {ccount} with {cpercentage}% \n")

    file.write(f"Li: {lcount} with {lpercentage}% \n")

    file.write(f"O'Tooley: {ocount} with {opercentage}% \n")
    
    file.write(f"Winner: {max(set(candidates), key=candidates.count)} \n")

    file.close()
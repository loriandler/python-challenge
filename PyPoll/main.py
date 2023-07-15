import os
import csv

#Set up the file path
csvpath = os.path.join('Resources','election_data.csv')

def analyze_poll_data(csvpath):

    #Initialize variables
    total_votes = 0
    candidates = {}
    winner = ""
    max_votes = 0

#Read the CSV file
with open(csvpath, 'r') as file:
    reader = csv.reader(file)
    
    #skip header row
    next(reader)

    total_votes = 0
    candidates = {}

    #Loop through data
    for row in reader:

        #count the total votes
        total_votes +=1
        candidate = row[2]
        
        #update candidate vote count
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

#Determine the winner

    winner = ""
    max_votes = 0

for candidate, votes in candidates.items():
    if votes > max_votes:
        max_votes = votes
        winner = candidate
        
#calculate the percentage of votes
percentages = {
    candidate: (votes / total_votes) * 100
    for candidate, votes in candidates.items()
}

# Print the analysis results
print("Election Results")
print("---------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------")

for candidate, votes in candidates.items():
    percentage = percentages[candidate]
    print(f"{candidate}: {percentage:.3f}% ({votes})")

print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

#Export results to a text file
output_file = "analysis/election_results.txt"
with open(output_file, 'w') as file:
    file.write("Election Results\n")
    file.write("_______________________\n")
    file.write(f"total Votes: {total_votes}\n")
    file.write("_______________________\n")
    
    for candidate, votes in candidates.items():
        percentage = percentages[candidate]
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    
    file.write("_______________________\n")
    file.write(f"Winner: {winner}\n")
    file.write("_______________________\n")

print(f"Analysis results have been exported to {output_file}")

#usage example
poll_data_file = 'election_data.csv'
analyze_poll_data(poll_data_file)

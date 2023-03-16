# Import built-in operating system and csv.
import os
import csv
# Create a path for our file.
csvpath = os.path.join('PyPoll/Resources/election_data.csv')
#set the output of the text file.
text_path = "Election_Analysis.txt"
#combine the filename with a folder named 'analysis'.
outfile = os.path.join('analysis', text_path)
#Open the csv and set file object.
with open(csvpath, newline="") as election_file:
    # Create a csv reader 
    csvreader = csv.reader(election_file, delimiter=',')
      # Reading header row
    csv_header = next(csvreader)
    ##Set variables.
    total_votes = 0
    charles_votes = 0
    diana_votes = 0
    raymon_votes = 0
    # Loop through each row in the csv
    for row in csvreader: 
        # Count the number of votes.
        total_votes +=1
        # We have thre candidates if the name is found, count the times it appears and store in a list. We can use this values in our percent vote calculation in the print statements
        if row[2] == "Charles Casper Stockham":
           charles_votes += 1
        elif row[2] == "Diana DeGette":
            diana_votes += 1
        elif row[2] == "Raymon Anthony Doane":
            raymon_votes += 1
        
 # To find the winner we want to make a dictionary out of the two lists we previously created 
list_candidates = ["Charles Casper Stockham", "Raymon Anthony Doane", "Diana DeGette"]
list_votes = [charles_votes, raymon_votes, diana_votes]
# We zip them together the list of candidate  and the total votes.
candidates_and_votes_dict = dict(zip(list_candidates, list_votes))
dict_candidates_and_votes = dict(zip(list_candidates,list_votes))
#Find the winner with max function.
winner = max(candidates_and_votes_dict, key=candidates_and_votes_dict.get)

# Find percent.
percent_charles_votes = (charles_votes / total_votes) * 100
percent_diana_votes = (diana_votes / total_votes) * 100
percent_raymon_votes = (raymon_votes / total_votes) * 100

#print the result.
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")
print(f"Charles Casper Stockham: {percent_charles_votes:.3f}% ({charles_votes})")
print(f"Diana DeGette: {percent_diana_votes:.3f}% ({diana_votes})")
print(f"Raymon Anthony Doane: {percent_raymon_votes:.3f}% ({raymon_votes})")
print("--------------------------")
print(f"Winner: {winner}")
print("--------------------------")

#Create and write the results to new file "Election Results.txt".
with open(text_path, 'w') as file:
    file.write("Election Results\n")
    file.write("--------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("--------------------------\n")
    file.write(f"Charles Casper Stockham: {percent_charles_votes:.3f}% ({charles_votes})\n")
    file.write(f"Diana DeGette: {percent_diana_votes:.3f}% ({diana_votes})\n")
    file.write(f"Raymon Anthony Doane: {percent_raymon_votes:.3f}% ({raymon_votes})\n")
    file.write("--------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("--------------------------\n")
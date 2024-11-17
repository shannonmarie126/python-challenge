# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv 
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidate_votes={}
candidate_list=[]

# Winning Candidate and Winning Count Tracker
winning_candidate=""
winning_count=0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name=row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidate_list:  
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name]=0 #starts the count at 0 for the new candidate
            

        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1
        

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print(f"Total Votes: {total_votes}")

    # Write the total vote count to the text file
    output_header=(
        "Election Results\n"
        "-------------------------\n"
        f"Total Votes: {total_votes}\n"
        "-------------------------\n"
    )
    txt_file.write(output_header)

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candidate_votes:
    
        # Get the vote count and calculate the percentage
        vote_count=candidate_votes[candidate]
        vote_percent=(vote_count)/(total_votes)*100
        vote_percent_rounded=round(vote_percent,3)
        # Update the winning candidate if this one has more votes
        #use if loop to loop though the candidates vote counts to find the winner 
        if vote_count>winning_count:
            winning_count=vote_count
            winning_candidate=candidate
        


        # Print and save each candidate's vote count and percentage
        #\n to move to a new line after ever iteration of the dictionary 
        candidate_result=f"{candidate}: {vote_percent_rounded}% ({vote_count})\n"
        print(candidate_result, end="")
        txt_file.write(candidate_result)

    # Generate and print the winning candidate summary
    winner_summary=(
        "-------------------------\n"
        f"Winner: {winning_candidate}\n"
        "-------------------------\n"
    )

    # Save the winning candidate summary to the text file
    print(f"Winner: {winning_candidate}")
    txt_file.write(winner_summary)
   
import os
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
#    print(f"csv Header: {csv_header}")

#   Set variables with empty list
    khan_votes = []
    correy_votes = []
    li_votes = []
    tooley_votes = []
    other_votes = []

#   Loop through each row assigning each to their respective list
    for row in csvreader:
        if row[2] == "Khan":
            khan_votes.append(row[0])
        elif row[2] == "Correy":
            correy_votes.append(row[0])
        elif row[2] == "Li":
            li_votes.append(row[0])
        elif row[2] == "O'Tooley":
            tooley_votes.append(row[0])
        else:
            other_votes.append(row[0])

    # set variables
    ttl_khan_votes = len(khan_votes)
    ttl_correy_votes = len(correy_votes)
    ttl_li_votes = len(li_votes)
    ttl_tooley_votes = len(tooley_votes)
    ttl_other_votes = len(other_votes)
    # Sum total votes
    ttl_votes = (ttl_khan_votes + ttl_correy_votes + ttl_li_votes + ttl_tooley_votes + ttl_other_votes)
    # Calc pecentage of votes cast
    pct_khan_votes = round(100*(ttl_khan_votes / ttl_votes),2)
    pct_correy_votes = round(100*(ttl_correy_votes / ttl_votes),2)
    pct_li_votes = round(100*(ttl_li_votes / ttl_votes),2)
    pct_tooley_votes = round(100*(ttl_tooley_votes / ttl_votes),2)
    pct_other_votes = round(100*(ttl_other_votes / ttl_votes),2)

    #  Determine winner
    winner = {
        'KHAN': ttl_khan_votes,
        'COOREY': ttl_correy_votes,
        'LI': ttl_li_votes,
        'TOOLEY': ttl_tooley_votes
        }
    elected = max(winner, key=winner.get)

    # print results
    print(" ")
    print("***** ELECTION RESULTS *************")
    print(" ")
    print("Total Votes Cast: " + str(ttl_votes))
    print(" ")
    print("***** BREAKDOWN BY CANDIDATE *******")
    print(" ")
    print("Khan: " + str(ttl_khan_votes) + " | " + str(pct_khan_votes) +"%")
    print("Correy: " + str(ttl_correy_votes) + " | " + str(pct_correy_votes) +"%")
    print("Li: " + str(ttl_li_votes) + " | " + str(pct_li_votes) +"%")
    print("O'Tooley: " + str(ttl_tooley_votes) + " | " + str(pct_tooley_votes) +"%")
    print("Other: " + str(ttl_other_votes) + " | " + str(pct_other_votes) +"%")
    print(" ")
    print("***** WINNER ***********************")
    print(" ")
    print(elected)
    print(" ")
    print("************************************")
#

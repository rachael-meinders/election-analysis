import csv
import os

# create var to load file from path
file_to_load = 'Resources/election_results.csv'
# create var to save file to path
file_to_save = os.path.join('analysis', 'election_analysis.txt')

# open the election results + read file
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    # read and print the header row
    headers = next(file_reader)
    print(headers)


# open w/ write mode
with open(file_to_save,'w') as txt_file:

    # write three counties to file
    txt_file.write('Counties in the Election\n________________________\nArapahoe\nDenver\nJefferson') 

# 1. total # of votes cast
# 2. complete list of candidates who received votes
# 3. % of votes each candidate won
# 4. total # of votes each candidate won
# 5. winner of election from popular vote
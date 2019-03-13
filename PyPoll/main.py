import os
import csv

# Path to collect data from the Resources folder
PollCSV = os.path.join('.', 'Resources', 'election_data.csv')

# Read in the CSV file
with open(PollCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    #Create empty list
    candidate = []

    Poll_data = list(csvreader)
    Votes = len(Poll_data)


    for i in range(Votes):
        if Poll_data[i][2] not in candidate:
            candidate.append(Poll_data[i][2])
 
   
    vote_count = []
  
    for person in candidate:
        vote_count.append(0)

    num_candidate = len(candidate)
 
    for i in range(Votes):
        for j in range(num_candidate):
            if Poll_data[i][2] == candidate[j]:
                vote_count[j] = vote_count[j] + 1

   

    percentage = []

    for candidate_vote in vote_count:
        percentage.append(candidate_vote/Votes)

    max_votes = max(vote_count)
    
    winner = candidate[vote_count.index(max_votes)]

    # '{percentage:.2%}'.format(percentage)
    f_percent =[]
    f_percent = ["{:.3%}".format(percentage[0]),"{:.3%}".format(percentage[1]), "{:.3%}".format(percentage[2]), "{:.3%}".format(percentage[3])]

    #print calculated values
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {Votes}")
    print("-------------------------")
    print(candidate[0] +": "+ str(f_percent[0]) +" ("+ str(vote_count[0]) + ")")
    print(candidate[1] + ": "+ str(f_percent[1]) +" ("+ str(vote_count[1]) + ")")
    print(candidate[2] + ": "+ str(f_percent[2]) +" (" + str(vote_count[2]) + ")")
    print(candidate[3] + ": "+ str(f_percent[3]) +" (" + str(vote_count[3]) + ")")
    print("-------------------------")  
    print(f"Winner:  {winner}")
    print("-------------------------")

#create text file and write results to it.
# Set variable for output file
output_file = os.path.join("Election_Results.txt")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    datafile.write("Election Results\n")
    datafile.write("-------------------------\n")
    datafile.write(f"Total Votes: {Votes}\n")
    datafile.write("-------------------------\n")
    datafile.write(candidate[0] + ": " + str(f_percent[0]) + " (" + str(vote_count[0]) + ")\n")
    datafile.write(candidate[1] + ": " + str(f_percent[1]) + " (" + str(vote_count[1]) + ")\n")
    datafile.write(candidate[2] + ": " + str(f_percent[2]) + " (" + str(vote_count[2]) + ")\n")
    datafile.write(candidate[3] + ": " + str(f_percent[3]) + " (" + str(vote_count[3]) + ")\n")
    datafile.write("-------------------------\n")
    datafile.write(f"Winner:  {winner}\n")
    datafile.write("-------------------------\n")

    datafile.close()








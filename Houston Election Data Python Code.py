# Import CSV File:
import os
import csv

# Declare Initiatl Variable:
ElectionData_Dictionary = {}

# Open, Read, and Create Dictionary from CSV File

csv_path_input = os.path.join('C:/Users/kodar/Desktop/Homework Files (WIP)', 'houston_election_data.csv')

with open(csv_path_input, encoding="utf8", newline='') as input_file:

    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.DictReader(input_file, delimiter=',')
   
    # Read each row of data after the header and Count the number of Votes Casted
    for row in csv_reader:
               
        # Assign a value of 1 if Candidate is not already in ElectionData_Dictionary
        if row['Candidate'] not in ElectionData_Dictionary:
            ElectionData_Dictionary[row['Candidate']] = 1
        # Otherwise, incrementally add a value of 1 to Candidates in ElectionData_Dictionary 
        else:
            ElectionData_Dictionary[row['Candidate']] += 1

# Print Summary Title to the Terminal
print()
print()
print("Houston Mayoral Election Results")
print("------------------------------------------")

# Sum Total Votes and Print to the Terminal
Total_Votes = sum(ElectionData_Dictionary.values())
print(f"Total Cast Votes: {Total_Votes}")
print("------------------------------------------")

# Sort Data by Descending Value and Print Election Results to the Terminal
Sorted_ElectionData_Dictionary = sorted(ElectionData_Dictionary.items(), key=lambda t:t[1], reverse=True)

for Key, Value in Sorted_ElectionData_Dictionary:
    print(f"{Key}: {Value / Total_Votes:.2%} ({Value})")

# Create Candidate List from Sorted Dictionary and Print First Two Advancing Candidates to the Terminal
Sorted_Candidate_List = []
Sorted_Candidate_List = [i[0] for i in Sorted_ElectionData_Dictionary]

print("------------------------------------------")
print("1st Advancing Candidate: " + str(Sorted_Candidate_List[0]))
print("2nd Advancing Candidate: " + str(Sorted_Candidate_List[1]))
print("------------------------------------------")

# Create, Open, and Write Text File
csv_path_output = os.path.join('C:/Users/kodar/Desktop/Homework Files (WIP)', 'houston_election_data_analysis.txt')

with open(csv_path_output, "w") as output_file:
    output_file.write("\n")
    output_file.write("\n")
    output_file.write("Houston Mayoral Election Results")
    output_file.write("\n")
    output_file.write(f"Total Cast Votes: {Total_Votes}")
    output_file.write("\n")
    output_file.write(f"--------------------------------------------------\n")
    for Key, Value in Sorted_ElectionData_Dictionary:
        output_file.write(f"{Key}: {Value / Total_Votes:.2%} ({Value})\n")
    output_file.write("\n")
    output_file.write("--------------------------------------------------")
    output_file.write("\n")
    output_file.write("1st Advancing Candidate: " + str(Sorted_Candidate_List[0]))
    output_file.write("\n")
    output_file.write("2nd Advancing Candidate: " + str(Sorted_Candidate_List[1]))
    output_file.write("\n")
    output_file.write("--------------------------------------------------")
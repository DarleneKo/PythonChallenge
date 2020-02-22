# Import CSV File and Statistics Library:
import os
import csv
from statistics import mean

# Declare Initial Variables:
Total_Months = 0
Total_NetProfit = []
Date = []
Monthly_ProfitChange = []


# Open, Read, and Create Dictionary from CSV File

csv_path_input = os.path.join('Resources', 'budget_data.csv')

with open(csv_path_input, encoding="utf8", newline='') as input_file:

    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.DictReader(input_file, delimiter=',')
   
    # Read each row of data after the header, Count the number of Months, Sum Total Net Profit, and Adds the Date onto the end of a List
    for row in csv_reader:

        Total_Months = Total_Months + 1    
        Total_NetProfit.append(int(row["Profit/Losses"]))
        Date.append(row["Date"])

    # Calculate difference (e.g. Change in Profit) between adjacent elements in given list using Naive Approach
    for i in range(len(Total_NetProfit)):
        if i !=0:
            Monthly_ProfitChange.append(int(Total_NetProfit[i]) - int(Total_NetProfit[i-1]))

# Calculate the Average Monthly Profit Change, Maximum Monthly Profit Change and Minimum Profit Change
Average_ProfitChange = mean(Monthly_ProfitChange)
Greatest_Increase = max(Monthly_ProfitChange)
Greatest_Decrease = min(Monthly_ProfitChange)

# Determine the date associated with the Greatest Increase and Greatest Decrease in Profit
Date_GreatestIncrease = Date[Monthly_ProfitChange.index(Greatest_Increase) + 1]
Date_GreatestDecrease = Date[Monthly_ProfitChange.index(Greatest_Decrease) + 1]

# Print to Terminal
print()
print()
print("Financial Analysis")
print("--------------------------------------------------")
print(f"Total Months: {Total_Months}")
print(f"Total: ${sum(Total_NetProfit)}")
print("Average Change: $""{:.2f}".format(Average_ProfitChange))
print("Greatest Increase in Profits: " + str(Date_GreatestIncrease) + " ($""{:.0f}".format(Greatest_Increase) + ")")
print("Greatest Decrease in Profits: " + str(Date_GreatestDecrease) + " ($""{:.0f}".format(Greatest_Decrease) + ")")
print()
print()

# Create, Open, and Write Text File
csv_path_output = os.path.join('Output', 'budget_data_analysis.txt')

with open(csv_path_output, "w") as output_file:
    output_file.write("\n")
    output_file.write("\n")
    output_file.write("Financial Analysis")
    output_file.write("\n")
    output_file.write("--------------------------------------------------")
    output_file.write("\n")
    output_file.write(f"Total Months: {Total_Months}")
    output_file.write("\n")
    output_file.write(f"Total: ${sum(Total_NetProfit)}")
    output_file.write("\n")
    output_file.write("Average Change: $""{:.2f}".format(Average_ProfitChange))
    output_file.write("\n")
    output_file.write("Greatest Increase in Profits: " + str(Date_GreatestIncrease) + " ($""{:.0f}".format(Greatest_Increase) + ")")
    output_file.write("\n")
    output_file.write("Greatest Decrease in Profits: " + str(Date_GreatestDecrease) + " ($""{:.0f}".format(Greatest_Decrease) + ")")
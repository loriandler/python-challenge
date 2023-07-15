import os
import csv

# Set up the file path
csvpath = os.path.join('Resources', 'budget_data.csv')

# Initialize variables
total_months = 0
net_total = 0
prev_profit = None
profit_losses = []
profit_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Read the CSV file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    next(csvreader)

    # Loop through the rows in the dataset
    for row in csvreader:
        # Count the total number of months
        total_months += 1

        # Calculate the net total amount of Profit/Losses
        net_total += int(row[1])

        # Append the profit/losses value to the list
        profit_losses.append(int(row[1]))

        # Calculate the change in profit/loss since the previous month
        if prev_profit is not None:
            change = int(row[1]) - prev_profit
            profit_changes.append(change)

            # Find the greatest increase and decrease in profits
            if change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = change
            if change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = change

        prev_profit = int(row[1])

# Calculate the average change in profits
average_change = sum(profit_changes) / len(profit_changes)

# Print the analysis results
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")


#Export results to a text file
output_file = "analysis/financial_results.txt"
with open (output_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_total}\n")
    file.write(f"Average Change: ${round(average_change, 2)}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(f"Analysis results have been exported to {output_file}")




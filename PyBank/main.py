# Import built-in operating system and csv.
import os
import csv
# create a path for our file.
csvpath = os.path.join('PyBank/Resources/budget_data.csv')
#set the output of the text file
text_path = "Financial_Analysis.txt"
#combine the filename with a folder named 'analysis'
outfile = os.path.join('analysis', text_path)
#Open the csv and set file object.
with open(csvpath, newline="") as budget_file:
    # Create a csv reader 
    csvreader = csv.reader(budget_file, delimiter=',')   
    # Reading header row
    csv_header = next(csvreader)
    #Set variables
    months=0
    profit=[]
    total_profit=[]
    monthly_profit_change=[]
    months_name=[]
    #Loop through each row .
    for row in csvreader:
      #Count the number of months.
      months +=1
      #Append the profit value to a list 
      total_profit.append(int(row[1]))
      #Append the month name to a list.
      months_name.append(row[0])
       # Take the difference between two months and append to monthly profit change
    for x in range(len(total_profit)-1):
     monthly_profit_change.append(total_profit[x+1]-total_profit[x])
     # calculate the max and min of the the montly profit change list.
    max_increase_value = max(monthly_profit_change)
    max_decrease_value = min(monthly_profit_change)
    

# Correlate max and min to the proper month using month list and index from max and min. We use +1 at the end since month associated with change is the  next month
max_increase_months = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_months = monthly_profit_change.index(min(monthly_profit_change)) + 1 
#print the result.
print (f"Total Months : {(months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change:$ {round(sum(monthly_profit_change)/85,2)}")
print(f"Greatest Increase in Profits: {months_name[max_increase_months]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {months_name[max_decrease_months] } (${(str(max_decrease_value))})")

#Create and write the results to new file "Financial_Analysis.txt".
with open(text_path, 'w') as file:
        file.write("Financial Analysis\n")
        file.write("---------------------\n")
        file.write("Total Months: %d\n" % (months))
        file.write("Total : $%d\n" % (sum(total_profit)))
        file.write("Average Change : $%d\n" % ((round(sum(monthly_profit_change)/85,2))))
        file.write(f"Greatest Increase in Profits: {months_name[max_increase_months]} (${(str(max_increase_value))})")
        file.write(f"Greatest Decrease in Profits: {months_name[max_decrease_months] } (${(str(max_decrease_value))})")


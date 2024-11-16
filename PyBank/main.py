import csv
import os

#define file paths
file_to_load = os.path.join("Resources","budget_data.csv")
file_to_output = os.path.join("analysis", "budget_analysis.txt")

#initalize variables
total_months = 0
total_net = 0
changes=[]
max_profit_loss=float('inf')
max_profit_gain=float('-inf')

#open and read the data from the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    header = next(reader)

    #read and set first row values for initial calculations 
    first_row=next(reader)
    previous_profit_loss=float(first_row[1])
    total_months+=1
    total_net+= previous_profit_loss
  
    #use a for loop to loop thoruhg the rows and count the total months
    for row in reader:
        total_months+=1
        month_prof_loss=float(row[1])   #profit loss/gain for the current month
        total_net += month_prof_loss    #updates total profit loss/gain
        change=month_prof_loss-previous_profit_loss #calculates change from previous month
        changes.append(change)      #add to the change list 
        
        #run an if loop within the for loop to calculae max and min 
        # using -inf for max and inf for min starting values
        if change>max_profit_gain:
            max_profit_gain=change  #update max gain
            max_profit_month=row[0]     #stores the value
        elif change<max_profit_loss:
            max_profit_loss=change
            max_loss_month=row[0]
        previous_profit_loss=month_prof_loss    #resets for the next iteration
        previous_month=row[0]

#calculate totals and averages and round results        
total_net_rounded=int(total_net)
total_change=sum(changes)
average_change=total_change/len(changes)
average_change_rounded=round(average_change,2)
max_profit_loss_rounded=int(max_profit_loss)
max_profit_gain_rounded=int(max_profit_gain)

#output results
print("Total Months: " + str(total_months))
print("Total: $" + str(total_net_rounded))
print("Average Change: $"+ str(average_change_rounded))
print("Greatest Increase in Profits: "+max_profit_month+ " ($" + str(max_profit_gain_rounded)+")")
print("Greatest Decrease in Profits: "+max_loss_month+ " ($" + str(max_profit_loss_rounded)+")")

#write results to text file as a string
output  = "\n".join((
    f"Financial Analysis",
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net_rounded}\n"
    f"Average Change: ${average_change_rounded}\n"
    f"Greatest Increase in Profits: {max_profit_month} (${max_profit_gain_rounded})\n"
    f"Greatest Decrease in Profits: {max_loss_month} (${max_profit_loss_rounded})\n"
    ))

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
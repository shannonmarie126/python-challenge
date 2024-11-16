import csv
import os

file_to_load = os.path.join("Resources","budget_data.csv")
file_to_output = os.path.join("analysis", "budget_analysis.txt")

total_months = 0
total_net = 0
changes=[]
max_profit_loss=float('inf')
max_profit_gain=float('-inf')

with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    header = next(reader)

    first_row=next(reader)
    previous_profit_loss=float(first_row[1])
    total_months+=1
    total_net+= previous_profit_loss
  
    for row in reader:
        total_months+=1
        month_prof_loss=float(row[1])
        total_net += month_prof_loss
        change=month_prof_loss-previous_profit_loss
        changes.append(change)
        
        if change>max_profit_gain:
            max_profit_gain=change
            max_profit_month=row[0]
        elif change<max_profit_loss:
            max_profit_loss=change
            max_loss_month=row[0]
        previous_profit_loss=month_prof_loss
        previous_month=row[0]
        
total_net_rounded=int(total_net)
total_change=sum(changes)
average_change=total_change/len(changes)
average_change_rounded=round(average_change,2)
max_profit_loss_rounded=int(max_profit_loss)
max_profit_gain_rounded=int(max_profit_gain)

print(total_net_rounded)
print(total_months)
print(average_change_rounded)
print(max_profit_loss_rounded)
print(max_profit_gain_rounded)
print(max_profit_month)
print(max_loss_month)

output  = "\n".join((
    f"Financial Analysis",
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net_rounded}\n"
    f"Average Change: ${average_change_rounded}\n"
    f"Greatest Increase in Profits: {max_profit_month} (${max_profit_gain_rounded})\n"
    f"Greatest Decrease in Profits: {max_profit_month} (${max_profit_loss_rounded})\n"
    ))

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
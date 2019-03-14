import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# Reads in csv file using python reader function

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"csv Header: {csv_header}")
#   Set variables with empty list
    monthdate = []
    profitloss = []
#   Loop through each row assigning each to their respective list
    for row in csvreader:
        monthdate.append(row[0])
        profitloss.append(int(row[1]))

#   Sets list so that only unique values are returned
    u_monthdate=list(set(monthdate))
#   In our case there were no duplicates
    n_months = len(u_monthdate)
#   Sum the total profit
    total = sum(profitloss)
#   Calc the average
    avg = round((total/n_months),2)

#   Calculating the average percent change and largest/smallest monthly change
#    def main():
    #setup variables
    yearly_change = []
    change=0.0
    total_change=0
    average_change=0
    greatest_increase=0
    smallest_increase=0

    for i in range(1, len(profitloss)):
        change = profitloss[i] - profitloss[i-1]
        yearly_change.append(change)
        sum_yearly_change = sum(yearly_change)
        average_change = round((sum_yearly_change/(n_months-1)),2)

        #if this is the first year, set trackers to its value
        if i==1:
            greatest_increase = change
            smallest_increase = change
            greatest_year = 1
            smallest_year = 1
#        #this is not the first change in profit
#        #update the trackers if relevent
        else:
            if change>greatest_increase:
                greatest_increase = change
                greatest_year = i
            elif change<smallest_increase:
                smallest_increase = change
                smallest_year = i
#            total_change = (sum(yearly_change))
#            average_change = (total_change/(n_months-1))

#    print("Total Change: "+ str(sum_yearly_change))
    print("--------")
    print("--------")
    print("Total profit: " + str(total))
    print("--------")
    print("Total months: " + str(n_months))
    print("--------")
    print("Average monthly profit: "+ str(avg))
    print("--------")
    print("Average Monthly Change: "+ str(average_change))
    print("--------")
    print("Smallest Increase: " + str(smallest_increase))
    print("--------")
    print("Greatest_Increase: " + str(greatest_increase))
    print("--------")
    print("--------")
    print("*******************List Data****************")
    print("--------")
    print("--------")
    print("-----col1---")
    print(monthdate)
    print("-----col2---")
    print(profitloss)
    print("-----YrCng--")
    print(yearly_change)

#   send output to csv file
#   Specify the file to write to
    output_path = os.path.join("..", "output", "newbankpy.csv")

    # Open the file using "write" mode. Specify the variable to hold the contents
    with open(output_path,'w' , newline='') as csvfile:

        # Initialize csv.writer
        csvwriter = csv.writer(csvfile, delimiter=' ')

        # Write the rows to csv (column headers)

        csvwriter.writerow("Total profit: " + str(total))
        csvwriter.writerow("Total months: " + str(n_months))
        csvwriter.writerow("Average monthly profit: "+ str(avg))
        csvwriter.writerow("Average Monthly Change "+ str(average_change))
        csvwriter.writerow("Smallest Increase " + str(smallest_increase))
        csvwriter.writerow("Greatest_Increase " + str(greatest_increase))

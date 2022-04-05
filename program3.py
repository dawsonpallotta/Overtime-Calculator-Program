#
#Author: Dawson Pallotta
#Program: Program3
#
#Description:
#   This program is being used to figure out an amount due for hours working a four week given\
#        with invoice data, while also testing input for errors, and and introducing three main fuctions that read weekly hours,\
#               hourly rate, and employee name. While also introducing a main function to house the billing module.
#-------------------------------------------------------------------------------------------------------------------------------------------------

from BillingModule import *

def main():
    another = 'y'
    while another == 'y':

        employeeName = readEmployeeName('Employee Name: ')
        hourlyRate = readHourlyRate('Hourly Rate: ')
        week1 = readWeeklyHours('Enter hours worked for week 1: ')
        week2 = readWeeklyHours('Enter hours worked for week 2: ')
        week3 = readWeeklyHours('Enter hours worked for week 3: ')
        week4 = readWeeklyHours('Enter hours worked for week 4: ')
        
        
        total_Hours = 0.0
        average_Hours = 0.0
        REGULAR_HOURS = 160.0
        total_Hours = week1 + week2 + week3 + week4
        average_Hours = total_Hours/4
        overtime_Hours = total_Hours - REGULAR_HOURS
        overtime_Rate = float(round(hourlyRate * 1.05, 2))
        overtime_Amount= overtime_Hours * overtime_Rate
        regular_Amount = REGULAR_HOURS * hourlyRate
        invoice_Amount = total_Hours * hourlyRate
        overtime_Total = regular_Amount + overtime_Amount

        if total_Hours > REGULAR_HOURS:
            print('\n',employeeName, ' worked ', overtime_Hours, ' hours of overtime.', sep='')
            print('\nInvoice')
            print('Resource:', employeeName, '\tAverage weekly  hours:', format(average_Hours, '.2f'))
            print('Total billable hours:',\
              format(total_Hours, '.2f'),'\trate: $',\
              format(hourlyRate,'.2f'), sep='')
            print('Overtime Hours:', format(overtime_Hours, '.2f'), '@', '$'+ format(overtime_Rate, '.2f'), '=', '$'+ format(overtime_Amount, '.2f'))
            print('Regular Hours:', format(REGULAR_HOURS, '.2f'), '@', '$'+ format(hourlyRate, '.2f'), '=', '$'+ format(regular_Amount, ',.2f'))    
            print('Amount Due: $', format(overtime_Total, ',.2f'), sep='')
        else:
            print('\n', employeeName,' worked no overtime.', sep='')
            print('\nInvoice')
            print('Resource:', employeeName, '\tAverage weekly  hours:', format(average_Hours, '.2f'))
            print('Total billable hours:',\
              format(total_Hours, '.2f'),'\trate: $',\
              format(hourlyRate,'.2f'), sep='')
            print('Regular Hours:', format(REGULAR_HOURS, ',.2f'), '@', '$'+ format(hourlyRate, '.2f'), '=', '$'+ format(regular_Amount, ',.2f'))    
            print('Amount Due: $', format(invoice_Amount, ',.2f'), sep='')

        another = input('\nEnter another employee? ("y" = yes) :')
    print('\nProgram ended normally.')

main()



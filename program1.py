#
#Author: Dawson Pallotta
#Program: Program1
#
#Description:
#   This program is being used to figure out an amount due for hours working a four week given\
#        with invoice data.
#
regular_Hours = 160

total_Hours = float()

employee = input('Employee Name:')
rate = float(input('Hourly Rate:'))
             
week1 = float(input('Enter hours worked for week 1:'))
week2 = float(input('Enter hours worked for week 2:'))
week3 = float(input('Enter hours worked for week 3:'))
week4 = float(input('Enter hours worked for week 4:'))

total_Hours = week1 + week2 + week3 + week4
average_Hours = total_Hours / 4

overtime_Hours = total_Hours - regular_Hours
overtime_Rate = round(rate * 1.05, 2)
overtime_Amount= overtime_Hours * overtime_Rate
regular_Amount = regular_Hours * rate
invoice_Amount = total_Hours * rate

if total_Hours > regular_Hours:
    print('\n',employee, ' worked ', overtime_Hours, ' hours of overtime.', sep='')
    print('\nInvoice')
    print('Resource:', employee, '\tAverage weekly  hours:', format(average_Hours, '.2f'))
    print('Total billable hours:',\
      format(total_Hours, '.2f'),'\trate: $',\
      format(rate,'.2f'), sep='')
    print('Overtime Hours:', format(overtime_Hours, '.2f'), '@', '$'+ format(overtime_Rate, '.2f'), '=', '$'+ format(overtime_Amount, '.2f'))
    print('Regular Hours:', format(regular_Hours, '.2f'), '@', '$'+ format(rate, '.2f'), '=', '$'+ format(regular_Amount, '.2f'))    
    print('Amount Due: $', format(invoice_Amount, ',.2f'), sep='')
else:
    print('\n', employee,' worked no overtime.', sep='')
    print('\nInvoice')
    print('Resource:', employee, '\tAverage weekly  hours:', format(average_Hours, '.2f'))
    print('Total billable hours:',\
      format(total_Hours, '.2f'),'\trate: $',\
      format(rate,'.2f'), sep='')
    print('Regular Hours:', format(regular_Hours, '.2f'), '@', '$'+ format(rate, '.2f'), '=', '$'+ format(regular_Amount, '.2f'))    
    print('Amount Due: $', format(invoice_Amount, ',.2f'), sep='')

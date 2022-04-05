#
#Author: Dawson Pallotta
#Program: Program0
#
#Description:
#   This program is being used to figure out an amout due for hours working a four week given\
#        with invoice data.
#


totalHours = float()
averageHours = float()

employee = input('Employee Name:')
rate = float(input("Hourly Rate:"))

week1 = float(input('Enter hours worked for week 1:'))
week2 = float(input('Enter hours worked for week 2:'))
week3 = float(input('Enter hours worked for week 3:'))
week4 = float(input('Enter hours worked for week 4:'))

totalHours = week1 + week2 + week3 + week4
averageHours = totalHours/4

invoiceAmount = totalHours * rate

print('\nInvoice')
print('Resource:', employee, '\tAverage weekly  hours:', format(averageHours, '.2f'))
print('nTotal billable hours:',\
      format(totalHours, '.2f'),'\trate: $',\
      format(rate,'.2f'), sep='')
print('Amount Due : $', format(invoiceAmount, ',.2f'), sep='')

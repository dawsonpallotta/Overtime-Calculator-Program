#
#Author: Dawson Pallotta
#Program: Program4
#
#Description:
#   This program is being used to figure out an amount due for hours working a four week given\
#        with invoice data, while also testing input for errors, and and introducing three main fuctions that read weekly hours,\
#               hourly rate, and employee name. While also introducing a main function to house the billing module, while alos incorperating a\
#                   billing text record.
#-------------------------------------------------------------------------------------------------------------------------------------------------

from BillingModule import *

def main():
    another = 'y'
    resetFile('Billing.txt')
    while another == 'y':

        employeeName = readEmployeeName('Employee Name: ')
        hourlyRate = readHourlyRate('Hourly Rate: ')
        week1 = readWeeklyHours('Enter hours worked for week 1: ')
        week2 = readWeeklyHours('Enter hours worked for week 2: ')
        week3 = readWeeklyHours('Enter hours worked for week 3: ')
        week4 = readWeeklyHours('Enter hours worked for week 4: ')

        writeBillingRecord(employeeName, hourlyRate, week1, week2, week3, week4)
        
        
        totalHours = 0.0
        averageHours = 0.0
        REGULAR_HOURS = 160.0
        regularAmount = REGULAR_HOURS * hourlyRate
        totalHours = week1 + week2 + week3 + week4
        averageHours = totalHours/4
        overtimeAmount = 0.0
        if totalHours > REGULAR_HOURS:
            overtimeHours = totalHours - REGULAR_HOURS
            overtimeRate = round(hourlyRate * 1.05, 2)
            overtimeAmount = round(overtimeHours * overtimeRate, 2)
            output1 = 'worked' + str(overtimeHours) + 'hours of overtime.'
            output2 = '\nOvertime Hours: ' +\
                    str(format(overtimeHours, '.2f')) + '@' +\
                    '$'+format(overtimeRate, '.2f') +' =' +\
                    '$'+format(overtimeAmount, '.2f')
        else:
            output1 = 'worked no overtime'
            output2 = ''

        invoiceAmount = regularAmount + overtimeAmount

        print('\n'+str(employeeName),  output1)
        print('\nInvoice')
        print('Resource: ', employeeName, '\tAverage weekly hours: ',format(averageHours, '.2f'))
        print('\nTotal billable hours: ',\
          format(totalHours, ',.2f'), '\trate: $',\
          format(hourlyRate,  ',.2f'), sep='', end='')
        print(output2)
        print('Regular Hours:', \
                format(REGULAR_HOURS, ',.2f'), ' @ ',\
                '$'+format(hourlyRate, ',.2f'), ' = ',\
                '$'+format(regularAmount, ',.2f'))
        print('Amount Due: $',format(invoiceAmount, ',.2f'),sep='')
        another = input('\nEnter another employee? ("y" = yes) :')
    print('\nProgram ended normally.')





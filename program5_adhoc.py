from BillingModule import *
def main():

    infile = openForRead('Billing.txt')


    print('Employee\t'+
          'Rate\t'+
          'Week 1\t'+
          'Week 2\t'+
          'Week 3\t'+
          'Week 4\t'+
          'Hours\t'+
          'Total\t')

    name = readAsString(infile)

    while name !='':
        rate = readAsFloat(infle)
        week1 = readAsFloat(infle)
        week2 = readAsFloat(infle)
        week3 = readAsFloat(infle)
        week4 = readAsFloat(infle)
        hours = week1+week2+week3+week4


        print(name + '\t'+
              str(rate) + '\t'+
              str(week1) + '\t'+
              str(week2) + '\t'+
              str(week3) + '\t'+
              str(week4) + '\t'+ str(hours))

        name = readAsString(infile)
          

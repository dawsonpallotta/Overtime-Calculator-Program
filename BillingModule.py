def readEmployeeName(promt):
    employeeName = input(promt)
    while employeeName =='':
        print('Employee name must be entered.')
        employeeName = input('\n'+promt)    
    return employeeName    


def readHourlyRate(promt):
    error = True
    while error:
        try:    
            hourlyRate = float(input(promt))
            while hourlyRate =='' or hourlyRate <20:
                print('Invalid Hourly Rate, must be at least $20.00/hour.')
                hourlyRate = float(input('\n'+promt))
            if hourlyRate >= 20.0:
                error = False
        except ValueError:
            print("Invalid Hourly Rate, must be at least $20.00/hour.")
    return hourlyRate
            



def readWeeklyHours(promt):
    error = True
    while error:
        try:

            week = float(input(promt))
            while week =='' or week > 80 or week < 35:
                print('Invalid number of hours, must be between 35 and 80.')
                week = float(input('\n'+promt))

            if week <= 80 and week >= 35:
                error = False
        except ValueError:
            print(' Invalid number of hours, must be between 35 and 80. \n')
    return week

def resetFile(file):
    open(file,'w').close()

def writeBillingRecord(outemployeeName, outhourlyRate, outWeek1, outWeek2, outWeek3, outWeek4):
    outfile = open('Billing.txt','a')
    outfile.write(outemployeeName+'\n'+str(outhourlyRate)+\
            '\n'+str(outWeek1)+'\n'+str(outWeek2)+ \
            '\n'+str(outWeek3)+'\n'+str(outWeek4)+'\n')
    outfile.close()

def readAsString(file):
    return file.readline().rstrip('\n')

def readAsFloat(file):
    return float(readasFloat(file))

def openForRead(file):
    again = True
    while again:
        try:

            fileObj = open(file, 'r')
            again = False
        except FileNotFoundError:
            resetFile(file)
    return fileObj                    

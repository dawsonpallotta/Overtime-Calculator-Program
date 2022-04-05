import program4
import program5-adhoc

def main():
    loopControl = True
    while loopControl:
        try:
            print('\nBilling Sustem Menu:\n')
            print('\t0 - end')
            print('\t1 - Enter Billing Data')
            print('\t2 - Display ad-hoc Billing Report')

            option = int(input('\nOption ==> '))

            if option == 0:
                loopControl = False
            elif option == 1:
                program4.main()
            elif option == 2:
                program5-adhoc.main()
            else:
                print('Please enter an available option.')
        except ValueError:
            print('Please enter an available option.')

    print('Menu ended successfully')

main()

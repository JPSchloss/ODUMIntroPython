def main():
    keep_going = 'y'

    while keep_going == 'y':
        # Getting Sales and Commission Rates
        sales = float(input('Enter the number of sales: '))
        commission_rate = float(input('Enter the commission rate: '))

        # Calculating the commission
        commission = sales * commission_rate

        # Display the result
        print('The commission is $', format(commission, ',.2f'))

        # See if the user wants to continue
        keep_going = input('Do you want to calculate another commission? (y/n)')

main()
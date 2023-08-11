# Created On: March 20th, 2023
# Author: Zimuzo Akanne

import datetime

# read default values from file
with open('OSICDef.dat', 'r') as f:
    # Read the first line of the file and convert it to an integer
    POLICY_NUMBER = int(f.readline())
    BASIC_PREMIUM = float(f.readline())
    DISCOUNT = float(f.readline())
    LIABILITY_COST = float(f.readline())
    GLASS_COST = float(f.readline())
    LOANER_COST = float(f.readline())
    HST_RATE = float(f.readline())
    PROCESSING_FEE = float(f.readline())
    f.close()

# list of valid provinces
provinces = ['NL', 'PE', 'NS', 'NB', 'QC', 'ON', 'MB', 'SK', 'AB', 'BC', 'YT', 'NT', 'NU']

while True:
    # get customer information
    print('\nEnter customer information:')
    while True:
        first_name = input('First name: ').title()
        if first_name == "":
            print("First name cannot be blank")
        else:
            break

    last_name = input('Last name: ').title()
    address = input('Address: ')
    city = input('City: ').title()
    while True:
        province = input('Province: ').upper()
        if not province in provinces:
            print('Invalid province. Please enter a valid province')
        else:
            break

    postal_code = input('Postal code: ')
    phone_number = input('Phone number: ')

    # get car information
    num_cars = int(input('\nNumber of cars: '))
    while True:
        extra_cost = 0
        liability_option = input('Extra liability coverage (Y/N): ').upper()
        if liability_option == "":
            print("cannot be balnk")
        else:
            break


    glass_option = input('Glass coverage (Y/N): ').upper()
    loaner_option = input('Loaner car (Y/N): ').upper()
    payment_option = input('Payment method (F/M): ').upper()

    # calculate insurance premium

    for i in range(num_cars):
        if liability_option == 'Y':
            extra_cost += LIABILITY_COST
        if glass_option == 'Y':
            extra_cost += GLASS_COST
        if loaner_option == 'Y':
            extra_cost += LOANER_COST
    total_cost = BASIC_PREMIUM + (DISCOUNT * (num_cars - 1)) + extra_cost
    hst = HST_RATE * total_cost
    total_cost += hst

    # calculate monthly payment
    if payment_option == 'M':
        total_cost += PROCESSING_FEE
        monthly_payment = total_cost / 8
    else:
        monthly_payment = None

    currentDate = datetime.datetime.now()


    # display receipt
    print('\n\n********** The One Stop Insurance Company **********')
    print(f'Date:    {currentDate}')
    print(f'Policy Number: {POLICY_NUMBER}')
    print('Customer Information:')
    print('   Name:', first_name, last_name)
    print('   Address:', address)
    print('   City:', city)
    print('   Province:', province)
    print('   Postal Code:', postal_code)
    print('   Phone Number:', phone_number)
    print('Car Information:')
    print('   Number of cars:', num_cars)
    print('   Extra liability coverage:',             liability_option)
    print('   Glass coverage:',                      glass_option)
    print('   Loaner car:',                             loaner_option)
    print('Payment Information:')
    print('   Payment method:', payment_option)
    print('   Total cost:', '$%.2f' % total_cost)
    if monthly_payment is not None:
        print('   Monthly payment:', '$%.2f' % monthly_payment)
    print('\n\n')


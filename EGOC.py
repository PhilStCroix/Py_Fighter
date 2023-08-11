# python program for practice
# author: phil st croix
# written: March 25, 2023

# imports
# create a data file called EGOCDef.dat

# start of EGOC program
# read values from 'EGOCDef.dat'

# using a loop so that if file is not found user can make new 1 and enter the data
while True:
    try:
        with open('EGOCDef.dat', 'r') as f:
            growOpNum = int(f.readline().strip())
            growOpCost = float(f.readline().strip())
            discount = float(f.readline().strip())
            replaceCrop = float(f.readline().strip())
            kitCoverage = float(f.readline().strip())
            loanLight = float(f.readline().strip())
            hstRate = float(f.readline().strip())
            processFee = float(f.readline().strip())
    except:
        print("'EGOCDef.dat' not found. Exiting program!")
        exit()
    else:
        break

# loop for continuation
while True:
    # get first name
    while True:
        firstName = input("Enter first name: ").title()
        if firstName == "":
            print("First name cannot be blank - try again")
        else:
            break

    # get last name
    while True:
        lastName = input("Enter last name: ").title()
        if lastName == "":
            print("Last name cannot be blank - try again")
        else:
            break

    # get address
    while True:
        streetAdd = input("Enter street address: ").title()
        if streetAdd == "":
            print("Street address cannot be blank - try again")
        else:
            break

    # get city
    while True:
        city = input("Enter city: ").title()
        if city == "":
            print("City cannot be blank - try again")
        else:
            break

    # get validated province
    provinces = ["AB", "BC", "MB", "NB", "NL", "NT", "NS", "NU", "ON", "PE", "QE", "SK", "YT"]
    while True:
        province = input("Enter province (XX): ").upper()
        if province == "":
            print("Province cannot be blank - try again")
        elif province not in provinces:
            print("Province is invalid - try again")
        else:
            break

    # get postal code
    while True:
        postalCode = input("Enter postal code(X9X 9X9): ").upper()
        postalCode = postalCode.replace(" ", "").replace("-", "")
        if postalCode == "":
            print("Postal code cannot be blank - try again")
        elif not (len(postalCode) == 6 and postalCode[0].isalpha() and postalCode[1].isdigit() and postalCode[2].isalpha() and postalCode[3].isdigit() and postalCode[4].isalpha() and postalCode[5].isdigit()):
            print("postal code is invalid - try again (X9X 9X9)")
        else:
            break

    # get phone number
    while True:
        phoneNum = input("Enter phone number(9999999999): ")
        if phoneNum == "":
            print("Phone number cannot be blank - try again")
        elif len(phoneNum) != 10:
            print("Please enter a 10 digit phone number only")
        else:
            break

    # get number of grow ops
    while True:
        try:
            numGrowOps = int(input("Enter the number of grow ops: "))
        except:
            print("Number of grow ops is invalid - try again")
        else:
            if numGrowOps == 0:
                print("Number of grow ops cannot be zero - try again")
            elif numGrowOps < 0:
                print("Number of grow ops cannot be negative - try again")
            else:
                break

    # get replacement crop coverage
    while True:
        replaceCropFee = 0
        replaceCropCoverage = input("Crop replacement Coverage? (Y) or (N)o: ").upper()
        if replaceCropCoverage == "":
            print("Crop Replacement cannot be blank - try again")
        elif replaceCropCoverage != "Y" and replaceCropCoverage != "N":
            print("Choice can only be (Y)es or (N)o - try again")
        else:
            if replaceCropCoverage == "Y":
                replaceCropFee += replaceCrop
                break
            else:
                break

    # get optional kit coverage
    while True:
        kitCoverageFee = 0
        kitCoverageOpt = input("Accept kit coverage (Y)es or (N)o: ").upper()
        if kitCoverageOpt == "":
            print("Kit coverage cannot be blank - try again")
        elif kitCoverageOpt != "Y" and kitCoverageOpt != "N":
            print("Kit coverage option can only be (Y)es or (N)o - try gain")
        else:
            if kitCoverageOpt == "Y":
                kitCoverageFee += kitCoverage
                break
            else:
                break

    # get optional loaner lights
    while True:
        loanLightFee = 0
        loanLightCover = input("Accept Loan Light insurance (Y)es or (N)o: ").upper()
        if loanLightCover == "":
            print("Loan light cannot be blank - try again")
        else:
            if loanLightCover == "Y":
                loanLightFee += loanLight
                break
            else:
                break

    # get payments
    while True:
        paymentType = input("Enter payment type (F)ull or (M)onthly: ").upper()
        if paymentType == "":
            print("Payments cannot be blank - try again")
        elif paymentType != "M" and paymentType != "F":
            print("Choice can only be (F)ull or (M)onthly")
        else:
            if paymentType == "F":
                payments = 1
                break
            else:
                payments = 8
                break

    # calculations
    # save all input values to "GrowOps.dat"
    # Display the message “Grow op information processed and saved.” And increase the next policy number by 1.

    cont = input("Process another policy?  (Y)es or (N)o: ")
    if cont != "Y":
        # they want to leave program so save all data
        with open('EGOCDef.dat', 'w') as f:
            f.write("{}\n".format(growOpNum))
            f.write("{}\n".format(growOpCost))
            f.write("{}\n".format(discount))
            f.write("{}\n".format(replaceCrop))
            f.write("{}\n".format(kitCoverage))
            f.write("{}\n".format(loanLight))
            f.write("{}\n".format(hstRate))
            f.write("{}\n".format(processFee))
            exit()
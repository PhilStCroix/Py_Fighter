# ONE STOP INSURANCE COMPANY customer policy system
# FILE READ WRITE APPEND
# Author: Phil St Croix
# Written: Mar 18, 2023

import datetime
import time
import FormatValues as FV

def main():
    # Load default values from "OSICDef.dat"
    while True:
        try:
            with open("OSICDef.dat", "r") as f:
                policyNum = int(f.readline().strip())
                basicPrem = float(f.readline().strip())
                discount = float(f.readline().strip())
                xtraLiabCost = float(f.readline().strip())
                glassCovCost = float(f.readline().strip())
                loanCarCovCost = float(f.readline().strip())
                hstRate = float(f.readline().strip())
                processFee = float(f.readline().strip())
        except:
            print("'OSICDef.dat' not found.  Exiting program")
            exit()
        else:
            print()
            print("Loading default values from 'OSICDef.dat'", end="", flush=True)
            for i in range(6):
                print(".", end="", flush=True)
                time.sleep(0.5)
            print("\nDefault file loaded OK!")
            break

    # Main loop for continuation
    while True:
        # Get user inputs
        # Loop for first name to be entered
        while True:
            firstName = input("Enter customer's first name:                    ").title()
            if firstName == "":
                print("Customer first name cannot be blank - try again")
            else:
                break

        # Loop for last name to be entered
        while True:
            lastName = input("Enter customer's last name:                     ").title()
            if lastName == "":
                print("Customer last name cannot be blank - try again")
            else:
                break

        # Loop for street address to be entered
        while True:
            streetAdd = input("Enter customer's street address:                ")
            if streetAdd == "":
                print("Customer street address cannot be blank - try again")
            else:
                break

        # loop for city to be entered
        while True:
            city = input("Enter customer's city:                          ").title()
            if city == "":
                print("Customer city cannot be blank - try again")
            else:
                break

        # Loop for province to be entered and validated
        provList = ["AB", "BC", "MB", "NB", "NL", "NT", "NS", "NU", "ON", "PE", "QE", "SK", "YT"]
        while True:
            province = input("Enter customer's province (XX):                 ").upper()
            if province == "":
                print("Customer province cannot be blank - try again")
            elif not province in provList:
                print("Customer province is invalid - try again")
            else:
                break

        # Loop for postal code to be entered
        while True:
            postCode = input("Enter customers postal code(A1A 1A1):           ").upper()
            if postCode == "":
                print("Customer postal code cannot be blank - try again")
            else:
                break

        # loop for phone number to be entered
        while True:
            phoneNum = input("Enter customer's phone number(9999999999):      ")
            if phoneNum == "":
                print("Customer phone number cannot be black - try again")
            elif len(phoneNum) != 10:
                print("Phone numbers are 10 digits long - try again")
            else:
                break

        # loop for nuber of cars being insured
        while True:
            try:
                carNums = int(input("Enter the number of cars to be insured:         "))
            except:
                print("Number of cars is invalid - try again")
            else:
                if carNums == 0:
                    print("You can not insure 0 cars - try again")
                else:
                    break

        # Loop for extra liability
        while True:
            extraLiabFee = 0
            extraLiab = input("Extra liability up to $1,000,000 (Y)es or (N)o: ").upper()
            if extraLiab == "":
                print("Extra liability cannot be blank - try again")
            elif extraLiab != "Y" and extraLiab != "N":
                print("Answer can only be (Y)es or (N)o - try again(Y/N)")
            else:
                if extraLiab == "Y":
                    extraLiabFee += xtraLiabCost*carNums
                    break
                else:
                    break

        # Loop for optional glass coverage
        while True:
            glassCovFee = 0
            glassCov = input("Accept glass coverage insurance (Y)es or (N)o:  ").upper()
            if glassCov == "":
                print("Glass coverage cannot be blank - try again")
            elif glassCov != "Y" and glassCov != "N":
                print("Answer can only be (Y)es or (N)o - try again(Y/N)")
            else:
                if glassCov == "Y":
                    glassCovFee += glassCovCost*carNums
                    break
                else:
                    break

        # Loop for optional loaner car insurance coverage
        while True:
            loanCarFee = 0
            loanCar = input("Accept loaner car insurance (Y)es or (N)o:      ").upper()
            if loanCar == "":
                print("Loaner car insurance cannot be blank - try again")
            elif loanCar != "Y" and loanCar != "N":
                print("Answer can only be (Y)es or (N)o - try again(Y/N)")
            else:
                if loanCar == "Y":
                    loanCarFee += loanCarCovCost*carNums
                    break
                else:
                    break

        # Loop for amount of payments
        while True:
            paymentType = input("Payment in (F)ull or (M)onthly payments:        ").upper()
            if paymentType == "":
                print("Payment type cannot be blank - try again")
            elif paymentType != "F" and paymentType != "M":
                print("Answer can only be (F)ull or (M)onthly - try again(F/M)")
            else:
                if paymentType == "F":
                    payments = 1
                    break
                else:
                    payments = 8
                    break

        # Calculations
        # Determine from user input Insurance premiums
        insurancePrem = basicPrem + (basicPrem * .75)*(carNums - 1)
        totalExtraCharges = extraLiabFee + glassCovFee + loanCarFee
        totalInsurancePremium = insurancePrem + totalExtraCharges
        HST = totalInsurancePremium * hstRate
        totalCustCost = totalInsurancePremium + HST
        invoiceDateObj = datetime.date.today()
        if payments == 8:
            monthlyPayment = round((totalCustCost + processFee)/payments, 2)
            if invoiceDateObj == 12:
                nextPayDueObj = datetime.date(invoiceDateObj.year + 1, 1, 1)
            else:
                nextPayDueObj = datetime.date(invoiceDateObj.year, invoiceDateObj.month + 1, 1)
        # test output here and then comment out incase i need it again
        # print(insurancePrem, totalExtraCharges, totalInsurancePremium, HST, totalCustCost, monthlyPayment, nextPayDueObj)

        # Concatonate my customer info for reciept printing
        fullName = firstName + " " + lastName
        fullAdd = city + ", " + province + " " + postCode

        # OUTPUT SECTION / PRINT RECIEPT
        print()
        print("       One Stop Insurance Company")
        print("       Customer Insurance Reciept")
        print("========================================")
        print()
        print(" Customer:")
        print(f"  {fullName:<20s} Phone: {phoneNum:>10s}")
        print(f"  {streetAdd:<20s} Policy #: {policyNum:>7d}")
        print(f"  {fullAdd:<20s}")
        print()
        print(f"  Number of cars covered: {carNums:>14d}")
        print(f"  Insurance Base Premium: {FV.FDollar2(insurancePrem):>14s}")
        print("                              ----------")
        if extraLiabFee == 0:
            print(f"  Extra Liability Declined!")
        if extraLiabFee:
            print(f"  Extra Liability Coverage: {FV.FDollar2(extraLiabFee):>12s}")
        if glassCovFee == 0:
            print(f"  Glass Coverage Declined!")
        if glassCovFee:
            print(f"  Glass Replacement Coverage: {FV.FDollar2(glassCovFee):>10s}")
        if loanCarFee == 0:
            print(f"  Loan Car Coverage Declined!")
        if loanCarFee:
            print(f"  Loaner Car Coverage: {FV.FDollar2(loanCarFee):>17s}")
        print("                              ----------")
        print(f"  Total Extra Charges: {FV.FDollar2(totalExtraCharges):>17s}")
        print()
        print(f"  Total Insurance Premium: {FV.FDollar2(totalInsurancePremium):>13s}")
        print(f"  HST: {FV.FDollar2(HST):>33s}")
        print("                              ----------")
        print(f"  Total Insurance Cost: {FV.FDollar2(totalCustCost):>16s}")
        if paymentType == "M":
            print("                              ----------")
            print(f"  Monthly Payment Plan")
            print(f"  Processing Fee: {FV.FDollar2(processFee):>22s}")
            print(f"  Monthly Payments: {FV.FDollar2(monthlyPayment):>20s}")
            print(f"  Next Payment Due Date: {FV.FDateM(nextPayDueObj):>15s}")
        print("========================================")

        # Saving all user inputs to 'Policies.dat'
        # Using with open automatically closes file when done
        with open("policies.dat", "a") as f2:
            f2.write("{}, ".format(policyNum))
            f2.write("{}, ".format(invoiceDateObj))
            f2.write("{}, ".format(firstName))
            f2.write("{}, ".format(lastName))
            f2.write("{}, ".format(streetAdd))
            f2.write("{}, ".format(city))
            f2.write("{}, ".format(province))
            f2.write("{}, ".format(postCode))
            f2.write("{}, ".format(phoneNum))
            f2.write("{}, ".format(extraLiab))
            f2.write("{}, ".format(glassCov))
            f2.write("{}, ".format(loanCar))
            f2.write("{}, ".format(paymentType))
            f2.write("{}, ".format(nextPayDueObj))
            # break after last value
            f2.write("{}\n".format(totalCustCost))

        print()
        print("Saving user inputs to 'policies.dat'", end="", flush=True)
        for i in range(6):
            print(".", end="", flush=True)
            time.sleep(0.5)
        print("\nPolicy information processed and saved.")

        # increment policy number
        policyNum += 1

        # Query user to do another policy
        cont = input("Process another Insurance Policy (Y)es or (N)o: ").upper()
        if cont != "Y":
            # leaving program so need to save all defaults into 'OSICDef.dat'
            with open("OSICDef.dat", "w") as f3:
                f3.write("{}\n".format(policyNum))
                f3.write("{}\n".format(basicPrem))
                f3.write("{}\n".format(discount))
                f3.write("{}\n".format(xtraLiabCost))
                f3.write("{}\n".format(glassCovCost))
                f3.write("{}\n".format(loanCarCovCost))
                f3.write("{}\n".format(hstRate))
                f3.write("{}\n".format(processFee))
                print("Saving default values to 'OSICDef.dat'", end="", flush=True)
                for i in range(6):
                    print(".", end="", flush=True)
                    time.sleep(0.5)
                print("\n'OSICDef.dat' has been updated and saved!")
                exit()
        else:
            print("Lets process another policy!!!")


if __name__ == "__main__":
    main()

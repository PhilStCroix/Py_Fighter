# KSD Lesson 33 DATA FILES
# Author: Phil St Croix
# Written: Mar 14, 2023

import datetime
import time
import FormatValues as FV


def main():
    # loop for reading from data file and loading variables
    while True:
        try:
            with open("Sales.dat", "r") as f:
                print()
                print("Loading sales data from 'Sales.dat', Please standby", end="", flush=True)
                for i in range(6):
                    print(".", end="", flush=True)
                    time.sleep(0.5)
                print("\nSales file loaded OK!\n")
                for salesDataLine in f:
                    salesLine = salesDataLine.split(",")
                    empNum = salesLine[0]
                    empName = salesLine[1]
                    itemCost = float(salesLine[2])
                    HST = float(salesLine[3])
                    totalCost = float(salesLine[4].strip())
                    print(f" {empNum:>5} {empName:<20s}  {FV.FDollar2(itemCost):>9s}  {FV.FDollar2(HST):>9s}  {FV.FDollar2(totalCost):>9s}")
        except:
            print("Error loading 'Sales.dat'.  Exiting program")
            exit()
        else:
            break

    # Loading the Customer data file and making 2 tables
    print()
    print("Loading customer data from 'Customers.dat', Please standby", end="", flush=True)
    for i in range(6):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\nCustomer data loaded OK!\n")
    # Creating the first report
    print()
    print(f"{'WIDGITS INCORPORATED':^63s}")
    print()
    print(f"{'ACCOUNTS RECEIVABLE CUSTOMER LISTING':^63s}")
    print()
    print(f"{'ACCOUNT          CUSTOMER          PHONE':^63s}")
    print(f"{'NUMBER             NAME            NUMBER':^63s}")
    print(f"{'=========================================':^63s}")
    with open("Customers.dat", "r") as f:
        customerCount = 0
        for custDataLine in f:
            custData = custDataLine.split(",")
            custAccNum = custData[0]
            custName = custData[1]
            custPhone = custData[4]
            customerCount += 1
            print(f"           {custAccNum:>5}     {custName:^20}  {custPhone}")
    print(f"{'=========================================':^63s}")
    print(f"            TOTAL CUSTOMER LISTED: {customerCount}")

    # Create second table
    curDateObj = datetime.date.today()
    print()
    print()
    print(f"{'WIDGITS INCORPORATED':^63s}")
    print()
    print("{:^63s}".format("ACCOUNTS RECEIVABLE SUMMARY REPORT AS OF " + curDateObj.strftime("%m-%d-%Y")))
    print()
    print(" ACCOUNT       CUSTOMER          BALANCE    CREDIT      MINIMUM")
    print(" NUMBER          NAME              DUE     REMAINING    PAYMENT")
    print(" ==============================================================")
    with open("Customers.dat", "r") as f:
        custCount = 0
        balanceDue = 0
        minPayment = 0
        for custDataLine in f:
            custData = custDataLine.split(",")
            custAccNum = custData[0]
            custName = custData[1]
            custBalDue = float(custData[5])
            custCredMax = float(custData[6])
            if custBalDue > custCredMax:
                custCreditRemain = 0
                custMinPay = (custBalDue * .1)+(custBalDue - custCredMax)
            if custBalDue <= custCredMax:
                custCreditRemain = custCredMax - custBalDue
                custMinPay = custBalDue * .1
            custCount += 1
            balanceDue += custBalDue
            minPayment += custMinPay
            print(f" {custAccNum:>5s}   {custName:^19s}   {FV.FDollar2(custBalDue):>9s}   {FV.FDollar2(custCreditRemain):>9s}  {FV.FDollar2(custMinPay):>9s}")
    print(" ==============================================================")
    print(f" Customers listed: {custCount:>3d}         {FV.FDollar2(balanceDue):>9s}              {FV.FDollar2(minPayment):>9s}")
    print()
    print(f"{'END OF LISTING':^63}")

if __name__ == "__main__":
    main()
# KSD LESSON 34 DETAILED AND EXCEPTION REPORTS AND DATA FILES
# Author: Phil St Croix
# Written: Mar 20, 2023

import datetime
import time
import FormatValues as FV

def main():

    print()
    print("Loading Customer data, please standby", end="", flush=True)
    for i in range(6):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\nCustomer Data Loaded!\n")

    # Create a detailed report
    print()
    print("Granite Planet Studios")
    print("Customer Listing")
    print()
    print("CUSTOMER      CUSTOMER                     BALANCE      NEXT PAY")
    print(" NUMBER         NAME           PHONE         DUE          DATE")
    print("=================================================================")
    counter = 0
    balDueAcc = 0
    with open("CustExtra.dat", "r") as f:
        for custDataLine in f:
            custLine = custDataLine.split(",")
            custNum = custLine[0]
            custName = custLine[1]
            phone = custLine[2]
            balDue = float(custLine[3])
            nextPayDateDue = custLine[9].strip()
            print(f"{custNum:>6s} {custName:^20s} {phone:>10s}  {FV.FDollar2(balDue):>9s}   {nextPayDateDue:>10}")
            counter += 1
            balDueAcc += balDue
    print("=================================================================")
    print(f"Total Customers: {counter:>3d}                       {FV.FDollar2(balDueAcc):>5s}")

    # Create exception report
    curDate = datetime.datetime.now()
    print()
    print("Granite Planet Studios")
    print(F"OVER LIMIT REPORT AS OF {FV.FDateM(curDate)}")
    print()
    print("CUSTOMER      CUSTOMER             PHONE        CREDIT     AMOUNT      NEXT      PAYMENT")
    print(" NUMBER         NAME               NUMBER       LIMIT       OVER     PAY DATE      DUE")
    print("=========================================================================================")
    counterOL = 0
    payDueACC = 0
    with open("CustExtra.dat", "r") as f:
        for custDataLine in f:
            custLine = custDataLine.split(",")
            custNum = custLine[0]
            custName = custLine[1]
            phone = custLine[2]
            balDue = float(custLine[3])
            credLimit = float(custLine[4])
            amountOver = balDue - credLimit
            nextPayDate = custLine[9].strip()
            nextPayDateObj = datetime.datetime.strptime(nextPayDate, "%Y-%m-%d")
            paymentDue = (credLimit * .05) + amountOver
            if amountOver > 0:
                print(f"{custNum:<6s} {custName:^20s}  {phone:^14s}   {FV.FDollar2(credLimit):>9s}  {FV.FDollar2(amountOver):>9s}   {FV.FDateM(nextPayDateObj)}  {FV.FDollar2(paymentDue)}")
                counterOL += 1
                payDueACC += paymentDue

    print("=========================================================================================")
    print(f"Total Customers over Limit: {counterOL:>3} {FV.FDollar2(payDueACC):>56}")

if __name__ == "__main__":
    main()

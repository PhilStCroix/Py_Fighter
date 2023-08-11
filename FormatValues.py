import datetime

def FDollar2(DollarValue):
    # Function will accept a value and format it to $#,###.##.
    DollarValueStr = "${:,.2f}".format(DollarValue)
    return DollarValueStr


def FDollar0(DollarValue):
    # Function will accept a value and format it to $#,###.##.
    DollarValueStr = "${:,.0f}".format(DollarValue)
    return DollarValueStr


def FComma2(Value):
    # Function will accept a value and format it to $#,###.##.
    ValueStr = "{:,.2f}".format(Value)
    return ValueStr


def FComma0(Value):
    # Function will accept a value and format it to $#,###.##.
    ValueStr = "{:,.0f}".format(Value)
    return ValueStr


def FNumber0(Value):
    # Function will accept a value and format it to $#,###.##.
    ValueStr = "{:.0f}".format(Value)
    return ValueStr


def FNumber1(Value):
    # Function will accept a value and format it to $#,###.##.
    ValueStr = "{:.1f}".format(Value)
    return ValueStr


def FNumber2(Value):
    # Function will accept a value and format it to $#,###.##.
    ValueStr = "{:.2f}".format(Value)
    return ValueStr


def FDateS(DateValue):
    # Function will accept a value and format it to yyyy-mm-dd.
    DateValueStr = DateValue.strftime("%Y-%m-%d")
    return DateValueStr


def FDateM(DateValue):
    # Function will accept a value and format it to dd-Mon-yy.
    DateValueStr = DateValue.strftime("%m-%d-%Y")
    return DateValueStr


def FDateL(DateValue):
    # Function will accept a value and format it to Day, Month dd, yyyy.
    DateValueStr = DateValue.strftime("%A, %B %d, %Y")
    return DateValueStr

def ObjDate(dateString):
    # Function will accept a string date in YYYY-MM-DD format and convert it to a date object
    dateObj = datetime.datetime.strptime(dateString, "%Y-%m-%d")
    return dateObj

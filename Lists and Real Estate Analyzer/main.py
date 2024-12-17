# prompt for input, check for positive numeric value AND >0

def getFloatInput(sPrompt):
    while True:
        try:
            fVal = float(input(sPrompt))
            if fVal <= 0:
                print("Input a number that is greater than 0.")
            else:
                return fVal
        except ValueError:
            print("Input a number that is greater than 0.")


# if number of entries rcv'd is odd divide count by 2 for median
# if number of entries rcv'd is even divide the count by 2, take that amt and the entry amt before it and avg those 2
# store median, min, max, total, average, commissions to pull later in main

def getMedian(salesValues):
    salesValues.sort()
    q = len(salesValues) // 2
    if len(salesValues) % 2 != 0:
        return salesValues[q]
    else:
        return (salesValues[q - 1] + salesValues[q]) / 2


def getMin(salesValues):
    return min(salesValues)


def getMax(salesValues):
    return max(salesValues)


def getTotal(salesValues):
    return sum(salesValues)


def getAverage(salesValues):
    return sum(salesValues) / len(salesValues) if len(salesValues) > 0 else 0


def getCommission(salesValues, rate=0.03):
    return getTotal(salesValues) * rate


# code a loop that repeats until the user enters an N to exit the loop
# each time thru loop call getFloatInput function to prompt user for sales value
# each value returned added to the list
def main():
    salesValues = []

    while True:
        fSalesPrice = getFloatInput("Enter property sales value: ")
        salesValues.append(fSalesPrice)

# prompt user with Y or N to enter another value, repeat loop if Y or y / exit if N or n
        while True:
            sChoice = input("Enter another value Y or N: ")
            if sChoice.lower() == "y":
                break
            elif sChoice.lower() == "n":
                break
        if sChoice.lower() == "n":
            break


# sort the list from smallest to largest
    salesValues.sort()


# display property sales values in order, followed by min, max, total, average, median, & commission cost
    for i, value in enumerate(salesValues, start=1):
     print(f"Property {i:<1} $ {value:>12,.2f}")

    fMin = getMin(salesValues)
    fMax = getMax(salesValues)
    fTotal = getTotal(salesValues)
    fAverage = getAverage(salesValues)
    fMedian = getMedian(salesValues)
    fCommission = getCommission(salesValues)

    print(f"{'Minimum:':<12} $ {fMin:>12,.2f}")
    print(f"{'Maximum:':<12} $ {fMax:>12,.2f}")
    print(f"{'Total:':<12} $ {fTotal:>12,.2f}")
    print(f"{'Average:':<12} $ {fAverage:>12,.2f}")
    print(f"{'Median:':<12} $ {fMedian:>12,.2f}")
    print(f"{'Commission:':<12} $ {fCommission:>12,.2f}")


main()

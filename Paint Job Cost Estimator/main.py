import math

#prompt for input and convert to float
#check for positive value AND >0
def getFloatInput(sPrompt):
    while True:
        try:
            fVal = float(input(sPrompt))
            if fVal <= 0:
                print("Error: The value must be greater than zero. Please try again.")
            else:
                return fVal
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")

#calculates the number of gallons needed for the job, rounded up
def getGallonsOfPaint(fSqFeet, fFeetPerGal):
    return math.ceil(fSqFeet / fFeetPerGal)

#calculates total labor hours required for the job
def getLaborHours(iGallons, fHoursPerGal):
    return iGallons * fHoursPerGal

#calculates labor cost for the job
def getLaborCost(fLaborHours, fCostPerHour):
    return fLaborHours * fCostPerHour

#calculates total paint cost for the job
def getPaintCost(iGallons, fPaintPrice):
    return iGallons * fPaintPrice

#returns sales tax rate for the given state
def getSalesTax(sState):
    stateTaxRates = {
        "CT": 0.06,
        "MA": 0.0625,
        "ME": 0.085,
        "NH": 0.0,
        "RI": 0.07,
        "VT": 0.06
    }
    return stateTaxRates.get(sState.upper(), 0.0)

def writeToFile(sFileName, iGallons, fLaborHours, fPaintCost, fLaborCost, fTaxAmount, fTotalCostWithTax):
    with open(sFileName, 'w') as file:
        file.write(f"Gallons of paint: {iGallons}\n")
        file.write(f"Hours of labor: {fLaborHours:.1f}\n")
        file.write(f"Paint charges: ${fPaintCost:,.2f}\n")
        file.write(f"Labor charges: ${fLaborCost:,.2f}\n")
        file.write(f"Tax: ${fTaxAmount:.2f}\n")
        file.write(f"Total cost: ${fTotalCostWithTax:,.2f}\n")

def main():
#get input
    fSqFeet = getFloatInput("Enter wall space in square feet: ")
    fPaintPrice = getFloatInput("Enter paint price per gallon: ")
    fFeetPerGal = getFloatInput("Enter feet per gallon: ")
    fHoursPerGal = getFloatInput("How many labor hours per gallon: ")
    fCostPerHour = getFloatInput("Labor charge per hour: ")
    sState = input("State job is in: ")
    sName = input("Customer Last Name: ")

#calculate values
    iGallons = getGallonsOfPaint(fSqFeet, fFeetPerGal)
    fLaborHours = getLaborHours(iGallons, fHoursPerGal)
    fLaborCost = getLaborCost(fLaborHours, fCostPerHour)
    fPaintCost = getPaintCost(iGallons, fPaintPrice)
    fSalesTaxRate = getSalesTax(sState)
    fTotalCost = fLaborCost + fPaintCost
    fTaxAmount = fTotalCost * fSalesTaxRate
    fTotalCostWithTax = fTotalCost + fTaxAmount

#print results
    print(f"Gallons of paint: {iGallons}")
    print(f"Hours of labor: {fLaborHours:.1f}")
    print(f"Paint charges: ${fPaintCost:,.2f}")
    print(f"Labor charges: ${fLaborCost:,.2f}")
    print(f"Tax: ${fTaxAmount:.2f}")
    print(f"Total cost: ${fTotalCostWithTax:,.2f}")

#output to file
    sFileName = f"{sName}_PaintJobOutput.txt"
    writeToFile(sFileName, iGallons, fLaborHours, fPaintCost, fLaborCost, fTaxAmount, fTotalCostWithTax)

    print(f"\nFile: {sFileName} was created.")


main()

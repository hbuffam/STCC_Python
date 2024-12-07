#function asks for input, formats it, and while loop ensures it is above minimum amount(found in main function)
#prompts user for correction if requirements not met

def get_info(sPrompt: str, iMinAmt: float) -> float:

    while True:
        try:
            fValue = float(input(f"{sPrompt}: "))
            if fValue > iMinAmt:
                return fValue
            else:
                print(f"Input must be a positive numeric value")
        except ValueError:
            print(f"Input must be a positive numeric value")


#calculates the future dollar amount of the original deposit after compounding for a given number of months
#outputs the month number and new account balance for each month
def FutureValue(fPrincipal: float, fMPR: float, iMonths: int) -> None:

    for iMonth in range(1, iMonths + 1):
        fInterest = fPrincipal * fMPR
        fPrincipal += fInterest
        print(f"Month: {iMonth} Account Balance is: ${fPrincipal:,.2f}")


#calculates the number of months required to reach the goal amount
#outputs the number of months it will take
def Goal(fPrincipal: float, fMPR: float, fGoal: float) -> None:

    iTargetMonth = 0
    while fPrincipal < fGoal:
        fPrincipal += (fPrincipal * fMPR)
        iTargetMonth += 1

    print(f"\nIt will take: {iTargetMonth:,} months to reach the goal of ${fGoal:,.2f}")


#main function runs the ship. asks users for input, defines minimum values
def main():

    fOriginalDeposit = get_info("What is the Original Deposit (positive value)", 0)
    fInterestRate = get_info("What is the Interest Rate (positive value)", 0)
    iMonths = int(get_info("What is the Number of Months (positive value)", 0))
    fGoal = get_info("What is the Goal Amount (can enter 0 but not negative)", -1)

    fMPR = (fInterestRate / 100) / 12 #calculate monthly interest rate

    FutureValue(fOriginalDeposit, fMPR, iMonths)

    if fGoal > 0:
        Goal(fOriginalDeposit, fMPR, fGoal)

main()
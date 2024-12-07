# fv = pv (1 + interest rate / how many time to compound) ** (how many time to compound * Years to accrue)

pv = float(input("What is your starting principal?: "))
fR = float(input("Enter the annual interest rate: "))/100

iN = int(input("How many times per year is the interest compounded? "))
iTime = int(input("For how many years will the account earn interest? "))

fBalance = pv * (1 + fR / iN) ** (iN * iTime)

print(f"At the end of {iTime} years you will have ${fBalance:,.2f}")


#Welcome Message & blank line
print("Holly B's Temp Converter: ")
print()

#Ask user for real temperature and check if it is Fahrenheit or Celcius
fTemp1 = float(input("Enter a temperature: "))
sTempScale = (input("Is the temp F for Fahrenheit or C for Celsius? ").upper())

#If they respond with anything other than F or C (case insensitive), prompt them to do so.
#If they enter anything above 212 it will be invalid. Otherwise the input will be converted
if fTemp1 > 212 and sTempScale == "C":
    print("Temp can not be > 100")

elif sTempScale == "F":
    Celsius = (fTemp1 - 32) * 5 / 9
    print(f"The Celsius equivalent is:  {Celsius:.1f}")

elif sTempScale == "C":
    Fahrenheit = (fTemp1 * 9 / 5) + 32
    print(f"The Fahrenheit equivalent is: {Fahrenheit:.1f}")

else:
    print("You must enter a F or C")

#Ask user for their Name
iName = (input("Name of the person that we are calculating the grades for: "))

#Ask for test grades one at a time (whole numbers only)
iTest1 = int(input("Test 1: "))
iTest2 = int(input("Test 2: "))
iTest3 = int(input("Test 3: "))
iTest4 = int(input("Test 4: "))

# Ask user if they want to calculate lowest grade and drop it
iLowestGrade = (input("Do you wish to Drop the Lowest Grade Y or N? "))

#Check that all of the grades are greater than 0
if iTest1 <= 0 or iTest2 <= 0 or iTest3 <= 0 or iTest4 <= 0:
    input("Test scores must be greater than 0")
    exit()

#Prompt user to only use Y or N for iLowestGrade
if iLowestGrade != 'Y' and iLowestGrade != 'y' and iLowestGrade != 'N' and iLowestGrade != 'n':
    input("Enter Y or N to Drop the Lowest Grade.")
    exit()

#Find lowest grade, drop it, and average the other three grades
#Define variable for storing average grade
average = 0
if iLowestGrade == 'Y' or iLowestGrade == 'y':
    if iTest1 <= iTest2 and iTest1 <= iTest3 and iTest1 <= iTest4:
        average = (iTest2 + iTest3 + iTest4) / 3
    elif iTest2 <= iTest1 and iTest2 <= iTest3 and iTest2 <= iTest4:
        average = (iTest1 + iTest3 + iTest4) / 3
    elif iTest3 <= iTest1 and iTest3 <= iTest2 and iTest3 <= iTest4:
        average = (iTest1 + iTest2 + iTest4) / 3
    else:
        average = (iTest1 + iTest2 + iTest3) / 3
    print(f"{iName} test average is: {average:.1f}")

#Provide Letter Grade based on test average
    if average >= 97.0:
        print("Letter Grade for the test is: A+")
    elif average >= 94.0 and average <= 96.9:
        print("Letter Grade for the test is: A")
    elif average >= 90.0 and average <= 93.9:
        print("Letter Grade for the test is: A-")
    elif average >= 87.0 and average <= 89.9:
        print("Letter Grade for the test is: B+")
    elif average >= 84.0 and average <= 86.9:
        print("Letter Grade for the test is: B")
    elif average >= 80.0 and average <= 83.9:
        print("Letter Grade for the test is: B-")
    elif average >= 77.0 and average <= 79.9:
        print("Letter Grade for the test is: C+")
    elif average >= 74.0 and average <= 76.9:
        print("Letter Grade for the test is: C")
    elif average >= 70.0 and average <= 73.9:
        print("Letter Grade for the test is: C-")
    elif average >= 67.0 and average <= 69.9:
        print("Letter Grade for the test is: D+")
    elif average >= 64.0 and average <= 66.9:
        print("Letter Grade for the test is: D")
    elif average >= 60.0 and average <= 63.9:
        print("Letter Grade for the test is: D-")
    elif average <= 59.9:
        print("Letter Grade for the test is: F")

#Otherwise, average all four grades
elif iLowestGrade == 'N' or iLowestGrade == 'n':
    average = (iTest1 + iTest2 + iTest3 + iTest4) / 4
    print(f"{iName} test average is: {average:.1f}")

#Provide Letter Grade based on test average
    if average >= 97.0:
        print("Letter Grade for the test is: A+")
    elif average >= 94.0 and average <= 96.9:
        print("Letter Grade for the test is: A")
    elif average >= 90.0 and average <= 93.9:
        print("Letter Grade for the test is: A-")
    elif average >= 87.0 and average <= 89.9:
        print("Letter Grade for the test is: B+")
    elif average >= 84.0 and average <= 86.9:
        print("Letter Grade for the test is: B")
    elif average >= 80.0 and average <= 83.9:
        print("Letter Grade for the test is: B-")
    elif average >= 77.0 and average <= 79.9:
        print("Letter Grade for the test is: C+")
    elif average >= 74.0 and average <= 76.9:
        print("Letter Grade for the test is: C")
    elif average >= 70.0 and average <= 73.9:
        print("Letter Grade for the test is: C-")
    elif average >= 67.0 and average <= 69.9:
        print("Letter Grade for the test is: D+")
    elif average >= 64.0 and average <= 66.9:
        print("Letter Grade for the test is: D")
    elif average >= 60.0 and average <= 63.9:
        print("Letter Grade for the test is: D-")
    elif average <= 59.9:
        print("Letter Grade for the test is: F")

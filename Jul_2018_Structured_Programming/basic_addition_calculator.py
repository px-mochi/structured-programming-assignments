'''
Created on 7 Aug 2018

@author: Pei Xuan
'''

def main():
    
    #user input of the numbers to add
    numA = int(input("Enter first number (3 digits): "))
    numB = int(input("Enter second number (3 digits): "))
    
    
    #obtaining each digit from the two inputed numbers
    hundredsA = int(numA/100)
    tensA = int((numA - (hundredsA*100))/10)
    onesA = int(numA - (hundredsA*100)- (tensA*10))
    
    hundredsB = int(numB/100)
    tensB = int((numB - (hundredsB*100))/10)
    onesB = int(numB - (hundredsB*100)- (tensB*10))
    
    
    #obtaining calculated values
    # ___ Ans is the answer values, ___Carry is the value to carry
    onesAns = (onesA + onesB)%10
    onesCarry = int((onesA + onesB)/10)
    
    tensAns = (tensA + tensB + onesCarry)%10
    tensCarry = int((tensA + tensB + onesCarry)/10)
    
    #Add back the %10 to separate the digits into their own output
    hundredsAns = (hundredsA + hundredsB + tensCarry)%10
    
    #Including a new digit for the thousands digit
    #Since the input is only 3 digit, the thousands answer is simply tensCarry (at the hundreds place) 
    
    #Show the carry only if the carry is non-zero
    if onesCarry == 0:
        onesCarry = ""
    
    if tensCarry == 0:
        tensCarry = ""
    
    
    #Just a blank line to make it neater
    print()
    
    #printing results
    #width of each digit is 2, main numbers on the right, carry on the left
    print(" ","{0:<2}{1:<2}".format(tensCarry,onesCarry))
    print(" ","{0:>2}{1:>2}{2:>2}".format(hundredsA,tensA,onesA))
    print("+","{0:>2}{1:>2}{2:>2}".format(hundredsB,tensB,onesB))
    print("","-------")
    print("{0:>2}{1:>2}{2:>2}{3:>2}".format(tensCarry,hundredsAns,tensAns,onesAns))
    

    #Including name and student number at end of output
    print("\nName: <removed for upload to github>")
    print("Student Number: <removed for upload to github>")
    

main()

'''
[Pseudologic explaining this code]

- Input
User inputs values of two numbers.

- Processing
Call the two numbers numA, numB
Obtain each individual digits of the two numbers, call them hundreds/tens/onesA and B
Repeat this for each place value (hundreds, tens, ones):
Add each number together to get a result
To get the answer value for each place. separate any two-digit results using the modulus (%) operator (For ALL values)
Obtain value for carry digit by subtracting the answer value from the initial result (For ALL values)

As the original numbers are only three digit, the thousands digit will be the value of the carry at hundreds place.

If carry digit is 0:
    Change the 0 digit into a blank character (showing carry only if non-zero)
If thousands digit is 0:
    Change the 0 digit into a blank character (showing carry only if non-zero)


- Output
Repeat this for each row of output (carry, numA, numB, line, answer):
    Using string formatting, print out each digit for the calculation, with a width of 2. 
    The carry row will be left justified, and the other numbers right justified.
    Add in the new thousands value in output.

Print out student name and number at the end of the program.
'''
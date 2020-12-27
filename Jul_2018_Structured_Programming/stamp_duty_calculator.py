'''
Created on 10 Nov 2018

@author: Pei Xuan

This program calculates the total stamp duty payable in Singapore for property purchase.
BSD = Buyer Stamp Duty
ABSD = Additional Buyer Stamp Duty

Output is shown in 2 decimal places as this is dealing with currency, even though the example does not include it.
**To get the output shown in the example, just use integers, round() on the value, or {:.0f} when formatting the string.
'''
from _datetime import datetime


def calcBSD(propPrice):  #This function calculates the property BSD amount.
    if propPrice <= 180000:  #1% of the 1st S$180,000
        BSD = propPrice * 0.01
    
    elif propPrice <= 360000: #2% of the next S$180,000 (180000 + 180000)
        BSD = 180000 * 0.01  #Adding the 1% of the 1st S$180,000
        remainingPrice = propPrice - 180000  #Calculate remaining amount left
        BSD = BSD + (remainingPrice * 0.02)  #Adding next 2% BSD to the 1% before
    
    elif propPrice <= 1000000: #3% of the next S$640,000
        BSD = (180000 * 0.01) + (180000 * 0.02) #Adding both the 1st 1% and 2% of BSD
        remainingPrice = propPrice - 360000 #Calculate remaining amount left
        BSD = BSD + (remainingPrice * 0.03)  #Adding next 3% BSD
    
    else: #If property price is higher than S$1,000,000
        BSD = (180000 * 0.01) + (180000 * 0.02) + (640000 * 0.03)  #Adding previous BSD tiers
        remainingPrice = propPrice - 1000000  #Calculate remaining amount left
        BSD = BSD + (remainingPrice * 0.04)  #Adding next 4% BSD

    
    return BSD  #Returns BSD value to main


def percentABSD(citizenType, numProp, purchDate):  #This function calculates the ABSD rate in % form.
    ''' 
    I am using a dictionary to locate and return the percentABSD value.
    This is to prevent excessive use of 'if' as shown in the flowchart.'''
    
    after6Jul2018_ABSD = {"S":{"1st purchase":0,"2nd purchase":0.12,"3rd or more":0.15},\
            "P":{"1st purchase":0.05,"2nd purchase":0.15,"3rd or more":0.15},\
            "F":{"1st purchase":0.20,"2nd purchase":0.20,"3rd or more":0.20}}
    
    
    before6Jul2018_ABSD = {"S":{"1st purchase":0,"2nd purchase":0.07,"3rd or more":0.10},\
            "P":{"1st purchase":0.05,"2nd purchase":0.10,"3rd or more":0.10},\
            "F":{"1st purchase":0.15,"2nd purchase":0.15,"3rd or more":0.15}}
    
    
    #Finding out which ABSD data table to use
    if purchDate < datetime(2018,7,6):  #if the buyer purchase date is before 6 July 2018
        ABSDdata = before6Jul2018_ABSD
    
    else:  #If the buyer purchase date is on or after 6 July 2018
        ABSDdata = after6Jul2018_ABSD


    #Linking buyer properties to ABSD data table
    if numProp == 0:
        purchase = "1st purchase"
    
    elif numProp == 1:
        purchase = "2nd purchase"
    
    else:  #if current property purchase is 3rd or more
        purchase = "3rd or more"
        
    
    
    percentABSD = ABSDdata[citizenType][purchase]  #Obtain the percent ABSD based on citizen type and purchase type
    
    return percentABSD
    
    

def main():
    while True:  #Repeat this loop till valid propertyPrice is inputed (> 0)
        propPrice = float(input("Enter price of property: "))  #Get property price input
        
        if propPrice > 0:
            break
        
        else:
            print("Please enter a positive, non-zero whole number.")
    
    while True:  #Repeat this loop till valid citizenType is inputed ("S", "P", "F"
        print("Type of citizenship:\
        \n   S - Singaporean\
        \n   P - Singapore Permanent Resident\
        \n   F - Foreigner")
        citizenType = input("Enter citizen type: ")[0].capitalize()  #Get citizen type input. 1st letter of input is taken and capitalized.
        
        if citizenType == "S" or citizenType == "P" or citizenType == "F":
            break
        
        else:
            print("Please enter a valid citizen type.")
            
    purchDate = datetime.strptime(input("Enter date of purchase in d/m/yyyy format: "),"%d/%m/%Y")
    

    if citizenType == "F":  #Skip number of properties input if buyer is foreigner
        numProp = 0  #number of Properties defaults to 0 since ABSD is the same for all foreigners.

    elif citizenType == "S" or citizenType == "P":  #Get number of properties input
        while True:  #Repeat this loop till valid numProp is inputed (>= 0)
            numProp = int(input("Enter number of properties already purchased in Singapore: "))
            if numProp >= 0:
                break
            
            else:
                print("Please enter positive whole number which includes 0.")
            
    else:  #If an invalid citizen type was entered, quit program
        print("Invalid citizen type inputed. Ending program.")
        exit()

    
    
    BSD = calcBSD(propPrice)  #run calcBSD function to get BSD
    ABSDpercent = percentABSD(citizenType, numProp, purchDate)  #run percentABSD function to get percentABSD
    ABSD  = propPrice * ABSDpercent  #Calculate ABSD
    totalStampDuty = BSD + ABSD  #Calculate total stamp duty
    
    #Printing cost of stamp duties payable
    print("Buyer stamp duty = ${:.2f}".format(BSD))
    if ABSD == 0:  #Obtain new line to print if there is no ABSD to pay
        pABSD = "No additional stamp duty is applicable"
    
    else:  #Convert ABSD price to 2 decimal places
        pABSD = "Additional buyer stamp duty = ${:.2f}".format(ABSD)
    print(pABSD)
    print("Total stamp duty payable = ${:.2f}".format(totalStampDuty))
    

if __name__ == '__main__':
    main()


'''
-- Top-down design algorithm in pseudocode showing at least 3 levels of refinement. --
Top level design algorithm:
def main():
Room data is saved in a dictionary rooms
Print a menu and get menu choice menuChoice
Run bookRoom or releaseRoom based on menuChoice
Check if rooms are booked using roomCheck and get number of rooms available roomNum
Display booked and available rooms if needed using roomDisplay


Second level design:
printMenu():
#Main menu of library booking program
Print options for students to book
Get inputs: menuChoice
return menuChoice

roomCheck(rooms):
Using dictionary operations, check room occupancy.
Use a variable bookedNum to store number of booked rooms
return bookedNum

 
roomDisplay(rooms):
Using dictionary operations, check room occupancy
Print Booked rooms 
Print Available rooms

bookRoom(bookedNum, rooms):
If rooms are fully booked by checking bookedNum:
    Print an error message
    Return to main menu
If there are multiple rooms available:
    List unoccupied room numbers in ascending order and allow student to make a choice using multiRoom
If there is only one room left by checking bookedNum:
    Inform student and ask if student wishes to proceed using oneRoom
If a room was not chosen, no changes will be made to rooms
return rooms

 releaseRoom(bookedNum, rooms):
If there are no booked rooms by checking bookedNum:
    Print an error message
    Return to main menu
Else:
    Get room number for release using getRelease
If a room was not chosen, no changes will be made to rooms
return rooms 


Third level design:
bookRoom and releaseRoom have further steps needed, so it is split into further functions to simplify each function.
## Under bookRoom
multiRoom(rooms):
#Run if there are multiple rooms available for booking
Using sort on availableRooms, sort availableRooms in ascending order
Print availableRooms
Get user input on room selected using getSelect to get selectedRoom
return selectedRoom

oneRoom(rooms):
#Run if there is only one room available for booking
Print a statement to inform student of the only room number left
Print and ask if student wishes to proceed 
If student chooses to proceed:
    selectedRoom = the room number left
return selectedRoom
## Under releaseRoom
getRelease(rooms):
Get inputs: selectedRoom
If selectedRoom is not a currently booked room:
    Print an error message
    selectedRoom  = False

return selectedRoom


Fourth level design:
multiRoom and releaseRoom have user inputs required. The functions getSelect and getRelease are to obtain user inputs (getRelease is technically 3rd level design so it is not here)

getSelect(rooms, availableRooms):
Get inputs: selectedRoom
Print rooms available to select availableRooms
If selectedRoom was terminated with ‘-1’:
    selectedRoom = False
If selectedRoom is invalid:
    Loop getSelect till valid room is selected, check using rooms dict
return selectedRoom

'''

'''
Created on 10 Nov 2018

@author: Pei Xuan

This program runs a library study room booking program.

This is revamped from ECA Question 2b, to record the student ID of the student booking.
Releasing of study rooms can only be done by the student with the recorded ID.
'''

def main():
    
    #Saving study room information in a dictionary
    #1/2/3 = room number. If room status = true, means room is booked
    #Student ID is added to room data
    rooms = {1:{"Room Name":"Room 1","Room status":False,"Student Number":None},\
             2:{"Room Name":"Room 2","Room status":False,"Student Number":None},\
             3:{"Room Name":"Room 3","Room status":False,"Student Number":None}}  
    
    
    while True:  #Loops menu and menu selection option till application is exited
        menuChoice = printMenu()  #Prints library menu option, and get student menu choice
        bookedNum = roomCheck(rooms)  #Checks current status of rooms
        
        #Running different functions based on menu choice selected
        if menuChoice == "":  #If user just presses enter i.e. giving a blank option
            print("Please choose an option.")
        
        elif menuChoice[0] == '1':
            rooms = bookRoom(bookedNum, rooms)
            
        elif menuChoice[0] =='2':
            rooms = releaseRoom(bookedNum, rooms)
        
        elif menuChoice[0] == '0':  #If 0 is chosen, exit the program
            print("Application exiting")
            break  #Breaks out of loop, and main function ends normally
        
        else:  #If an invalid choice is chosen
            print("Please input a valid option")
            print()
    

def printMenu():
    #Main menu of library booking program
    
    #Printing menu options
    print("1. Book a Study Room")
    print("2. Release a Study Room")
    print("0. Exit")
    
    menuChoice = input("Enter choice: ")  #Get user input on menu options
    
    return menuChoice
    

def roomCheck(rooms):
    '''On 2nd thoughts, I shouldn't hardcode the values here, but since this ECA only has 1.5 days
    to complete, the variable used will be the number of booked rooms. Ideally some other variable 
    that can accommodate future changes such as new library study rooms would be better to reduce
    code changes.
    Affected functions: bookRoom, releaseRoom'''
    #Returns number of booked rooms
    bookedNum = 0  #Initialize number of booked rooms to 0 

    for Room in rooms:  #If room is booked, add 1 to bookedNum
        if rooms[Room]["Room status"] is True:
            bookedNum += 1

    return bookedNum


def roomDisplay(rooms):
    #Display current occupancy of rooms
    
    #Realised that I didn't even need to do 'for Room in rooms:'
    ## ****  Question 2c *****
    #Sorts dict of rooms, add room + student number to list of booked rooms
    booked_list = []
    for i in sorted(rooms):  #Loop over rooms in ascending order
        if rooms[i]["Room status"] is True:  #If room is booked
            booked_list.append( "{} {}".format(i, rooms[i]["Student Number"]))
    
    available_list = [Room for Room in rooms if rooms[Room]["Room status"] is False]  #Using list comprehension to place booked rooms in available list
    
    #Sorts both lists. sort() modifies the list in-place and returns none, so that is used.
    #booked_list.sort()  # This is not required anymore as it is already sorted
    available_list.sort()
    
    #Printing current occupancy of rooms
    if bool(booked_list) is False:  #If the booked rooms list is empty
        print("No booked rooms")
        print()  #I can use \n, but this is for easier reading of code
    
    else: 
        print("Booked rooms")
        print(*booked_list, sep = "   ")  #Prints items in list, separated by a 3 spaces to make it clearer
        print()  #I can use \n, but this is for easier reading of code
        
    if bool(available_list) is False:  #if the available room list is empty
        print("No Available rooms")
        print()  #I can use \n, but this is for easier reading of code
        
    else:
        print("Available rooms")
        print(*available_list)  #Prints items in list, separated by a space
        print()  #I can use \n, but this is for easier reading of code
        
    
def bookRoom(bookedNum, rooms):
    #Books a room based on student selection
    if bookedNum == 3:  #If rooms are fully booked
        print("No study room available currently")  #Print an error message
        print()  #I can use \n, but this is for easier reading of code (also, to make output look neater)
        return rooms #terminates room booking (No changes made to rooms, returned to prevent error)
        
    elif bookedNum == 2:  #If there is only one room left (as there are a total of 3 rooms)
        selectedRoom = oneRoom(rooms) 
        
    elif bookedNum <= 1:  #if there is more than one available room (as there are a total of 3 rooms)
        selectedRoom = multiRoom(rooms)
    
    if selectedRoom is None:  #If no room was selected, or booking was cancelled
        print("Booking room is abandoned")
        return rooms #terminates room booking (No changes made to rooms, returned to prevent error)
    
    else: 
        rooms[selectedRoom]["Room status"] = True  #Change room status to True
        
        ## ****  Question 2c *****
        #Obtain and store student number details of student booking
        studentNumber = input("Enter student number of student making the booking: ").capitalize()
        rooms[selectedRoom]["Student Number"] = studentNumber
        
        print("Room is successfully booked")
        
        roomDisplay(rooms)  #Display rooms that have been booked and unbooked
        
        return rooms
        
    
def multiRoom(rooms):
    #Provides a selection of available rooms (rooms available > 1), returns selection
    available_list = [Room for Room in rooms if rooms[Room]["Room status"] is False]  #Get available rooms
    available_list.sort()  #sort available rooms in ascending order
    availableRooms = [rooms[Room]["Room Name"] for Room in available_list if Room in rooms]  #Add room name to availableRooms list if room is in the sorted available_list
    
    selectedRoom = getSelect(rooms, availableRooms)  #Run function to get student input till valid option is selected
    
    return selectedRoom
    


def getSelect(rooms, availableRooms):
    #Get room number from student to book room from list of rooms in multiRoom
    while True:  #Loop question till a valid option is inputed
        print("List of available Rooms")
        print(*availableRooms, sep = "  ")  #Prints list of available room names, separated by 2 spaces
    
        selectedRoom = int(input("Select a room or -1 to quit room booking: "))
        if selectedRoom == -1:
            selectedRoom = None
            return selectedRoom
        
        elif selectedRoom in rooms and rooms[selectedRoom]["Room status"] is False:  #Ensure that room exists and is available
            return selectedRoom
        
        else:  
            print("Select a valid available room number or -1 to quit room booking")
    

def oneRoom(rooms):
    #Display room available (rooms available = 1), returns selection
    for Room in rooms:  #Identify the only room that is available
        if rooms[Room]["Room status"] is False:
            onlyRoom = Room
    
    print("Only room {} is available".format(onlyRoom))  #Print notice informing student of room left
    confirm = input("Proceed? y/n: ").lower()[0]
    
    if confirm == "y":  #Return room selection to higher function if student decides to book
        selectedRoom = onlyRoom
    
    else:
        selectedRoom = None  #"n" was chosen, so the room was not selected.
    
    return selectedRoom


def releaseRoom(bookedNum, rooms):
    #Releases a room based on student selection
    if bookedNum == 0:  #If there are no booked rooms
        print("There is currently no room booking to release")  #changed print statement to be clearer
        print()  #I can use \n, but this is for easier reading of code (also, to make output look neater)
        return rooms #terminates room release (No changes made to rooms, returned to prevent error)
    
    elif bookedNum >= 1:  #There is at least one booked room to release
        selectedRoom = getRelease(rooms)
        
    
    if selectedRoom is None:  #If no room was selected, or incorrect room was selected
        print("There is no booking in this study room")
        return rooms #terminates room release (No changes made to rooms, returned to prevent error)
    
    elif selectedRoom == "Incorrect Student Number":
        print("Incorrect student number.")
        roomDisplay(rooms) #Display rooms that have been booked and unbooked
        return rooms #terminates room release (No changes made to rooms, returned to prevent error)
    
    else:
        rooms[selectedRoom]["Room status"] = False  #Changes room status to False
        print("Room is successfully released")
        
        roomDisplay(rooms) #Display rooms that have been booked and unbooked
        
        return rooms
    

def getRelease(rooms):
    #Get room number from student to release currently booked study room
    selectedRoom = int(input("Enter the room number to release: "))
    if selectedRoom in rooms and rooms[selectedRoom]["Room status"] is True:  #Ensure that room exists and is currently booked
        ## ****  Question 2c *****
        #Obtain student number of student releasing room
        studentNumber = input("Enter student Number: ").capitalize()
        if studentNumber == rooms[selectedRoom]["Student Number"]:
            return selectedRoom
        
        else:  #If student number inputed does not match with rooms data
            selectedRoom = "Incorrect Student Number"
            return selectedRoom
            
    
    else:
        selectedRoom = None  #Since an incorrect or invalid room number was chosen, a room was not selected
        return selectedRoom


if __name__ == '__main__':
    main()

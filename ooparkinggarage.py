class Parking_Garage():

    """This class will create a parking garage with:
        -takeTicket
        -parkingSpaces
        -payForParking
        -currentTicket
        -leaveGarage
        
        This class will have the following attributes:
        -tickets: expected to be a list
        -parkingSpaces: expected to be a list
        -currentTicket: expected to be a dictionary
        """

    def __init__(self):
        self.tickets = 6
        self.spots = ["A1", "B1", "C1", "D1", "E1", "F1"]
        self.takenSpaces = []
        self.currentTicket = {
            'paid': False 
        }

# 1. 
    # create a method to show how many parking spaces.
    def showParkingSpaces(self):
        print('\nThese are the available spots to park:') 
        for spot in self.spots:
            print(spot)

# 2.
    # create a method for taking a ticket that decreases the amount of tickets and parking spaces available by 1.
    def takeTicket(self):
        if self.tickets > 0:  
            print("Let's get you parked!")  
            print('\nThese are the available spots to park:') 
            for spot in self.spots:
                print(spot)  
            parking_selection = (input("Please select a spot: ")) 
            if parking_selection.lower() == "a1" or parking_selection.lower() == "b1" or parking_selection.lower() == "c1" or parking_selection.lower() == "d1" or parking_selection.lower() == "e1" or parking_selection.lower() == "f1":                
                self.takenSpaces.append(parking_selection.upper())
                self.spots.remove(parking_selection.upper())
                self.tickets -= 1           
                print(f"{parking_selection.upper()}; an excellent choice. That's my favorite letter of the alphabet.")
            else:
                print("Sorry, I think you made a mistake. Try again!")
        elif self.tickets == 0:
            print("Sorry, there are no more spots for you to park. I recommend taking a few spins around the block and consider if you could have biked here instead.")

# 3.
    # create a method that allows to pay for parking.
    # This will display an input ("Please insert amount") and stores it in a variable.
    # If the payment variable is not empy (ticket paid), then --> display a message saying ticket is paid and they have 15 mins to leave.
    # This should also update the 'currentTicket' dictionary key "paid" to True
    def payForParking(self):
        if self.tickets == 6:
            print("Silly, why are you trying to pay for a parking spot you didn't park in?")
        if self.tickets <= 5:
            amount = input("Your parking fee is 100 dollars. Please insert 100: ")
            if amount == "100":
                self.currentTicket['paid'] = True
                print("Thank you for your payment, now please get out within 15 minutes.")
            else:
                print("Let's try that one again!")





# 4.  
    # create a method for leaving the garage.
    # If the ticket has been paid, display a message: "Thank You, have a nice day"
    # update 'parkingSpaces' list to increase by 1 (that means add to the parkingSpaces list)
    # update 'tickets' list to increase by 1 (meaning add to the tickets list)
    def leaveGarage(self):
        if self.currentTicket['paid'] == False:
            print("\nWhoopsie, looks like you either forgot to pay, or you aren't parked here in the first place!")
            wrong_turn = (input("\nTry again: type 'forgottopay' or 'neverparked': \n"))
            if wrong_turn == "forgottopay":
                self.payForParking()
            elif wrong_turn == "neverparked":
                self.showParkingSpaces()
                self.takeTicket()
        elif self.currentTicket['paid'] == True:
            abandoned_spot = (input("\nPlease enter your current spot: "))
            # ------Note: The below "if" statement is non-functioning; program accepts any input (not just "a", "b", or "c") and follows the conditional steps            
            if abandoned_spot.lower() == "a1" or abandoned_spot.lower() == "b1" or abandoned_spot.lower() == "c1" or abandoned_spot.lower() == "d1" or abandoned_spot.lower() == "e1" or abandoned_spot.lower() == "f1":
                print("Thank you! Have a great day.")
                self.takenSpaces.remove(abandoned_spot.upper())
                self.spots.append(abandoned_spot.upper())
                self.tickets += 1
                self.currentTicket['paid'] = False
# ------Note: The below "elif" statement is non-functioning. 
            else:
                print("Try again, liz")

# Turn the dream into a reality. 
my_Garage = Parking_Garage()


def run():
    print('\nWelcome to what can only be objectively described as the greatest parking garage in the world!')
    while True:
        print('\nWhat do you want to do?')
        response = input('\nType: \n-"show" to show available spaces, \n-"park" to choose a space, \n-"pay" to pay your fee, \n-"leave" to escape the garage, or \n-"quit" to quit the program:\n ')
        
        if response.lower() == 'quit':            
            print('Okay, later gator!')
            break
        elif response.lower() == 'show':
            my_Garage.showParkingSpaces()
        elif response.lower() == 'park':
            my_Garage.takeTicket()
        elif response.lower() == 'pay':
            my_Garage.payForParking()
        elif response.lower() == 'leave':
            my_Garage.leaveGarage()
        else: 
            print("Try something else, please. Look closely at the options.")

# Call it!
run()
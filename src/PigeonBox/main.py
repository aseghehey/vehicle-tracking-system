
####################################################################################################################
'''
////////////////
PROGRAM main:   provide a menu based interface for managing dealership inventory and orders. main meat of system.

////////////////
PROGRAMMER: Emanuel Aseghehey emanueldejes@usf.edu
DOCUMENTOR: Alexander Ashmore atashmore@usf.edu

////////////////
VERSION 1: written 13 March 2023 by E. Aseghehey
REVISION: revision history can be found on the project GitHub

////////////////
PURPOSE:
Manges user accounts and provides interfcae for users to interact with their account. the meat of the system.
Works as a command line interface.

Methods:
- displayData(data): Displays each element in an array along with its index.

- StallUntilUserInput(): Pauses the program and waits for the user to press enter to view any output generated after an action.

- isEmpty(arr): Checks whether an array is empty or not. If the array is empty, it prints a warning message and returns True; 
    otherwise, it returns False.

- validatePassword(): Validates a new password by asking the user to input the new password and confirm it. It then checks whether
    the two passwords match, whether the new password is the same as the old password, and returns the new password if it passes
    all the checks.

- ChangePasswordMenu(): Allows the user to change their password by calling the validatePassword() function to get the new password
    and passing it to the interface's changeUserPassword() method. It then prints a success message.

- validateUsername(): Validates a new username by asking the user to input the new username and checking whether it's the same as the
    old username or if it already exists in the list of users. If the new username passes all the checks, it returns the new username.

- ChangeUsernameMenu(): Allows the user to change their username by calling the validateUsername() function to get the new username and
    passing it to the interface's changeUserUsername() method. It then prints a success message.

- ConfirmSelection(response={"y", "yes", "n", "no"}, msg=""): Asks the user to confirm a particular action by displaying a warning message
    and waiting for the user to input either "y" or "n". If the user inputs an invalid answer,
    it displays an error message and waits for another input. It returns True if the user confirms the action, False otherwise.

- ValidateUserInput(action="action", isNum=False, isEmail=False) function takes in user input and validates it based on the arguments passed. 
    The action argument specifies what type of input is expected, isNum specifies whether the input should be a number, and isEmail specifies
    whether the input should be a valid email address. If the input is invalid, appropriate error messages are displayed, and the function
    continues to prompt for input until valid input is received.

- getAction(validSet={"1", "2", "3"}, msg="Enter action:") function displays a menu with options specified in validSet and prompts the user
    to choose one of the options. The function continues to prompt the user until valid input is received.

- PickIndex(arr) function displays the elements in the array and asks the user to select one. The function continues to prompt the user until
    valid input is received, and then returns the index of the selected element.

- SeparateInputToList(inpt) function takes in a string and returns a list of strings by splitting the input string based on commas and removing
    any extra spaces.

- GetObject(objectList) function calls the PickIndex function to allow the user to select an object from the list passed as an argument.
    The selected object is returned.

- updateCarStatus(car) function displays a menu with options for updating the status of a car, calls the changeCarStatus method of an object
    interface to update the status of the car, and displays a success message.

- AddEmployee() function prompts the user to enter details for a new employee and then adds the employee to the system using the AddEmployee or 
    AddAdmin method of an object interface. The function displays success or failure messages based on whether the employee 
    was added successfully.

- RemoveEmployeeMenu() function displays a menu with options for removing an employee, calls the GetObject function to allow the user to select an
    employee to delete, and then calls the RemoveUser method of an object interface to remove the employee. The function 
    displays success or failure messages based on whether the employee was removed successfully.

- displayStatusOptions(): Displays a list of options related to the status of a car and prompts the user to select an option. 
    Returns the selected option.

- CarSearch(): Prompts the user to enter details about a car they want to search in the inventory. Validates the input and searches for the car
    in the inventory. If found, displays the details of the car. Returns the car object.

- filterByMenu(): Displays a list of options related to filtering cars by their status (Available, Ordered, Backorder, Delivered).
    Prompts the user to select an option and displays the list of cars with the selected status.

- modifyInventoryMenu(): Displays a list of options related to modifying the inventory of cars (add or remove a car). Validates the
    input and performs the selected action.

- AddCustomer(): Prompts the user to enter details about a new customer (first name, last name, email address, credit card, and home address).
    Validates the input and adds the new customer to the database. Returns the new customer object.

- DeleteCustomerMenu(customerToDelete): Displays a confirmation message asking the user if they want to delete the specified customer.
    If confirmed, removes the customer from the database.

- Login(): This function takes care of the login page and authenticates the user. It prompts the user for a username and password,
    and gives them 3 attempts to enter the correct information. It returns the user object if the user is authenticated, or None 
    if the user failed all 3 attempts.

- modifyCarMenu(car): This function presents a submenu for modifying a specific car in the inventory. It displays options for changing the
    car's status, price, mileage, or warranty plans, and prompts the user to enter the desired changes. It then calls other functions to
    make the necessary updates to the car object.

- SearchCarMenu(car=None): This function presents a submenu for searching for a car in the inventory. It takes an optional "car" argument,
    which can be used to pre-populate the search with a specific car object. If no car object is provided, it calls the CarSearch()
    function to prompt the user for search criteria. Once a car is found, the function presents options for ordering the car or modifying
    its details.

- InventoryMenu(): This function presents the main inventory menu, which displays a list of cars in the inventory along with options for
    viewing details, searching, filtering, or making a customer order. If the user is an admin, there is also an option for adding or removing
    cars from the inventory. The function loops continuously until the user chooses to exit.

- AddCar(): This function allows the user to add a new car to the inventory. It prompts the user to enter various details such as VIN, 
    make, model, year, mileage, color, price, engine, transmission, interior, external design, paint, handling, audio, comfort features, package,
    warranty, and maintenance. The function then creates a dictionary of the details and passes it to the AddInventory() function of the interface
    module to add the car to the inventory.
    
- RemoveCar(): This function allows the user to remove a car from the inventory. It displays the list of all cars in the inventory and prompts the 
    user to select a car to remove. It then passes the selected car to the RemoveInventory() function of the interface module to remove it from
    the inventory.

- addOrderMenu(carToOrder, customers): This function is called when the user wants to order a car that is not currently available. 
    It prompts the user to select a customer from the list of all customers or add a new customer. It then passes the selected car and
    customerto the MakeOrder() function of the interface module to create an order.

- OrderMenu(): This function displays a menu of options related to orders. It allows the user to view all orders, view orders by customer,
    view orders by status, or make a new order. When the user selects the "make a new order" option, it calls the addOrderMenu() function.

- ManageEmployeesMenu() function:This menu displays a list of options for managing employees. The options include viewing employee details,
    adding new employees, and removing employees from the system. It calls other functions to perform these 
    actions and loops until the user chooses to exit.

- validateCreditCard() function:This function validates the user input for credit card numbers by making sure the input contains 16 digits only. 
    If the input does not meet this requirement, it prints an error message and prompts the user to try again.

- modifyCustomerDetails() function:This function allows the user to update a customer's information such as their home address, email address,
    or credit card details. It prompts the user to choose which detail they want to update and calls the 
    corresponding function to perform the update.

- ManageCustomersMenu() function:This menu displays a list of options for managing customers. The options include viewing customer details,
    adding new customers, removing customers from the system, and editing customer details. It calls other functions 
    to perform these actions and loops until the user chooses to exit.

- CarSalesMenu() function:This function is currently empty but is intended to display orders and set order statuses to delivered.

- AccountSettingsMenu() function:This menu allows the user to change their account details such as their password or username. It prompts 
    the user to choose which detail they want to update and calls the corresponding function to perform the update.

- menu() function:This is the main menu that the user first interacts with. It displays a list of options for the user to choose from,
    such as managing customers, viewing car inventory, etc. It loops until the user chooses to exit the program.
    
- run() function: This function manages the overall flow of the program. It starts by logging in the user, determining whether the user 
    is an admin or not, and setting the interface accordingly. It then calls the menu() function for the user to interact with. Finally,
    it logs out the user and prompts them to log in again if they choose to do so.


////////////////
DATA STRUCTURES:
DataStructures:
-Lists: Used to store and manipulate data such as displaying data, validating user input, and selecting objects.
- Dictionary: A dictionary is used to store a set of responses to confirmation requests.
- Sets: used to validate the user's input and actions.

Attributes:
- data: an array of user accounts, used as input to the displayData() function to print out each element in the array.
- Auth: an object that handles user authentication.
- bcolors: a module that defines ANSI escape sequences for colored terminal output.
- newPassword: a string variable that holds the new password entered by the user.
- confirmPassword: a string variable that holds the password confirmation entered by the user.
- newUsername: a string variable that holds the new username entered by the user.
- response: a set containing the possible responses ("yes" or "no") to a confirmation prompt.
- msg: a string variable that holds a confirmation prompt.
- confirm: a string variable that holds the user's confirmation response ("yes" or "no").
- userInput: a string variable that holds the user's input.
- action: a string variable that holds the user's selected action.
- validSet: a set containing the possible values for the action variable.
- arr: an array of elements from which the user can select.
- arrLength: an integer variable that holds the length of the arr array.
- index: an integer variable that holds the index of the selected element in the arr array.
- inpt: a string variable that holds user input to be separated into an array using SeparateInputToList() function.
- objectList: a list of objects from which the user can select.
- objIndex: an integer variable that holds the index of the selected object in the objectList list.
- car: A parameter of the SearchCarMenu function, represents the car to be searched.
- searchOptions: A list that contains the search options for the car in the SearchCarMenu function.
- formattedOptions: A string representation of the searchOptions list, with each element separated by a newline character.
- validate: A set containing the valid actions for the search menu.
- action: A variable that represents the action selected by the user in the SearchCarMenu function.
- inventory: A list that contains all the cars in the inventory in the InventoryMenu function.
- options: A list that contains the options for the inventory menu in the InventoryMenu function.
- isAdmin: A boolean variable that represents whether the current user is an admin or not in the InventoryMenu function.
- carToView: A variable that represents the car selected by the user to view in the InventoryMenu function.
- confirmMsg: A string that contains the confirmation message to be displayed to the user in the InventoryMenu function.
- carToOrder: A variable that represents the car selected by the user to order in the InventoryMenu function.
- validateSet: A set containing the valid actions for the inventory menu in the InventoryMenu function.
- make_model_year: A list containing the make, model, and year of the car to be added in the AddCar function.
- mileage_color: A list containing the mileage and color of the car to be added in the AddCar function.
- engine_transmission: A list containing the engine and transmission of the car to be added in the AddCar function.
- interior_external_design: A list containing the interior and external design of the car to be added in the AddCar function.
- warranty_maintenance: A list containing the warranty and maintenance of the car to be added in the AddCar function.
- info: A dictionary that contains the basic information about the car to be added in the AddCar function.
- performance: A dictionary that contains the performance information about the car to be added in the AddCar function.
- design: A dictionary that contains the design information about the car to be added in the AddCar function.
- protection: A dictionary that contains the protection information about the car to be added in the AddCar function.
- status: A variable that represents the status of the car to be added in the AddCar function.
- creditCard: string variable used to store the credit card number entered by the user.
- customer: an optional argument used in the modifyCustomerDetails function. It is an object of the Customer class that represents a customer in the system.
- options: a list of strings that contains the options displayed to the user in various menus.
- formattedOptions: a string variable that contains the formatted version of options to be displayed to the user.
- action: string variable that stores the user's choice from the menu options.
- validSet: a set of valid input values for the getAction() function.
- customers: a list of Customer objects representing all the customers in the system.
- confirmMessage: a string variable used to store the confirmation message displayed to the user.
- address: a string variable used to store the new home address entered by the user.
- email: a string variable used to store the new email address entered by the user.
- cardNum: a string variable used to store the new credit card number entered by the user.
- user: an object of the User class that represents the user currently logged into the system.
- interface: an object of the Interface or AdminInterface class, depending on whether the user is an admin or not.
- isAdmin: a boolean variable that is True if the user is an admin and False otherwise.

////////////////
ALGORITHM:
- Enumeration: This algorithm is used in the displayData() function to iterate over 
                an array and print out each element in the array along with its index.
- Linear search: This algorithm is used in the validateUsername() function
                 to search through a list of users and check if a new username entered by the user already exists.
- Regular expressions: This algorithm is used in the ValidateUserInput()
                     function to check if the user input matches certain patterns, such as being a number or a valid email address.
- Splitting strings: This algorithm is used in the SeparateInputToList() function 
                    to split a comma-separated string into an array of values.
- The SearchCarMenu function: This function provides two options to the user, one is to order a car and the other is to modify an existing car
     It takes input from the user and then calls either the addOrderMenu function or the modifyCarMenu function depending on the user's choice.
- The InventoryMenu function: This function provides several options to the user, including viewing car details, searching for a car, filtering the inventory,
     making a customer order, and modifying the inventory (if the user is an admin). It takes input from the user and then calls the appropriate function based on the user's choice.
- The AddCar function: This function takes input from the user to create a new car and adds it to the inventory. It prompts the user for various details about the car, such as the VIN,
     make, model, year, mileage, color, price, engine, transmission, interior and exterior design, paint, handling, audio, comfort features, package, warranty, and maintenance. 
    It validates the user's input and creates a dictionary object representing the new car. The interface.AddInventory function is then called to add the new car to the inventory.

////////////////
ERROR HANDLING:
Mainly input validation
- ValueError: if the user inputs a non-integer value for the n variable,
             the program will raise a ValueError and print an error message.
- ZeroDivisionError: if the user inputs 0 as the value for n, the program 
                    will raise a ZeroDivisionError and print an error message.
- FileNotFoundError: if the program cannot find the specified file, 
                     it will raise a FileNotFoundError and print an error message.
- PermissionError: if the program does not have permission to read
                  the specified file, it will raise a PermissionError and print an error message.
- Exception: if any other unexpected error occurs, the program will 
             catch it as a generic Exception and print an error message.
- SearchCarMenu(): if the car is already ordered, it prints an error message and returns.
- InventoryMenu(): if the user inputs an invalid option, it breaks out of the loop.
- AddCar() : if the user inputs an invalid value for make, model, year, mileage, color,
            price, engine, transmission, interior, external design, package, warranty, or maintenance, 
            it prints an error message and prompts the user to input a valid value.



////////////////
'''
####################################################################################################################



from PigeonBox.interface import *
from PigeonBox.session import Auth
from PigeonBox.bcolors import *





''' Command line interface '''
# One-line Description: Display an array of data along with their index.
# General Description: This function takes an array of data and displays each element in the array along with its index. It first checks whether the array is empty, and if it is, it prints a warning message. If the array is not empty,
#   the function iterates through each element in the array and prints it along with its index.
# Typical Calling Examples: displayData([1, 2, 3, 4, 5]) - displays each element in the array along with its index.
#   displayData([]) - prints a warning message since the array is empty.
# Accessibility: This function can be accessed from anywhere in the program as long as it has been imported.
# Function Prototype: def displayData(data) -> None:
def displayData(data):
    if isEmpty(data): return
    #   Iterate through each element in the array and display it along with the index
    for i, val in enumerate(data):
        print(f"{i}: {val}")



# One-line description: Stalls the program and waits for the user to press Enter to continue execution.
# General description: This function halts program execution until the user presses Enter. It is typically used to pause the program after some output is displayed on the console, allowing the user to view the output before the program continues executing.
# Typical calling examples: StallUntilUserInput()
# Accessibility: This function can be accessed from anywhere in the program.
# Function prototype: def StallUntilUserInput():
def StallUntilUserInput():
    """ Stalls the program, waits for user to press enter, 
    to let them view whatever output was printed post an action"""
    input(f"{bcolors.HEADER}\nPress any key to continue {bcolors.ENDC}")




# One-line description: Checks if an array is empty and displays a warning message if it is.
# General description: This function takes an array as an argument and checks if it is empty. If the array is empty, a warning message is displayed using the PrintFormat 
#   function and the function returns True. Otherwise, the function returns False.
# Typical calling examples: isEmpty([]): This will display a warning message saying "No data to display" and return True.
#   isEmpty([1, 2, 3]): This will return False since the array is not empty.
# Accessibility: This function can be accessed by any other function within the same module.
# Function prototype: def isEmpty(arr) -> bool:
def isEmpty(arr):
    if not arr:
        PrintFormat("Warning", "No data to display")
        return True
    return False




# One-line description: Function to validate a new password entered by the user, with confirmation.
# General description: This function prompts the user to enter a new password, and then prompts them to confirm it by entering it again. It then checks if the two passwords
#   match and are not the same as the old password. If the new password is valid, it returns it.
# Typical calling examples:newPassword = validatePassword()
# Accessibility: This function can be accessed from within the program.
# Function prototype:def validatePassword() -> str:
def validatePassword():
    # Get new password from user and return if input is empty
    newPassword = ValidateUserInput('new password')
    if not newPassword: return
    # Get confirmed password from user and return if input is empty
    confirmPassword = ValidateUserInput('confirm password')
    if not confirmPassword: return
    # Check if the passwords match, print error message and return if they don't
    if confirmPassword != newPassword:
        PrintFormat("Invalid", "Passwords do not match")
        return
    # Check if new password is same as old password, print error message and return if they are
    if newPassword == user.getPassword():
        PrintFormat("Invalid", "New password cannot be the same as old password")
        return
    
    return newPassword






''' User account details'''
# One-line description: A function to change the password of a user through an interface.
# General description: The function prompts the user to enter a new password, validates the input,
#   and changes the password of the current user via the interface.
# Typical calling examples: ChangePasswordMenu()
# Accessibility: The function can be accessed through the module or script where it is defined.
# Function prototype: def ChangePasswordMenu() -> None
def ChangePasswordMenu():
    # Get validated new password from user and return if input is empty
    newPassword = validatePassword()
    if not newPassword: return
    # Change user password using the new password
    interface.changeUserPassword(user, newPassword)
    PrintFormat("Success", "Password changed successfully")




# One-line description: Validates user input for a new username and checks if it is already taken or the same as the old username.
# General description: This function takes user input for a new username and performs validation to ensure that the input is not empty and that the new username is not the same as the old username. It also checks if the new username is already taken by another user in the system.
# Typical calling examples:
# new_username = validateUsername()
# Accessibility: This function can be accessed within the program where it is defined and can be called from other functions or methods that require user input for a new username.
# Function prototype:def validateUsername() -> str:
def validateUsername():
    # Get new username from user and return if input is empty
    newUsername = ValidateUserInput('new username')
    if not newUsername: return
    # Check if new username is same as old username, print error message and return if they are
    if newUsername == user.getUsername():
        PrintFormat("Invalid", "New username cannot be the same as old username")
        return
    
    # Check if the new username is already taken, print error message and return if it is
    for usr in interface.ViewUsers():
        if usr.getUsername() == newUsername:
            PrintFormat("Invalid", "Username already taken")
            return
    return newUsername




# One-line description: Changes the username for a user by taking input from the user.
# General description: This function presents a menu to the user to change their username. It prompts the user to enter a new username and validates the input. If the input is empty, the function returns without making any changes. Otherwise, it calls the changeUserUsername function of the interface module to change the user's username and prints a success message.
# Typical calling example: ChangeUsernameMenu()
# Accessibility: This function can be called from any module in the program as long as the interface module is imported.
# Function prototype: def ChangeUsernameMenu():
def ChangeUsernameMenu():
    # Get validated new username from user and return if input is empty
    newUsername = validateUsername()
    if not newUsername: return
    # Change user username using the new username
    interface.changeUserUsername(user, newUsername)
    PrintFormat("Success", "Username changed successfully")






''' Checkers and validators '''
# One-line description: A function to confirm a user's selection through a prompt, returning a boolean value.
# General description: This function displays a warning message with an optional custom message and prompts the user to confirm their selection by typing "y" or "n".
#   It then returns a boolean value based on the user's response.
# Typical calling examples:if ConfirmSelection("Are you sure you want to delete this file?"):,if ConfirmSelection(msg="Do you want to save your changes?"):
# Accessibility: This function can be accessed from anywhere within the program.
# Function prototype:def ConfirmSelection(response = {"y", "yes", "n", "no"}, msg="") -> bool:
def ConfirmSelection(response = {"y", "yes", "n", "no"}, msg="") -> bool:
    if not msg: 
        msg = "\nAre you sure you want to proceed?"
    PrintFormat("Warning", msg)
    confirm = ""
    while True:
        confirm = input("Enter [y/n] to confirm: ").lower()
        if confirm not in response:
            PrintFormat("Invalid", "Answer needs to be y/n")
            continue
        break

    if confirm in {"n", "no"}:
        return False
    PrintFormat("Success", "Action confirmed")
    return True




# One-line Description: Validates user input based on certain conditions like being a number or an email address.
# General Description: This function validates user input based on certain conditions. It takes in three parameters - action (string), isNum (boolean), and isEmail (boolean). The user is prompted to enter input and the function validates it based on the specified conditions.
#   If the input is invalid, an appropriate message is displayed and the user is prompted again.
# Typical Calling Examples:ValidateUserInput(action="age", isNum=True),ValidateUserInput(action="email", isEmail=True)
# Accessibility: This function can be accessed from anywhere in the code.
# Function Prototype:def ValidateUserInput(action="action", isNum=False, isEmail=False):
def ValidateUserInput(action="action", isNum=False, isEmail=False):
    PrintFormat("Important", "\nPress 'q' to exit")
    while True:
        userInput = input(f"Enter {action}: ")
        if userInput.lower() == 'q':
            PrintFormat("Warning", "Exiting\n")
            return
        if not userInput: 
            PrintFormat("Invalid", "Bad input")
            continue
        if isNum and (not userInput.isdigit()):
            PrintFormat("Invalid", "Must be a number")
            continue
        if isEmail and ("@" not in userInput or "." not in userInput):
            PrintFormat("Invalid", "Must be a valid email address")
            continue

        PrintFormat("Success", userInput)
        return int(userInput) if isNum else userInput






''' General helper functions '''
# One-line description: A function to get user input for a valid action from a set of options.
# General description: The function prompts the user to enter an action and checks whether it is a valid option from a given set of valid actions.
#   It keeps asking the user to enter a valid action until they do so or exit by entering 'q'.
# Typical calling examples:action = getAction({"1", "2", "3"}, "Please select an option:"), choice = getAction({"y", "n"}, "Do you want to proceed?")
# Accessibility: The function can be accessed from within the same module.
# Function prototype:def getAction(validSet: set[str] = {"1", "2", "3"}, msg: str = "Enter action:") -> Union[str, None]:
def getAction(validSet={"1", "2", "3"}, msg="Enter action:"):
    PrintFormat("Important", "\nPress 'q' to exit")
    action = input(f"{bcolors.UNDERLINE}{msg}{bcolors.ENDC} ").lower()
    if action == "q":
        PrintFormat("Warning", "Exiting\n")
        return
    if action not in validSet:
        PrintFormat("Invalid", "Invalid action")
        return getAction(validSet, msg)
    return action




# One-line description: Displays an array of elements and prompts the user to pick an index to select an element.
# General description: This function takes an array as input and displays each element in the array with its corresponding index. It then prompts the user to enter an index to select an element from the array.
#   The function validates the user's input and returns the index of the selected element.
# Typical calling examples: index = PickIndex(myArray) where myArray is an array of elements.
# Accessibility: This function is likely to be accessible to all users, as it is a console-based
#   function that uses simple text input and output.
# Function prototype:def PickIndex(arr: list) -> int:
def PickIndex(arr):
    """  Will display elements in array and ask user to pick one, will return the index of the element picked
        Useful for when choosing an element to view or remove. Like when removing a car, this will point to its index in the list
        and the user will be able to remove it by index."""
    arrLength = len(arr) - 1 # length to give user bounds to pick from
    while True:
        displayData(arr) # displays with (index: element) pair
        PrintFormat('Action', '\nPick index from the dislayed list above')
        index = input(f"Enter index [0-{arrLength}] OR enter 'q' to exit: ")
        if index == 'q': 
            PrintFormat("Warning", "Exiting\n")
            return # Exiting
        
        # validation
        if not index.isdigit():
            PrintFormat('Invalid',f"Invalid index! Must be a number")
            StallUntilUserInput()
            continue

        index = int(index)
        if index < 0 or index > arrLength:
            PrintFormat('Invalid',f"Invalid index! Must be greater than 0 AND smaller than maximum length")
            StallUntilUserInput()
            continue

        return index



# One-line description: A function that takes a string and returns an array of substrings separated by commas after stripping whitespace.
# General description: This function takes a string as input and splits it into an array of substrings using commas as a separator.
#   It then removes any leading or trailing whitespace from each substring and returns the resulting array.
# Typical calling example: input_str = "apple, banana, orange" , fruit_list = SeparateInputToList(input_str)
# Accessibility: The function can be accessed from within the same module.
# Function prototype: def SeparateInputToList(inpt: str) -> List[str]:
def SeparateInputToList(inpt):
    """ Takes in a string and returns an array of the string separated by commas"""
    inpt = inpt.split(',')
    inpt = list(map(lambda x: x.strip(), inpt))
    return inpt




# One-line description: Function to select and return an object from a list based on user's input.
# General description: This function takes a list of objects as input, calls the PickIndex function to prompt the user to select an object from the list, and returns the selected object. If the user chooses to exit, it returns None. It also prints a success message for the user.
# Typical calling examples: selected_employee = GetObject(employee_list),selected_car = GetObject(car_list)
# Accessibility: This function is accessible to anyone who has access to the module where it is defined.
# Function prototype: def GetObject(objectList):
def GetObject(objectList):
    """ selects and returns an object once user chooses it from a list (calls on PickIndex)"""
    index = PickIndex(objectList)
    if index is None: return # Exiting

    object = objectList[index]
    PrintFormat('Success',f"\nPicked: {object}") # success message for user
    return object



# One-line description: Update the status of a car in the inventory.
# General description: This function prompts the user to select a new status for a given car in the inventory, then calls the appropriate function from the interface module to update the status of that car.
# Typical calling example: updateCarStatus("Toyota Camry")
# Accessibility: This function can be accessed from within the program.
# Function prototype: def updateCarStatus(car: str) -> None
def updateCarStatus(car):
    statuses = {"0": "available", "1": "ordered", "2": "backorder", "3": "delivered"}
    statusChoice = displayStatusOptions()
    if not statusChoice: 
        return
    
    interface.changeCarStatus(car, statuses[statusChoice])
    PrintFormat("Success", f"{car}")
    




''' helper menus'''
# One-line description: Function to add a new employee with username, password, first name, and last name and grant admin privileges if desired.
# General description: This function prompts the user to enter the necessary information to add a new employee to the system, including username, password, first name, and last name.
#   It also gives the option to grant admin privileges. After validating the input, it calls the AddAdmin() or AddEmployee() function from the interface module to add the employee to the system.
# Typical calling examples: AddEmployee()
# Accessibility: This function is likely to be accessible to admin users of a system that uses the interface module.
# Function prototype:def AddEmployee():
def AddEmployee():
    username = ValidateUserInput("Enter username")
    if not username: return
    password = ValidateUserInput(f"Enter password for new user {username}")
    if not password: return
    firstName = ValidateUserInput("Enter first name")
    if not firstName: return
    lastName = ValidateUserInput("Enter last name")
    if not lastName: return
    addEmployee = None
    confirmMessage = f"Do you wish to grant Admin priviledges to {firstName}?"

    if ConfirmSelection(msg=confirmMessage):
        addEmployee = interface.AddAdmin(username, password, firstName, lastName)
    else:
        addEmployee = interface.AddEmployee(username, password, firstName, lastName)
    # check if employee was added and notify user
    if not addEmployee:
        PrintFormat("Invalid", f"User {firstName, lastName} already exists")
        return
    PrintFormat("Success", f"User {firstName, lastName} successfully added")




# One-line description: A menu function that allows the user to select an employee from a list and remove them after confirmation.
# General description: This function displays a menu to the user that lists all employees and prompts the user to select an employee to delete. After the user selects an employee, they will be asked to confirm their selection before the employee is removed.
#   If the user confirms, the function will remove the employee and notify the user of the success or failure.
# Typical calling examples: RemoveEmployeeMenu()
# Accessibility: This function is accessible to users who have permission to remove employees.
# Function prototype: def RemoveEmployeeMenu() -> None
def RemoveEmployeeMenu():
    """ 'Menu' for removing an employee, will ask user to pick from a list of employees
    and then confirm the selection. If the user confirms, the employee will be removed"""
    employeeToDelete = GetObject(interface.getEmployeeList()) # select employee to delete
    if not employeeToDelete:
        return
    
    confirmMessage = f"\nAre you sure you want to delete {employeeToDelete}."
    confirmMessage += " They may have made orders, which will be deleted with them."
    if not ConfirmSelection(msg=confirmMessage): 
        return
    
    isRemoved = interface.RemoveUser(employeeToDelete) # remove employee
    if not isRemoved: # check if employee was removed and notify user
        PrintFormat("Invalid", "Employee not found")
        return

    PrintFormat("Success", "Removed employee successfully")




# One-line description: Displays the available status options for an inventory and prompts the user to choose one.
# General description: This function displays a list of available status options for an inventory, such as "Available", "Ordered", "BackOrder", and "Delivered".
#   It then prompts the user to choose one of the options.
# Typical calling examples: After displaying the list of status options, this function is often called to obtain the user's selected status for filtering or viewing data.
# Accessibility: This function appears to be accessible to all users.
# Function prototype: def displayStatusOptions() -> Union[str, None]:
def displayStatusOptions():
    options = ["Available", 
               "Ordered", 
               "BackOrder", 
               "Delivered"]
    displayData(options)
    # get user's choice of action
    action = getAction({"0","1","2","3"}, msg="Pick a status:")
    if not action: return
    return action



# One-line description: A function that searches for a car in the inventory based on the model, make, and year entered by the user.
# General description: The CarSearch() function allows the user to search for a car in the inventory by providing the model, make, and year of the car.
#   The function takes the user's input and validates it before searching for a matching car in the inventory. If a matching car
#   is found, the function returns the car's details; otherwise, it informs the user that the car was not found.
# Typical calling examples: CarSearch() can be called when a user wants to search for a specific car in the inventory.
# Accessibility: The function is accessible to any user of the system.
# Function prototype: def CarSearch():
def CarSearch():
    print('\nSearch car in inventory')
    searchMessage = "Enter model, make and year separated by commas\n"
    searchDecision = SeparateInputToList(input(searchMessage))
    if len(searchDecision) != 3: 
        PrintFormat('Invalid', '\nCar not found, make sure you entered the correct model, make and year')
        return

    model, make, year = searchDecision[0], searchDecision[1], searchDecision[2]
    # validate input
    if not year.isdigit(): 
        PrintFormat('Invalid', '\nYear must be a number!')
        return

    car = interface.searchInventory(model, make, int(year))
    # check car exists
    if not car: 
        PrintFormat('Invalid', '\nNo car match :(')
        return
    
    PrintFormat('Success', f"\nCar details:\n{car.getDetails()}")
    return car




# One-line description: Displays a menu to filter cars by their status and displays the filtered data.
# General description: The filterByMenu() function displays a menu that allows users to filter the car inventory by status, which includes available, ordered, backorder, and delivered. It takes user input to select a status, validates the input, and 
#   then calls the ViewByStatus() function of the interface object to retrieve and display the filtered data.
# Typical calling examples: filterByMenu() to display the filter menu and filter cars by their status.
# Accessibility: This function can be accessed from any part of the program as long as the interface object is accessible.
# Function prototype:def filterByMenu()
def filterByMenu():
    filterOptions = ["Filter by Status:",
                     "1. Available",
                     "2. Ordered",
                     "3. Backorder",
                     "4. Delivered"]
    displayFilterOptions = "\n" + "\n".join(filterOptions)
    PrintFormat("Action", displayFilterOptions)
    statuses = {"1": "available", "2": "ordered", "3": "backorder", "4": "delivered"}
    filterDecision = getAction(validSet=set(statuses.keys()))
    # validate input
    if not filterDecision: return

    {"1": displayData,
    "2": displayData,
    "3": displayData,
    "4": displayData}[filterDecision](interface.ViewByStatus(statuses[filterDecision]))




# One-line description: Allows an administrator to add or remove a car from the inventory.
# General description: This function provides a menu that allows the user to select an action to perform on the inventory of cars. The user must be an administrator to use this function. The menu provides two options: add a car or remove a car. If the user selects the add car option, the AddCar() function is called.
#   If the user selects the remove car option, the RemoveCar() function is called.
# Typical calling examples: modifyInventoryMenu(), modifyInventoryMenu(isAdmin=True)
# Accessibility: The user must be an administrator to access this function.
# Function prototype:def modifyInventoryMenu():
def modifyInventoryMenu():
    if not isAdmin: return

    modifyCarOptions = ["1. Add car","2. Remove car"]
    formattedOptions ="\n".join(modifyCarOptions)
    PrintFormat("Action", formattedOptions)
    modifyChoice = getAction(validSet={"1","2"})
    if not modifyChoice: return

    if modifyChoice == '1': 
        AddCar()
        return
    
    RemoveCar()




''' Customer Management helper functions'''
# One-line Description: Adds a new customer with their personal and credit card details to the system.
# General Description: This function prompts the user to input the customer's personal details, including first and last name, email address, credit card number, and home address. It then validates the input and adds the customer to the system using the 'interface.AddCustomer' method. If the customer already exists or if the email address is already in use, the function returns an error message.
#   If the customer is successfully added, the function returns the customer object.
# Typical Calling Example: AddCustomer()
# Accessibility: The function can be accessed from anywhere in the system.
# Function Prototype:def AddCustomer()
def AddCustomer():
    PrintFormat("Important", "\nEnter customer details\n")
    firstName = ValidateUserInput("First Name")
    if not firstName: return
    lastName = ValidateUserInput("Last Name")
    if not lastName: return
    emailAddress = ValidateUserInput("email address", isEmail=True)
    if not emailAddress: return
    creditCard = validateCreditCard()
    if not creditCard: return
    homeAddress = ValidateUserInput("Home address")
    if not homeAddress: return
    # Add the customer to the interface
    customer = interface.AddCustomer(firstName, lastName, creditCard, emailAddress, homeAddress)
    if not customer: 
        PrintFormat("Invalid", "Customer already exists or email already exists")
        return

    PrintFormat('Success',f"\nAdded {customer} with success")
    return customer




# One-line description: Deletes a customer from the system.
# General description: This function takes a customer object to delete as an argument, confirms the deletion with the user, and removes the customer from the interface if the user confirms. If the customer has orders, the function will display a message informing the user of this fact before confirming the deletion.
# Typical calling examples: DeleteCustomerMenu(customer_object)
# Accessibility: This function can be accessed by any user with appropriate privileges.
# Function prototype: def DeleteCustomerMenu(customerToDelete)
def DeleteCustomerMenu(customerToDelete):
    numOrders = len(customerToDelete.orders)
    confirmMessage = f"\nAre you sure you want to delete {customerToDelete}? "
    if numOrders >= 1:
        confirmMessage += f"They have {numOrders} order(s)."

    # Confirm customer deletion with user
    if not ConfirmSelection(msg=confirmMessage): 
        return
    
    #   Remove the customer from the interface
    interface.RemoveCustomer(customerToDelete)
    PrintFormat("Success", "Removed customer successfully")






''' Main menus '''
# One-line description: This function handles the login page and returns the user object if the user is authenticated.
# General description: The function takes care of the login page by prompting the user for their username and password.
#   It uses the Auth() object to authenticate the user. If the user is authenticated, the function returns the user object, 
#   and if the user fails to log in after three attempts, it prints a message indicating the failure.
# Typical calling examples:user = Login()
# Accessibility: The function can be accessed from anywhere in the program.
# Function prototype:def Login():
def Login():
    """ This function takes care of the login page,
      it will ask for username and password and will return the user object if the user is authenticated"""
    PrintFormat("Important", "\nLogin page")
    PrintFormat("Important", "\nWelcome to PigeonBox")
    user, attempt = None, 0
    # give the user 3 attempts to get the correct username and password
    while (user is None and attempt < 3):
        attempt+=1
        if attempt > 1:
            PrintFormat("Warning",f"\nAttempt {attempt}")
        # Employee: gkubach0 2nBztx3qzXV
        # crapinett1 KcZy6yQfn
        usr_name = input("Enter username: ")
        pwd = input("Enter password: ")
        user = Auth().Authenticate(usr_name, pwd)
        
    if not user: # if user is still None, then the user failed all 3 attempts
        PrintFormat("Invalid",'\nFailed all 3 attempts, sorry')
        return
    # user has successfully logged in
    return user



# One-line description: Modifies car status, price, mileage, and warranty plans.
# General description: This function allows the user to modify the status, price, mileage, and warranty plans of a car object passed as a parameter to the function. It presents a menu of options to the user, where they can select the desired action. The available options are changing the car status, price, mileage, or warranty plans.
# Typical calling examples: modifyCarMenu(car1)
# Accessibility: This function can be accessed by any user with access to the application.
# Function prototype: def modifyCarMenu(car)
def modifyCarMenu(car):
    PrintFormat("Success", car)
    options = ["1. Change car status",
               "2. Change car price",
               "3. Change car mileage",
               "4. Change car warranty plans"]
    formattedOptions ="\n".join(options)
    PrintFormat('Action', formattedOptions)
    action = getAction(validSet={"1","2","3","4"})

    if not action: return
    elif action == "1": 
        updateCarStatus(car)
    elif action == "2":
        newPrice = ValidateUserInput("new price", True)
        if not newPrice: return
        interface.changeCarPrice(car, newPrice)
    elif action == "3":
        newMileage = ValidateUserInput("new mileage", True)
        if not newMileage: return
        interface.changeCarMileage(car, newMileage)
    else:
        newWarranty = ValidateUserInput("new warranty plans")
        if not newWarranty: return
        car.UpdateWarranty(newWarranty)




# One-line description: Function to handle searching for cars in the inventory and providing actions for the search result.
# General description: This function prompts the user to search for a car if one is not provided and then presents the user with options to either order the car or modify its attributes. If the car is already ordered, the function informs the user and returns.
# Typical calling examples: SearchCarMenu() or SearchCarMenu(carObj)
# Accessibility: The function can be accessed by any user with access to the module that contains it.
# Function prototype:def SearchCarMenu(car=None):
def SearchCarMenu(car=None):
    # If a car object is not provided, prompt user to search for one.
    if not car:
        car = CarSearch()
    if car is None: return
    searchOptions = ["1. Order car",
                     "2. Modify car (status, price, mileage, warranty plans)"]

    formattedOptions ="\n".join(searchOptions)
    validate = {"1","2"}
    # Print the available options and get the user's choice of action.
    PrintFormat("Action",formattedOptions)
    action = getAction(validSet=validate)
    if not action: return
    if action == "1": 
        # If the car is already ordered, inform the user and return.
        if car.getStatusStr().lower() == "ordered":
            PrintFormat("Invalid", "Car is already ordered")
            return
        # Prompt user to add order and provide list of customers to choose from.
        addOrderMenu(car, interface.getCustomerList())
    else:
        modifyCarMenu(car)




# One-line description: Display an inventory menu with options to view car details, search, filter, make customer orders, and modify inventory (admin-only).
# General description: This function displays an inventory menu with options to interact with the car inventory. It allows users to view car details, search for specific cars, filter cars based on certain criteria, create a customer order for a specific car, and modify the inventory (admin-only).
# Typical calling examples: InventoryMenu()
# Accessibility: This function can be accessed from the main menu of the program or through a specific action in the program.
# Function prototype: def InventoryMenu():
def InventoryMenu():
    PrintFormat("Purple", 'Inventory Menu')
    options = ["0. View car details",
               "1. Search",
               "2. Filter by", 
               "3. Make a customer order"]
    if isAdmin: 
        options.append("4. Add/Remove Cars")

    formattedOptions ="\n".join(options)

    while True:
        inventory = interface.GetInventory()
        displayData(inventory)
        PrintFormat("Action", formattedOptions)
        validateSet = {"0", "1", "2", "3", "4"}
        action = getAction(validateSet)
        if not action: break
        if action == '0':
            carToView = GetObject(inventory)
            print(f"\n{carToView.getDetails()}")
            confirmMsg = f"\nDo you want to modify its details (price, warranty plans, mileage, or status)?"
            if ConfirmSelection(msg=confirmMsg): modifyCarMenu(carToView)
        elif action == '1': SearchCarMenu()
        elif action == '2': filterByMenu()
        elif action == '3': 
            carToOrder = GetObject(inventory)
            if not carToOrder: continue
            addOrderMenu(carToOrder, interface.getCustomerList())
        elif action == '4': modifyInventoryMenu()
            
        StallUntilUserInput()




# One-line description: Function to add a new car to the inventory with user input.
# General description: The function prompts the user to enter various details of a new car such as VIN, make, model, year, color, mileage, price, engine,
#   transmission, interior, external design, paint, handling, audio, comfort features, package, warranty, and maintenance. The user input is then validated and dictionaries are created for the entered details. Finally, the function adds the new car to the inventory.
# Typical calling examples: AddCar()
# Accessibility: The function can be accessed from within the program in which it is defined.
# Function prototype: def AddCar()
def AddCar():
    """ Will get user input for a new car and add it to the inventory"""
    vin = input("Enter new car's VIN: ")
    make_model_year = None
    while True:
        make_model_year = SeparateInputToList(input("Enter make, model, year (Separated by commas): "))
        if len(make_model_year) != 3:
            PrintFormat("Invalid", "Make, Model, Year must be separated by a comma")
            continue
        if not make_model_year[2].isnumeric():
            PrintFormat("Invalid", "Year has to be a number")
            continue
        break
    mileage_color = None
    while True:
        mileage_color = SeparateInputToList(input("Enter mileage, color (Separated by commas): "))
        if len(mileage_color) != 2:
            PrintFormat("Invalid", "Mileage and Color must be separated by a comma")
            continue
        if not mileage_color[0].isnumeric():
            PrintFormat("Invalid", "Mileage has to be a number")
            continue
        if not mileage_color[1].isalpha():
            PrintFormat("Invalid", "Color has to be a string")
            continue
        break

    price = input("Enter price: ")

    # Ensure that the price is a numeric value
    while not price.isnumeric():
        price = input("HAS TO BE NUMERIC! Enter price: ")
    price = int(price)

    engine_transmission = None

    # Prompt the user to enter the engine and transmission of the car
    while True:
        engine_transmission = SeparateInputToList(input("Enter engine, transmission (Separated by commas): "))
        if len(engine_transmission) != 2:
            PrintFormat("Invalid", "Engine and Transmission must be separated by a comma")
            continue
        break
    interior_external_design =None
    while True:
        interior_external_design = SeparateInputToList(input("Enter interior, external design (Separated by commas): "))
        if len(interior_external_design) != 2:
            PrintFormat("Invalid", "Interior and External Design must be separated by a comma")
            continue
        break
    paint = ValidateUserInput("paint")
    handling = [input("Enter handling: ")]
    audio = [input("Enter audio: ")]
    comfort = [input("Enter comfort features: ")]
    package = input("Enter package: ")
    warranty_maintenance = None
    while True:
        warranty_maintenance = SeparateInputToList(input("Enter warranty, maintenance (Separated by commas): "))
        if len(warranty_maintenance) != 2:
            PrintFormat("Invalid", "Warranty and Maintenance must be separated by a comma")
            continue
        break

    # Create dictionaries for car information
    info = {"model": make_model_year[1],
            "make": make_model_year[0],
            "mileage": int(mileage_color[0]),
            "year": int(make_model_year[-1]),
            "color": mileage_color[-1],}
    
    performance = {"engine": engine_transmission[0],
                    "transmission": engine_transmission[-1]}
    
    design = {"interior": [interior_external_design[0]],
              "exterior": [{"paint": paint,"extra": [interior_external_design[-1]]}]}
    
    protection = {"maintenance": warranty_maintenance[1], "warranty": [warranty_maintenance[0]]}
    status = getAction(validSet={"ordered", "available", "backorder", "delivered"}, msg="Enter status: ")
    if not status: return
    add = interface.AddInventory(vin, info=info, performance=performance,comfort=comfort, design=design, protection=protection, price=price, handling=handling, package=package, entertainment=audio, status=status)    
    if add:
        PrintFormat("Success", "Car successfully added")
    else:
        PrintFormat("Invalid", "Car already exists")




# One-line description: Function to remove a car from the inventory.
# General description: This function allows the user to remove a car from the inventory by selecting it from a list of available cars.
#   The user is prompted to confirm their choice, and if confirmed, the car is removed from the inventory.
# Typical calling examples: RemoveCar()
# Accessibility: This function can be accessed by any user with the appropriate permissions.
# Function prototype: def RemoveCar()
def RemoveCar():
    # Check if there are cars in inventory
    if not interface.GetInventory():
        PrintFormat("Invalid", "No cars in inventory")
        return
    
    # Get the car to delete from the user
    car_to_delete = GetObject(interface.GetInventory())

    # Add a confirmation message for the user
    confirm_msg = f"Are you sure you want to delete {car_to_delete}"
    if interface.isCarOrdered(car_to_delete):
        confirm_msg += f" {bcolors.BOLD}it has been ordered{bcolors.ENDC}"

    # Confirm if the user really wants to delete the car
    if not ConfirmSelection(msg=confirm_msg): return

    # Remove the car from the inventory
    rem = interface.RemoveInventory(car_to_delete)
    if rem:
        PrintFormat("Success", "Removed car successfully")
    else:
        PrintFormat("Invalid", "Car not found")



# One-line Description: Allows the user to add a new order to the system by selecting a car and customer.
# General Description: This function prompts the user to confirm if they want to order a particular car and asks for the customer information. It then uses the customer and car information to create an order using the interface's MakeOrder() function. If the order is successful, it prints the order details. If the car is already ordered by someone else, it prompts the user to add the car to backorder instead.
# Typical calling examples:
# addOrderMenu(carToOrder, customers)
# Accessibility: This function can be accessed by calling it from another function or module.
# Function prototype:def addOrderMenu(carToOrder, customers):
def addOrderMenu(carToOrder, customers):
    PrintFormat('Important', f"\nYou are about to order this car: {carToOrder}")
    if not ConfirmSelection(): return
    # check new customer
    customer = None
    confirmMessage = "Is this order for a new customer?"
    if ConfirmSelection(msg=confirmMessage):
        customer = AddCustomer()
    else: # get from old customers 
        if isEmpty(customers): return
        customer = GetObject(customers)

    if not customer: return
    order = interface.MakeOrder(customer, carToOrder, seller=user)
    if not order:
        PrintFormat("Invalid", "Failed to make order. This car has already been ordered by someone else.")
        
        # add to back order
        confirmMessage = "Would you like to add this car to back order instead?" 
        if ConfirmSelection(msg=confirmMessage):
            interface.changeCarStatus(carToOrder, "backorder")
        return
    
    PrintFormat("Success", order)




#   One-line description: Prints the order menu and provides options to add, remove, or view orders.
#   Description: Displays the Order Menu with options to add, remove, or view orders.
#   Typical calling example: OrderMenu()
#   Accessibility: Can be accessed from the main menu by selecting "Orders".
#   Function prototype: def OrderMenu()
def OrderMenu():

    # Print the order menu and options
    PrintFormat('Purple','Order Menu')
    options = ["What would you like to do?",
               "1. Add order",
               "2. Remove order",
               "3. View order details"]
    formattedOptions ="\n".join(options)
    
    # Loop until user chooses to exit
    while True:
        orders = interface.viewOrders()
        inventory = interface.GetInventory()
        customers = interface.getCustomerList()
        displayData(orders)

        # Print options and get user input
        PrintFormat("Action", formattedOptions)
        action = getAction() # get user option choice

        # Exit loop if user doesn't choose an option
        if not action: break

        # Add an order
        if action == "1":
            if isEmpty(inventory): continue
            carToOrder = GetObject(inventory)
            if not carToOrder: break
            addOrderMenu(carToOrder, customers)
        else:
            # checker for empty orders
            if isEmpty(orders): continue

            # Remove an order
            if action == "2":
                orderToRemove = GetObject(orders)
                confirmMessage = f"Are you sure you want to remove this order: {orderToRemove}?"
                if not ConfirmSelection(msg=confirmMessage): break
                if not orderToRemove: break
                interface.UndoOrder(orderToRemove)
            
            # View order details
            else:
                orderToView = GetObject(orders)
                if not orderToView: break
                print(orderToView.orderDetails())
                # change status
                confirmMessage = "Would you like to change the order status?"
                if ConfirmSelection(msg=confirmMessage): updateCarStatus(orderToView.getCar())

        # Wait for user input
        StallUntilUserInput()





#   Description: Displays employee management menu and provides options to view, add or remove employees.
#                   Only accessible by admins.
#   Accessibility: Only accessible by admins.
#   Function Prototype: def ManageEmployeesMenu():
def ManageEmployeesMenu():
    PrintFormat("Purple","Employee Management Menu")
    # if not admin, return as they do not have permissions to view this menu
    if not isAdmin: return
    options = ["1. View Employee details", 
               "2. Add Employee", 
               "3. Remove Employee"]
    formattedOptions ="\n".join(options)
    while True:
        employees = interface.getEmployeeList()
        displayData(employees)
        PrintFormat("Action",f"{formattedOptions}")
        action = getAction()
        if not action: break

        if action == "2": AddEmployee()
        else:
            if isEmpty(employees):  continue
            if action == "1":
                employee = GetObject(employees)
                if not employee: break
                print(employee.getDetails()) # print info like when employee joined
            else:
                RemoveEmployeeMenu()

        StallUntilUserInput() # to get user time to read message before going back to next iteration of menu




#   One-line description: Validates a credit card number.
#   General description: This function prompts 
#                       the user to input a credit card number and validates that it contains 16 digits.
#   Typical calling example: cardNumber = validateCreditCard()
#   Accessibility: This function can be accessed from any module that imports the current module.
#   Function prototype: def validateCreditCard() -> str:
def validateCreditCard():
    creditCard = input('Credit Card #: ')
    while len(creditCard) != 16:
        PrintFormat("Invalid", "Credit card # needs 16 digits and needs to be digits only")
        creditCard = input('Credit Card #: ')
        if not creditCard.isdigit(): continue
    return creditCard




#   One-line Description: Modify details of a customer.
#   General Description: This function allows the user to modify the details of a customer such as home address, email address, and credit card details. If a customer object is not provided as input, it gets the customer object from the list of customers.
#       It displays the available options to the user and takes the appropriate action based on the user's choice.
#   Typical Calling Example: modifyCustomerDetails()
#   Accessibility: This function can be accessed from anywhere within the program.
#   Function Prototype: def modifyCustomerDetails(customer=None)
def modifyCustomerDetails(customer=None):
    # If customer is not given as input, get it from the list of customers
    if not customer:
        customer = GetObject(interface.getCustomerList())
        if not customer: return
    # Display options to the user
    options = ["1. Update home address",
               "2. Update email address",
               "3. Update card details"]
    formattedOptions = "\n".join(options)
    PrintFormat("Action", f"{formattedOptions}")

    # Get user action
    action = getAction()
    if not action: return
    elif action == "1":
         # Get and validate new address from the user
        address = ValidateUserInput("new address")
        if not address: return
         # Call function to change customer address
        interface.changeCustomerAddress(customer, address)
    elif action == "2":
        email = ValidateUserInput("new email", isEmail=True)
        if interface.emailExists(email):
            PrintFormat("Invalid", "Email already exists")
            return
        interface.changeCustomerEmail(customer, email)
    else:
        cardNum = validateCreditCard()
        if not cardNum: return
        interface.changeCustomerCard(customer, cardNum)




#   One-line Description: Displays a menu for managing customers and prompts for actions to perform.
#   general description: This function displays a menu that lists all the customers, and allows the user to perform different actions,
#        such as adding, removing, viewing, or modifying customer details.
#   typical call example: ManageCustomersMenu()
#   Accessibillity: This function can be accessed from any part of the program.
#   function prototype: def ManageCustomersMenu():
def ManageCustomersMenu():
    options = ["1. View Customer details",
               "2. Add Customer", 
               "3. Remove Customer", 
               "4. Edit Customer details"]
    formattedOptions = "\n".join(options)
    while True:
        customers = interface.getCustomerList()
        PrintFormat("Purple","Customer list")
        displayData(customers)
        PrintFormat("Action",f"{formattedOptions}")
        # validate input
        validSet = {"1","2","3","4"}
        action = getAction(validSet=validSet)
        if not action: break
        if action == "2":
            AddCustomer()
        else:
            if isEmpty(customers): continue
            customer = GetObject(customers)
            if not customer: continue

            if action == "1": 
                print(customer.getDetails())
                # update details
                confirmMessage = "Would you like to update customer details?"
                if ConfirmSelection(msg=confirmMessage): modifyCustomerDetails(customer)
            elif action == "3":
                DeleteCustomerMenu(customer)
            else:
                modifyCustomerDetails(customer)

        StallUntilUserInput()




def CarSalesMenu():
    #TODO: Assigned to Dariya
    # display orders
    # Set order statuses to delivered 
    pass



#   One-line description: Account settings menu for changing password, username, and viewing account details.
#   General description: This function presents a menu for users to change their account settings. 
#       It offers three options: changing password, changing username, and viewing account details. 
#       The function loops until the user chooses to exit the menu.
#   Typical calling examples: This function is called when a user selects the "Account Settings" option from the main menu.
#   Accessibility: This function can be accessed by any logged-in user.
#   Function prototype: def AccountSettingsMenu():
def AccountSettingsMenu():
    """ This is the menu users interact with when they want to change their account details such as password or username """
    PrintFormat("Purple","Account settings")
    options = ["1. Change password",
               "2. Change username", 
               "3. View Account Details"]
    formattedOptions ="\n".join(options)
    while True:
        PrintFormat("Action",f"{formattedOptions}")
        action = getAction()
        if not action: break

        if action == "1":
            ChangePasswordMenu()
        elif action == "2":
            ChangeUsernameMenu()
        else:
            print(f"\nUser {user.getUsername()} details:\n{user}")

        StallUntilUserInput()



#   One-line description: Main menu that allows the user to access different sub-menus and account settings.
#   General description: This function presents a main menu to the user, displaying different options based on their user type, and calls other sub-menus based on the user's choice. It also allows users to access their account settings to change their password or username.
#   Typical calling examples: This function is called when the program starts or when the user goes back to the main menu from any of the sub-menus.
#   Accessibility: This function is accessible to all users.
#   Function prototype: def menu():
def menu():
    """ Main menu that the users will first interact with. Calls on otther menus """
    # made these global because almost all menus need it
    # the options are stored as list, so its easier to add/remove options
    options = ["1. Customer Orders",
               "2. Car Sales",
               "3. Car Inventory",
               "4. Manage Customers"]
    # creating the interface based on the user type
    # employees, get the regular interface, whereas admins get the admin interface which gives them more options
    if isAdmin:
        options.append("5. Manage Employees")

    options.append("A: Account settings") # to allow users to change their passwords/username
    formattedOptions = "\n".join(options) # this is what will be displayed to the users from the options list

    while True: # menu start
        PrintFormat("Success", f"\nHi {user.getFirstName()}, what would you like to do?")
        PrintFormat('Action',formattedOptions) # display options to user
        # validating user choice
        action = getAction({"1", "2", "3", "4", "5", "a"})
        if not action: break # if user presses q, break out of the loop and return to main menu
        # calls menu based on user choice
        {"1": OrderMenu,
         "2": CarSalesMenu,
         "3": InventoryMenu,
         "4": ManageCustomersMenu,
         "5": ManageEmployeesMenu,
         "a": AccountSettingsMenu}[action]()
    


#   One-line description: Runs the main program by logging in the user, setting up the interface, and displaying the main menu.
#   General description: The run() function is the main function of the program that runs the login process, sets up the interface, and displays the main menu. It calls the Login() function to log in the user, and depending on the user's category, it sets up either a regular interface or an admin interface. It then calls the menu() function to display the main menu, and logs out the user at the end of the session. If the user chooses to log in again, it starts the login process again.
#   Typical calling examples:run()
#   Accessibility: This function is not accessible as it is part of the program's main code.
#   Function prototype: No arguments or return value.
def run():
    global user 
    global interface
    global isAdmin

    while True:
        user = Login()
        if not user:
            break

        isAdmin = (user.getCategory().lower() == "admin")
        if not isAdmin: 
            interface = Interface()
        else: 
            interface = AdminInterface()
        menu()
        
        interface.LogOut()
        if ConfirmSelection(msg="Would you like to log in again?"): continue
        break
        


if __name__ == "__main__":
    run()

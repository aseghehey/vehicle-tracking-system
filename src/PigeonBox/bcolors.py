####################################################################################################################
'''
////////////////
PROGRAM bcolors:   print colored text in the console for improved readability and clarity.

////////////////
PROGRAMMER: Emanuel Aseghehey emanueldejes@usf.edu

////////////////
VERSION 1: written [day] [month] 2023 by [firstInitial]. [lastName]
REVISION [revision# ex: 1.1]: [day] [month] 2023 by [firstInitial]. [lastName] to [purpose of revision]

////////////////
PURPOSE:
The purpose of the code is to define a class bcolors that contains various color codes that can be used for printing colored text in the console.
The PrintFormat() function is defined to print the text with the specified color and formatting options.
The function takes two parameters: color_status and print_info, where color_status is a string specifying the color option to use,
and print_info is the string that needs to be printed.

The PrintFormat() function uses a dictionary color_options that maps each color status string to its corresponding color code.
The function then selects the appropriate color code based on the color_status parameter and
prints the print_info string with the selected color code using the print() function.

Methods:
None

////////////////
DATA STRUCTURES:
None

////////////////
ALGORITHM:
None

////////////////
ERROR HANDLING:
No explicit error handling.

////////////////
'''
####################################################################################################################

#   define a class the contains various colros to format output text
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#   prints text with colors and formatting
def PrintFormat(color_status, print_info):
    """
        There are various colors and formatting for one to choose from, like bold, underline, etc.
        Works exactly like print() """
    
    # Define a dictionary with color options
    color_options = {"Invalid": bcolors.FAIL, 
                     "Success": bcolors.OKGREEN, 
                     "Action": bcolors.OKBLUE, 
                     "Important": bcolors.BOLD, 
                     "Warning": bcolors.WARNING, 
                     "Purple": bcolors.HEADER, 
                     "Cyan": bcolors.HEADER}
    
    # Set the color based on the color status parameter
    color_status = color_options[color_status]
    # Print the text with the specified color
    print(f"{color_status}{print_info}{bcolors.ENDC}")

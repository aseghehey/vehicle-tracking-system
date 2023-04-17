####################################################################################################################
'''
////////////////
PROGRAM bcolors:   print colored text in the console for improved readability and clarity.

////////////////
PROGRAMMER: Emanuel Aseghehey emanueldejes@usf.edu
DOCUMENTOR: Alexander Ashmore atashmore@usf.edu

////////////////
VERSION 1: written 13 March 2023 by E. Aseghehey
REVISION: revision history can be found on the project GitHub

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
Name: PrintFormat()
    # One-line description: A function that prints formatted text in different colors.
    # General description: The function takes two parameters, the color status and the text to be printed, and prints the text in the specified color. 
    #   It works like the print()
    #   function but allows the user to select from different color and formatting options.
    # Typical calling examples: PrintFormat("Success", "The operation was successful.") would print "The operation was successful." in green text.
        PrintFormat("Important", "Please enter your credentials.")
    #   would print "Please enter your credentials." in bold text.
    # Accessibility: This function can be accessed from within the module where it is defined.
    # Function prototype: def PrintFormat(color_status, print_info)

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
from colorama import init
init()

class bcolors:
    """define a class the contains various colros to format output text"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


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

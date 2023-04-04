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

def PrintFormat(color_status, print_info):
    """ Will print with color and make everything pretty for the user
        There are various colors and formatting for one to choose from, like bold, underline, etc.
        Works exactly like print() """
    
    color_options = {"Invalid": bcolors.FAIL, "Success": bcolors.OKGREEN, "Action": bcolors.OKBLUE, "Important": bcolors.BOLD, "Warning": bcolors.WARNING}
    color_status = color_options[color_status]
    print(f"{color_status}{print_info}{bcolors.ENDC}")

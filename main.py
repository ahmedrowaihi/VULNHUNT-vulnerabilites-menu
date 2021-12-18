import pyfiglet
import os
import json
import sys

# Get Current Execution Path
currentPath =str(__file__.replace("main.py", ""))
# Get All Files
files = [file for file in os.listdir() if file.endswith(".txt")]

# Main Tool Title "VULNHUNT"
print(pyfiglet.figlet_format("VULNHUNT", font="alligator"))

# while loop depends on chosen VUL if no chosen (VUL = "none") it will keep asking to choose a VUL
VUL = "none" # VUL Variable
while VUL == "none":
    print("Choose the vulnerability : \n")
    # For Loop to Print All vulnerabilities names from all texts in the same directory of main.py script
    for idx in range(len(files)):
        # Get File Path For Each
        filePath = open(currentPath + str(files[idx]))
        # Load as json from text and display section "Title"
        print(str(idx) + ".", json.load(filePath)["Title"])
    # out of the loop scope print last option Exit
    print("\n" + str(len(files)), "Exit\n")
    # Try Catch expression to validate that user input must be Integer "رقم"
    try:
        VUL = int(input("Select the number of the vulnerability from the menu: "))
        #     if user choose last option "Exit" then tell him Bye Bye and Break Script
        if VUL == len(files):
            print("\n Bye Bye!!\n")
            VUL = "none"
            break
        # if user choose a number that is not from the VULs list, tell him that it does'nt exist
        # and make him re-Choose
        elif not(VUL in range(0, len(files))):
            print("\nOption Doesn't Exist!\n")
            VUL = "none"
    # if user wrote anything wrong as if not a number "Integer", tell him to input only numbers
    # and make him re-Choose
    except:
         print("Input Must be Numerical only")
         VUL = "none"


# IF ALL ABOVE CODE WENT SUCCESSFULLY
# Second Menu will show up
VUL_SECTION = "none"
# VUL_SECTION describes the examination chosen
# Second Menu will show up as long as no examination chosen (VUL_SECTION ="none") And a VUL is chosen Example (VUL = 0)
# While loop checks if VUL is Integer and No Examination Chosen
while isinstance(VUL, int) and VUL_SECTION == "none":
    # Load Chosen VUL and read text as JSON
    SelectedFileData = json.load(open(currentPath + str(files[VUL])))
    # Print Chosen Vulnerability
    print("Chosen Vulnerability: ", SelectedFileData["Title"])
    # Print Available Examination AND Exit
    print("""
    Choose the examination method :
    1.Describe
    2.Manually
    3.Bypasses
    
    4.Exit/Quit
    
""")
    # Try Catch expression to validate that examination input must be Integer "رقم"
    try:
        VUL_SECTION = int(input("Select the number of the method from the menu: \n"))
        #  if user choose 4 "Exit/Quit" then tell him Bye Bye and Break Script
        if VUL_SECTION == 4:
            print("\n Bye Bye!!\n")
            VUL_SECTION ="none"
            VUL = "none"
            break
        #  if user choose 1 "Describe" then print Describe section of Chosen Vulnerability
        elif VUL_SECTION == 1:
            print("\n", SelectedFileData["Describe"])
            break
        #  if user choose 2 "Manually" then print Manually section of Chosen Vulnerability
        elif VUL_SECTION == 2:
            print("\n", SelectedFileData["Manually"])
            break
        #  if user choose 2 "Bypasses" then print Bypasses section of Chosen Vulnerability
        elif VUL_SECTION == 3:
            print("\n", SelectedFileData["Bypasses"])
            break
        # if user wrote anything wrong as if not a number "Integer", tell him to input only numbers
        # Or Section File Doesn't Exist in text file
        # and make him re-Choose
    except:
        print("Invalid Option Or Not Found Content")
        VUL_SECTION = "none"


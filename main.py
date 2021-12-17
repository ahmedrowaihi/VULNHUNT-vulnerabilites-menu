import pyfiglet
import os
import json
import sys

# Get Current Execution Path
currentPath =str(__file__.replace("main.py", ""))
# Get All Files
files = [file for file in os.listdir() if file.endswith(".json")]
# VUL Variable
VUL = "none"
# Main Tool Title "VULNHUNT"
print(pyfiglet.figlet_format("VULNHUNT", font="alligator"))








while VUL == "none":
    print("Choose the vulnerability : \n")
    # Print All provided vulnerabilities names
    for idx in range(len(files)):
        filePath = open(currentPath + str(files[idx]))
        print(str(idx) + ".", json.load(filePath)["Title"])
    print("\n" + str(len(files)), "Exit\n")
    try:
        VUL = int(input("Select the number of the vulnerability from the menu: "))

        if VUL == len(files):
            print("\n Bye Bye!!\n")
            VUL = "none"
            break
        elif not(VUL in range(0, len(files))):

            print("\nOption Doesn't Exist!\n")
            VUL = "none"
    except:
         print("Incorrect Input")
         VUL = "none"





VUL_SECTION = "none"


while isinstance(VUL, int) and VUL_SECTION == "none":
    SelectedFileData = json.load(open(currentPath + str(files[VUL])))
    print(SelectedFileData["Title"])
    print("""
    Choose the examination method :
    1.Describe
    2.Manually
    3.Bypasses
    
    4.Exit/Quit
    
""")

    try:
        VUL_SECTION = int(input("Select the number of the method from the menu: "))
        if VUL_SECTION == 4:
            print("\n Bye Bye!!\n")
            VUL_SECTION ="none"
            VUL = "none"
            break

        elif VUL_SECTION == 1:
            print(SelectedFileData["Manually"])
            break
        elif VUL_SECTION == 2:
            print(SelectedFileData["Manually"])
            break
        elif VUL_SECTION == 3:
            print(SelectedFileData["Bypasses"])
            break
    except:
        print("Invalid Option Or Not Found Content")
        VUL_SECTION = "none"


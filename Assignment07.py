#------------------------------------------------------#
# Title: Assignment07
# Dev:   Miguel Rovira-Gonzalez
# Date:  March 2nd, 2019
# ChangeLog: (Who, When, What)
#   Miguel Rovira-Gonzalez, March 2nd, Created Script
#-------------------------------------------------------#

import pickle
# Data
list_table = []

# Processing
def pickle_insert():
    # Grabbing User Data and Loading it into the File
    try:
        print("Hi, let's load some data into our binary file. It provides a good way of encrypting your data")
        str_name = input("What is your name? ")
        while (True):
            try:
                str_age = int(input("How old are you? "))
            except ValueError as value:
                print("\nPlease type in a number only for your age.")
                continue
            else:
                break
        dict_input = {"Name": str_name, "Age": str_age}
        print("\n" + str(dict_input))
        print("It's loading time!")

        # Initialize Loading Process
        objFile = open("binary_file.dat", "ab")
        pickle.dump(dict_input, objFile)
        print("Wooooo, loading complete")
        objFile.close()

    except Exception as excep:
        print("Oops, Let's try that again")

def pickle_extract():
    try: # Extracting data from the binary file
        print("\nLet's read this binary file")
        objFile = open("binary_file.dat", "rb")
        while (True):
            # Unloading the binary file into our list table
            try:
                list_table.append(pickle.load(objFile))
            except EOFError as error:
                print("The loop has finished reading the file." + "\n")
                break

        objFile.close()
        # Creating a for loop to extract the key value pairs in our dictionary
        for list in list_table:
            print("Name:", "{}".format(list["Name"]), "\nAge:", "{}".format(list["Age"]))
            print("")

    except Exception as excep:
        print("There is a bug in your code")
        print("Python can help you find it.", excep)

# Input / Output
pickle_insert()
pickle_extract()

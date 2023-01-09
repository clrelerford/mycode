#!/usr/bin/env python3

"""Using the CSV library to work with CSV data. Extra challenge."""

import csv

choice = input("Press 1 to manually create a file or 2 to process csv_users.txt: ")

if choice == "1":
    # prompt the user for the values to use in the file
    url = input("Enter the OS_AUTH_URL: ")
    project_name = input("Enter the OS_PROJECT_NAME: ")
    project_domain = input("Enter the OS_PROJECT_DOMAIN_NAME: ")
    username = input("Enter the OS_USERNAME: ")
    user_domain = input("Enter the OS_USER_DOMAIN_NAME: ")
    password = input("Enter the OS_PASSWORD: ")

    # create the file using the user-specified values
    with open("admin.rc", "w") as rcfile:
        print("export OS_AUTH_URL=" + url, file=rcfile)
        print("export OS_IDENTITY_API_VERSION=3", file=rcfile)
        print("export OS_PROJECT_NAME=" + project_name, file=rcfile)
        print("export OS_PROJECT_DOMAIN_NAME=" + project_domain, file=rcfile)
        print("export OS_USERNAME=" + username, file=rcfile)
        print("export OS_USER_DOMAIN_NAME=" + user_domain, file=rcfile)
        print("export OS_PASSWORD=" + password, file=rcfile)

elif choice == "2":
    # counter to create unique file names
    i = 0

    # open our csv data (we want to loop across this)
    with open("csv_users.txt", "r") as csvfile:
        # loop across our open file line by line
        for row in csv.reader(csvfile):
            i = i + 1 # increase i by 1 (to create unique admin.rc file names)
            filename = f"admin.rc{i}" # this f string says "fill in the value of i"

            # open a file via "with". This file will autoclose when the indentations stop
            with open(filename, "w") as rcfile:
                # use the standard library print function to print our data
                # out to the open file open rcfile (open in write mode)
                print("export OS_AUTH_URL=" + row[0], file=rcfile)
                print("export OS_IDENTITY_API_VERSION=3", file=rcfile)
                print("export OS_PROJECT_NAME=" + row[1], file=rcfile)
                print("export OS_PROJECT_DOMAIN_NAME=" + row[2], file=


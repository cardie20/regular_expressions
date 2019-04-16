#!/usr/bin/env python
import argparse
import passwordTask
from tempfile import mkstemp
from shutil import move
import os

"""
    File name : passwordTask.py
    script that ask the user for a password

"""
__author__ = 'Rebeca Perez Lainez'
__email__ = 'rebeca.perez.lainez@gmail.com'

def task2(database_path):
    """
    Method to query the user for their user name.
    It query the user for their password twice, making sure the user enters the same password
in both instances.
    Allow only three attempts to set a correct password.
   The rules for the password are as follows:
    - It must contain at least one number.
    - It must contain at least one lower case letter.
    - It must contain at least one upper case letter.
    - Allowed characters: numbers, letters, '_' (underscore), '-' (dash) and '.' (fullstop).
    - Other characters are not allowed.
    :return:
    """
    print "Username:"
    user_name = raw_input()
    fh, abs_path = mkstemp()
    with open(abs_path, 'w') as new_file:
        with open(database_path) as old_file:

            #search for the username in the data base
            found = False
            for line in old_file:
                if user_name in line:
                    found = True
                    #always ask for the password
                    new_password = passwordTask.check_valid_password()
                    line_replaced = None
                    if new_password:
                        initial_password = line.split()[1]
                        if initial_password == new_password:
                             print "ERROR : Password has no changed"
                             new_file.write(line)
                        elif ord(new_password[-1])- ord (initial_password[-1]) == 1:
                            print "ERROR: Incremental password are not allowed"
                            new_file.write(line)
                        else:
                            new_file.write(line.replace(initial_password, new_password))

                else:
                    new_file.write(line)
        if not found:
            new_password = passwordTask.check_valid_password()
            if new_password:
                new_file.write(user_name + " " + new_password + "\n")


    os.close(fh)
    #Remove original file
    os.remove(database_path)
    #Move new file
    move(abs_path, database_path)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Find port frequency')
    parser.add_argument('--directory', help='Initial directory')
    args = parser.parse_args()
    if args.directory:
        task2(args.directory)
    else:
        parser.print_help()

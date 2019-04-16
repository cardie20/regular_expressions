#!/usr/bin/env python
import re
"""
    File name : passwordTask.py
    script that ask the user for a password

"""
__author__ = 'Rebeca Perez Lainez'
__email__ = 'rebeca.perez.lainez@gmail.com'

PASSWORD_PATTERN = "^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d_.-]{8,}$"

ERROR_MESSAGE = "The password should have: \n" \
                "- At least one number\n" \
                "- At least one lower case\n" \
                "- At least one upper case\n" \
                "- Allowed characters : numbers, letters, '_','-' and '.'\n" \
                "Try again\n"

def check_valid_password():
    '''
    Method to interact with the user to ask for the password
    The password should have:
        - At least one number
        - At least one lower case
        - At least one upper case
        - Allowed characters : numbers, letters, '_','-' and '.'

    Once the user introduced the password , he/she must confirm the password. It has
    3 attempts to confirm he password otherwise Incorrect password message will be presented
    :return: the Password or None in case it is not valid
    '''

    print "New password:"
    password1 = raw_input()
    attemps = 1

    while not re.match(PASSWORD_PATTERN, password1) and attemps <= 3:
        print ERROR_MESSAGE

        password1 = raw_input()
        attemps += 1

    if attemps < 3:
        print "Confirm password:"
        password2 = raw_input()
        while (password1 != password2) and attemps <= 3:
            print "Password not confirmed, try again:"
            password2 = raw_input()
            attemps += 1

        if attemps > 3:
            print "Password does not match"
            return None
        return password1

    else:
        print "Incorrect password"
        return None

def task1():
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

    check_valid_password()


if __name__ == "__main__":
    task1()






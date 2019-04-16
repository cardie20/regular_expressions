#!/usr/bin/env python
import pexpect
import sys

def test_valid_password_empty_database():
    """
    Evaluates that the user introduce a valid password and is writen in the database/emptydatabase file
    which initialy is empty
    """
    print "------------------"
    print "test_valid_password_empty_database"
    print "------------------"
    ssh_child = pexpect.spawn("python qualcomm/exercise3/passwordTask2.py --directory qualcomm/exercise3/database/emptydatabase")
    ssh_child.logfile = sys.stdout
    ssh_child.expect("Username:\r\n", timeout=10)
    ssh_child.sendline("userA")
    ssh_child.expect_exact("New password:\r\n", timeout=10)
    ssh_child.sendline("miNewPassword1")
    ssh_child.expect("Confirm password:\r\n", timeout=10)
    ssh_child.sendline("miNewPassword1")
    ssh_child.sendline('exit')

def test_valid_password_existing_user():
    """
    Evaluates that the user "a" exisits in "database/existing_user" with password "MyCatcat122"
    When it is required the user introduce a new valid password  "Today.123"
    which is updated in the  "database/existing_user" file
    """
    print "------------------"
    print "test_valid_password_existing_user"
    print "------------------"
    ssh_child = pexpect.spawn("python qualcomm/exercise3/passwordTask2.py --directory qualcomm/exercise3/database/existing_user")
    ssh_child.logfile = sys.stdout
    ssh_child.expect("Username:\r\n", timeout=10)
    ssh_child.sendline("a")
    ssh_child.expect_exact("New password:\r\n", timeout=10)
    ssh_child.sendline("Today.123")
    ssh_child.expect("Confirm password:\r\n", timeout=10)
    ssh_child.sendline("Today.123")
    ssh_child.sendline('exit')


def test_invalid_incremental_password():
    """
     Evaluates that the user "a" exisits in "database/existing_user" with password "Today.123"
     When it is required the user introduce a new valid password  "Today.124" but due to the password is incremental
     it is not updated in the database and the user receives "ERROR: Incremental password are not allowed"
     """
    print "------------------"
    print "test_invalid_incremental_password"
    print "------------------"
    ssh_child = pexpect.spawn("python qualcomm/exercise3/passwordTask2.py --directory qualcomm/exercise3/database/existing_user")
    ssh_child.logfile = sys.stdout
    ssh_child.expect("Username:\r\n", timeout=10)
    ssh_child.sendline("a")
    ssh_child.expect_exact("New password:\r\n", timeout=10)
    ssh_child.sendline("Today.124")
    ssh_child.expect("Confirm password:\r\n", timeout=10)
    ssh_child.sendline("Today.124")
    ssh_child.expect("ERROR: Incremental password are not allowed\r\n", timeout=10)
    ssh_child.sendline('exit')


def test_password_no_change():
    """
    Evaluates that the user "a" exisits in "database/existing_user" with password "Today.123"
    When it is required the user introduce a new valid password  "Today.123" but due to the password has no changed,
    therefore,  it is not updated in the database and the user receives "ERROR : Password has no changed"
    """
    print "------------------"
    print "test_password_no_change"
    print "------------------"
    ssh_child = pexpect.spawn("python qualcomm/exercise3/passwordTask2.py --directory qualcomm/exercise3/database/existing_user")
    ssh_child.logfile = sys.stdout
    ssh_child.expect("Username:\r\n", timeout=10)
    ssh_child.sendline("a")
    ssh_child.expect_exact("New password:\r\n", timeout=10)
    ssh_child.sendline("Today.123")
    ssh_child.expect("Confirm password:\r\n", timeout=10)
    ssh_child.sendline("Today.123")
    ssh_child.expect("ERROR : Password has no changed\r\n", timeout=10)
    ssh_child.sendline('exit')

def test_invalid_password():
    """
    Evaluates that the user "a" exisits in "database/existing_user" with password "Today.123"
    When it is required the user introduce a new invalid password  "asd". after 3 attempts
    Incorrect password message is obtained and not updated in the database"""
    print "------------------"
    print "test_invalid_password"
    print "------------------"
    ssh_child = pexpect.spawn("python qualcomm/exercise3/passwordTask2.py --directory qualcomm/exercise3/database/existing_user")
    ssh_child.logfile = sys.stdout
    ssh_child.expect("Username:\r\n", timeout=10)
    ssh_child.sendline("maa")
    ssh_child.expect_exact("New password:\r\n", timeout=10)
    ssh_child.sendline("ads")
    ERROR_MESSAGE = "The password should have: \r\n" \
                    "- At least one number\r\n" \
                    "- At least one lower case\r\n" \
                    "- At least one upper case\r\n" \
                    "- Allowed characters : numbers, letters, '_','-' and '.'\r\n" \
                    "Try again\r\n"

    ssh_child.expect(ERROR_MESSAGE, timeout=10)
    ssh_child.sendline("asd")
    ssh_child.expect(ERROR_MESSAGE, timeout=10)
    ssh_child.sendline("asd")
    ssh_child.expect(ERROR_MESSAGE, timeout=10)
    ssh_child.sendline("asd")
    ssh_child.expect("Incorrect password\r\n", timeout=10)
    ssh_child.sendline('exit')



if __name__ == "__main__":
  test_valid_password_empty_database()
  test_valid_password_existing_user()
  # test_invalid_incremental_password()
  # test_password_no_change()
  # test_invalid_password()



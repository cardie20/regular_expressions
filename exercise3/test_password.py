#!/usr/bin/env python
import pexpect
import sys

ERROR_MESSAGE = "The password should have: \r\n" \
                "- At least one number\r\n" \
                "- At least one lower case\r\n" \
                "- At least one upper case\r\n" \
                "- Allowed characters : numbers, letters, '_','-' and '.'\r\n" \
                "Try again\r\n"
def test_valid_password():
    '''

    :return:
    '''
    print "------------------"
    print "test_valid_password"
    print "------------------"

    ssh_child = pexpect.spawn("python qualcomm/exercise3/passwordTask.py")
    ssh_child.logfile = sys.stdout
    ssh_child.expect("Username:\r\n", timeout=10)
    ssh_child.sendline("Valid user")
    ssh_child.expect_exact("New password:\r\n", timeout=10)
    ssh_child.sendline("ValidUser1")
    ssh_child.expect("Confirm password:\r\n", timeout=10)
    ssh_child.sendline("ValidUser1")
    ssh_child.sendline('exit')


def test_invalid_password():
    print "------------------"
    print "test_invalid_password"
    print "------------------"

    ssh_child = pexpect.spawn("python qualcomm/exercise3/passwordTask.py")
    ssh_child.logfile = sys.stdout
    ssh_child.expect("Username:\r\n", timeout=10)
    ssh_child.sendline("Reb")
    ssh_child.expect_exact("New password:\r\n", timeout=10)
    ssh_child.sendline("Reb")
    ssh_child.expect(ERROR_MESSAGE, timeout=10)
    ssh_child.sendline("Reb")
    ssh_child.expect(ERROR_MESSAGE, timeout=10)
    ssh_child.sendline("Reb")
    ssh_child.expect(ERROR_MESSAGE, timeout=10)
    ssh_child.sendline("Reb")
    ssh_child.expect("Incorrect password\r\n", timeout=10)
    ssh_child.sendline('exit')



if __name__ == "__main__":
  test_valid_password()
  test_invalid_password()



#Qualcomm test homework

    Author: Rebeca Perez Lainez 
    email:  rebeca.perez.lainez@gmail.com


To solve this exercise Python language has been used. All exercise has been developed using python 2.7 and tested in Ubuntu operative system
##Password Task

###Task P1
Write a script that asks a user to set a password. It must:
- Query the user for their user name.
- Query the user for their password twice, making sure the user enters the same password
in both instances.
- Allow only three attempts to set a correct password.

The rules for the password are as follows:
- It must contain at least one number.
- It must contain at least one lower case letter.
- It must contain at least one upper case letter.
- Allowed characters: numbers, letters, '_' (underscore), '-' (dash) and '.' (full stop).
- Other characters are not allowed.

The scripts used to solve this exercise can be found in:

    qualcomm/exercise3/passwordTask.py

and the solution under this method
```python
    def task1(text):
```

The regular expression to check the password is

```python
    "^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d_.-]{8,}$"
```

The test cases proposed to validate the regular expression can be found in  *test_password_regular_expression.py*. It should be executed as follows:
 
    python qualcomm/exercise3/test_password_regular_expression.py
   
This file contains several test cases:

```python
def test_password_pattern()
```
This test case validates the regular expression proposed before with positive and negative tcs:

Positive cases
- MyFile1isBeautiful
- M1n1m3is.
- M1n1m3is.
- M_n-m3is.
   
negative cases
- hello
- 12345678
- __-.-.-.-
- M_n-m3\nis.


To test the interaction with the user to ask the user name and the password, it has been created a several tests cases that uses pexpect python module  to interact with the command line. They can be found in *
test_password.py*. It should be executed as follows

    python qualcomm/exercise3/test_password.py
    

This file contains several test cases:

```python
def test_valid_password()
def test_invalid_password()
```

```python
def test_valid_password():
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

```
###Task P2
Write a script that asks the user for their password:
- Query the user for their user name.
-If the user name is not in the 'company database'(*), then reject it, otherwise continue.
- Query the user for their password.
- If this is the first time that the user has entered their password, ask for it twice.
- If this is not the first time and if it is correct, ask the user to change their password.
(*)Note that we are not expecting a fully featured database design or password changing functionality.
The rules for the password are the same as for Task 1 (above), and in addition:
- Do not allow incremental passwords when changing the password (e.g.
{PasswordRoot}{n} changed into {PasswordRoot}{n+1}, where 'n' is a number).


The scripts used to solve this exercise can be found in "passwordTask2.py" to run this script  

    python passwordTask2.py --directory database/existing_user
    
The test cases proposed for this Use case (UC) can be found test_passwordTask2.py. It should be executed as follows:

   python qualcomm/exercise3/test_passwordTask2.py
    
These testcases uses some database files included under 
exercise3/
    ├── database
       ├── emptydatabase 
       └── existing_user 

The test case proposed are:

```python
test_valid_password_empty_database()
```
This test case evaluates that the user introduce a valid password and is written in the database/emptydatabase file which initially is empty

```python
def test_valid_password_existing_user()
```
Evaluates that the user "a" exist in "database/existing_user" with password "MyCatcat122". When it is required the user introduce a new valid password  "Today.123" which is updated in the  "database/existing_user" file

```python
def test_invalid_incremental_password()
```
Evaluates that the user "a" exist in "database/existing_user" with password "Today.123". When it is required the user introduce a new valid password  "Today.124" but due to the password is incremental it is not updated in the database and the user receives "ERROR: Incremental password are not allowed"
  
```python
def test_password_no_change()
```
Evaluates that the user "a" exists in "database/existing_user" with password "Today.123"  When it is required the user introduce a new valid password  "Today.123" but due to the password has no changed,     therefore,  it is not updated in the database and the user receives "ERROR : Password has no changed

```python
def test_invalid_password():
```   
Evaluates that the user "a" exists in "database/existing_user" with password "Today.123" . When it is required the user introduce a new invalid password  "asd". after 3 attempts Incorrect password message is obtained and not updated in the database
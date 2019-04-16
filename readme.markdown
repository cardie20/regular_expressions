#Qualcomm test homework

    Author: Rebeca Perez Lainez 
    email:  


To solve this exercise Python language has been used. All exercise has been developed using python 2.7 and tested in Ubuntu operative system

## Regular Expressions Warm-up Exercise

The scripts used to solve this exercise can be found in:

    qualcomm/exercise1/exercise1.py : script that implements the regular expressions required
    qualcomm/exercise1/test_exercise1.py : Is he test suite that test each use case proposed.

How to run these exercise?

    python qualcomm/exercise1/test_exercise1.py

####Use case W1:

Write a regular expression that only matches the string (wherever it occurs): ABC

Assumptions:
- The word ABC is valid with lower case and capital letters
- Cardinality : ABC must appear one or more
- multiple lines are allowed
- scape characters are allowed at least once

The solution of this Use case (UC) can be found *exercise1.py* script under method: 
    
```python
def find_abc(text):
```
The regular expression used is.

```python
    "ABC+"
```

The test case proposed for this Use case (UC) can be found *test_exercise1.py* script under   method:

```python
def test_find_abc(text):
```
Positive test cases proposed are:
- "Hola ABC me llamo ACBC y leo ABC \n mi ABC "
- "ABC"
- "abc"
- "abcABC"
    
Negative test cases are:
- "Bye"
- "My name"
- "123"    

####Use case W2:
Write a regular expression that matches any of the following, and no others: ABC ACC ADC
AXC

Assumptions :
- lower case and capital letters are allowed.
- The only valid words are: ABC or  ACC or ADC or AXC and its combinations
- ABC or ACC or ADC or AXC can appear one or more
- multiple lines are allowed
- scape characters are allowed


The solution of this Use case (UC) can be found *exercise1.py* script under method: 
    
```python
def match_abc_acc_adc_axc_no_others(text):
```
The regular expression used is.

```python
    "(AB|ACC|ADC|AXC)+"
```
The test case proposed for this Use case (UC) can be found *test_exercise1.py* script under   method:
```python
def test_match_abc_acc_adc_axc_no_others()
```
Positive test cases proposed are:
- "ABC"
- "ACC"
- "ADC"
- "AXC"
- "ABCACCADCAXC"
- "ABCACCADCAXC\nabc"
- "ABCACCADCAXC\tabc"

Negative test cases proposed are:
- "."
- ".ABC"
- "123"

####Use case W3:
Write a regular expression that will only match the following string when it is on a line entirely
by itself: ABC

Assumptions:
- ABC can only appears once
- lower case and capital letters are allowed
- Scape characters are not allowed


The solution of this Use case (UC) can be found *exercise1.py* script under method: 
    
```python
match_abc_entire_line(text):
```
The regular expression used is.

```python
    "^ABC$"
```
The test case proposed for this Use case (UC) can be found *test_exercise1.py* script under   method:
```python
def test_match_abc_entire_line()
```

Positive test cases proposed are:
- "ABC"
- "abc"
Negative test cases
- "\tABC"
- "123"
- "abc\n"
   

####Use case W4:
Write a regular expression that matches only the string that starts with 'A' and ends with 'B',
with anything in-between. Make a note of any assumptions you make.

Assumptions:
- The text must start with A and ends with B
- lower case and capital letters are allowed
- Scape characters are not allowed
- Numbers are allowed
- Speciall characters are allowed



The solution of this Use case (UC) can be found *exercise1.py* script under method: 
    
```python
matches_starts_with_a_ends_with_b(text):
```
The regular expression used is.

```python
    "^A.*B$"
```
The test case proposed for this Use case (UC) can be found *test_exercise1.py* script under   method:
```python
test_matches_starts_with_a_ends_with_b()
```
Positive test cases proposed are:
  exercise1.matches_starts_with_a_ends_with_b("AB"
- "ab"
- "a1b"
- "aHere this expression is validb"
- "ABAB"
Negtive test cases
- "a\n\tb"
- "a*b"
- "Hello"
- "."
- "1"
- "A\nB\n"
- "A\nBAB"


####Use case W5:
Write a regular expression that matches only the string that starts with 'A' and ends with 'B',
with a run of one or more of either 'XO' or 'OX' in-between. Make a note of any assumptions
you make.

Assumptions:
- The text must start with A and ends with B
- XO and/or OX are the only valid values between A and B
- lower case and capital letters are allowed
- Scape characters are not allowed
- OX an XO can appear one or more


The solution of this Use case (UC) can be found *exercise1.py* script under method: 
    
```python
matches_starts_with_a_ends_with_b_xo_ox_in_between(text):
```
The regular expression used is.

```python
    '^A[OX|XO]+B$'
```
The test case proposed for this Use case (UC) can be found *test_exercise1.py* script under   method:
```python
test_matches_starts_with_a_ends_with_b_xo_ox_in_between()
```
Positive test cases proposed are:
- AOXB
- AXOB
- axoB

Negative test cases:
- ax0B
- aB
- axo\nB
- hello

## File Searching for 'port #nnnn'

The scenario:
You have a big directory tree with many files and dire ctories in it. Some of those files have the extension '.inform'. Some of the files with that extension contain instances of the string 'port#nnnn', where nnnn is a hexadecimal number of some length.

Assumptions:
- Each line can only contains one port#nnnn sequence
- Lower letters and capital letters are allowed only for Hexadecimal numbers
- The range of Hexadecimal numbers of 32 bit is [0- 7fffffff]
- The Hexadecimal value can start with 0X 0x 0x or without the 0x
- An Hexadecimal value can not start with 0 , this is not valid : 0x09
    
The scripts used to solve this exercise can be found in:

    qualcomm/exercise2/file_searching.py : script that implements he scenario
    
    qualcomm/exercise1/test_exercise1.py : Is he test suite that test each use case proposed.

How to run these exercise?

    python qualcomm/exercise2/file_searching.py --directory qualcomm/exercise2/test1
    
if any kind of help is needed run this command

    python qualcomm/exercise2/file_searching.py --help

The regular expression used to process each "port#nnnnn" line is

The regular expression used is:

```python
    "^port#((?:0[xX])?(?:[1-7])?[1-9a-fA-F][0-9a-fA-F]{1,6})$"
```
it means:
- Each line must start with "port#"
- (?:0[xX])? : An hexadecimal number optionally can start or not by 0x or Ox

- (?:[1-7])?[1-9a-fA-F][0-9a-fA-F]{1,6}):  A 32 bit hexadecimal allows values from [0,7fffffff].

The solution of this exercise can be found in

    python qualcomm/exercise2/file_searching.py
 

The test cases proposed for this Use case (UC) can be found *test_file_searching.py*. It should be executed as follows:
 
 python qualcomm/exercise2/test_file_searching.py
 
This file contains several test cases:

```python
def test_port_hexadecimal_pattern()
```
This test case validates the regular expression proposed before with positive and negative tcs:

Positive cases

- port#1FFFFFFF
- port#0x1fffffff
- port#0x7fffffff
- port#AAAA

negative cases
- port#FFFFFFFF
- port#X12
- port#0x01
- PORT AAAA
- PORT X12
- port OXAAABB

```python
def test_count_only_inform_files()
```

Directory test1 ("qualcomm/exercise2/test1 contains these files :a.inform , b.inform , c.inform and file.txt

Each of these file contains valid and invalid port#nnnn lines

The test case only counts the ports included in .inform files

```python
def test_count_inform_files()
```

Directory test1 contains these files :a.inform , b.inform , c.inform

Each of this file contains valid and invalid port#nnnn lines

The test case only counts the valid ports included in .inform files

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
- Allowed characters: numbers, letters, '_' (underscore), '-' (dash) and '.' (fullstop).
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

    ssh_child = pexpect.spawn("python passwordTask.py")
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

    ssh_child = pexpect.spawn("python passwordTask.py")
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

    python test_passwordTask2.py
    
These testcases uses some database files included under 
exercise3/
    ├── database
       ├── emptydatabase 
       └── existing_user 

The test case proposed are:

```python
test_valid_password_empty_database()
```
This test case evaluates that the user introduce a valid password and is writen in the database/emptydatabase file which initialy is empty

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
Evaluates that the user "a" exisits in "database/existing_user" with password "Today.123"  When it is required the user introduce a new valid password  "Today.123" but due to the password has no changed,     therefore,  it is not updated in the database and the user receives "ERROR : Password has no changed

```python
def test_invalid_password():
```   
Evaluates that the user "a" exisits in "database/existing_user" with password "Today.123" . When it is required the user introduce a new invalid password  "asd". after 3 attempts Incorrect password message is obtained and not updated in the database
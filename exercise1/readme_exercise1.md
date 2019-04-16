#Qualcomm test homework

    Author: Rebeca Perez Lainez 
    email:  rebeca.perez.lainez@gmail.com


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
- Special characters are allowed



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
- "aHere this expression is valid"
- "ABAB"
Negative test cases
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

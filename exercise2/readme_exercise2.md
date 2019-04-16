#Qualcomm test homework

    Author: Rebeca Perez Lainez 
    email:  rebeca.perez.lainez@gmail.com


To solve this exercise Python language has been used. All exercise has been developed using python 2.7 and tested in Ubuntu operative system

## File Searching for 'port #nnnn'

The scenario:
You have a big directory tree with many files and directories in it. Some of those files have the extension '.inform'. Some of the files with that extension contain instances of the string 'port#nnnn', where nnnn is a hexadecimal number of some length.

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
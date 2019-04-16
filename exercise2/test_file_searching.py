#!/usr/bin/env python
import re
import file_searching

"""
    File name : test_file_searching.py
    script that implements the test of file searching use case

"""
__author__ = 'Rebeca Perez Lainez'
__email__ = 'rebeca.perez.lainez@gmail.com'



def assert_positive_text (text):
    assert re.match(file_searching.PORT_HEXADECIMAL_PATTERN, text),( text + " not matched")
def assert_negative_text (text):
    assert not re.match(file_searching.PORT_HEXADECIMAL_PATTERN, text), text + " not matched"

def test_port_hexadecimal_pattern():
    """
    Method in charged of test regular expression file_searching.PORT_HEXADECIMAL_PATTERN
    :param text: text to be tested
    """
    #positive cases
    assert_positive_text("port#1FFFFFFF")
    assert_positive_text("port#0x1fffffff")
    assert_positive_text("port#0x7fffffff")
    assert_positive_text("port#AAAA")
    # negative cases
    assert_negative_text("port#FFFFFFFF")
    assert_negative_text("port#X12")
    assert_negative_text("port#0x01")
    assert_negative_text("PORT AAAA")
    assert_negative_text("PORT X12")
    assert_negative_text("port OXAAABB")

def test_count_only_inform_files():
    """
    Directory test1 contains these files :a.inform , b.inform , c.inform and file.txt
    Each of this file contains valid and invalid port#nnnn lines
    The test case only counts the ports included in .inform files
    """
    assert (file_searching.get_port_frequency(file_searching.find_files("qualcomm/exercise2/test1"))
                                              == "port frequency\n"+\
                                                 "AAAA 15\n"+\
                                                 "0x7fffffff 1\n"+\
                                                 "1FFFFFFF 1\n"+\
                                                 "0x1fffffff 1\n"), "Not matches"

def test_count_inform_files():
    """
    Directory test1 contains these files :a.inform , b.inform , c.inform
    Each of this file contains valid and invalid port#nnnn lines
    The test case only counts the valid ports included in .inform files
    """
    assert (file_searching.get_port_frequency(file_searching.find_files("qualcomm/exercise2/test1"))
                                              == "port frequency\n"+\
                                                 "AAAA 15\n"+\
                                                 "0x7fffffff 1\n"+\
                                                 "1FFFFFFF 1\n"+\
                                                 "0x1fffffff 1\n"), "Not matches"


if __name__ == "__main__":
    test_port_hexadecimal_pattern()
    test_count_only_inform_files()
    test_count_inform_files()
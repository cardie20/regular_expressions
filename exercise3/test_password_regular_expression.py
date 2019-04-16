#!/usr/bin/env python
import re
import passwordTask

"""
    File name : test_file_searching.py
    script that implements the test of file searching use case

"""
__author__ = 'Rebeca Perez Lainez'
__email__ = 'rebeca.perez.lainez@gmail.com'

def assert_positive_text (text):
    assert re.match(passwordTask.PASSWORD_PATTERN, text), (text + " not matched")
def assert_negative_text (text):
    assert not re.match(passwordTask.PASSWORD_PATTERN, text), text + " not matched"

def test_password_pattern():
    """
    Method in charged of test regular expression passwordTask.PASSWORD_PATTERN
    :param text: text to be tested
    """
    #positive cases
    assert_positive_text("MyFile1isBeautiful")
    assert_positive_text("M1n1m3is.")
    assert_positive_text("M1n1m3is.")
    assert_positive_text("M_n-m3is.")
    assert_positive_text("R3beca11")
    # negative cases
    assert_negative_text("hello")
    assert_negative_text("12345678")
    assert_negative_text("__-.-.-.-")
    assert_negative_text("M_n-m3\nis.")

if __name__ == "__main__":
    test_password_pattern()

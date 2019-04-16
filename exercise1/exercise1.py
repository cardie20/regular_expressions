#!/usr/bin/env python
"""
    File name : exercise.1py
   script that implements the following five regular expressions tasks:
    W1:  Write a regular expression that only matches the string (wherever it occurs): ABC
    W2:  Write a regular expression that matches any of the following, and no others: ABC ACC ADC
    AXC
    W3: Write a regular expression that will only match the following string when it is on a line entirely
    by itself: ABC
    W4: Write a regular expression that matches only the string that starts with 'A' and ends with 'B',
    with anything in-between. Make a note of any assumptions you make.
    W5: Write a regular expression that matches only the string that starts with 'A' and ends with 'B',
    with a run of one or more of either 'XO' or 'OX' in-between. Make a note of any assumptions
    you make.
"""
__author__ = 'Rebeca Perez Lainez'
__email__ = 'rebeca.perez.lainez@gmail.com'

import re

def display_match(taskId, text, value):
    print "Task {}:\n{}\n{} ".format(taskId, text, value)

def find_abc(text):
    """
    Write a regular expression that only matches the string (wherever it occurs): ABC
        Assumptions:
        - The word ABC is valid with lower case and capital letters
        - Cardinality : ABC must appear one or more
        - multiple lines are allowed
        - scape characters are allowed
        at least once
        :param text: string with the text data to be evaluated
    """
    pattern = "ABC+"
    p = re.compile(pattern, re.IGNORECASE)
    value = "MATCH: {}".format(pattern) if p.search(text) else "NO MATCH"
    display_match("W1", text, value)

def match_abc_acc_adc_axc_no_others(text):
    """
        W2 regular expression that matches any of the following, and no others: ABC ACC ADC AXC
        Assumptions :
        - lower case and capital letters are allowed.
        - The only valid words are: ABC or  ACC or ADC or AXC and its combinations
        - ABC or ACC or ADC or AXC can appear one or more
        - multiple lines are allowed
        - scape characters are allowed
        :param text: string with the text data to be evaluated
    """
    pattern = "(ABC|ACC|ADC|AXC)+"
    p = re.compile(pattern, re.IGNORECASE)
    value = "MATCH: {}".format(pattern) if p.match(text) else "NO MATCH"
    display_match("W2", text, value)

def match_abc_entire_line(text):
    """
        W3:  Write a regular expression that will only match the following string when it is on a line entirely
    by itself: ABC
        Assumptions:
        - ABC can only appears once
        - lower case and capital letters are allowed
        - Scape characters are not allowed
        :param text: string with the text data to be evaluated
        :return:
     """
    pattern = "^ABC$"
    p = re.compile(pattern, re.IGNORECASE)
    value = "MATCH: {}".format(pattern) if p.match(text) else "NO MATCH"
    display_match("W3", text, value)

def matches_starts_with_a_ends_with_b(text):
    """
        Write a regular expression that matches only the string that starts with 'A' and ends with 'B',
        with anything in-between. Make a note of any assumptions you make
        by itself: ABC
        Assumptions:
        - The text must start with A and ends with B
        - lower case and capital letters are allowed
        - Scape characters are not allowed
        - Numbers are allowed
        - Speciall characters are allowed

    :return:
    """
    pattern = "^A.*B$"
    p = re.compile(pattern, re.IGNORECASE)
    value = "MATCH: {}".format(pattern) if p.match(text) else "NO MATCH"
    display_match("W4", text, value)

def matches_starts_with_a_ends_with_b_xo_ox_in_between(text):
    """
       Write a regular expression that matches only the string that starts with 'A' and ends with 'B',
       with a run of one or more of either 'XO' or 'OX' in-between.
    Assumptions:
        - The text must start with A and ends with B
        - XO and/or OX are the only valid values between A and B
        - lower case and capital letters are allowed
        - Scape characters are not allowed
        - OX an XO can appear one or more
    """
    pattern = '^A[OX|XO]+B$'
    p = re.compile(pattern, re.IGNORECASE)
    value = "MATCH: {}".format(pattern) if p.search(text) else "NO MATCH"
    display_match("W5", text, value)

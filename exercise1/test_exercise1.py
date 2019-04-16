#!/usr/bin/env python
import exercise1
"""
    File name : test_exercise.1py

    Script in charged of test the different use cases
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

def test_find_abc():
    """
        Test use case related with task W1
        Evaluates a text that only matches the string (wherever it occurs): ABC
    """
    # Positive test cases
    exercise1.find_abc("Hola ABC me llamo ACBC y leo ABC \n mi ABC ")
    exercise1.find_abc("ABC")
    exercise1.find_abc("abc")
    exercise1.find_abc("abcABC")
    # Negative test cases
    exercise1.find_abc("Bye")
    exercise1.find_abc("My name")
    exercise1.find_abc("123")

def test_match_abc_acc_adc_axc_no_others():
    """
        Test use case related with task W2
        Evaluates a text that matches any of the following, and no others: ABC ACC ADC
    """
    # Positive test cases
    exercise1.match_abc_acc_adc_axc_no_others("ABC")
    exercise1.match_abc_acc_adc_axc_no_others("ACC")
    exercise1.match_abc_acc_adc_axc_no_others("ADC")
    exercise1.match_abc_acc_adc_axc_no_others("AXC")
    exercise1.match_abc_acc_adc_axc_no_others("ABCACCADCAXC")
    exercise1.match_abc_acc_adc_axc_no_others("ABCACCADCAXC\nabc")
    exercise1.match_abc_acc_adc_axc_no_others("ABCACCADCAXC\tabc")
    # Negative test cases
    exercise1.match_abc_acc_adc_axc_no_others(".")
    exercise1.match_abc_acc_adc_axc_no_others(".ABC")
    exercise1.match_abc_acc_adc_axc_no_others("123")

def test_match_abc_entire_line():
    """
        Test use case related with task W3
        Evaluates a text that will only match the following string when it is on a line entirely
        by itself: ABC
    """
    # Positive test cases
    exercise1.match_abc_entire_line("ABC")
    exercise1.match_abc_entire_line("abc")
    # Negative test cases
    exercise1.match_abc_entire_line("\tABC")
    exercise1.match_abc_entire_line("123")
    exercise1.match_abc_entire_line("abc\n")

def test_matches_starts_with_a_ends_with_b():
    """
        Test use case related with task W4
        Evaluates a text  that matches only the string that starts with 'A' and ends with 'B',
        with anything in-between.
    """
    # Positive test cases
    exercise1.matches_starts_with_a_ends_with_b("AB")
    exercise1.matches_starts_with_a_ends_with_b("ab")
    exercise1.matches_starts_with_a_ends_with_b("a1b")
    exercise1.matches_starts_with_a_ends_with_b("aHere this expression is validb")
    exercise1.matches_starts_with_a_ends_with_b("ABAB")
    # Negaive test cases
    exercise1.matches_starts_with_a_ends_with_b("a\n\tb")
    exercise1.matches_starts_with_a_ends_with_b("a*b")
    exercise1.matches_starts_with_a_ends_with_b("Hello")
    exercise1.matches_starts_with_a_ends_with_b(".")
    exercise1.matches_starts_with_a_ends_with_b("1")
    exercise1.matches_starts_with_a_ends_with_b("A\nB\n")
    exercise1.matches_starts_with_a_ends_with_b("A\nBAB")

def test_matches_starts_with_a_ends_with_b_xo_ox_in_between():
    """
        Test use case related with task W5
        Evaluates a text that matches only the string that starts with 'A' and ends with 'B',
        with a run of one or more of either 'XO' or 'OX' in-between.
    """
    # Positive test cases
    exercise1.matches_starts_with_a_ends_with_b_xo_ox_in_between("AOXB")
    exercise1.matches_starts_with_a_ends_with_b_xo_ox_in_between("AXOB")
    exercise1.matches_starts_with_a_ends_with_b_xo_ox_in_between("axoB")
    # Negative test cases
    exercise1.matches_starts_with_a_ends_with_b_xo_ox_in_between("ax0B")
    exercise1.matches_starts_with_a_ends_with_b_xo_ox_in_between("aB")
    exercise1.matches_starts_with_a_ends_with_b_xo_ox_in_between("axo\nB")
    exercise1.matches_starts_with_a_ends_with_b_xo_ox_in_between("hello")

def main():
    test_find_abc()
    test_match_abc_acc_adc_axc_no_others()
    test_match_abc_entire_line()
    test_matches_starts_with_a_ends_with_b()
    test_matches_starts_with_a_ends_with_b_xo_ox_in_between()

if __name__ == '__main__':
    main()

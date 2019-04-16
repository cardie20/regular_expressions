#!/usr/bin/env python
import os
import re
import collections
import argparse

"""
    File name : file_searching.py
    script that implements the following scenario:
    You have a big directory tree with many files and directories in it.
    Some of those files have the extension '.inform'.
    Some of the files with that extension contain instances of the string 'port#nnnn', where nnnn is a hexadecimal number
    of some length.
"""
__author__ = 'Rebeca Perez Lainez'
__email__ = 'rebeca.perez.lainez@gmail.com'

PORT_HEXADECIMAL_PATTERN = "^port#((?:0[xX])?(?:[1-7])?[1-9a-fA-F][0-9a-fA-F]{1,6})$"

def display_port_frequency(counter):
    """
    Method in charged of print the elements included in counter in he followin format
    :param counter: type of collections.Counter it contains he port value and its frequency
    """
    print get_port_frequency(counter)

def get_port_frequency(counter):
    """
        Method in charged processing the counter elements an assing the processing to a string tha follows this format
        port frequency
        nnnnn frequency
        nnnnn frequency
        nnnnn frequency
        :param counter: type of collections.Counter it contains he port value and its frequency
        :return a string with the suitable format
    """
    port_frequency = "port frequency\n"
    for port, frequency in counter.most_common():
        port_frequency += ("{} {}\n").format(port, frequency)
    return port_frequency

def find_files(initial_path):
    """
    Method to find all files with the .inform extension and count the number of instances
     of each different 'port#nnnn' string , Where nnnn is a four or more digit hexadecimal number to a maxium of 32 bits
    Assumptions:
    - One line can only contains one port#nnnn sequence
    - Lower letters and capital letters are allowed only for hexadecimal numbers
    - The range of Hexadecimal numbers of 32 bit is [0- 7fffffff]
    - The Hexadecimal value can start with 0X 0x 0x or without the 0x
    - An Hexadecimal value can not start with 0 , this is not valid : 0x09
    :param initial_path: the root path of the search
    :return: c type of collections.Counter it stores the port value and its frequency
    """
    c = collections.Counter()
    for path, subdirs, files in os.walk(initial_path):
        for file in files:
            if file.endswith(".inform"):
                f = open( os.path.join(path, file), "r")
                for line in f:
                    #findall will retrieve the groups in this case the port number
                    #match with or without Ox Patern
                    #1 digit = 4 bits 8digits*4bits = 32 bits
                    #0X can be optional
                    #The maximum value for 32 bits is 7fffffff  -->(?:[1-7])?
                    #This 0x01 is not valid [1-9a-fA-F]
                    elements = re.findall(PORT_HEXADECIMAL_PATTERN, line)
                    c = c + collections.Counter(elements)
                f.close()

    return c

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find port frequency')
    parser.add_argument('--directory', help='Initial directory')
    args = parser.parse_args()
    if args.directory:
        display_port_frequency(find_files(args.directory))
    else:
        parser.print_help()

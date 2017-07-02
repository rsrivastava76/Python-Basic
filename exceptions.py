#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 22:28:33 2017

@author: rsrivastava
"""


try:
    fh = open('xlines.txt')
    for line in fh.readlines():
        print(line)
except IOError as e:
    print("Something bad happen ({})".format(e))
except:
    print("error Occured")

print("Next Steps to take")

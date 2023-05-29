#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 11:23:21 2023

@author: francois
"""

def find_language(word):
    match word:
        case "Oui" | "Non":
            print(word, "est français")
        case "No":
            print(word, "est anglais ou espagnol")
        case "Yes":
            print(word, "est anglais")
        case "Si":
            print(word, "est espagnol")
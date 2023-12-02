#!/usr/bin/python3
"""chrismass module"""


def chrismass_tree(n):
    """chrismass tree 2023"""
    
    #from 1- n  length of tree
    for i in range(n):
        #get spaces = n-i - 1 and the trees 2 * i +1
        print(" " * (n - i - 1) + "🎄" * (2 * i + 1))
        #get the trunk
    for i in range(3):
        print(" " * (n - 1) + "🎄🎄")

chrismass_tree(30)





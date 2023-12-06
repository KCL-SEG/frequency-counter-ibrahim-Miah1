"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    
    for item in items:
        if isinstance(item, int):
            item = abs(item)
            item = str(item)
        if item in frequencies:
            frequencies[item] += 1
        else:
            frequencies[item] = 1



    return frequencies

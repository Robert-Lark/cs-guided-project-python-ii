"""
Challenge #8:

Given an integer, write a function that returns "Even" for even integers and
"Odd" for odd integers.

Examples:
- parity(0) -> "Even"
- parity(1) -> "Odd"
- parity(2) -> "Even"
"""

def parity(input_int):
      if input_int % 2: 
        return "odd"
      else:
        return "even"

parity(5)



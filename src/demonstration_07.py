"""
Challenge #7:

Given a string of lowercase and uppercase alpha characters, write a function
that returns a string where each character repeats in an increasing pattern,
starting at 1. Each character repetition starts with a capital letter and the
rest of the repeated characters are lowercase. Each repetition segment is
separated by a `-` character.

Examples:
- repeat_it("abcd") -> "A-Bb-Ccc-Dddd"
- repeat_it("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
- repeat_it("cwAt") -> "C-Ww-Aaa-Tttt"
"""
def repeat_it(input_str):
  arr = [input_str.lower()[x - 1] * x for x in range(1, len(input_str) + 1)]
  new_arr= ["-".join(x[0].upper() + x for x in arr )]

  print(new_arr)
  
repeat_it("cwAt")

#  -> "C-Ww-Aaa-Tttt"


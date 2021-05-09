#!/usr/bin/python3

"""
https://docs.google.com/spreadsheets/d/1YJ72-mjvw_aljgqK123kAZNVCkJgQzygrIH-oyyYqMw/edit?usp=sharing
"""

import sys

u = ["ab", "ov", "eb", "el", "ow", "wi", "th", "in", "be", "yo", "nd", "no", "rt", "hæ", "st", "so", "ut", "hw", "es"]
g = {"ab": "ee", "ov": "b", "eb": "c", "el": "d", "ow": "f", "wi": "g", "hæ": "wh", "th": "i", "in": "j", "be": "k", "yo": "l", "nd": "m", "no": "n", "rt": "o", "st": "p", "so": "q", "ut": "urv", "hw": "xsz", "es": "t", "th": "y", "æ": "ae", "ææ": "ea"}
s = "æ"
ss = "ææ"

def chunks(lst, n):
  """Yield successive n-sized chunks from lst."""
  for i in range(0, len(lst), n):
    yield lst[i:i + n]

def main():
  targ = sys.argv[1]
  targ = targ.replace("est", "es")
  targ = targ.lower()
  if s in targ:
    prev_c = ""
    i = 0
    for c in targ:
      if prev_c == "" and c != s:
        i += 1
        prev_c = c
        continue
      elif prev_c == "" and c == s:
        targ = list(targ)
        targ[0] = ss
        targ = "".join(targ)
      elif c == s:
        if prev_c == "h":
          i += 1
          prev_c = c
          continue
        else:
          targ = list(targ)
          targ[i] = ss
          targ = "".join(targ)
      
      i += 1
      prev_c = c

  targ_l = targ.split()
  out_a = []
  for targ_i in targ_l:
    in_f = ''
    targ_i = chunks(targ_i, 2)
    for c in targ_i:
      if c == ' ' or c == ',' or c == '.' or c == ':' or c == ';' or c == '/' or c == '\\' or c == '=' or c == '*' or c == '`' or c == '(' or c == ')' or c == '[' or c == ']' or c == '-' or c == '—' or c == '?' or c == '!' or c == '+' or c == '"' or c == "'":
        in_f += c
      else:
        in_f += g[c]
    out_a.append(in_f)
  
  out_f = " ".join(out_a)
  print(out_f)


if __name__ == "__main__":
  main()
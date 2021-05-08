#!/usr/bin/python3

"""
https://docs.google.com/spreadsheets/d/1YJ72-mjvw_aljgqK123kAZNVCkJgQzygrIH-oyyYqMw/edit?usp=sharing

hæab hæabthest owrtut yothwihæest ovutest ovabhærtyoel elabutbenoabhwhw
"""

import sys

g = {'a': 'ab','b': 'ov','c': 'eb','d': 'el','e': 'ab','f': 'ow','g': 'wi','h': 'hæ','i': 'th','j': 'in','k': 'be','l': 'yo','m': 'nd','n': 'no','o': 'rt','p': 'st','q': 'so','r': 'ut','s': 'hw','t': 'est','u': 'ut','v': 'ut','w': 'hæ','x': 'hw','y': 'th','z': 'hw','ae': 'æ','ea': 'æ'}
a = 'a'
e = 'e'

def chunks(lst, n):
  """Yield successive n-sized chunks from lst."""
  for i in range(0, len(lst), n):
    yield lst[i:i + n]

def main():
  targ = sys.argv[1]
  targ_l = list(targ)
  out_f = ''
  i = 0
  ccast = False
  for c in targ_l:
    c = c.lower()
    if ccast is True:
      ccast = False
      i += 1
      continue
    elif c == ' ' or c == ',' or c == '.' or c == ':' or c == ';':
      out_f += c
    elif c == a and targ[i+1] == e:
      out_f += g['ae']
      ccast = True
    elif c == e and targ[i+1] == a:
      out_f += g['ea']
      ccast = True
    else:
      out_f += g[c]

    i += 1

  print(out_f)



if __name__ == "__main__":
  main()
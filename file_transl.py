#!/usr/bin/python3

import subprocess

file_i = 'in-file.enc.txt'
text_p = []
text_o = []

with open(file_i) as file_in:
  for line in file_in:
    p_i = line.strip()
    p_i = p_i.replace('\n','')
    text_p.append(p_i)

for l in text_p:
  proc = subprocess.Popen(['./translate.py',l], stdout=subprocess.PIPE)
  while True:
    line = proc.stdout.readline()
    if not line:
      break
    # print(line.decode("utf-8"))
    text_o.append(line.decode("utf-8"))

outtext = "".join(text_o)
print(outtext)

#!/usr/bin/python
import sys
import re

## ref: https://github.com/sirthias/pegdown/issues/160#issuecomment-948796616
def replace_special_chars(str):
  str = str.replace(" ", "-")
  return re.sub(r'[^a-zA-Z0-9-]', "", str)

if len(sys.argv) != 2:
  print('please provide a file name!')
  sys.exit(1) 

f = open(sys.argv[1], "r")
Lines = f.readlines()

# Strips the newline character
for line in Lines:
  if "##" in line: 
    line = line.lstrip("##")
    line = line.lstrip(" ")
    line = line.rstrip("\n")
    print('- [' + line + '](#' + replace_special_chars(line) + ')\n')



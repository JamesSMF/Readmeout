import re
import os

with open("to_be_read.txt", "rt") as f:
   with open("out_text.txt", "wt") as fo:
      for line in f:
         print(line)     # print to console
         re.sub('\'','',line)
         re.sub('\"','',line)
         fo.write(line)

# Read it out
os.system('say -f out_text.txt')

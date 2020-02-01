import re
import os
import time

with open("to_be_read.txt", "rt") as f:
   with open("out_text.txt", "wt") as fo:
      for line in f:
         re.sub('[\'\"<>~`]','',line)
         fo.write(line)

# Open the file
os.system('open to_be_read.txt -a textedit')

# Read it out
time.sleep(0.5)
os.system('say -f out_text.txt')

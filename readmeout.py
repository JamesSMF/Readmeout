import re
import os
import time

with open("to_be_read.txt", "rt") as f:
   with open("out_text.txt", "wt") as fo:
      for line in f:
         line = re.sub('[\'\"<>~`]','',line)
         line = re.sub('\-\s+','',line)
         fo.write(line)

# Open the file
os.system('open to_be_read.txt -a textedit')

# Read it out
time.sleep(1)
os.system('say -f out_text.txt')

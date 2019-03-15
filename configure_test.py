import sys
import os
import re

scriptRes = str()

with open("Makefile", "r") as mfile:
     if not sys.argv[1]:
         print("please provide testname as argv1")
     targetName = sys.argv[1]
     test_command = targetName + ": " + targetName + ".cpp libvm_app.o\n   ${CC} -o $@ $^ -ldl"
     scriptRes = re.sub(r'# tests:', '# tests: \n' + test_command, mfile.read())     

with open("Makefile", "w+") as mfile:
    mfile.truncate(0) # clear the file
    mfile.write(scriptRes)
    

import sys

inputfile = open(sys.argv[1], 'r')
num = 0
for line in inputfile:
    if "SyntaxError" in line:
       num += 1

print("number of syntax error : " + str(num))
inputfile.close()

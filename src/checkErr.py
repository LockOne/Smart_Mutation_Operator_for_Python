import sys

inputfile = open(sys.argv[1], 'r')
errtypes = ["SyntaxError", "IndentationError", "ImportError", "NameError", "ValueError"]
errs = {}
for line in inputfile:
    for errT in errtypes:
        if errT in line:
            if errT in errs.keys():
                errs[errT] += 1
	    else:
	        errs[errT] = 1
            break


for er in errs.keys():
    print(er +  " : " + str(errs[er]))
inputfile.close()

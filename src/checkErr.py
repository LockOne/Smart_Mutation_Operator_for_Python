import sys

inputfile = open(sys.argv[1], 'r')
errs = {}
for line in inputfile:
    if "Error" in line:
        err = line.lstrip()
        err = err[:err.index("Error")]
        if len(err) > 10:
            continue
        if err in errs.keys():
            errs[err] += 1
        else:
            errs[err] = 0
for er in errs.keys():
    print(er + "Error :  " + str(errs[er]))
inputfile.close()

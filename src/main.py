#from generate_operators import generate_operators
import init2
import sys
init2.init()
if len(sys.argv) < 4:
    init2.dirloc = "./"
    init2.mutloc = "./"
else:
    init2.dirloc = sys.argv[2]
    init2.mutloc = sys.argv[3]
dirloc = init2.dirloc + "/"
mutloc = init2.mutloc + "/"
from parsing import parse
from parsing import Token
from compare_token import mutation_operator
from subprocess import call
from random import randrange

#operators = generate_operators()

def parse_operators():
    operators_file = open(dirloc + 'src/mutation_operators.txt','r')
    operators = []
    for line in operators_file:
        before = line.split('  ->  ')[0]
        before = before[1:len(before)-1]
        after = line.split('  ->  ')[1]
        after = after[1:len(after)-1]
        before_tokens = []
        after_tokens = []
        for t in before.split(', '):
            if t == 'str':
                before_tokens.append(Token('string',''))
            elif t[0] == '$':
                before_tokens.append(Token('identifier',t))
            else:
                before_tokens.append(Token('keyword',t))
        for t in after.split(', '):
            if t == 'str':
                after_tokens.append(Token('string',''))
            elif t[0] == '$':
                after_tokens.append(Token('identifier',t))
            else:
                after_tokens.append(Token('keyword',t))
        operators.append(mutation_operator(before_tokens, after_tokens))
    return operators

operators = parse_operators()        
num_lines = sum(1 for line in open(sys.argv[1]))

input_file = open(sys.argv[1], 'r')
mut_index = 0
for i in range(num_lines):
    line = input_file.readline().rstrip()
    if "'''" in line or '"""' in line:
        continue
    line_tokens = parse(line)
    if len(line_tokens) <= 2 or len(line_tokens) >= 10:
        continue
    ideninarow = 0
    numOfiden = 0
    for t in line_tokens:
        if t.type == 'identifier':
            ideninarow += 1
            numOfiden += 1
            if ideninarow == 3:
                continue
        else:
            ideninarow = 0
    if numOfiden >= 4:
        continue

    operator_candidates = []
    for o in operators:
        if o.before == line_tokens:
            operator_candidates.append(o.after)
    operators_to_use = []
    tmp = []
    if len(operator_candidates) > 5:        #pick only 5 operators to perform mutation
        while len(operators_to_use) != 5:
            ind = randrange(0, len(operator_candidates))
            if ind not in tmp:
                operators_to_use.append(operator_candidates[ind])
                tmp.append(ind)
    else:
        operators_to_use = operator_candidates
    for o in operators_to_use:
        ifn = sys.argv[1].split('/')
        infn = ifn[len(ifn)-1]
        outputfile = open(mutloc + 'mutants/'+ infn + "." + str(mut_index),'w')
        inputfile2 = open(sys.argv[1], 'r')
        mut_index += 1
        for ind2 in range(i):
            outputfile.write(inputfile2.readline())
        identifiers = []
        strings = []
        for tok in line_tokens:
            if tok.type == 'identifier':
                identifiers.append(tok.content)
            elif tok.type == 'string':
                strings.append(tok.content)
        afterline = ""
        idindex = 0
        strindex = 0
        tmp = 0
        for tok in o:
            if tok.type == 'string':
                tmp += 1
        if tmp != len(strings):
            outputfile.close()
            inputfil2.close()
            call(['rm', 'mutants/' + infn + "." + str(mut_index-1)])
            continue
        for tok in o:
            if tok.type == 'identifier':
                afterline += identifiers[idindex]
                idindex +=1
            elif tok.type == 'string':
                afterline += strings[strindex]
                strindex += 1
            else:
                afterline += tok.content
        outputfile.write(afterline)
        inputfile2.readline()
        for line2 in inputfile2:
            outputfile.write(line2 )
        inputfile2.close()
        outputfile.close()
print("generated " + str(mut_index) + " muntants")
input_file.close()

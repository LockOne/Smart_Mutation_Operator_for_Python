import init
from parsing import parse
from compare_token import compareTok
import sys

def getRepoNames():
    repo_names_file = open('../resources/repository_names', 'r')
    ret = []
    for line in repo_names_file:
        ret.append(line.strip())
    repo_names_file.close()
    return ret

repo_names = getRepoNames()
new_operators = []
output = open('mutation_operators.txt','w')
init.init()
for repo in repo_names:
    print("repo name : " + repo)
    diff_file = open('../resources/diffs_modified/'+repo+'_diff_modified','r')
    minus = None
    plus = None
    for line in diff_file:
        if minus is None:
            minus = line.strip()
        elif plus is None:
            plus = line.strip()
        
        if plus is not None:
            #parse both minus and plus
            if not (("'''" in minus) or ("'''" in plus)):
                token_minus = parse(minus[1:])
                token_plus = parse(plus[1:])
                new_operator = compareTok(token_minus, token_plus)
                if (new_operator is not None):
                    if (new_operator in new_operators):
                        init.duplicate += 1
                    else:
                        output.write(str(new_operator)+ "\n")
                        new_operators.append(new_operator)
            minus = None
            plus = None
    print("size : " + str(len(new_operators)) );

print("less and equal Than 2 : " + str(init.lessThan2))
print("more and equal than 10 tokens  : " + str(init.moreThan10))
print("same afterToken, beforeToken : " + str(init.same))
print("more and equal than 4 identifiers : " + str(init.moreThan4Iden))
print("3 identifers in a row : " + str(init.inArow))
print("unmatched bracket : " + str(init.unmatchedBracket))
print("duplicate : " + str(init.duplicate))
output.close()

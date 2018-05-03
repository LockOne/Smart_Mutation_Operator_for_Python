from parsing import parse
from compare_token import compareTok

def getRepoNames():
    repo_names_file = open('repository_names', 'r')
    ret = []
    for line in repo_names_file:
        ret.append(line.strip())
    repo_names_file.close()
    return ret

repo_names = getRepoNames()
new_operators = []
for repo in repo_names:
    print("repo name : " + repo)
    diff_file = open('diffs_modified/'+repo+'_diff_modified','r')
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
                if new_operator is not None:
                    new_operators.append(new_operator)
            minus = None
            plus = None
    break
print(new_operators)
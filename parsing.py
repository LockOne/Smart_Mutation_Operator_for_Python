class Token:
    def __init__(self, typ, content = ''):
        self.type = typ
        self.content = content
    def __repr__(self):
        return self.type + " : " + self.content

def getRepoNames():
    repo_names_file = open('repository_names', 'r')
    ret = []
    for line in repo_names_file:
        ret.append(line.strip())
    repo_names_file.close()
    return ret

def getKeywords():
    keyword_file = open('python_language_def', 'r')
    ret = []
    for line in keyword_file:
        if line[0:3] != '###':
            ret.append(line.strip())
    keyword_file.close()
    return ret

repo_names = getRepoNames()

indicator_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                   '0','1','2','3','4','5','6','7','8','9','_',
                   'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
keywords = getKeywords()

def getCandinates(ch):
    if ch in ['+','-','%','=','^','|','&','~']:
        return [ch+'=']
    elif ch in ['/','*','<','>']:
        return [ch+ch, ch+'=',ch+ch+'=']
    elif ch == '!':
        return ['!=']
    else :
        return []
    print(ret)
    return ret

def parse(string):
    #parse them in to tokens.
    token_candinates = []
    indicator = ''
    delayed = ''
    candi_index = 0
    tokens = []
    for ch in string:
        if indicator != '':
            if ch in indicator_alphabet:
                indicator += ch
            else:
                tokens.append(indicator)
                candis = getCandinates(ch)
                indicator = ''
                if len(candis) == 0:
                    if ch == ' ':
                        continue
                    tokens.append(ch)
                else:
                    token_candinates = candis
                    candi_index = 1
                    delayed = ch
        else:
            if candi_index != 0:
                tmp = []
                for t in token_candinates:
                    if len(t) > candi_index and t[candi_index] == ch:
                        tmp.append(t)
                if len(tmp) == 0:
                    tokens.append(delayed)
                    delayed = ''
                    candi_index = 0
                    token_candinates = []
                    if ch in indicator_alphabet:
                        indicator +=ch
                    else:
                        candis = getCandinates(ch)
                        if len(candis) == 0:
                            if ch == ' ':
                                continue
                            tokens.append(ch)
                        else:
                            token_candinates = candis
                            candi_index = 1
                            delayed = ch
                elif len(tmp) == 1:
                    tokens.append(tmp[0])
                    delayed = ''
                    candi_index = 0
                    token_candinates = []
                else:
                    delayed += ch
                    candi_index += 1
                    token_candinates = tmp
            else:
                if ch in indicator_alphabet:
                    indicator += ch
                else:
                    candis = getCandinates(ch)
                    if len(candis) == 0:
                        if ch == ' ':
                            continue
                        tokens.append(ch)
                    else:
                        token_candinates = candis
                        candi_index = 1
                        delayed = ch

    if indicator != '':
        tokens.append(indicator)
    if delayed != '':
        tokens.append(delayed)
    ret = [] 
    string = ''
    curToken = None
    for t in tokens:
        if string != '':
            if string == t:
                ret.append(curToken)
                string = ''
            else:
                curToken = Token(curToken.type, curToken.content+t)
        elif t in ["'", '"']:
            string = t
            curToken = Token('string','')
        else:
            if t in keywords:
                if t == '#':
                    break
                ret.append (Token('keyword',t))
            elif t[0] in numbers:
                ret.append (Token('number',t))
            else:
                ret.append(Token('indicator',t))

    print(ret)
    return ret

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
            minus = None
            plus = None


import init2

class Token:
    def __init__(self, typ, content = ''):
        self.type = typ
        self.content = content
    def __repr__(self):
        if self.type == 'string':
            return 'str'
        return  self.content

    def __eq__(self, token2):
        if (self.type == token2.type):
            if (self.type == 'string'):
                return True
            if (self.content == token2.content):
                return True
        return False
    

def getKeywords():
    keyword_file = open(init2.dirloc + '/resources/rules/python_language_def', 'r')
    #keyword_file = open('../resources/rules/python_language_def','r')
    ret = []
    for line in keyword_file:
        if line[0:3] != '###':
            ret.append(line.strip())
    keyword_file.close()
    return ret

keywords = getKeywords()
identifier_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                   '0','1','2','3','4','5','6','7','8','9','_',
                   'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']

def getCandinates(ch):
    if ch in ['+','-','%','=','^','|','&','~']:
        return [ch+'=']
    elif ch in ['/','*','<','>']:
        return [ch+ch, ch+'=',ch+ch+'=']
    elif ch == '!':
        return ['!=']
    else :
        return []
    return ret

def parse(string):
    #parse them in to tokens.
    token_candinates = []
    identifier = ''
    delayed = ''
    candi_index = 0
    tokens11111 = []
    for ch in string:
        if identifier != '':
            if ch in identifier_alphabet:
                identifier += ch
            else:
                tokens11111.append(identifier)
                candis = getCandinates(ch)
                identifier = ''
                if len(candis) == 0:
                    if ch == ' ':
                        continue
                    tokens11111.append(ch)
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
                    tokens11111.append(delayed)
                    delayed = ''
                    candi_index = 0
                    token_candinates = []
                    if ch in identifier_alphabet:
                        identifier +=ch
                    else:
                        candis = getCandinates(ch)
                        if len(candis) == 0:
                            if ch == ' ':
                                continue
                            tokens11111.append(ch)
                        else:
                            token_candinates = candis
                            candi_index = 1
                            delayed = ch
                elif len(tmp) == 1:
                    tokens11111.append(tmp[0])
                    delayed = ''
                    candi_index = 0
                    token_candinates = []
                else:
                    delayed += ch
                    candi_index += 1
                    token_candinates = tmp
            else:
                if ch in identifier_alphabet:
                    identifier += ch
                else:
                    candis = getCandinates(ch)
                    if len(candis) == 0:
                        if ch == ' ':
                            continue
                        tokens11111.append(ch)
                    else:
                        token_candinates = candis
                        candi_index = 1
                        delayed = ch

    if identifier != '':
        tokens11111.append(identifier)
    if delayed != '':
        tokens11111.append(delayed)
    tokens = [] 
    string = ''
    curToken = None
    for t in tokens11111:
        if string != '':
            if string == t:
                tokens.append(curToken)
                tokens.append(Token('keyword',t))
                string = ''
            else:
                curToken = Token(curToken.type, curToken.content+t)
        elif t in ["'", '"']:
            string = t
            tokens.append(Token('keyword',t))
            curToken = Token('string','')
        else:
            if t in keywords:
                if t == '#':
                    break
                tokens.append (Token('keyword',t))
            elif t[0] in numbers:
                tokens.append (Token('number',t))
            else:
                tokens.append(Token('identifier',t))
    return tokens


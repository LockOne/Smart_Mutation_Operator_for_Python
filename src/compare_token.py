from parsing import Token
import init

class mutation_operator:
    def __init__(self, token1, token2):
        self.before = token1
        self.after = token2

    def __repr__(self):
        return str(self.before) + "  ->  " + str(self.after) 

    def __eq__(self, op2):
        return (self.before == op2.before) and (self.after == op2.after)


def compareTok(tokminus, tokplus):
    identifiers = []
    for t in tokplus:
        if t.type == 'identifier' and (t.content not in identifiers):
            identifiers.append(t.content)

    for t in tokminus:
        if t.type == 'identifier' and (t.content not in identifiers):
            return None

    beforeToks = []
    afterToks = []
    for t in tokplus:
        if t.type == 'identifier':
            beforeToks.append(Token('identifier', '$'+ str(identifiers.index(t.content))))
        else:
            beforeToks.append(t)
    for t in tokminus:
        if t.type == 'identifier':
            afterToks.append(Token('identifier', '$'+str(identifiers.index(t.content))))
        else:
            afterToks.append(t)


    if len(beforeToks) <= 2 or len(afterToks) <= 2:
        init.lessThan2 += 1
        return None

    if len(beforeToks) >= 10 or len(afterToks) >= 10:
        init.moreThan10 += 1
        return None


    if beforeToks == afterToks:
        init.same += 1
        return None


    if len(identifiers) >= 4:
        init.moreThan4Iden += 1
        return None

    idenInARow = 0
    for t in tokplus:
        if t.type == 'identifier' and (t.content not in identifiers):
            idenInARow += 1
            if idenInARow == 3:
                init.inArow += 1
                return None
        else:
            idenInARow = 0
    idenInARow = 0
    for t in tokminus:
        if t.type == 'identifier' and (t.content not in identifiers):
            idenInARow += 1
            if idenInARow == 3:
                init.inArow += 1
                return None
        else:
            idenInARow = 0

    brackets = 0
    for t in tokplus:
        if t.type == 'keyword' and t.content == '{':
            brackets += 1
        elif t.type == 'keyword' and t.content == '}':
            brackets -= 1
            if brackets < 0:
                init.unmatchedBracket += 1
                return None

    if brackets < 0:
        init.unmatchedBracket += 1
        return None

    brackets = 0
    for t in tokminus:
        if t.type == 'keyword' and t.content == '{':
            brackets += 1
        elif t.type == 'keyword' and t.content == '}':
            brackets -= 1
            if brackets < 0:
                init.unmatchedBracket += 1
                return None

    if brackets < 0:
        init.unmatchedBracket += 1
        return None







    return mutation_operator(beforeToks, afterToks)

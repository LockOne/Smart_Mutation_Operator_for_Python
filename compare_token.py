from parsing import Token

class mutation_operator:
    def __init__(self, token1, token2):
        self.before = token1
        self.after = token2

    def __repr__(self):
        return str(self.before) + "  ->  " + str(self.after) 

    def __eq__(self, op2):
        return (self.before == op2.before) and (self.after == op2.after)


def compareTok(tokminus, tokplus):
    indicators = []
    for t in tokplus:
        if t.type == 'indicator' and (t.content not in indicators):
            indicators.append(t.content)
    for t in tokminus:
        if t.type == 'indicator' and (t.content not in indicators):
            return None
    beforeToks = []
    afterToks = []
    for t in tokplus:
        if t.type == 'indicator':
            beforeToks.append(Token('indicator', '$'+ str(indicators.index(t.content))))
        else:
            beforeToks.append(t)
    for t in tokminus:
        if t.type == 'indicator':
            afterToks.append(Token('indicator', '$'+str(indicators.index(t.content))))
        else:
            afterToks.append(t)

    if len(beforeToks) >= 20 or len(afterToks) >= 20:
        return None

    if len(beforeToks) <= 2 or len(afterToks) <= 2:
        return None

    return mutation_operator(beforeToks, afterToks)

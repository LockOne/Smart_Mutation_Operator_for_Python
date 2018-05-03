from parsing import Token

class mutation_operator:
    def __init__(self, token1, token2):
        self.before = token1
        self.after = token2

    def __repr__(self):
        return str(self.before) + "  ->  " + str(self.after) + "\n"


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

    return mutation_operator(beforeToks, afterToks)


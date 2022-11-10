

class FiniteAutomata:

    def __init__(self, filePath):
        self.separator = ','
        self.states = []
        self.alphabet = []
        self.transitionSeparator = '~'
        self.transitions = dict()
        self.finalStates = []
        self.readFromFile(filePath)


    def isDeterministic(self):
        for state in self.states:
            symbols = []
            for (symbol, _) in self.transitions[state]:
                if symbol not in symbols:
                    symbols.append(symbol)

            if len(symbols) != len(self.transitions[state]):
                return False

        return True


    def readFromFile(self, filePath):
        try:
            file = open(filePath, "r")

            self.states = file.readline().replace('\n', '').split(self.separator)

            for state in self.states:
                self.transitions[state] = []

            self.alphabet = file.readline().replace('\n', '').split(self.separator)

            tokens = file.readline().replace('\n', '').split(self.separator)
            for token in tokens:
                tks = token.split(self.transitionSeparator)
                self.transitions[tks[0]].append((tks[1], tks[2]))

            self.finalStates = file.readline().replace('\n', '').split(self.separator)

            # print(self.states)
            # print(self.alphabet)
            # print(self.transitions)
            # print(self.finalStates)

        except Exception as ex:
            print(ex)


    def accepts(self, sequence):
        if not self.isDeterministic():
            return False

        currState = self.states[0]

        for i in range(len(sequence)):
            currSymbol = sequence[i]
            nextTransitions = self.transitions[currState]

            if len(nextTransitions) == 0:
                return False

            OK = False
            for (tranSymbol, tranDest) in self.transitions[currState]:
                if currSymbol == tranSymbol:
                    currState = tranDest
                    OK = True

            if not OK:
                return False

        return True


# fa = FiniteAutomata("..\\OutputFiles\\FAIdentifiers.in")
# print(fa.accepts("idk"))
# print(fa.accepts("1idk"))
# print(fa.accepts("I5154dk"))
#
# fan = FiniteAutomata("..\\OutputFiles\\FAIntegerConstant.in")
# print(fan.accepts("120"))
# print(fan.accepts("+1402"))
# print(fan.accepts("012"))
# print(fan.accepts("1f2"))
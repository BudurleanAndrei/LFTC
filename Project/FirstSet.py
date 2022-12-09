from Grammar import Grammar

class FirstSet:

    def __init__(self, grammar: Grammar):
        self.grammar = grammar
        self.firstSets = dict()

    def getFirstTerminalsForNonTerminal(self, nonTerminal):
        terminals = []

        for production in self.grammar.productions[nonTerminal]:
            firstSymbol = production.split(" ")[0]
            if firstSymbol in self.grammar.terminals:
                terminals.append(firstSymbol)
        return terminals

    def computeFirstConcatenation(self, production):

        tokens = production.split(" ")

        if len(tokens) == 1:
            return self.getFirstOfPrevious(tokens[0])
        return list()

    def computeFirstSets(self):
        for nonTerminal in self.grammar.nonTerminals:
            self.firstSets[nonTerminal] = self.getFirstTerminalsForNonTerminal(nonTerminal)

        sameSets = False
        while not sameSets:
            sameSets = True
            tempFirstSets = dict()

            for nonTerminal in self.grammar.nonTerminals:
                print("----------------------------")
                print(nonTerminal)
                tempFirstSets[nonTerminal] = self.firstSets[nonTerminal]

                for production in self.grammar.productions[nonTerminal]:
                    tempFirstSets[nonTerminal].extend(self.computeFirstConcatenation(production))

                if tempFirstSets != self.firstSets:
                    sameSets = False

            self.firstSets = tempFirstSets



g = Grammar()
g.loadFromFile("..\\OutputFiles\\G1.txt")
g.printNonTerminals()
g.printStartingSymbol()
g.printTerminals()
g.printProductions()

fs = FirstSet(g)
fs.computeFirstSets()
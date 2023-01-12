from Grammar import Grammar
import copy

class Parser:

    def __init__(self, grammar: Grammar):
        self.grammar = grammar
        self.firstTable = dict()
        self.followTable = dict()
        self.eps = "EPS"

    def initTable(self, table: dict, doFollow = False):
        for nonTerminal in self.grammar.nonTerminals:
            table.update({nonTerminal: set()})
        if doFollow:
            table[self.grammar.startingSymbol].add(self.eps)

    def first(self):
        previousTable = dict()
        self.initTable(previousTable)
        self.initTable(self.firstTable)

        done = False
        while not done:
            for nonTerminal in self.firstTable.keys():
                for production in self.grammar.productions[nonTerminal]:
                    productionFirst = production.split(" ")[0]
                    if productionFirst in self.grammar.terminals or productionFirst == self.eps:
                        self.firstTable[nonTerminal].add(productionFirst)
                    else:
                        if self.eps not in previousTable[productionFirst]:
                            self.firstTable[nonTerminal].update(previousTable[productionFirst])
                        else:
                            i = 0
                            while self.eps in previousTable[productionFirst]:
                                self.firstTable[nonTerminal].update(previousTable[productionFirst])
                                i = i + 1
                                if i >= len(production.split(" ")):
                                    break
                                productionFirst = production.split(" ")[i]

            if self.firstTable == previousTable:
                done = True
            previousTable = copy.deepcopy(self.firstTable)

    def follow(self):
        previousFollow = dict()
        self.initTable(previousFollow, True)
        self.initTable(self.followTable, True)

        done = False
        while not done:
            for nonTerminal in self.followTable.keys():
                for production in [item for sublist in self.grammar.productions.values() for item in sublist]:
                    tokens = production.split(" ")
                    if nonTerminal in tokens:
                        if nonTerminal == tokens[-1]:
                            self.followTable[nonTerminal].update(self.followTable[{i for i in self.grammar.productions if production in self.grammar.productions[i]}.pop()])
                            break
                        start = False
                        addFollow = True
                        for token in tokens:
                            if start:
                                if token in self.grammar.terminals:
                                    self.followTable[nonTerminal].add(token)
                                    addFollow = False
                                    break
                                self.followTable[nonTerminal].update(self.firstTable[token])
                                if self.eps not in self.firstTable[token]:
                                    addFollow = False
                                    break
                            if token == nonTerminal:
                                start = True
                        if addFollow:
                            self.followTable[nonTerminal].update(self.followTable[{i for i in self.grammar.productions if production in self.grammar.productions[i]}.pop()])
            if previousFollow == self.followTable:
                done = True
            previousFollow = copy.deepcopy(self.followTable)


# g = Grammar()
# g.loadFromFile("..\\OutputFiles\\G1.txt")
# p = Parser(g)
# p.first()
# print(p.firstTable)
# p.follow()
# print(p.followTable)
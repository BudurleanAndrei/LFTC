from Grammar import Grammar
from Parser import Parser
from copy import deepcopy
from Scanner import Scanner

class Node:
    def __init__(self, symbol, depth):
        self.symbol = symbol
        self.depth = depth
        self.children = list()

class ParsingTable:

    def __init__(self, grammar: Grammar, firstTable, followTable):
        self.grammar = grammar
        self.firstTable = firstTable
        self.followTable = followTable
        self.parseTable = self.generateParseTable()

    def generateParseTable(self):
        table = dict()
        self.firstRule(table)
        self.secondRule(table)
        self.thirdRule(table)
        return table

    def getFirstForRhs(self, rhs):
        first = []
        for token in rhs.split(" "):
            if token in g.terminals:
                first.append(token)
                break
            first.extend(self.firstTable[token])
            if "EPS" not in self.firstTable[token]:
                break
            first.remove("EPS")
        return first

    def firstRule(self, table):
        for (lhs, rhs) in self.grammar.productionCodes:
            tokens = rhs.split(" ")
            code = self.grammar.productionCodes.index((lhs, rhs)) + 1
            if len(tokens) == 1 and tokens[0] == "EPS":
                for elem in self.followTable[lhs]:
                    if elem in table[lhs]:
                        raise Exception("Boom!")
                    if elem != "EPS":
                        table[lhs][elem] = (["EPS"], code)
                    else:
                        table[lhs]["$"] = (["EPS"], code)
            else:
                for elem in self.getFirstForRhs(rhs):
                    val = rhs.split(" ")
                    if "EPS" in val:
                        val.remove("EPS")
                    if lhs not in table.keys():
                        table[lhs] = dict()
                    table[lhs][elem] = (val, code)

    def secondRule(self, table):
        for terminal in self.grammar.terminals:
            if terminal not in table.keys():
                table[terminal] = dict()
            table[terminal][terminal] = (["POP"], -1)

    def thirdRule(self, table):
        if "$" not in table.keys():
            table["$"] = dict()
            table["$"]["$"] = (["ACC"], -2)

    def parseSequence(self, sequence):
        output = list()
        inputStack = list()
        inputStack.extend(sequence)
        inputStack.append("$")
        workingStack = [g.startingSymbol, "$"]

        finished = False

        while not finished:
            inputTop = inputStack[0]
            workingTop = workingStack.pop(0)
            if workingTop in self.parseTable.keys():
                if inputTop in self.parseTable[workingTop].keys():
                    data, action = self.parseTable[workingTop][inputTop]
                    # Pop
                    if action == -1:
                        inputStack.pop(0)
                        # Accept
                    elif action == -2 and inputTop == "$" and workingTop == "$":
                        finished = True
                    else:
                        if "EPS" in data:
                            data.remove("EPS")
                        aux = deepcopy(data)
                        aux.extend(workingStack)
                        workingStack = aux
                        output.append(action)
                else:
                    raise Exception("Boom")
            else:
                raise Exception("Boom")

        return output

    def buildDerivationString(self, sequence):
        str = ""
        for productionNumber in sequence:
            lhs, rhs = self.grammar.productionCodes[productionNumber - 1]
            str += lhs + "->" + rhs + ", "
        return str

    def __str__(self):
        string = ""
        for key in self.parseTable:
            string += key + " : " + str(self.parseTable[key]) + "\n"
        return string

g = Grammar()
g.loadFromFile("..\\OutputFiles\\G1.txt")
p = Parser(g)
p.first()
p.follow()
print("First Table")
print(p.firstTable)
print("Follow Table")
print(p.followTable)
pt = ParsingTable(g, p.firstTable, p.followTable)
print("Parsing Table")
print(pt)

ps = pt.parseSequence(["int", "+", "int"])
print(ps)
print(pt.buildDerivationString(ps))

# scanner = Scanner("..\\Lab1a\\pbtest.ml")
# scanner.scan()
# print(scanner._PIF.getTokens())
# ps = pt.parseSequence(scanner._PIF.getTokens())
# print(ps)
# print(pt.buildDerivationString(ps))
from PIF import PIF
from SymbolTable import SymbolTable
from FiniteAutomata import FiniteAutomata
import re


class Scanner:

    def __init__(self, path):
        self._operators = ["+", "-", "*", "/", "%", "<", ">", "<=", ">=", "==", "="]
        self._separators = [" ", "{", "}", ":", ";", ",", "[", "]", "(", ")", "\n"]  # "\""
        self._reserved_words = ["list", "constant", "otherwise", "maybe", "integer", "bool", "ch", "real",
                                "program", "sk", "ps", "until", "also", "variable", "of", "is", "start", "end"]
        self._file_path = path
        self._symbol_table = SymbolTable()
        self._PIF = PIF()

    def getSymbolTable(self):
        return self._symbol_table

    def getPIF(self):
        return self._PIF

    def tokenize(self):
        try:
            file = open(self._file_path, "r")
            text = file.read()

            for sep in self._separators[1:]:
                text = text.replace(sep, self._separators[0] + sep + self._separators[0])

            tokens = text.split()

            return tokens
        except Exception as ex:
            print(ex)

    def scan(self):
        tokens = self.tokenize()
        error = False
        identifier_pattern = re.compile("^[A-Za-z]+[A-Za-z0-9]*$")
        constant_pattern = re.compile("^\"[A-Za-z0-9]*\"$")
        number_pattern = re.compile("^[0-9]+$")
        faidentif = FiniteAutomata("..\\OutputFiles\\FAIdentifiers.in")
        fanrconst = FiniteAutomata("..\\OutputFiles\\FAIntegerConstant.in")

        for token in tokens:
            if token in self._reserved_words:
                self._PIF.add((token, (-1, -1)), 2)
            elif token in self._operators:
                self._PIF.add((token, (-1, -1)), 3)
            elif token in self._separators:
                self._PIF.add((token, (-1, -1)), 4)
            elif faidentif.accepts(token):
                self._symbol_table.add(token)
                self._PIF.add((token, self._symbol_table.get(token)), 0)
            elif constant_pattern.match(token) or fanrconst.accepts(token):
                self._symbol_table.add(token)
                self._PIF.add((token, self._symbol_table.get(token)), 1)
            else:
                print("Lexical error at token: " + token)
                error = True

        if not error:
            print("Lexically correct!")

        stfile = open("..\\OutputFiles\\ST.out", "w")
        stfile.write(str(self._symbol_table))
        piffile = open("..\\OutputFiles\\PIF.out", "w")
        piffile.write(str(self._PIF))




scanner = Scanner("..\\Lab1a\\pb1.ml")
scanner.scan()
# print(scanner._PIF)
# print(scanner._symbol_table)

# scanner = Scanner("..\\Lab1a\\pb4.ml")
# scanner.scan()
# print(scanner._PIF)

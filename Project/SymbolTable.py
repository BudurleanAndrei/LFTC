class SymbolTable:

    def __init__(self, size = 4093):
        self._array = [None] * size
        self._size = size

    def hash(self, value):
        if type(value) is str:
            sum = 0
            for character in value:
                sum = (sum + ord(character)) % self._size
            return sum
        if type(value) is int:
            return value % self._size

    def add(self, value):
        key = self.hash(value)
        if self._array[key] is not None:
            for elem in self._array[key]:
                if elem == value:
                    return
                else:
                    self._array[key].append(value)

        else:
            self._array[key] = []
            self._array[key].append(value)

    def get(self, value):
        key = self.hash(value)

        if self._array[key] is None:
            return (None, None)

        for elem in self._array[key]:
            if elem is value:
                return (key, self._array[key].index(elem))

        return (None, None)

    def hasValue(self, value):
        key = self.hash(value)

        if self._array[key] is None:
            return False

        for elem in self._array[key]:
            if elem is value:
                return True

        return False

    def __str__(self):
        string = ""

        for i in range(len(self._array)):
            if self._array[i] is None:
                continue

            print(len(self._array[i]))

            for j in range(len(self._array[i])):
                string += self._array[i][j] + " - " + str(self.get(self._array[i][j]))

            string += "\n"

        return string


table = SymbolTable()

table.add("abc")
table.add(110)
table.add("Table")

assert(table.hasValue(110) is True)
assert(table.hasValue("110") is False)
assert(table.hasValue("idk") is False)

assert(table.get(110) == (110, 0))
key, pos = table.get("Table")
assert(table._array[key][pos] == "Table")
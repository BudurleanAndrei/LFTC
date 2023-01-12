class PIF:

    def __init__(self):
        self._tokens = []
        self._type = []

    def add(self, elem, _type):
        self._tokens.append(elem)
        self._type.append(_type)

    def getTokens(self):
        val = list()
        for (lhs, rhs) in self._tokens:
            if self._type[lhs] == 0:
                val.append("identif")
            elif self._type[lhs] == 1:
                val.append("const")
            else:
                val.append(lhs)
        return val

    def __str__(self):
        string = ""

        for i in range(len(self._tokens)):
            if self._type[i] == 0:
                string += "identif"
            elif self._type[i] == 1:
                string += "const"
            else:
                string += self._tokens[i][0]

            # string += " - " + str(self._tokens[i][1])
            string += "\n"

        return string

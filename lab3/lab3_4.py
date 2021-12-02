class StringFormatter():
    def __init__(self, string):
        self.__s = string

    def __str__(self):
        return self.__s
        
    def delwords(self, n):
        self.__s = self.__s.split(' ')
        self.__s = [s for s in self.__s if n < len(s)]
        self.__s = ' '.join(self.__s)
        return self
    
    def zamena(self):
        self.__s = [l if not l.isdigit() else '*' for l in self.__s ]
        self.__s = ''.join(self.__s)
        return self

    def probel(self):
        self.__s = [l+' ' for l in self.__s]
        self.__s = ''.join(self.__s)
        return self

    def sortPoRazmeru(self):
        self.__s = sorted(self.__s.split(), key=len)
        self.__s = ' '.join(self.__s)
        return self

    def sortPoLeks(self):
        self.__s = sorted(self.__s.split(), key=str.lower)
        self.__s = ' '.join(self.__s)
        return self


if __name__ == '__main__':
    s = StringFormatter('Th356is is3 a 23 te32st st64ring f3rom Igor')
    print(s.zamena())
    print(s.delwords(6))
    print(s.sortPoRazmeru())
    print(s.sortPoLeks())
    print(s.probel())

from abc import ABC, abstractmethod
class Taggable(ABC):
    @abstractmethod
    def tag(self):
        pass

class Book(Taggable):
    index = 0
    def __init__(self, a = None, n = None):
        if n == None or a == None:
            raise ValueError
        self.__name = n
        self.__author = a
        Book.index += 1
        self.__index = Book.index

    def __str__(self):
        an = self.__author.split(' ')
        an1 = an[0][0]+'.'
        an2 = an[1]
        return '[{0}] {1}{2} \'{3}\''.format(self.__index, an1,an2, self.__name)

    def tag(self):
        names = self.__name.split(' ')
        names = [n for n in names if n.istitle()]
        return names
            

class Library(object):
    def __init__(self, n, a):
        self.__num = n
        self.__address = a
        self.__books = []
        self.__index = -1

    def __iadd__(self, other):
        self.__books.append(other)
        return self
    
    def __iter__(self):
        return self
    def __next__(self):
        self.__index += 1
        if self.__index < len(self.__books):
            return self.__books[self.__index]
        else:
            self.__index = -1
            raise StopIteration


if __name__ == '__main__':

    lib = Library(1, '51 Some str., NY')
    lib += Book('Charles Dickens', 'David Copperfield')
    lib += Book('Leo Tolstoi', 'War and Peace')

    for book in lib:
        print(book)
        print(book.tag())
    
    

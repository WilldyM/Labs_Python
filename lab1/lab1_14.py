def non_empty(func):
    def wrapper():
        lst = func()
        while lst.count('') > 0:
            lst.remove('')
        while lst.count(None) > 0:
            lst.remove(None)
            return lst
    return wrapper

@non_empty
def get_pages():
    return ['chapter1', '', 'line1', '', 'contents', None]

print(get_pages())

    

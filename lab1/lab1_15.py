def pre_process(a=0.97):
    def _decorator(func):
        def _wrapper(s):
            for sp in range(1, len(s)):
                s[sp] = round(s[sp]-a*s[sp-1],10)
            func(s)
        return _wrapper
    return _decorator

@pre_process(0.93)
def plot_signal(s):
    for sample in s:
        print(sample)

spisok = list(range(1,11))
plot_signal(spisok)

def extra_enumerate(ar):
    ar[0] = (0, ar[0], ar[0], ar[0]/10)
    yield ar[0]
    for i in range(1, len(ar)):
        ar[i] = (i, ar[i], ar[i]+ar[i-1][2], (ar[i]+ar[i-1][2])/10)
        yield ar[i]
    


arr = [1,3,4,2]
for i,elem,cum,frac in extra_enumerate(arr):
    print((elem,cum,frac))

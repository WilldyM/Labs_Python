def get_frames(signal, size, overlap):
    i = 0
    while len(signal) > i:
        yield list(signal[int(i):int(size+i)])
        i+=int(size*overlap)

signal = range(1, 10)
for frame in get_frames(signal, 4, 0.5):
    print(frame)

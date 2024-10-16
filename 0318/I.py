s="学而时习之，不亦说乎？有朋自远方来，不亦乐乎？人不知而不愠，不亦君子乎？"
fh=0
hz=0
for c in s:
    if ord(c)>65000:
        fh=fh+1
    else:
        hz=hz+1
print("A:",fh)
print("B:",hz)
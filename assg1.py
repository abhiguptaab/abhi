def word_count(str):
    count=dict()
    w=str.split()
    for s in w:
        if s in count:
            count[s]+=1
        else:
            count[s]=1
    return count
d=word_count('we are we are in te in')

e=sorted(d.items())
l=''.join(d)
print(d)
print(e)
print(l)



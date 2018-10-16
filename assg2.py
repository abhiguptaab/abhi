A=set({1,3,5,7,8})

print (2 in A) 
print (5 in A)

print (len(A))

print ("Union:")
print ({1,3,5}|{7,8})

print ("intersection:")
print ({1,3,5} & {3,5,8})

print ("difference:",{1,3,5,7,8}-{1,3,5})

print ("symmetric difference:",{1,3,5,7,8}^{7,8})
A.add(9)
print(A)

A.copy()
print(A)

A.discard(9)
print(A)

A.pop()
print(A)

A.remove(5)
print(A)

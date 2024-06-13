s={2,3,4,2,6}
print(s)
info={"shahzad",19,False,2.3,19}
print(info)
me =set()
print(type(me))
for value in info:
 print(value)

 #method of sets

s1={2,3,4,}
s2={3,4,6,7}
print(s1.intersection(s2)) #we also use same process for union here
s1.update(s2)
print(s1,s2)

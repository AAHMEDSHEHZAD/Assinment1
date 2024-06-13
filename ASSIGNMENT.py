#string
name="shahzad"
print(name)

#type casting 
z="3"
x="8"
print((int(z)-int(x)))
print((int(z)+int(x)))
print((int(z)*int(x)))
#COMPLEX
d=2-3
e=5-4
print(complex(d,e))
#int
A=23
B=21
print(A+B)
#input using int,float,complex
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print(a-b)
a=float(input("Enter first number:"))
b=float(input("Enter second number:"))
print(a-b)
a=complex(input("Enter first number:"))
b=complex(input("Enter second number:"))
print(a-b)
#LIST
list=[2,3,4,5,3,5]
list[2]=25
print(list)
print(list[4])
print(type(list))

#TUPLE

tup=(2,2,3,4,344,5444,54,5,5,)
print(len(tup))
print(type(tup),tup)
if 5444 in tup:
    print("yes 5444 is in tup")
    tup2=tup[0:4]
    print(tup2)
    #DIC
dic={
        "name":"AHMED SHEHZAD",
        "class":"BS computer science",
        "age":19
    }
print(dic)
print(type(dic))
#SETS
s={1,2,3,4,5,6,3,6}
print(s)
print(type(s))

letter =" my name is {1} i am from {0} "
name = "shahzad"
country="pakistan"
print(letter.format(country,name))
print(f"my name is {name} i am from {country}")

price=23.99999
txt = f"For only {price:.2f} dollars"
print(txt)

#new update 
print(type(f"{2*30}"))
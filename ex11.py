print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

name = input("What's your surname? ")
print(f"""Nice to meet you Mr. {name}, we've been expecting you. 
       It's been a long time since your last visit.""")

print("When where you born?", end=' ' )
born_in = input()
year = 2017
years_old = year - int(born_in)

print(f"So you are approximately {years_old} years-old")

#Define variable formatter
formatter = "{} {} {} {}"

#Turn formatter variable into function
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))

#I first forgot to write this line of code
print(formatter.format(formatter, formatter, formatter, formatter))

#This line prints the four strings one following the other
print(formatter.format(
		"Try your",
		"Own text here",
		"Maybe a poem",
		"Or a song about fear"
))

#Think Like A Computer Scientist Chapter 2: Exercise 1

#All work and no play makes Jack a dull boy

firstword = ("All")
secondword = ("work")
thirdword = ("and")
fourthword = ("no")
fifthhword = ("play")
sixthword = ("makes")
seventhword = ("Jack")
eightword = ("a")
nineword = ("dull")
tenword = ("boy")

print(firstword, secondword, thirdword, fourthword, fifthhword, sixthword, seventhword, eightword, nineword, tenword)

#Think Like A Computer Scientist Chapter 2: Exercise 2

withoutparenthesis = 6 * 1 - 2
print(withoutparenthesis)

withparenthesis = 6 * (1 - 2)
print(withparenthesis)

#Think Like A Computer Scientist Chapter 2: Exercise 4

bruce = 6

print(bruce + 4)

#Think Like A Computer Scientist Chapter 2: Exercise 5

#Assigns the principal amount of $10000 to variable P, assign to n the value 12, and assign to r the interest rate of 8%

p = 10000
n = 12
r = 0.08
t = int(input('How many Years'))

CompoundIntrest_A = p * ( 1 + (r/n))**(n*t)
print(CompoundIntrest_A)

#Think Like A Computer Scientist Chapter 2: Exercise 7

nowtime = int(input("what time now: "))
t = int(input("Input the hour go off your wanted: "))
time = t + nowtime
days = time//24
hour = time % 24
print ("The hour will go off after days: ", days, " at hour: ", hour)




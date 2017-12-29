# I was able to solve this problem by reading the logic of the problem carefully, and typing out what I read.
#
# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.
#
# Could have also divided the problem up as well.

# Proposed Code

def is_leap(year):
    
    leap = False
    
    if year % 4 == 2:
    	if year % 100 == 0:
    		if year % 400 == 0:
    			leap = True
    
    return leap

year = int(input())
print(is_leap(year))

# Alternative Code

def is_leap(year):
    
    leap = False
    
    if year % 4 == 0:
    	if year % 100 == 0:
    		if year % 400 == 0:
    			leap = True

    return leap

year = [2000,2400,1800,1900,2100,2200,2300,2500]
i=0

while i < len(year):
    print(str(year[i]) + ": " + str(is_leap(year[i])))
    i = i+1

# Code That Worked

def is_leap(year):
    
    leap = False
    
    if year % 4 == 0:
        leap = True

    if year % 100 == 0:
        if year % 400 == 0:
            leap = True
        else:
            leap = False
    
    return leap

year = int(input())
print(is_leap(year))

# LESSON: You can integrate statements as booleans, as proposed code

def is_leap(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

# LESSON: You also have libraries. As person said, "Why reinvent the wheel?" (this dude lol)

import calendar

def is_leap(year):
    return calendar.isleap(year)

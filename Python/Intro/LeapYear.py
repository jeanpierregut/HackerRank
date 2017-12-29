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
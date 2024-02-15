import sys

c1 = input()
c2 = input()
c3 = input()

o1 = 0
o2 = 0

if c1 == "black" and c2 == "black":
    sys.stdout.write(str(0))
 
elif c1 == "black" and c2 != "black":
    
    if c2 == "brown": 
        o2 = 1
    elif c2 == "red": 
        o2 = 2
    elif c2 == "orange": 
        o2 = 3
    elif c2 == "yellow": 
        o2 = 4
    elif c2 == "green": 
        o2 = 5
    elif c2 == "blue": 
        o2 = 6
    elif c2 == "violet": 
        o2 = 7
    elif c2 == "grey": 
        o2 = 8
    elif c2 == "white": 
        o2 = 9

    if c3 == "black":    
        o2 *= 1
    if c3 == "brown":    
        o2 *= 10
    if c3 == "red":      
        o2 *= 100
    if c3 == "orange":   
        o2 *= 1000
    if c3 == "yellow":   
        o2 *= 10000
    if c3 == "green":    
        o2 *= 100000
    if c3 == "blue":     
        o2 *= 1000000
    if c3 == "violet":   
        o2 *= 10000000
    if c3 == "grey":     
        o2 *= 100000000
    if c3 == "white":    
        o2 *= 1000000000

    sys.stdout.write(str(o2))
        
    
elif c1 != "black" and c2 == "black":
    
    if c1 == "brown": 
        o1 = 1
    if c1 == "red": 
        o1 = 2
    if c1 == "orange": 
        o1 = 3
    if c1 == "yellow": 
        o1 = 4
    if c1 == "green": 
        o1 = 5
    if c1 == "blue": 
        o1 = 6
    if c1 == "violet": 
        o1 = 7
    if c1 == "grey": 
        o1 = 8
    if c1 == "white": 
        o1 = 9

    if c3 == "black":   
        o1 *= 10
    if c3 == "brown":   
        o1 *= 100
    if c3 == "red":     
        o1 *= 1000
    if c3 == "orange":  
        o1 *= 10000
    if c3 == "yellow":  
        o1 *= 100000
    if c3 == "green":   
        o1 *= 1000000
    if c3 == "blue":    
        o1 *= 10000000
    if c3 == "violet":  
        o1 *= 100000000
    if c3 == "grey":    
        o1 *= 1000000000
    if c3 == "white":   
        o1 *= 10000000000

    sys.stdout.write(str(o1))
        
elif c1 != "black" and c2 != "black":
    
    if c1 == "brown": 
        o1 = 1
    if c1 == "red": 
        o1 = 2
    if c1 == "orange": 
        o1 = 3
    if c1 == "yellow": 
        o1 = 4
    if c1 == "green": 
        o1 = 5
    if c1 == "blue": 
        o1 = 6
    if c1 == "violet": 
        o1 = 7
    if c1 == "grey": 
        o1 = 8
    if c1 == "white": 
        o1 = 9

    if c2 == "brown": 
        o2 = 1
    if c2 == "red": 
        o2 = 2
    if c2 == "orange": 
        o2 = 3
    if c2 == "yellow": 
        o2 = 4
    if c2 == "green": 
        o2 = 5
    if c2 == "blue": 
        o2 = 6
    if c2 == "violet": 
        o2 = 7
    if c2 == "grey": 
        o2 = 8
    if c2 == "white": 
        o2 = 9

    if c3 == "black":   
        o2 *= 1
    if c3 == "brown":   
        o2 *= 10
    if c3 == "red":     
        o2 *= 100
    if c3 == "orange":  
        o2 *= 1000
    if c3 == "yellow":  
        o2 *= 10000
    if c3 == "green":   
        o2 *= 100000
    if c3 == "blue":    
        o2 *= 1000000
    if c3 == "violet":  
        o2 *= 10000000
    if c3 == "grey":    
        o2 *= 100000000
    if c3 == "white":   
        o2 *= 1000000000
    
    sys.stdout.write(str(o1))
    sys.stdout.write(str(o2))
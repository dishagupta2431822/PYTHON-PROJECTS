name="Disha"
print(len(name))  #output: 5

nameshort=name[0:3]  #start from index 0 till 3 excluding 3
print(nameshort)    #output: Dis

char=name[0]
print(char) #output: D


#negative indexing
char=name[-1]
print(char) #output: a

print(name[-4:-1]) #output: ish
print(name[1:4]) #output: ish


# more

print(name[:4]) #output: Dish
print(name[1:]) #output: isha


#slicing with skip value

word="amazing"
print(word[1:5:3]) #output: mi
print(word[::2]) #output: aaig




#functions of strings

name="Disha"
print(len(name)) #output: 5 [length of the string]
print(name.endswith("a")) #output: True
print(name.startswith("D")) #output: True
print(name.capitalize()) #output: Disha
print(name.upper()) #output: DISHA
print(name.lower()) #output: disha
print(name.replace("D","M")) #output: Misha
print(name.split("i")) #output: ['D', 'sha']   
print(name.find("s")) #output: 2 [index of the first occurrence of "s"]
print(name.count("a")) #output: 1 [number of occurrences of "a"]    
print(name.isalpha()) #output: True [checks if all characters are alphabetic]
print(name.isdigit()) #output: False [checks if all characters are digits]  
print(name.islower()) #output: False [checks if all characters are lowercase]
print(name.isupper()) #output: False [checks if all characters are uppercase]
print(name.strip()) #output: Disha [removes leading and trailing whitespace]
print(name.center(20)) #output:       Disha        [centers the string within a specified width]    
print(name.ljust(20)) #output: Disha               [left-justifies the string within a specified width]
print(name.rjust(20)) #output:                Disha [right-justifies the string within a specified width]
print(name.zfill(10)) #output: 00000Disha [pads the string with zeros on the left to a specified width]
print(name.isalnum()) #output: True [checks if all characters are alphanumeric]
print(name.isidentifier()) #output: True [checks if the string is a valid identifier]   
print(name.isprintable()) #output: True [checks if all characters in the string are printable]
print(name.isascii()) #output: True [checks if all characters in the string are ASCII]
print(name.isnumeric()) #output: False [checks if all characters in the string are numeric]
print(name.isdecimal()) #output: False [checks if all characters in the string are decimal characters]
print(name.isspace()) #output: False [checks if all characters in the string are whitespace]
print(name.istitle()) #output: True [checks if the string is in title case]


# escape sequence

title="Disha loves to learn \nand \nshe is self desciplined" #new line
print(title)
title="Disha loves to learn \tand \tshe is self desciplined"  #tab space
print(title)
title="Disha loves to learn and she is \'self desciplined\'"  #single quote
print(title)
title="Disha loves to learn and she is \"self desciplined\""  #double quote
print(title)
title="Disha loves to learn and she is \\self desciplined\\"  #backslash
print(title)
title="Disha loves to learn and she is \rself desciplined"  #carriage return (moves the cursor to the beginning of the line)
print(title)
title="Disha loves to learn and she is \bself desciplined"  #backspace (deletes the character before the cursor)
print(title)
title="Disha loves to learn and she is \fself desciplined"  #form feed (advances the cursor to the next line and clears the current line)
print(title)
title="Disha loves to learn and she is \vself desciplined"  #vertical tab (advances the cursor to the next line)
print(title)
title="Disha loves to learn and she is \0self desciplined"  #null character (represents the end of a string)
print(title)
title="Disha loves to learn and she is \a self desciplined"  #bell/alert (produces a sound or visual alert)
print(title)
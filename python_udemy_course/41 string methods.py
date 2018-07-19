
#get length of string

str1 = "i can check the length of this string with the len() function"

print(len(str1))

#capitalize the first letter of the string

print(str1.capitalize())

#give string title casing - notice that these are not changing the original string

print(str1.title())

#replace words in a string

print(str1.replace('the', 'a'))

str2 = "THIS STRING IS WRITTEN TO MEMORY IN ALL CAPS. THE LOWER() FUNCTION IS PUTTING IT IN LOWERCASE"

print(str2.lower())

#print number of times a char sequence appears inside of a string. Using 'ng' to demonstrate

print(str1.count('ng'))

#split string up
print(str1.split())

#can use linebreaks as well using splitline

str3 = 'The split() function\nis very useful for parsing\nstring values'
print(str3)

print(str3.splitlines())


str4 = "ThIs Is A wOnKy SeNtEnCe. We CaN sWaP cApS wItH tHe SwApCaSe() MeThOd"

print(str4.swapcase())
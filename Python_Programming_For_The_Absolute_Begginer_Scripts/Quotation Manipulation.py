#Quotation Manipulation
#Demonstrates string methods
#Evan Piercy
#3.15.15

# quote from IMB Chairman, Thomas Watson, in 1943
quote = "I think there is a world market for maybe five computers."

print("Original Quote:")
print(quote)

print("\nIn uppercase:")
print(quote.upper())

print("\nIn lowercase:")
print(quote.lower())

print("\nAs a title:")
print(quote.title())

print("\nWith a minor replacement:")
print(quote.replace("five" , "millions of"))

print("\nOriginal quote is still:")
print(quote)

input("Press the enter key to exit")

#try/catch

#every try block needs at least one except block
#finally blocks are always optional

try:
    num=int(input("Enter a number: "))
    print(45/num)
except ValueError:
    print("That wasn't a number")
except ZeroDivisionError:
    print("You attempted to divide by zero. Idiot...")
except:
    print("You did something screwy")
finally:
    print("All done...")
#Tipper Program
#Second Challenge, Second Chapter

bill = float(input("How much was your bill? "))

bigTip = bill * .2
littleTip = bill * .15

print("A fifteen percent tip for the meal would be: $" , littleTip + bill , ".") 
print("A twenty percent tip for the meal would be: $" , bigTip + bill , ".") 

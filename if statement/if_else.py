a = 10
b = 12
c = 10
if a > b:
    print('a is greater than b')
elif a > c:
    print('a is greater than c')
#elif a < b:
 #   print('a is less than b')
elif a==c:#only the first cndition excute even if this statement is true
    print('a is greater than or equal to c')
else:
    print('we dont know about them')
#new if statement 
if a > b and a > c:
    print('a is the biggest number')
elif a < b and a < c:
    print("a is the smallest number")
else:
    print("am checking .....")
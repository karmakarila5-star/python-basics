print("enter marks obtained in 5 subject:")
markone = int(input())
marktwo = int(input())
markthree = int(input())
markfour = int(input())
markfive = int(input())
total = markone + marktwo + markthree + markfour + markfive
avg = int(total /5)
validrange = range(0,101)
if avg not in validrange:
    print("invalid input")
elif avg in range(91 , 101):
    print("your grade is a1")
elif avg in range (81 , 91):
    print("your grade is a2")
elif avg in range (71 , 81):
    print("your grade is b1")
elif avg in range (61 , 71):
    print("your grade is b2")
elif avg in range (51 , 61):
    print("your grade is c1")
elif avg in range (41 , 51):
    print("your grade is c2")
elif avg in range (33 ,41):
    print("your grade is d")
elif avg in range (0,33):
    print("your grade is e1")
    
     

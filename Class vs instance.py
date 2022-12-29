age=int(input())
if age<0:
    print("Age is not valid, setting age to 0.")
    age=0
    print("You are young.")
    age+=3
    print("You are young.")

elif age==10 and age<13:
        print("You are young.")
        age+=3
        print("You are a teenager.")
elif age==16 and age>=13 and age<18:
        print("You are a teenager.")
        age+=3
        print("You are old.")
else:
    print("You are old")
    age+=3
    print("You are old")





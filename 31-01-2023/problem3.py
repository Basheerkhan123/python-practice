a=input("enter the text \n")

if("hyderabad" in a):
    spam=True
elif("king" in a):
    spam=True
elif("hi" in a):
    spam=True
elif("hello" in a):
    spam=True
else:
    spam=False
if(spam):
    print("spam")
else:
    print("not spam")
print("Asslamuallaikum! welcome to the quiz prject \n ==> projected by the Arslan Tufail")
a=input("**do you wanna play?**  \n")
#a1=YES
if a == "yes":
    print("==>lets staRT THE quiz!")
else:
    print("==>ok next time we'll see")
    quit()

score=0
Q1 ="\n What is the capital of pakistan?"

A1="islamabad"
A2="Lahore"
A3="Karachi"
print(Q1)
answer=input("==>ENter your answer: \n")

if answer ==A1:
    print("\n   correct!")
    score+=1
else:
    print("\n   sorry!but thats a  wrong one")



Q2=" \n who is the best founder OF PAKISTAN?"

A1="Quaid e azam"
A2="Khan Sab"
A3="Imran Khan"
A4="nawaz sharifboth "
print(Q2)
answer=input("==>ENter your answer: \n")
if answer ==A1:
    print("\n   correct!")
    score+=1
else:
    print("\n   sorry!but thats a  wrong one")

Q3="\n  How many provinces are there in pakistan?"

A1="4"
A2="5"
A3="6"
print(Q3)
answer=input("==>ENter your answer: \n")
if answer ==A2:
    print("\n   correct!")
    score+=1
else:
    print("\n   sorry!but thats a  wrong one")



print("==>you are doing a good job")

if score == 3:
    print("**Awsom!you have gained a score ==>",score," well done boy")
else:
    print("**good,keep it up,YOUR SOCRE IS==> ",score)



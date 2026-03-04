print("Asslamuallaikum! welcome to the quiz prject \n ==> projected by the Arslan Tufail")
a=print(input("do you wanna play!"))
#a1=YES
if a == "yes":
    print("lets staRT THE quiz!")
else:
    print("ok next time we'll see")
    raise SystemExit    

score=0
Q1 ="What is the capital of pakistan?"

A1="islamabad"
A2="Lahore"
A3="Karachi"
print(Q1)
answer=input("==>ENter your answer:")

if answer ==A1:
    print("correct!")
    score+=1
else:
    print("sorry!but thats a  wrong one")



Q2="who is the best PM OF PAKISTAN ever?"

A1="Nawaz Sharif"
A2="Khan Sab"
A3="Imran Khan"
A4="both A2 A3"
print(Q2)
answer=input("==>ENter your answer:")
if answer ==A4:
    print("correct!")
    score+=1
else:
    print("sorry!but thats a  wrong one")

Q3="How many provinces are there in pakistan?"

A1="4"
A2="5"
A3="6"
print(Q3)
answer=input("==>ENter your answer:")
if answer ==A2:
    print("correct!")
    score+=1
else:
    print("sorry!but thats a  wrong one")



print("==>you are doing a good job")

if score == 3:
    print("**Awsom!you have gained a score ==>",score," well done boy")
else:
    print("**good,keep it up,YOUR SOCRE IS==> ",score)

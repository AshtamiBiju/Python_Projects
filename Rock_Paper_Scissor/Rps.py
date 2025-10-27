import random
def rps():
    l=["Rock","Paper","Scissor"]
    print("My choice is:")
    print(random.choice(l))
    n=input("Do you want to play again:(y/n)")
    if n=="y":
        rps()
    else:
        return
rps()

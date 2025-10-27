import random
def dice():
    print("Your die number is:")
    print(random.randint(1,6))
    n=int(input("If you want to roll again enter 1 ...if not enter 2"))
    if n==1:
        dice()
    else:
        return
dice()

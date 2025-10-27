import time
def start(s):
    while s>0:
        print(s,end='\r')
        time.sleep(1)
        s=s-1
    print("Time is up")
        
def count(n):
    choose=int(input("Enter if it is 1)hour/2)minutes/3)seconds"))
    if choose==1:
        sec=n*3600
        start(sec)
    elif choose==2:
        sec=n*60
        start(sec)
    elif choose==3:
        sec=n
        start(sec)
    else:
        print("Invalid")

ti=int(input("Enter the time:"))
count(ti)
        
                
            

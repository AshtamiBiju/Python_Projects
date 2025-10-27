import time
global sec
sec=0
def start(s):
    print(s)
    time.sleep(1)
    s=s-1
    if s>0:
        start(s)
    else:
        return
        
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
        
                
            

counter = 1
def choose(n,mydict={}):
    global counter
    if n==1:
        task=input("Enter the task to add:")
        mydict[counter]=task
        counter+=1
        again=input("Do you want to eneter an other task?(y/n):")
        if again=="y":
            return choose(1)
        choose(choice())
    elif n==2:
        if not mydict:
            print("No tasks to display")
        else:
            for i,task in mydict.items():
                print(i,":",task,"[]")
        choose(choice())
    elif n==3:
        w=int(input("Enter the id of the task that is completed:"))
        if w in mydict.keys():
            del(mydict[w])
        else:
            print("No such task with that id")
        choose(choice())
    elif n==4:
        exit()
def choice():
    a=int(input("Please choose your option:\n1)Add task\n2)View tasks\n3)Delete task\n4)Exit"))
    return a

choose(choice())
            
        

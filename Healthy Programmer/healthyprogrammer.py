#healthy programmer
"""9 am-5 pm
1.water=wataer.mp3(3.5litres) drank log 18 times -200ml very 27 min
2.eyes-eyes.mp3(done) everym30min  eydone
3.physical.activity--physical_exercise.mp3   every45 min     exdone"""

"""            with open("water.txt","a") as f:
                
                f.write("\n")
                f.write(a1)
                f.write("\n")
               
"""
"""

            with open("arshu_exercise.txt", "r") as f:
                var4=f.read()
                print(var4)
                print("enter y to continue and n to exit")
                a = input()
                if a == "y":
                    read1()
                else:"""
from time import time
from pygame import mixer



def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a1=input()
        if a1==stopper:
            mixer.music.stop()
            break
        elif a1=="stop":
            print(" Thanks for using our Health Monitoring System !!")
            exit()
        elif a1=="retreive":
            read1()

import  time
def getdate():
    import datetime
    return datetime.datetime.now()
   # v = str(getdate())




if __name__ == '__main__':
    def read1():
        print("  w=waterstaus\n  e=eyestatus\n  p=physicalexercise_status")
        a2 = input("enter what do you want retrive?\n")
        if a2 == "w":

            with open("water.txt", "r") as f:
                var4 = f.read()
                print(var4)
                print("enter y to continue and n to exit")
                a = input()
                if a == "y":
                    read1()
                else:
                    exit()
        elif a2 == "e":

            with open("eye.txt", "r") as f:
                var4 = f.read()
                print(var4)
                print("enter y to continue and n to exit")
                a = input()
                if a == "y":
                    read1()
                else:
                    exit()
        elif a2 == "p":

            with open("physical.txt", "r") as f:
                var4 = f.read()
                print(var4)
                print("enter y to continue and n to exit")
                a = input()
                if a == "y":
                    read1()
                else:
                    exit()
    def func1():
       waterinit = time.time()
       eyeinit = time.time()
       physicalinit = time.time()
       while True:
           if time.time() - waterinit > watersecs:
               print("Well, I am feeling thirsty. Don't you? (1.Continue code: 'drank'   2.Exit code: 'stop')")
               musiconloop("music/About.mp3", "drank")
               waterinit = time.time()
               with open("water.txt", "a") as f:
                   v = str(getdate())

                   f.write(v)
                   f.write("\n")
                   f.write("drank")
                   f.write("\n")

           if time.time() - eyeinit > eyesecs:
               print("Let's do some Eye Exercises. (1.Continue code: 'eyedone'   2.Exit code: 'stop')")
               musiconloop("music/Flames.mp3", "eyedone")
               eyeinit = time.time()
               with open("eye.txt", "a") as f:
                   v = str(getdate())
                   f.write(v)
                   f.write("\n")
                   f.write("eyedone")
                   f.write("\n")

           if time.time() - physicalinit > physical:
               print("It's time for Physical Exercises. (1.Continue code: 'exdone'   2.Exit code: 'stop')")
               musiconloop("music/Flashes.mp3", "exdone")
               physicalinit = time.time()
               with open("physical.txt", "a") as f:
                   v = str(getdate())
                   f.write(v)
                   f.write("\n")
                   f.write("exdone")
                   f.write("\n")

    print("\n\n"
          "******************************************************************\n"
          "*                                                                *\n"
          "*      Welcome to  the Healthy Programmer Remainder System       *\n"
          "*                                                                *\n"
          "******************************************************************\n\n")
    print("Some Basic Instructions:\n")
    time.sleep(1)
    print("1.This is Healthy Programmer Remainder System.")
    time.sleep(2)
    print("2.This will take care of your eyes exercise, water intake and physical exercises.")
    time.sleep(2)
    print("3.Our system will alert you at the regular time intervals")
    time.sleep(2)
    print("NOTE: Music will not stop until you enter the correct input.\n")
    time.sleep(2)
    print("=> Enter 'retrieve' for getting the previous details.")
    time.sleep(2)
    print(("=> Enter 'start' for starting the reaminder system.\n"))
    var1=input("=> Enter your choice : ")
    if var1=="retrieve":
        read1()
    elif var1=="start":
        print("\nHow do you want to set the timings of your remainders.")
        print("1.Set Default(10s)\n2.Manual Input\n")
        a2=int(input("Enter your choice : "))
        if a2==1:
            watersecs=10
            eyesecs=20
            physical=30
            func1()

        elif a2==2:
            print("Drink Timer (in sec):")
            watersecs =int(input())
            time.sleep(2)
            print("Eye Exercise Timer (in sec):")
            eyesecs =int(input())
            time.sleep(2)
            print("Physical Exercise Timer (in sec):")
            physical =int(input())
            func1()
        else:
            print("Invalid Input !!")
    else:
        print("Incorrect Input !!")


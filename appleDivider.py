'''input -- take input n,mn,mx  from the user as a no of apples nd range of students
   output-- mn is a divisor of n or not
             mn+1 is a divisor of n or not
             mx is a divisor of n or not
HANDLING THE ERRORS-- mn =mx ;;print it is not a range      '''
def counttheapples():
    var2 = []
    var3 = []
    print("#####    DIVIDE THE APPLE SOLUTION  ####")
    n=int(input("Enter the no of apples you want to distribute??___"))
    print("enter the range----")
    mn=int(input("enter the minimum no. of students you may have___"))
    mx=int(input("enter the maximum no. of students you may have___"))
    print(mx-mn)
    if n > mx-mn:
        print("Invalid input!!!")
        print("number of apples cannot be less than no. of students")
        counttheapples()
    if mn > mx:
        print("Invalid input!!!!")
        counttheapples()
    elif mn == mx:
        print("This is not a range!!!")
        print("invalid input\nplease enter the valid range---")
        check()
    for i in range(mn,mx+1,1):
        if n%i==0:
            print(f"{i} is a divisor of ",n)
            var2.append(i)

        else:
            print(f"{i} is not a divisor of",n)
            #print(f" =>  if the number of students are '{i}',so '{n}' apples cannot be distributed equally....")
            var3.append(i)
    print(f" =>  if the number of students are {var2},so '{n}' apples can be distributed equally....")
    print(f" =>  if the number of students are {var3},so '{n}' apples cannot be distributed equally....")

def check():
    var1 = input("If you want to continue enter 'y' or enter 'n' to exit the code--")
    if var1 == "y":
        counttheapples()
    elif var1 == "n":
        exit()
    else:
        print("Invalid input!!!!")
        check()
if __name__ == '__main__':
    counttheapples()


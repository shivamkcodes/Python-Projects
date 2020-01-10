#age taken from user or taken the date of birth nd tell when will they become 100 aur what is the age in 2090
#optionally they can enter any year nd tell waht s their age in the year
#handle the errors
# 1.you are not yet born
# 2. you seem to be oldest person alive
print("###   WELCOME TO THE AGE MANAGER SYSTEM   ###")
age=int(input("please enter your age or date of birth!!!____"))
realage=0
dateofbirth=0
if age>= 1900:
    dateofbirth=age
    print("your date of birth is:",dateofbirth)
    realage = 2020 - dateofbirth
else:
    realage=age
    #print("your age is :",realage)
    dateofbirth=2020 - realage
    print("your date of birth is:", dateofbirth)
if dateofbirth>=2020:
    print(" you are npot yet born!!!!!")
    print("invalid input")
    exit()
elif realage>100:
    print("you seem to the oldest person alive!!!")
    print("invalid input")
    exit()
#realage = 2020 - dateofbirth
print(f"you are now {realage} years old!!!")
if realage<100:
    var1=100-realage
    print(f"you will become 100yrs after {var1} years in {2020+var1}")
year=int(input("enter any year in which you want to know what will be your age_______"))
if year>2020:
    year1=year-dateofbirth
    print(year1)
else:
    print("invalid input!!!")
    exit()

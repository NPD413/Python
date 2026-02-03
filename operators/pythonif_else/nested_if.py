"""you can have if statement inside if statements this is called nested if statement"""
x=12
if x>10:
    print("greater than 10")
    if x>20:
        print("greater than 20")
    else:
        print("no")

age=25
license=input("y or n: ")
if age>=18:
    print("yes")
    if license is "y":
        print("good")
    else:
        print("no")

score=85
attendance=90
submittedd=True
if score>30:
    print("student is passsed")
    if attendance>=75:
        print("eligible")
    else:
        print("not eligible")
else:
    print("fail")

temp=20
is_sunny=True
if temp>20:
    if is_sunny:
        print("prefect weather!")

username="npd"
password="Sef"
active=True
if username:
    if password:
        if active:
            print("log in")
        else:
            print("log out")
    else:
        print("passsword required")
else:
    print("invalid username")
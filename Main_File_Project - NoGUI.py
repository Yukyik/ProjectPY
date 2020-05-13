#Pangko and Nonny student score adder and delete project
#Com-ED15 
from pathlib import Path
def Deducepoints():
    Buffer = 0
    STD_name_to_reduce = input("Student name : ")
    file=open("d:\\UserData\\STD_DATA.txt", "r")
    STD_name_find = file.read()
    STD_name_find = STD_name_find.split(":")
    j = len(STD_name_find)
    for i in range(0,j):
        if STD_name_to_reduce == STD_name_find[i]:
            if j-i == 2: break
            Buffer = STD_name_find[i+1] 
            Buffer = int(Buffer)
            Buffer -= 5
            STD_name_find[i+1] = Buffer
    file.close()
    file=open("d:\\UserData\\STD_DATA.txt", "w")
    for a in range(0,j):
        write = STD_name_find[a]
        write = str(write)
        if 1 == j-a: break
        else: file.write(write+":")       
    file.close()
def Addstudent():
    std_room = input("Room : ")
    std_id = input("ID : ")
    std_name = input("Name : ") 
    file=open("d:\\UserData\\STD_DATA.txt", "a")
    file.write(std_room)
    file.write(":")
    file.write(std_id)
    file.write(":")
    file.write(std_name)
    file.write(":100:")
    file.close()
def Checkpoints():
    g = 0
    file=open("d:\\UserData\\STD_DATA.txt", "r")
    STD_name_find = file.read()
    STD_name_find = STD_name_find.split(":")
    j = len(STD_name_find)
    j = j//4
    for row in range(0,j):
        for column in range(0,4):
            print(STD_name_find[g],end="")
            print("      ",end="")
            g+=1
        print("")
def login_run():
    while True:
        print("Select function")
        A = input("1 > Add student\n2 > Reduce student score\n3 > Show Score\n4 > Exit\n > ")
        if A == "1": Addstudent()
        elif A == "2": Deducepoints()
        elif A == "3": Checkpoints()
        elif A == "4": quit
        else: print("Error")
def register():
    print("Please enter details below")
    R1 = input("Username : ")
    R2 = input("Password : ")
    Path("d:\\UserData").mkdir(parents=True, exist_ok=True)
    file=open("d:\\UserData\\Source.txt", "a") 
    file.write(R1+":")
    file.write(R2+":")
    file.close()
def login():
    global H1,H2
    i = 0
    print("เข้าสู่ระบบบันทึกคะแนนนักเรียน")
    H1 = input("Username : ")
    H2 = input("Password : ") 
    file=open("d:\\UserData\\Source.txt", "r")
    Check = file.read() #Check = ["aaa:111:aaa:222:aaa:333:"]
    Check = Check.split(":") #Check = ["aaa","111","aaa","222","aaa","333",""]
    del Check[-1]
    file.close()
    if H1 not in Check or H1 == "":
        print("Error Invaid Username or Password")
    if H1 in Check and H2 == "":
        print("Error Invaid Username or Password")
    j = len(Check)
    while True:
        try:
            for i in range(0,j):
                if H1 == Check[i] and H2 == Check[i+1]:
                    login_run()
        except IndexError: break
        else: break
def main():
    print("Do you have a username and password or not")
    print("1 : register")
    A = input("2 : login \n > ")
    while True:
        if A == "1":
            register()
            main()
        elif A == "2": login()
        else: 
            print("Error")
            break
while True:
    main()
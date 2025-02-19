import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="123456", database="football")
cs=con.cursor()
from tabulate import tabulate

def PlayerCheck_None(name):
    data=(name,)
    sql='select * from players where Name=%s'
    cs.execute(sql, data)
    x=cs.fetchone()
    if not x:
        return True
    else:
        return False

def AddPlayer():
    name=input("Enter Player's Name:")
    age=int(input("Enter Player's Age:"))
    pos=input("Enter Players Position (Short Form):")
    salary=int(input("Enter Player's Salary:"))
    data= (name,age,pos,salary)
    sql = 'insert into players values(%s,%s,%s,%s)'
    cs.execute(sql, data)
    con.commit()
    data= (name,age)
    sql = 'insert into injured values(%s,%s,%s,"None","N","N")'
    cs.execute(sql, data)
    con.commit()
    data= (name,age)
    sql = 'insert into penalties values(%s,%s,%s,"None")'
    cs.execute(sql, data)
    con.commit()
    print("completed Successfully")
    
def DelPlayer():
    name=input("Input Name of the player:")
    if PlayerCheck_None(name):
        print("Player Doesn't Exist,Try Again")
    else:
        data=(name,)
        sql= 'delete from players where Name=%s'
        cs.execute(sql, data)
        con.commit()
        data=(name,)
        sql= 'delete from injured where Name=%s'
        cs.execute(sql, data)
        con.commit()
        data=(name,)
        sql= 'delete from penalties where Name=%s'
        cs.execute(sql, data)
        con.commit()
        print("completed Successfully")
    
def PlayerDetails():
    name=input("Enter Player's Name:")
    if PlayerCheck_None(name):
        print("Player Doesn't Exist,Try Again")
    else:
        data=(name,)
        sql='select * from players where Name=%s'
        cs.execute(sql, data)
        x=cs.fetchall()
        h=['Name','Age','Positon','Salary']
        print(tabulate(x, headers=h, tablefmt="rounded_outline"))
        print("completed Successful")
    
def PlayerPayrise():
    name=input("Enter Player's Name:")
    if PlayerCheck_None(name):
        print("Player Doesn't Exist,Try Again")
    else:
        data=(name,)
        sql='select Salary from players where Name=%s'
        cs.execute(sql, data)
        x=cs.fetchone()
        print("Current Salary Is:",x[0])
        rise=int(input("Enter Increase in salary:"))
        Pay=x[0]+rise
        print("New Salary=", Pay)
        s='update players set Salary=%s where Name=%s'
        d=(Pay, name,)
        cs.execute(s, d)
        con.commit()
        print("Sucessful")
    
def PlayerAddInjury():
    print("Injury list:")
    print("  1)Hip pointers")
    print("  2)Quad,hamstring strains")
    print("  3)Ankle sprains")
    print("  4)Pulled Calf")
    print("  5)ACL")
    inj=int(input("Enter Injury Number"))
    if inj==1:
        injury="Hip pointers"
    elif inj==2:
        injury="Quad,hamstring strains"
    elif inj==3:
        injury="Ankle sprains"
    elif inj==4:
        injury="Pulled Calf"
    elif inj==5:
        injury="ACL"
    else:
        print("Incorrect Option Entered Try Again")
    if inj>=1:
        name=input("Enter Player's Name:")
        if PlayerCheck_None(name):
            print("Player Doesn't Exist,Try Again")
        else:
            data=(injury,name,)
            sql='update injured set Injury=%s, Treated="N", `Time Till Healed`="NULL" where Name=%s'
            cs.execute(sql, data)
            con.commit()
            print("Sucessful")

    
def PlayerInjuryDetails():
    sql='select * from injured where Injury !="None"'
    cs.execute(sql)
    x=cs.fetchall()
    injured=0
    h=['Name','Age','Positon','Injury','Treated','Recovery Time']
    print(tabulate(x, headers=h, tablefmt="rounded_outline"))
    for i in x:
        injured+=1
    print("Total Injured Players:",injured)
    print("Sucessful")

def PlayerTreatInjury():
    name=input("Enter Player's Name:")
    if PlayerCheck_None(name):
        print("Player Doesn't Exist,Try Again")
    else:
        data=(name,)
        sql='select * from injured where Name=%s'
        cs.execute(sql, data)
        x=cs.fetchall()
        h=['Name','Age','Positon','Injury','Treated','Recovery Time']
        print(tabulate(x, headers=h, tablefmt="rounded_outline"))
        for i in x:
            if i[4]=="N":
                 Time=input("Enter Number Of Days Required:")
                 Heal= Time +" "+"Days"
                 z='update injured set Treated="Y",`Time Till Healed`=%s where Name=%s;'
                 H=(Heal, name,)
                 cs.execute(z, H,)
                 con.commit()
                 print("Successful")
            elif i[4]=="Y":
                print("Player is already treated")
            else:
                print("Player is not injured/Details not given")
        
def RecoverPlayer():
    name=input("Enter Player's Name:")
    if PlayerCheck_None(name):
        print("Player Doesn't Exist,Try Again")
    else:
        data=(name,)
        sql='select * from injured where Name=%s'
        cs.execute(sql, data)
        x=cs.fetchone()
        y=cs.fetchall()
        h=['Name','Age','Positon','Injury','Treated','Recovery Time']
        print(tabulate(y, headers=h, tablefmt="rounded_outline"))
        if x[5]!="Y":
             z='update injured set Injury="None",Treated="NULL",`Time Till Healed`="NULL" where Name=%s;'
             H=(name,)
             cs.execute(z, H)
             con.commit()
             print("Successful")
        else:
            print("Player Is Not Treated Yet!")

def CardsDetails():
    sql='select * from penalties where Cards!="None"'
    cs.execute(sql)
    x=cs.fetchall()
    penalized=0
    red=0
    yellow=0
    h=['Name','Age','Penalty']
    print(tabulate(x, headers=h, tablefmt="rounded_outline"))
    for i in x:
        if i[3]=="Red":
            red+=1
        elif i[3]=="Yellow":
            yellow+=1
        penalized+=1
    print("Total Yellows:",yellow)
    print("Total Reds:",red)
    print("Total Penalized Players:",penalized)
    print("Sucessful")
    
def CardsADD():
    print("Choose 1 for Red Or 2 For Yellow Card")
    crd=int(input("Enter Card No"))
    if crd==1:
        name=input("Enter Player's Name:")
        if PlayerCheck_None(name):
            print("Player Doesn't Exist,Try Again")
        else:
            data=(name,)
            sql='update penalties set cards="Red" where Name=%s'
            cs.execute(sql, data)
            con.commit()
            print("Sucessful")
    elif crd==2:
        name=input("Enter Player's Name:")
        if PlayerCheck_None(name):
             print("Player Doesn't Exist,Try Again")
        else:
            data=(name,)
            sql='update penalties set Cards="Yellow" where Name=%s'
            cs.execute(sql, data)
            con.commit()
            print("Sucessful")
    else:
        print("Incorrect Option Entered Try Again")

def CardsDel():
        name=input("Enter Player's Name:")
        if PlayerCheck_None(name):
              print("Player Doesn't Exist,Try Again")
        else:
            data=(name,)
            sql='update penalties set Cards="None" where Name=%s'
            cs.execute(sql, data)
            con.commit()
            print("Sucessful")

def ViewStock():
    sql='select * from sales'
    cs.execute(sql)
    x=cs.fetchall()
    h=['Item','Quantity',]
    print(tabulate(x, headers=h, tablefmt="rounded_outline"))
    
def AddStock():
    print("Stock list:")
    print("  1)Kits(Home&Away)")
    print("  2)Kits(3rd)")
    print("  3)Footballs")
    print("  4)Shoes")
    stk=int(input("Enter Stock No: "))
    Stock="none"
    if stk==1:
        Stock="Kits(Home & Away)"
    elif stk==2:
        Stock="Kits(3rd)"
    elif stk==3:
        Stock="Footballs"
    elif stk==4:
        Stock="Shoes"
    else:
        print("Incorrect Option Entered Try Again")
    if stk>=1:
            data=(Stock,)
            sql='select Stock from sales where Item=%s'
            cs.execute(sql, data)
            x=cs.fetchone()
            print("Current Stock Is:",x[0])
            q=int(input("Enter Amount To Increase"))
            quan=x[0]+q
            print("New Stock=", quan)
            s='update sales set Stock=%s where Item=%s'
            d=(quan, Stock,)
            cs.execute(s,d)
            con.commit()
            print("Succesful")

def MinusStock():
    print("Stock list:")
    print("  1)Kits(Home&Away)")
    print("  2)Kits(3rd)")
    print("  3)Footballs")
    print("  4)Shoes")
    stk=int(input("Enter Stock No.: "))
    Stock="none"
    if stk==1:
        Stock="Kits(Home & Away)"
    elif stk==2:
        Stock="Kits(3rd)"
    elif stk==3:
        Stock="Footballs"
    elif stk==4:
        Stock="Shoes"
    else:
        print("Incorrect Option Entered Try Again")
    if stk>=1:
            data=(Stock,)
            sql='select Stock from sales where Item=%s'
            cs.execute(sql, data)
            x=cs.fetchone()
            print("Current Stock Is:",x[0])
            q=int(input("Enter Amount To Decrease"))
            quan=x[0]-q
            print("New Stock=", quan)
            s='update sales set Stock=%s where Item=%s'
            d=(quan, Stock,)
            cs.execute(s,d)
            con.commit()
            print("Succesful")
            
            
def ManagerMenu():
    print("Welcome Manager")
    while True:
        print("Choose Category:")
        print(" 1)Team Management")
        print(" 2)Medical")
        print(" 3)Inventory")
        print(" 4)LogOut")
        ch=int(input("Enter Option-"))
        if ch==1:
            print("  1)Add Players")
            print("  2)Remove Players")
            print("  3)Get Player Info")
            print("  4)Increase Salary")
            print("  5)Penalities Info")
            print("  6)Add Cards")
            print("  7)Remove Cards")
            print("  8)Back to Main Menu")
            zaz=int(input("Enter Option: "))
            if zaz==1:
                AddPlayer()
            elif zaz==2:
                DelPlayer()
            elif zaz==3:
                PlayerDetails()
            elif zaz==4:
                PlayerPayrise()
            elif zaz==5:
                CardsDetails()
            elif zaz==6:
                CardsADD()
            elif zaz==7:
                CardsDel()
            elif zaz==8:
                continue
            else:
                print("Incorrect Option")
        elif ch==3:
            print("  1)View Stock")
            print("  2)Add Stock")
            print("  3)Remove Stock")
            print("  4)Back To Main Menu")
            zaz=int(input("Enter Option: "))
            if zaz==1:
                ViewStock()
            elif zaz==2:
                AddStock()
            elif zaz==3:
                MinusStock()
            elif zaz==4:
                continue
            else:
                print("Incorrect Option")
        elif ch==2:
            print("  1)Add Injury")
            print("  2)View Injury")
            print("  3)Treat Injury")
            print("  4)Recover Player")
            print("  5)Back to Main Menu")
            zaz=int(input("Enter Option: "))
            if zaz==1:
                PlayerAddInjury()
            elif zaz==2:
                PlayerInjuryDetails()
            elif zaz==3:
                PlayerTreatInjury()
            elif zaz==4:
                RecoverPlayer()
            elif zaz==5:
                continue
            else:
                print("Wrong Option Entered, Try again")
        elif ch==4:
            print("Thank you")
            break

def MedicMenu():
    while True:
        print("Welcome Doc")
        print("  1)Add Injury")
        print("  2)View Injury")
        print("  3)Treat Injury")
        print("  4)Recover Player")
        print("  5)Log Out")
        zaz=int(input("Enter Option: "))
        if zaz==1:
            PlayerAddInjury()
        elif zaz==2:
            PlayerInjuryDetails()
        elif zaz==3:
            PlayerTreatInjury()
        elif zaz==4:
            RecoverPlayer()
        elif zaz==5:
            print("Thank you")
        else:
            print("Wrong Option Entered, Try again")
        
def SalesMenu():
    while True:
        print("Welcome Stocker")
        print("  1)View Stocks")
        print("  2)Add Stocks")
        print("  3)Reduce Stocks")
        print("  4)Log Out")
        zaz=int(input("Enter Option: "))
        if zaz==1:
            ViewStock()
        elif zaz==2:
            AddStock()
        elif zaz==3:
            MinusStock()
        elif zaz==4:
            print("Thank you")
            break
        else:
            print("Wrong Option Entered, Try again")


def LogIN(ID,Pass):
    sql='select * from users'
    cs.execute(sql)
    x=cs.fetchall()
    global LoggedIn
    global Manager
    global Medic
    for i in x:
            if i[0]==ID and i[1]==Pass:
                print("Login Success")
                print("You are now,Logged in as",ID)
                if ID=="Manager1":
                    print("!!!!!!!!!")
                    print("~~Welcome Manager~~")
                    print("!!!!!!!!!")
                    ManagerMenu()
                    Manager=1
                elif ID=="Manager2":
                    print("!!!!!!!!!")
                    print("~~Welcome Manager~~")
                    print("!!!!!!!!!")
                    ManagerMenu()
                    Manager=1
                elif ID=="Medic":
                    print("!!!!!!!!!")
                    print("~~Welcome Doc~~")
                    print("!!!!!!!!!")
                    MedicMenu()
                    Medic=1
                elif ID=="Sales":
                    print("!!!!!!!!!")
                    print("~~~Welcome to Stock Management~~~")
                    print("!!!!!!!!!")
                    SalesMenu()
                LoggedIn=1
                return True
                break
    else:
        print("Incorrect User Name//Password, Please Try Again")
        return False


while True:
    ID=input("Enter User Name:")
    Pass=input("Enter Password:")
    LogIN(ID,Pass)
    break

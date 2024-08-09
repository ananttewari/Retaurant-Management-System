import mysql.connector as sqltor
mycon = sqltor.connect(host="localhost", user="root",
                       passwd="Sweethome@123", database="db")
cursor = mycon.cursor()
passd ="mysql"
str= "SELECT amt from money"
cursor.execute(str)
money = cursor.fetchone()[0]

while True:
    x = int(input("""
     To exit enter 0,
     To add raw materials enter 1,
     To print receipt enter 2,
     To view data enter 3,
     For direct access using sql enter 4,
     Enter here: """))
    if x==0:
        break

    elif x == 1:
        idd = int(input("Hi! Enter ID number of Raw Material: "))
        stnt3 = """SELECT COUNT(*) FROM rawmaterial;"""
        cursor.execute(stnt3)

        sttnt3 = cursor.fetchone()[0]
        if idd<(sttnt3+1) and idd>0:
            amt = float(input("Enter the amount you want to buy: "))
            st = "UPDATE rawmaterial SET amount=amount+{} WHERE id={};".format(amt,idd)

            cursor.execute(st)
            mycon.commit()
            stt = """SELECT price FROM rawmaterial WHERE id={};""".format(idd)
            cursor.execute(stt)

            sttt = cursor.fetchone()

            money = money-(amt*sttt[0])
        else:
            print("Wrong Input")



    elif x == 2:
        menu_array = []
        money_array = []
        while True:
            y = input("enter ID number or enter n to finish: ")
            # finish condition
            if y == "n":
                total=0
                print("\n \n YOUR RECEIPT-")
                zo= "SELECT NOW(); "

                cursor.execute(zo)
                zstr=cursor.fetchone()[0]
                print("Time is ", zstr)
                for xy in range(len(money_array)):
                		print("    ",menu_array[xy],": ",money_array[xy])
                		total=total+money_array[xy]

                print("     TOTAL: ", total)
                print("THANK YOU, HAVE A GOOD DAY")
                break
            #menu_array.append(y)
            stnt = """SELECT COUNT(*) FROM items2;"""
            cursor.execute(stnt)

            sttnt = cursor.fetchone()[0]
            if int(y)<(sttnt+1) and int(y)>0:
                mn = """SELECT recipe FROM items2 WHERE id2={};""".format(y)
                cursor.execute(mn)
                mnn = cursor.fetchone()[0]
                arr = mnn.split()
                len_arr = len(arr)

                for d in range(int(len_arr/2)):
                    rawm = arr[2*d]
                    amnt = arr[(2*d)+1]

                    st2 = """UPDATE rawmaterial SET amount=amount-{} WHERE name=\"{}\";""".format(amnt, rawm)
                    cursor.execute(st2)


            	# adding money to total
                mn2 = """SELECT price2,named FROM items2 WHERE ID2={};""".format(y)
                cursor.execute(mn2)
                mnn2 =cursor.fetchone()
                money=money+mnn2[0]
                money_array.append(mnn2[0])
                menu_array.append(mnn2 [1])
            else:
                print("Wrong input")



             # subtracting amount of raw material


    elif x==3:
        print("Total money: ",money)
        z= "SELECT * FROM items2"
        cursor.execute(z)
        dat1=cursor.fetchall()
        print("""
    Menu: """)
        for row in dat1:
            print(row)

        w= "SELECT * FROM rawmaterial"
        cursor.execute(w)
        dat2=cursor.fetchall()
        print("""
    List of items:      """)

        for row in dat2:
            print(row)
    elif x==4:
        pas=input("What is the password? ")
        if pas==passd:
            strin=input("Enter sql: ")
            cursor.execute(strin)
            mycon.commit()
        else:
            print("Wrong password")


    else:
        print("not valid input")
    srt2="UPDATE money SET amt={}".format(money)
    cursor.execute(srt2)

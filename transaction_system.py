import mysql.connector
import getpass
import calendar
from datetime import date


class Vip:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="lol",
            auth_plugin="mysql_native_password",
        )
        self.db1 = self.db.cursor()
        self.create_table()
        self.balance = 0
        self.balance2 = 0
        self.var = ""
        self.user_name = ""
        self.user1 = ""
        self.user2 = ""
        self.me = "me"
        self.pin = 0
        self.w = "withdraw"
        self.d = "deposite"

    def user_nam(self):
        self.db1.execute(
            "select user_name from user_info where phone_no='{}' ".format(self.user1)
        )
        result = self.db1.fetchone()
        if result:
            self.user_name = result[0]

    def bala(self):
        self.db1.execute(
            "select balance from user_info where phone_no='{}' ".format(self.user1)
        )
        result = self.db1.fetchone()
        if result:
            self.balance = result[0]

    def bala2(self):
        self.db1.execute(
            "select balance from user_info where phone_no='{}' ".format(self.user2)
        )
        result = self.db1.fetchone()
        if result:
            self.balance2 = result[0]

#---------Tables-----------------------

    def create_table(self):
        self.db1.execute(
            """
        create table if not exists user_info(
        user_name varchar(30) unique,
        phone_no varchar(30) unique,
        pin varchar(30),
        balance int default 500
        )
      """
        )
        self.db.commit()

        self.db1.execute(
            """
        create table if not exists info(
        id int auto_increment primary key,
        user_name varchar(30),
        action varchar(30),
        amount int,
        date varchar(40)
        
        )
      """
        )
        self.db.commit()

        self.db1.execute(
            """
        create table if not exists info2(
        id int auto_increment primary key,
        user_1 varchar(30),
        user_2 varchar(30),
        amount int,
        date varchar(40)
        
        )
      """
        )
        self.db.commit()
        
   #----------------------Admin Login------------

    def admin_login(self):
        user_name = "vicky"
        pin = "456"
        print("\n-------------WELCOME----------------\n")
        name = input("--------- Enter Admin User Name --------:")
        pin2 = getpass.getpass("-------- Enter Pin----------:")
        if name == user_name:
            if pin2 == pin:
                print("\n---------- SUCCESSFULLY LOGIN ------------\n")
                while True:
                    choice = input(
                        "\nEnter choice\n:---1:Check Users \n---2:Check Transactions \n---3:Check MOney Transfer\n---4:Perticular User Withdraw Deposite\n---5:Perticular User Money Transfer\n---6:Exite---\n-:"
                    )
                    c = int(choice)
                    if c == 1:
                        bk.user()
                    elif c == 2:
                        bk.check_record()
                    elif c == 3:
                        bk.check_transfer()
                    elif c == 6:
                        break
                    elif c==5:
                        bk.one_user_t()
                    elif c==4:
                        bk.one_u()
                    else:
                        print("invalid choice")
            else:
                print("XXX-------INCORRECT PIN -------XXX")
        else:
            print("xxx---------INVALID USER_NAME--------XXX")

#--------------------- Check all Users-------------------

    def user(self):
      self.db1.execute("SELECT user_name, phone_no FROM user_info")
      rows = self.db1.fetchall()

      if not rows:
         print("No users found.")
         return

      print("\n{:<20} {:<15}".format("User Name", "Phone Number"))
      print("-" * 40)
      for row in rows:
         print("{:<20} {:<15}".format(row[0], row[1]))
         
#--------single user money transfer---------------

    def one_user_t(self):
        phone_no=input("----Enter phone_no:")
        self.db1.execute("select * from info2 where user_1='{}' ".format(phone_no))
        rows = self.db1.fetchall()
        if not rows:
          print("No transfer records found.")
          return

        print("\n{:<10} {:<15} {:<15} {:<10} {:<15}".format("ID", "From", "To", "Amount", "Date"))
        print("-" * 70)
        for row in rows:
          print("{:<10} {:<15} {:<15} {:<10} {:<15}".format(row[0], row[1], row[2], row[3], row[4]))
        
        
       

    #--------------------single user money withdraw and deposite
    def one_u(self):
        phone_no=input("----Enter phone_no:")
        self.db1.execute("select * from info where user_name='{}' ".format(phone_no))
        rows = self.db1.fetchall()
        if not rows:
            print("No transactions found.")
            return

        print("\n{:<12} {:<15} {:<10} {:<10} {:<15}".format("ID", "User Name", "Action", "Amount", "Date"))
          
        print("-" * 65)
        for row in rows:
           print("{:<12} {:<15} {:<10} {:<10} {:<15}".format(row[0], row[1], row[2], row[3], row[4]))

    

#--------------------Transactions------------------------------

    def check_record(self):
        self.db1.execute("select * from info")
        rows = self.db1.fetchall()
        if not rows:
            print("No transactions found.")
            return

        print("\n{:<12} {:<15} {:<10} {:<10} {:<15}".format("ID", "User Name", "Action", "Amount", "Date"))
          
        print("-" * 65)
        for row in rows:
           print("{:<12} {:<15} {:<10} {:<10} {:<15}".format(row[0], row[1], row[2], row[3], row[4]))


#---------------Money Transfer------------------

    def check_transfer(self):
        self.db1.execute("select * from info2")
        rows = self.db1.fetchall()
        if not rows:
          print("No transfer records found.")
          return

        print("\n{:<10} {:<15} {:<15} {:<10} {:<15}".format("ID", "From", "To", "Amount", "Date"))
        print("-" * 70)
        for row in rows:
          print("{:<10} {:<15} {:<15} {:<10} {:<15}".format(row[0], row[1], row[2], row[3], row[4]))

            
#------------REgister---------------------------

    def register(self):
        print("\n----------- REGISTER ------------\n")
        name = input("----- Enter User-Name ----:")
        l = [
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "^",
            ",",
            "!",
            "#",
            "@",
            ":",
            ")",
            "+",
            "-",
        ]
        for i in l:
            if name.startswith(i):
                print(
                    "xxx----Enter valid User_Name-(must strat with charecter)-----xxx"
                )
                return

        self.db1.execute(
            """select user_name from user_info where user_name='{}'; """.format(name)
        )
        if self.db1.fetchone():
            print("\nXXX--- This User_Name Is Already Register ---XXX")
            return
        try:
            phone_no1 = int(input("------Enter your 10 Digit Phone_no------ : "))
        except ValueError:
            print("\nxxx---- Invalid Input. Please Enter a valid Phone_No.----xxx")
        phone_no = str(phone_no1)
        if len(phone_no) != 10:
            print("\nxxx---Enter valid phone_no---xxx")
            return
        self.db1.execute(
            """select phone_no from user_info where phone_no='{}'; """.format(phone_no)
        )
        if self.db1.fetchone():
            print("\nxxx--- This Phone_No Is Already Register ---xxx")
            return
        try:
            p = int(input("---- Create 4-Digit pin ----:"))

        except ValueError:
            print("\nxxx---Invalid input Please Enter Pin Correctly.")
            return
        pin = str(p)
        if len(pin) != 4:
            print("\nxxx---Please Enter Valid 4 Digit Pin----xxx")
            return

        try:
            p2 = int(input("---- Conform Pin ----:"))

        except ValueError:
            print("\nInvalid input. Please enter a valid integer.")
            return

        pin2 = str(p)
        if len(pin) != 4:
            print("\nxxx---Please Enter Valid 4 Digit Pin----xxx")
            return

        if p2 != p:
            print("\nxxx---PIN DOSEN'T MATCH---XXX")
            return
        self.db1.execute(
            """insert into user_info (user_name,phone_no,pin)value('{}','{}',{}) """.format(
                name, phone_no, pin2
            )
        )
        self.db.commit()

        print("\n------Registration Succesfull------\n")

#------------Login--------------------------

    def u_login(self):
        print("\n--------------LOGIN----------------")
        p_no = input("\n---- Enter Phone_No ----:")

        self.db1.execute(
            "select phone_no,pin from user_info where phone_no='{}' ".format(p_no)
        )
        reuslt = self.db1.fetchone()
        if reuslt:
            self.v = reuslt[0]
            pin = getpass.getpass("-------- Enter pin -------:")
            if pin == reuslt[1]:
                print("\n----------LOGIN SUCCESSFULL--------")
                print("\n------------------- WELCOME ------------------\n")
                self.pin = pin
                self.user1 = p_no
                bk.bala()
                bk.user_nam()

                bk.user_interface()
            else:
                print("XXX------ Invalid Pin ------XXX")
        else:
            print(      "XXX------ Please Register First This Phone_No Is Not REgister -----XXX " )
            
#----------------Login functions--------------------------------

    def user_interface(self):
        while True:
            choice = int(
                input(
                    "\n 1:Check Balance \n 2:Withdraw \n 3:Deposite \n 4:Money Transfer  \n 5:Exit\nEnter choice :"
                )
            )
            if choice == 1:
                bk.c_balance()
            elif choice == 2:
                bk.widraw()
            elif choice == 3:
                bk.deposite()
            elif choice == 4:
                bk.money_transfer()
            elif choice == 5:
                break
            else:
                print("XXX------- Invalid Choice -------XXX")

#------------Check Balance-------------------------------

    def c_balance(self):

        print("\n---------Balance--:",self.balance)

#----------------------Widraw-------------------------

    def widraw(self):
        p = getpass.getpass("\n-------- Enter Pin ----------")
        if p != self.pin:
            print("xxx----------- Wrong Pin-------xxx")
            return
        v = date.today()
        try:
           amount = int(input("------------Enter Amount To Withdraw---:"))
        except ValueError:
            print("Enter valid Amount")
        if amount<=0:
            print("Enter Valid Amount")
            return
            
        if self.balance > 500:
            self.balance -= amount
            if self.balance > 100:
                self.db1.execute(
                    "update user_info set balance={} where phone_no='{}' ".format(
                        self.balance, self.user1
                    )
                )
                self.db.commit()
                self.db1.execute(
                    "insert into info(user_name,action,amount,date)values('{}','{}',{},'{}') ".format(
                        self.user1, self.w, amount, v
                    )
                )
                print("\n------Transaction Successfull--------\n")

            else:
                self.balance += amount
                print("xxx----------Inefficient Money In Banck Account (you must have 100rs in bank account after widraw )-------------xxx")
        else:
            print("xxx----------Inefficient Balance ------------xxx")
   
   #------------------Deposite-----------------------------

    def deposite(self):
        try:
           amount = int(input("------------Enter Amount To Deposite---:"))
        except ValueError:
            print("Enter valid Amount")
        if amount<=0:
            print("Enter Valid Amount")
            return
        self.balance = amount + self.balance
        v = date.today()
        self.db1.execute(
            "update user_info set balance={} where phone_no='{}' ".format(
                self.balance, self.user1
            )
        )
        self.db.commit()
        self.db1.execute(
            "insert into info(user_name,action,amount,date)values('{}','{}',{},'{}') ".format(
                self.user1, self.d, amount, v
            )
        )
        print("\n------Transaction Successfull--------\n")

#---------------------Money Transfer--------------------------

    def money_transfer(self):
        user2 = input("\n--------- Enter Phone_No You Want To Transfer Money ------------:")
        self.db1.execute(
            "select phone_no,user_name from user_info where phone_no='{}' ".format(
                user2
            )
        )
        reuslt = self.db1.fetchone()
        if reuslt:
            self.v = reuslt[0]
            if user2 == self.user1:
                print("xxx----- What are trying to pull here ----xxx")
                return
            print("\n------ Do You Want To Transfer Money To---:", reuslt[1], "----")
            while True:
                choice = int(input("\nEnter \n1:To Procced\n2:Exit\n:"))
                if choice == 1:
                    try:
                       amount = int(input("------------Enter Amount To Transfer---:"))
                    except ValueError:
                       print("Enter valid Amount")
                    if amount<=0:
                       print("Enter Valid Amount")
                       return
                    if self.balance > amount + 500:
                        pin = getpass.getpass("-----------Enter Pin------------:")
                        if pin == self.pin:
                            self.balance -= amount
                            self.db1.execute(
                                "update user_info set balance={} where phone_no='{}' ".format(
                                    self.balance, self.user1
                                )
                            )
                            self.db.commit()
                            self.user2 = user2
                            bk.bala2()
                            self.balance2 += amount
                            self.db1.execute(
                                "update user_info set balance={} where phone_no='{}' ".format(
                                    self.balance2, self.user2
                                )
                            )
                            self.db.commit()
                            v = date.today()
                            self.db1.execute(
                                "insert into info2(user_1,user_2,amount,date)values('{}','{}',{},'{}') ".format(
                                    self.user1, self.user2, amount, v
                                )
                            )
                            print("-------- Transaction Successfull --------")
                            break
                        else:
                            print("xxx-------- Wrong Pin ---------xxx")
                            break
                    else:
                        print("xxx--------- Inceficient Balance -----------xxx")
                        break
                elif choice == 2:
                    break
                else:
                    print("xxx--------- Invalid Input -----------xxx")
        else:
            print("xxx------This Phone_No Is Not Register")
            
#--------------------Home Page------------------------

    def home(self):
        while True:
            print("\n------------------ WELCOME To ATM ----------------\n")
            choice = int(
                input("1:Register \n2:Login \n3:Admin_login \n4:Exit \n Enter Choice:")
            )
            if choice == 1:
                bk.register()
            elif choice == 2:
                bk.u_login()
            elif choice == 3:
                bk.admin_login()
            elif choice == 4:
                break
            else:
                print("xxx--------- Invalid Choice ----------xxx")


bk = Vip()
bk.home()

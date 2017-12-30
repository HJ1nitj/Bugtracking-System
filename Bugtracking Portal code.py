import MySQLdb
import time
from time import sleep
db=MySQLdb.connect("localhost","root", "password","bugtrackingportal")

#<--------------------------------------------------------------------->

def bug_by_status():
    mycursor = db.cursor()
    print '-' * 100
    print 'ENTER CATEGORY NO WHICH YOU WANT TO VIEW THE BUGS ....'
    print '-' * 100
    print '1---> NEW BUGS'
    print '2---> ASSIGNED BUGS'
    print '3---> SOLVED BUGS'
    print '4---> BACK TO PREVOUS MENU'
    print "-"*100
    print "\n"
    sleep(1)
    print "-"*50
    bug_view = input("ENTER THE CHOICE --->  ")
    print "-"*50
    print "\n"
    if bug_view == 1:

        mycursor.execute("select * from bug where STATUS = 'NEW'")
        print '-' * 200
        print '                               *************NEW BUGS************             '
        print '-' * 200
        print "BID %-10s PID %-10s POSTED_BY %-10s POSTED_ON %-10s BTITLE %-10s BDESCRIPTION %-10s STATUS %-10s DOMAIN " %(" ", " "," ", " ", " ", " ", " ")
        print "-"*200
        for i in mycursor:
            print "%-15s %-15s %-15s %-25s %-15s %-23s %-15s %-10s" %(i[0], i[1], i[2], i[3], i[4], i[5], i[10], i[11])
        print "-"*200
        print"\n"
        sleep(1)
        ch = raw_input( 'PRESS ENTER TO GO BACK TO PREVIOUS MENU...')
        sleep(1)
        bug_by_status()



    elif bug_view == 2:
        mycursor.execute("select * from bug where STATUS = 'ASSIGNED'")
        print '-' * 200
        print '                                                 ***************ASSIGNED BUGS**************'
        print '-' * 200
        print "BID %-10s PID %-10s POSTED_BY %-10s POSTED_ON %-10s BTITLE %-28s BDESCRIPTION %-25s ASSIGNED_TO %-10s ASSIGNED_ON %-10s STATUS %-10s DOMAIN" %(" ", " ", " ", " ", " ", " ", " ", " ", " ")
        print "-"*200
        for i in mycursor:
            print "%-15s %-15s %-15s %-20s %-23s %-50s %-15s %-23s %-15s %-10s" %(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[10], i[11])
        print "-"*200
        ch = raw_input('PRESS ENTER TO GO BACK TO PREVIOUS MENU...')
        bug_by_status()

    elif bug_view == 3:
        mycursor.execute("select * from bug where STATUS = 'SOLVED'")
        print '-' * 200
        print '                                               **************************SOLVED BUGS**********************'
        print '-' * 200
        print "BID %-10s PID %-10s POSTED_BY %-10s POSTED_ON %-10s BTITLE %-15s BDESCRIPTION %-25s ASSIGNED_TO %-10s ASSIGNED_ON %-10s SOLVED_ON %-15s SOLUTION %-15s STATUS %-10s DOMAIN" %(" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ")
        print "-"*200
        for i in mycursor:
            print "%-15s %-15s %-15s %-20s %-26s %-45s %-15s %-23s %-25s %-18s %-15s %-15s " %(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11])

        ch = raw_input('PRESS ENTER TO GO BACK TO PREVIOUS MENU...')
        bug_by_status()

    elif bug_view == 4:
        view_bugs()

def bug_by_domain():
    mycursor = db.cursor()
    print "-" * 100
    print "           **********AVAILABLE DOMAINS**********"
    print "-" * 100
    sleep(1)
    sql = "select * from products"
    mycursor.execute(sql)
    print "PID %-10s PNAME %-10s PDOMAIN " % (" ", " ")
    print "-" * 100
    for row in mycursor:
        print "%-10s %-18s %-18s" % (row[0], row[1], row[2])

    print "-" * 100
    print "\n"
    print "-"*50
    view_bug_dom = raw_input("ENTER THE DOMAIN WHOSE BUG YOU WANT TO SEE --> ").lower()
    print "-"*50
    print "\n"
    sql = ("select * from bug where DOMAIN = '%s' ")
    mycursor.execute(sql % (view_bug_dom))
    if mycursor.rowcount > 0:
        print "-" * 200
        print "BID %-10s PID %-10s POSTED_BY %-10s POSTED_ON %-10s BTITLE %-15s BDESCRIPTION %-25s ASSIGNED_TO %-10s ASSIGNED_ON %-10s SOLVED_ON %-15s SOLUTION %-15s STATUS %-10s DOMAIN" % (" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ")
        print "-" * 200
        for i in mycursor:
            print "%-15s %-15s %-15s %-20s %-26s %-45s %-15s %-23s %-25s %-18s %-15s %-15s " % (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11])
        print "\n"
        print "-"*50
        ch = raw_input("PRESS ENTER TO GO BACK TO PREVOIRS MENU...")
        print "-"*50
        sleep(1)
        view_bugs()

    else:
        print "DOMAIN NAME IS NOT VALID...."
        print '1---> TRY WITH ANOTHER DOMAIN'
        print '2---> GO BACK TO PREVIOUS MENU'
        ch = input("ENTER THE CHOICE --->  ")
        if ch == 1:
            bug_by_domain()
        elif ch == 2:
            view_bugs()


def view_bugs():
    mycursor = db.cursor()
    print "-"*50
    print "************BUGS***********"
    print "-"*50
    print '1---> VIEW BUG BY STATUS'
    print '2---> VIEW BUG BY CATAGORY'
    print '3----> BACK TO PREVIOUS MENU'
    print"-"*50
    print "\n"
    sleep(1)
    print "-"*50
    bug_ch = input("ENTER THE CHOICE ---> ")
    print "-"*50
    print "\n"
    if bug_ch == 1:
        bug_by_status()

    elif bug_ch == 2:
        bug_by_domain()

    elif bug_ch == 3:
        admin_bug()


def assign_bug():
    mycursor = db.cursor()
    print '-' * 200
    print 'ERRORS TO BE ASSIGNED..'
    print '-' * 200
    mycursor.execute("select * from bug where STATUS = 'NEW'")
    print "BID %-10s PID %-10s POSTED_BY %-10s POSTED_ON %-10s BTITLE %-15s BDESCRIPTION %-25s STATUS %-10s BDOMAIN" % (" ", " ", " ", " ", " ", " ", " ")

    print "-" * 200
    for i in mycursor:
        print "%-15s %-15s %-15s %-20s %-23s %-50s %-15s %-10s" % (i[0], i[1], i[2], i[3], i[4], i[5], i[10], i[11])
    print "-" * 200

    ass_bug = input('ENTER BUG ID WHICH YOU WANT TO ASSIGN --->  ')
    sql = "select * from bug where BID = %d"
    mycursor.execute(sql % ass_bug)
    if mycursor.rowcount > 0:
        for i in mycursor:
            dom = i[11]

        sql = "select * from expert where EDOMAIN = '%s' "
        mycursor.execute(sql % dom)
        print '-' * 100
        print "--- RECOMMENDED ---"
        print '-' * 100
        print "EID %-10s ENAME %-10s ECONTACT_NO %-15s EEMAIL_ID %-25s ESTATUS %-15s EDOMAIN " % (" ", " " ," ", " ", " ")
        for i in mycursor:
            print"%-10s %-20s %-23s %-32s %-15s %-15s" %(i[0], i[3], i[4], i[5], i[10], i[11])

        ass_bug_to = input("ENTER THE EXPERT ID WHOM YOU WANT TO ASSIGN THE ERROR --->  ")
        sql = "update bug set ASSIGNED_TO = %d , ASSIGNED_ON =now(), STATUS = 'ASSIGNED' where BID = %d "
        values = (ass_bug_to, ass_bug)
        mycursor.execute(sql % values)

        sql = "select * from expert where EID = %d"
        mycursor.execute(sql % ass_bug_to)
        for i in mycursor:
            load = i[12]

        sql1 = "update expert set ELOAD = %d where EID = %d"
        load=load+1
        values = (load, ass_bug_to)
        mycursor.execute(sql1 % values)
        db.commit()
        print "PLEASE WAIT................."
        sleep(2)
        print ".............QUERY ASSIGNED SUCCESFULLY.............."
        print "\n"
        raw_input("PRESS ANY KEY TO GO BACK TO PREVIOUS MENU :--->")
        print "\n"
        sleep(2)
        admin_bug()





    else:
        print 'BUG ID DOES NOT EXIST....'
        return assign_bug()


def admin_bug():
    print "-"*50
    print '1:---> VIEW BUGS'
    print '2---> ASSIGN BUG TO EXPERTS'
    print '3---> GO BACK TO ADMIN MENU'
    print "-"*50
    print"\n"
    print "-"*50
    choice = input('ENTER YOUR CHOICE :---> ')
    print "-"*50
    print "\n"
    sleep(1)
    if choice == 1:
        view_bugs()

    elif choice == 2:
        assign_bug()

    elif choice == 3:
        admin()

    else:
        print "ENTER THE VALID CHOICE ...."
        print '*' * 100
        print 'REDIRECTING TO PREVIOUS MENU.....'
        print '*' * 100
        time.sleep(2)

#<----------------------------------------------------------------------->



def CSignUp():
    mycursor = db.cursor()
    CLOGINNAME = raw_input("ENTER YOUR LOGIN NAME :--->").lower()
    print"-" * 50
    print "\n"
    CPASSWORD = raw_input("ENTER YOUR PASSWORD :--->").lower()
    ask = 'n'
    while ask == 'n':
        try:
            CconfPASSWORD = raw_input("ENTER CONFIRM PASSWORD :--->").lower()
            if CconfPASSWORD == CPASSWORD:
                print "-" * 50
                pass
            else:
                raise RuntimeError("CONFIRM PASSWORD IS NOT SIMILAR TO PASSWORD, PLEASE TRY AGAIN....")

        except RuntimeError, Argument:
            print "\n"
            print Argument
            continue

        else:
            print "\n"
            print"-" * 50
            CADDRESS = raw_input("ENTER YOUR ADDRESS :--->").lower()
            print "-" * 50
            print "\n"
            ask1 = 'n'
            while ask1 == 'n':
                try:
                    print"-" * 50
                    CCONTACT_NO = raw_input("ENTER YOUR CCONTACT_NO :--->").lower()
                    if len(CCONTACT_NO) == 10:
                        print"-" * 50
                        pass
                    else:
                        raise RuntimeError("*******PLEASE ENTER ANY VALID CONTACT NUMBER, TRY AGAIN....")

                except RuntimeError, Argument:
                    print"\n"
                    print Argument
                    continue

                else:
                    print "\n"
                    print "-" * 50
                    CEMAIL_ID = raw_input("ENTER YOUR EAMIL ID :--->").lower()
                    print "-" * 50
                    print "\n"
                    print "-" * 50
                    CGENDER = raw_input("ENTER YOU GENDER?(M/F) :--->").lower()
                    print "-" * 50
                    print "\n"
                    print "-" * 50
                    CCITY = raw_input("ENTER YOUR CITY :--->").lower()
                    print "-" * 50
                    print "\n"
                    print "-" * 50
                    CSTATE = raw_input("ENTER YOUR STATE :--->").lower()
                    print "-" * 50
                    print "\n"
                    print "-" * 50
                    CCOUNTRY = raw_input("ENTER YOUR COUNTRY :--->").lower()
                    print "-" * 50
                    print "\n"
                    print "-" * 50
                    CPIN_NO = raw_input("ENTER YOUR PIN :--->").lower()
                    print "-" * 50
                    print "\n"
                    print "-" * 50
                    CNAME = raw_input("ENTER YOUR NAME :--->").lower()
                    print "-" * 50

                    sql = "insert into customer(CLOGINNAME, CPASSWORD, CADDRESS , CCONTACT_NO , CEMAIL_ID, CGENDER, CCITY, CSTATE, CCOUNTRY, CPIN_NO, CNAME) values('%s', '%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"
                    values = (
                    CLOGINNAME, CPASSWORD, CADDRESS, CCONTACT_NO, CEMAIL_ID, CGENDER, CCITY, CSTATE, CCOUNTRY, CPIN_NO,
                    CNAME)
                    mycursor.execute(sql % values)
                    print"\n"
                    print "!!!!!DATA INSERTED SUCCESSFULLY!!!!!"
                    print "\n"
                    db.commit()
                    database()

def admin():
            mycursor = db.cursor()
            #mycursor.execute("create table if not exists admin(AID integer primary key auto_increment, ALOGINNAME varchar(50), APASSWORD varchar(50), ANAME varchar(50), AEMAIL_ID varchar(50), ACONTACT_NO varchar(50))")
            print "\n"
            #print "!!!!!!!!!!!ADMIN TABLE  CREATED SUCCESSFULLY!!!!!!!!!!!"
            #print "\n"
            print"-"*50
            print "***************************WELCOME TO ADMIN MODULE***************************"
            print "-"*50
            ALOGINNAME=raw_input("ENTER YOUR LOGIN NAME :--->")
            APASSWORD=raw_input("ENTER YOUR PASSWORD:--->")
            print "-"*50
            print "\n"
            sql = "select * from admin where ALOGINNAME='%s' AND APASSWORD='%s' "
            values = (ALOGINNAME, APASSWORD)
            mycursor.execute(sql % values)
            print mycursor.rowcount

            if mycursor.rowcount > 0:
                def admin_menu():
                    print "***********************REDIRECTING TO ADMIN PORTAL, PLEASE WAIT......................."
                    sleep(3)
                    print "\n"
                    print "WELCOME", ALOGINNAME ,"!!!"
                    sleep(2)
                    print "-"*50
                    print "****ADMIN MENU****"
                    print "-"*50
                    print "1.--->PRODUCTS"
                    print "2.--->BUGS"
                    print "3.--->ACCOUNTS"
                    print "4.--->REPORTS"
                    print  "5.--->LOGOUT"
                    print "-"*50
                    print"\n"
                    sleep(1)
                    ask1=input("SELECT THE OPTION WHERE YOU WANT TO GO :--->")
                    sleep(2)
                    print "\n"

                    def products():
                        print "-"*50
                        print "***PRODUCT MENU***"
                        print "-"*50
                        sleep(1)
                        print "1.--->ADD PRODUCT"
                        print "2.--->UPDATE PRODUCT"
                        print "3.--->VIEW ALL PRODUCTS"
                        print "4.--->REMOVE PRODUCT"
                        print "5.--->RETURN TO ADMIN MENU"
                        print "-"*50
                        print"\n"
                        ask2=input("SELECT THE OPTION WHERE YOU WANT TO GO:--->")
                        sleep(2)
                        print "\n"

                        def add_product():
                            mycursor.execute("create table if not exists products(PID integer primary key auto_increment, PNAME varchar(50),PDOMAIN VARCHAR (50), PDESCRIPTION varchar(200))")
                            print "---------------PRODUCTS TABLE CREATED----------------- "
                            print "\n"
                            print "-"*50
                            PNAME=raw_input("ENTER THE NAME OF THE PRODUCT :--->")
                            print "-" * 50
                            print "\n"
                            print "-" * 50
                            PDOMAIN=raw_input("ENTER THE DOMAIN OF THE PRODUCT :--->")
                            print "-" * 50
                            print "\n"
                            print "-" * 50
                            PDESCRIPTION=raw_input("GIVE THE DESCRIPTION OF THE PRODCUT :--->")
                            print "-" * 50
                            print "\n"
                            sql = "insert into products(PNAME, PDOMAIN, PDESCRIPTION ) values('%s', '%s', '%s')"
                            values = (PNAME, PDOMAIN, PDESCRIPTION)
                            mycursor.execute(sql % values)
                            print "**********PLEASE WAIT...TASK IS IN PROGRESS................"
                            sleep(3)
                            print "\n"
                            print "!!!!!DATA INSERTED SUCCESSFULLY!!!!!"
                            print "\n"
                            db.commit()

                            raw_input ("PRESS ANY KEY TO RETURN TO PRODUCT MENU :--->")
                            products()

                        def update_product():
                            print "-"*100
                            print "**********PRODUCT AVAILABLE**********"
                            print "-"*100

                            sql = "select * from products"
                            mycursor.execute(sql)
                            print "PID %-10s PNAME %-10s PDOMAIN %-10s PDESCRIPTION" % (" ", " ", " ")
                            print "-" * 100
                            for row in mycursor:
                                print "%-10s %-18s %-18s %-10s" % (row[0], row[1], row[2], row[3])


                            print "-" * 100
                            print "\n"
                            print "-"*50
                            PNAME=raw_input("ENTER THE NAME OF THE PRODUCT :--->")
                            PID=input("ENTER PRODUCT ID :--->")
                            print "-"*50
                            print "\n"
                            sql="select * from products where PNAME='%s' AND PID=%d"
                            values=(PNAME,PID)
                            mycursor.execute(sql%values)
                            print "PLEASE WAIT, SYSTEM IS SEARCHING YOUR PRODUCT....."
                            sleep(3)
                            if mycursor.rowcount>0:
                                print "\n"
                                print "-"*50
                                PNAME=raw_input("ENTER THE NAME OF THE UPDATED PRODUCT :--->")
                                PDOMAIN=raw_input("ENTER DOMAIN OF THE UPDATED PRODUCT :--->")
                                PDESCRIPTION=raw_input("ENTER PRODUCT DESCROPTION :--->")
                                print "-"*50
                                sql="update products set PNAME='%s', PDOMAIN='%s', PDESCRIPTION='%s' where PID=%d"
                                values=(PNAME, PDOMAIN, PDESCRIPTION, PID)
                                mycursor.execute(sql%values)
                                print "\n"

                                print "PLEASE WAIT, SYSTEM IS UPDATING YOUR PRODUCT......."
                                sleep(3)
                                print "\n"
                                print "-"*100
                                print "*******************YOUR PRODUCT IS UPDATED SUCCESFULLY, THANKS***************************"
                                print "-"*100
                                sleep(2)
                                print "\n"
                                db.commit()
                                raw_input("PRESS ANY KEY TO GO BACK :--->")
                                sleep(1)
                                return products()


                            else:
                                print "\n"
                                print "YOUR ENTER PRODUCT IS NOT PRESENT IN THE DATABASE, PLEASE ENTER ANY VALID PRODUCT....."
                                sleep(1)
                                return update_product()

                        def viewall_products():
                            sql="select * from products"
                            mycursor.execute(sql)
                            print"-"*100
                            print "PID %-10s PNAME %-10s PDOMAIN %-10s PDESCRIPTION"%(" ", " ", " ")
                            print "-"*100
                            for row in mycursor:
                                print "%-10s %-18s %-18s %-10s" %(row[0], row[1], row[2], row[3])
                            print "-"*100
                            print "\n"
                            raw_input ("PRESS ANY KEY TO GO BACK :--->")
                            sleep(1)
                            return products()

                        def remove_product():
                            print "-" * 100
                            print "**********PRODUCT AVAILABLE**********"
                            print "-" * 100

                            sql = "select * from products"
                            mycursor.execute(sql)
                            print "PID %-10s PNAME %-10s PDOMAIN %-10s PDESCRIPTION" % (" ", " ", " ")
                            print "-" * 100
                            for row in mycursor:
                                print "%-10s %-18s %-18s %-10s" % (row[0], row[1], row[2], row[3])

                            print "-" * 100
                            print "\n"
                            print "-"*50
                            PID=input("ENTER PRODUCT ID WHICH YOU WANT TO REMOVE :--->")
                            print "\n"
                            sql="delete from  products where PID='%d'"
                            values=PID
                            mycursor.execute(sql%values)
                            print "PLEASE WAIT........."
                            sleep(2)
                            print "\n"
                            print "YOUR PRODUCT IS REMOVED SUCCESSFULLY..................."
                            sleep(1)
                            print "-"*50
                            raw_input("PRESS ANY KEY TO GO BACK TO PREVIOUS MENU :--->")
                            print "-"*50
                            print "\n"
                            return products()



                        if ask2==1:
                            add_product()

                        elif ask2==2:
                            update_product()

                        elif ask2==3:
                            viewall_products()

                        elif ask2==4:
                            remove_product()

                        elif ask2==5:
                            admin_menu()



                    def accounts():
                        print "-"*50
                        print "**********ACCOUNTS MODULE***********"
                        print "-"*50
                        print "1.--->CREATE NEW ACCOUNTS"
                        print "2.--->ACTIVATE/DEACTIVATE ACCOUNTS"
                        print "3.--->QUIT ACCOUNTS MODULE"
                        print "-"*50
                        print "\n"
                        sleep(1)
                        ask=input("SELECT THE OPTION WHERE YOU WANT TO GO :--->")
                        sleep(2)
                        print "\n"

                        def new_account():
                            print"-"*50
                            print "1.--->CREATE ACCOUNT FOR 'ADMIN' "
                            print "2.--->CREATE ACCOUNT FOR 'EXPERT' "
                            print "3.--->QUIT"
                            print "-"*50
                            print "\n"
                            sleep(1)
                            ask=input("SELECT 1 FOR ADMIN AND 2 FOR EXPERT :--->")
                            print ".............PLEASE WAIT.................."
                            sleep(2)
                            print"\n"
                            def newacc_admin():
                                print "-"*50
                                ALOGINNAME=raw_input("ENTER THE LOGIN NAME :--->")
                                print "-"*50
                                print "\n"
                                print "-"*50
                                APASSWORD=raw_input("ENTER THE PASSWORD :--->")
                                print "-"*50
                                print "\n"
                                print "-"*50
                                ANAME=raw_input("ENTER THE NAME :--->")
                                print "-"*50
                                print "\n"
                                print "-"*50
                                AEMAIL_ID=raw_input("ENTER THE EMAIL ID")
                                print "-"*50
                                print "\n"
                                print "-"*50
                                ACONTACT_NO=raw_input("ENTER THE CONTACT NUMBER :--->")
                                print "-"*50

                                sql="insert into admin(ALOGINNAME, APASSWORD, ANAME, AEMAIL_ID, ACONTACT_NO) values('%s', '%s', '%s', '%s', '%s') "
                                values=(ALOGINNAME, APASSWORD, ANAME, AEMAIL_ID, ACONTACT_NO)
                                mycursor.execute(sql % values)
                                print "\n"
                                print "********************************DATA INSERTED SUCCESSFULLY****************************"
                                db.commit()
                                print "\n"
                                return new_account()


                            def newacc_expert():
                                mycursor.execute("create table if not exists expert(EID integer primary key auto_increment, ELOGINNAME varchar(50), EPASSWORD varchar(50), ENAME varchar(50), ECONTACT_NO varchar(50), EEMAIL_ID varchar(100), EQUALIFICATION varchar(50), EEXPERIENCE varchar(20), EDOMAIN varchar(50), EGENDER varchar(20), ESTATUS varchar(20))")
                                print "TALBLE CREATED SUCCESSFULLY"
                                print "\n"
                                print "-"*50
                                ELOGINNAME=raw_input("ENTER LOGINNAME :---> ").lower()
                                print "-"*50
                                print "\n"
                                print "-" * 50
                                EPASSWORD=raw_input("ENTER PASSWORD :--->").lower()
                                print "-"*50
                                print "\n"
                                print "-" * 50
                                ENAME=raw_input("ENTER NAME OF THE EXPERT :--->").lower()
                                print "-"*50
                                print "\n"
                                print "-" * 50
                                ECONTACT_NO=raw_input("ENTER CONTACT NUMBER :--->").lower()
                                print "-"*50
                                print "\n"
                                print "-"*50
                                EEMAIL_ID=raw_input("ENTER EMAIL ID :--->").lower()
                                print "-"*50
                                print "\n"
                                print "-"*50
                                EQUALIFICATION=raw_input("ENTER EXPERT QUALIFICATION :--->").lower()
                                print "-"*50
                                print "\n"
                                print "-"*50
                                EEXPERIENCE=raw_input("ENTER EXPERT EXPERIENCE IN HIS/HER FIELD :--->").lower()
                                print "-"*50
                                print"\n"
                                print "-"*50
                                EDOMAIN=raw_input("ENTER DOMAIN OF EXPERTISE :--->").lower()
                                print "-"*50
                                print "\n"
                                print "-"*50
                                EGENDER=raw_input("ENTER GENDER(M/F) :--->").lower()
                                print "-"*50
                                print "\n"
                                print '-'*50
                                ESTATUS=raw_input("ENTER STATUS(ACTIVATE) :--->")
                                sql="insert into expert(ELOGINNAME, EPASSWORD, ENAME, ECONTACT_NO, EEMAIL_ID, EQUALIFICATION, EEXPERIENCE, EDOMAIN, EGENDER, ESTATUS) values('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"
                                values=(ELOGINNAME, EPASSWORD, ENAME, ECONTACT_NO, EEMAIL_ID, EQUALIFICATION, EEXPERIENCE, EDOMAIN, EGENDER, ESTATUS)
                                mycursor.execute(sql%values)
                                db.commit()
                                print "******************PLEASE WAIT.................."
                                sleep(2)
                                print "\n"
                                print "!!!!!!!!!!!!!!!!EXPERT ACCOUNT CREATED SUCCESSFULLY!!!!!!!!!!!!!!"
                                print "\n"
                                raw_input("PRESS ANY KEY TO GO BACK :--->")
                                sleep(2)
                                return new_account()


                            if ask==1:
                                newacc_admin()

                            elif ask==2:
                                newacc_expert()

                            elif ask==3:
                                accounts()




                        def act_dec_acc():
                            print"-"*50
                            print "*****************WELCOME TO ACTIVATE/DEACTIVATE MODULE****************"
                            print"-"*50
                            print"1.--->ACTIVATE EXPERT ACCOUNT"
                            print"2.--->DEACTIVATE EXPERT ACCOUNT"
                            print"3.--->QUIT"
                            print "-"*50
                            print "\n"
                            ask=input("SELECT THE OPTIION WHERE YOU WANT TO GO :--->")

                            def activate():
                                sql="select * from expert"
                                mycursor.execute(sql)
                                print "********EXPERTS IN THE ORGANISATION******"
                                sleep(2)
                                print "-"*100
                                print "EID %-10s ELOGINNAME %-10s ENAME %-10s ESTATUS" %(" ", " ", " ")
                                print "-" * 100
                                for row in mycursor:
                                    print "%-10s %-10s %-18s %-10s" %(row[0], row[1], row[3], row[10])
                                print"-"*100
                                print "\n"
                                sleep(2)
                                print "-"*50
                                EID=input("ENTER EXPERT ID TO WHOM YOU WANT TO ACTIVATE:--->")
                                sleep(1)
                                print "\n"
                                sql="select * from expert where EID=%d"
                                values=(EID)
                                mycursor.execute(sql%values)

                                if mycursor.rowcount >0:
                                    sql="update expert set ESTATUS='%s' where EID=%d"
                                    values=('ACTIVATE', EID)
                                    mycursor.execute(sql%values)
                                    db.commit()
                                    print "***********PLEASE WAIT.........."
                                    sleep(2)
                                    print "\n"
                                    print "**********STATUS IS UPDATE TO ACTIVATE**********"
                                    print "\n"
                                    sleep(1)
                                    raw_input("PRESS ANY KEY TO GO BACK :--->")
                                    sleep(2)
                                    return act_dec_acc()

                                else:
                                    print "***********PLEASE WAIT.........."
                                    sleep(2)
                                    print "EID IS NOT CORRECT, PLEASE ENTER ANY VALID EID...."
                                    return activate()

                            def deactivate():
                                sql = "select * from expert"
                                mycursor.execute(sql)
                                print "********EXPERTS IN THE ORGANISATION******"
                                sleep(2)
                                print "-" * 100
                                print "EID %-10s ELOGINNAME %-10s ENAME %-10s ESTATUS" % (" ", " ", " ")
                                print "-" * 100
                                for row in mycursor:
                                    print "%-15s %-15s %-18s %-15s" %(row[0], row[1], row[3], row[10])
                                print"-" * 100
                                print "\n"
                                print "-" * 50
                                sleep(1)
                                EID = input("ENTER EXPERT ID :--->")
                                print "\n"
                                sql = "select * from expert where EID=%d"
                                values = (EID)
                                mycursor.execute(sql % values)


                                if mycursor.rowcount > 0:
                                    sql = "update expert set ESTATUS='%s' where EID=%d"
                                    values = ('DEACTIVATE', EID)
                                    mycursor.execute(sql % values)
                                    db.commit()
                                    print "***********PLEASE WAIT.........."
                                    sleep(2)
                                    print "\n"
                                    print "**********ACCOUNT IS  DEACTIVATE**********"
                                    print "\n"
                                    raw_input("PRESS ANY KEY TO GO BACK :--->")
                                    sleep(1)
                                    return act_dec_acc()
                                else:
                                    print "***********PLEASE WAIT.........."
                                    sleep(2)
                                    print "EID IS NOT CORRECT, PLEASE ENTER ANY VALID EID...."
                                    return deactivate()

                            if ask==1:
                                activate()
                            elif ask==2:
                                deactivate()
                            elif ask==3:
                                accounts()





                        if ask==1:
                            new_account()

                        elif ask==2:
                            act_dec_acc()

                        elif ask==3:
                            admin_menu()


                    def Reports():
                        mycursor = db.cursor()
                        print "-"*50
                        print "***************REPORTS MAIN MENU**************"
                        print "-"*50
                        print("1---> EXPERT WISE BUGS ")
                        print("2---> DOMAIN WISE BUGS")
                        print("3---> GO BACK TO PREVIOUS MENU")
                        print "-"*50
                        print "\n"
                        sleep(1)
                        choice = input("ENTER YOUR CHOICE :---> ")
                        print "\n"
                        sleep(1)

                        if (choice == 1):

                            sql1 = "select * from expert"
                            mycursor.execute(sql1)
                            print "********EXPERTS IN THE ORGANISATION******"
                            sleep(2)
                            print "-" * 100
                            print "EID %-10s ENAME" % (" ")
                            print "-" * 100
                            for row in mycursor:
                                print "%-10s %-10s" % (row[0], row[3])
                            print"-" * 100
                            print"\n"
                            sleep(1)
                            print"-"*50
                            Assigned_to = input("ENTER THE EXPERT ID WHOSE REPORT YOU WANT TO SEE :--->  ")
                            print "-"*50
                            print "\n"
                            sleep(1)

                            sql1 = "select * from expert where EID =%d "
                            value = (Assigned_to)
                            mycursor.execute(sql1 % value)
                            if mycursor.rowcount > 0:
                                print "-"*50
                                print '........REPORT...........'
                                print "-"*50
                                for i in mycursor:
                                    print"EXPERT NAME: ", i[3]
                                    print"EXPERT CONTACT NUMBER: ", i[4]
                                    print"EXPERT EMAIL ID: ", i[5]
                                    X = mycursor.execute(
                                        "select * from bug where ASSIGNED_TO =%d AND STATUS ='ASSIGNED'" % (Assigned_to))
                                    z = mycursor.execute(
                                        "select * from bug where ASSIGNED_TO =%d AND STATUS ='PENDING'" % (Assigned_to))

                                    print "EXPERT ASSIGNED BUGS: ", X + z
                                    y = mycursor.execute(
                                        "select * from bug where ASSIGNED_TO =%d AND STATUS ='SOLVED'" % (Assigned_to))
                                    print "EXPERT SOLVED BUGS: ", y
                                print "-"*50
                                sleep(1)
                                print "\n"
                                raw_input('PRESS ANY KEY TO RETERN TO PREVIOUS MENU :--->')
                                return Reports()

                        if (choice == 2):
                            print "-" * 100
                            print "**********PRODUCT AVAILABLE**********"
                            print "-" * 100

                            sql = "select * from products"
                            mycursor.execute(sql)
                            print "PID %-10s PNAME" % (" ")
                            print "-" * 100
                            for row in mycursor:
                                print "%-10s %-18s" % (row[0], row[1])

                            print "-" * 100
                            print "\n"
                            sleep(1)


                            pid = input("ENTER PROSUCT ID WHICH YOU WANT TO SEE :---> ")
                            sql1 = "select * from products where PID =%d"
                            value = (pid)
                            mycursor.execute(sql1 % value)
                            if mycursor.execute > 0:
                                for j in mycursor:
                                    print"PRODUCT DOMAIN:", j[2]
                                    print"PRODUCT NAME", j[1]
                                    a = mycursor.execute("select * from bug where PID=%d" % (pid))
                                    print"ASSIGN_TO: ", a
                                    print "\n"
                                    sleep(1)
                                    raw_input("PRESS ANY KEY TO GO BACK TO PREVIOUS MENU :--->")
                                    sleep(1)
                                    return Reports()


                        if choice==3:

                           admin_menu()
















                    def bugs():

                       admin_bug()




                    if ask1 == 1:
                                products()

                    elif ask1 == 2:
                                bugs()

                    elif ask1 == 3:
                                accounts()


                    elif ask1 == 4:
                                Reports()

                    elif ask1 == 5:
                                print "\n"
                                print "!!!!!!!!!!YOU HAVE SUCCESSFULLY LOGGED OFF!!!!!!!!! "
                                print "\n"
                                sleep(2)
                                CSignIn()

                admin_menu()

            else:
                        print "LOGIN FAILED ........PLEASE TRY AGAIN...."
                        sleep(2)
                        return admin()

def solved_query(EID):
                            mycursor = db.cursor()

                            sql = "select * from bug where ASSIGNED_TO = %d and STATUS = 'SOLVED'"
                            mycursor.execute(sql % (EID))
                            print '                                               **************************SOLVED BUGS**********************'
                            print '-' * 200
                            print "BID %-10s PID %-10s POSTED_BY %-10s POSTED_ON %-10s BTITLE %-15s BDESCRIPTION %-25s ASSIGNED_TO %-10s ASSIGNED_ON %-10s SOLVED_ON %-15s SOLUTION %-15s STATUS %-10s DOMAIN" % (" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ")
                            print "-" * 200
                            for i in mycursor:
                                print "%-15s %-15s %-15s %-20s %-26s %-45s %-15s %-23s %-25s %-18s %-15s %-15s " % (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11])
                            print "-"*200
                            sleep(1)
                            print "\n"
                            print "-"*50
                            ch = raw_input("PRESS ANY KEY TO CONTINUE ....")
                            print "-"*50
                            sleep(1)
                            expert_menu(EID)

def assigned_query(EID):
                            mycursor = db.cursor()

                            sql = "select * from bug where ASSIGNED_TO = %d and STATUS = 'ASSIGNED' "
                            mycursor.execute(sql % (EID))
                            print "**************************************ASSIGNED BUGS****************************************"
                            print '-' * 200
                            print "BID %-10s PID %-10s POSTED_BY %-10s POSTED_ON %-10s BTITLE %-15s BDESCRIPTION %-25s ASSIGNED_TO %-10s ASSIGNED_ON %-10s SOLVED_ON %-15s SOLUTION %-15s STATUS %-10s DOMAIN" % (" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ")
                            print "-" * 200
                            for i in mycursor:
                                print "%-15s %-15s %-15s %-20s %-26s %-45s %-15s %-23s %-25s %-18s %-15s %-15s " % (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11])
                            print "-"*200
                            sleep(1)
                            print "\n"
                            print "-"*50
                            ch = raw_input("PRESS ANY KEY TO CONTINUE ....")
                            print "-"*50
                            print "\n"
                            print "PLEASE WAIT............."

                            sleep(2)
                            expert_menu(EID)

def provide_solution(EID):
                                mycursor = db.cursor()

                                sql = "select * from bug where ASSIGNED_TO = %d and STATUS = 'ASSIGNED' "
                                mycursor.execute(sql % (EID))
                                print "**************************************ASSIGNED BUGS****************************************"
                                print '-' * 200
                                print "BID %-10s PID %-10s POSTED_BY %-10s POSTED_ON %-10s BTITLE %-15s BDESCRIPTION %-25s ASSIGNED_TO %-10s ASSIGNED_ON %-10s SOLVED_ON %-15s SOLUTION %-15s STATUS %-10s DOMAIN" % (
                                " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ")
                                print "-" * 200
                                for i in mycursor:
                                    print "%-15s %-15s %-15s %-20s %-26s %-45s %-15s %-23s %-25s %-18s %-15s %-15s " % (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11])
                                print "-" * 200
                                print "\n"
                                sleep(1)
                                print"-"*50
                                BID = input('ENTER THE QUERY ID WHOSE SOLUTION YOU WANT TO PROVIDE --->  ')
                                print "-"*50
                                print "\n"
                                sql = "select * from bug where ASSIGNED_TO = %d and BID = %d"
                                mycursor.execute(sql % (EID, BID))
                                if mycursor.rowcount > 0:
                                    print "-"*50
                                    sol = raw_input("PROVIDE SOLUTION --> ")
                                    print "-"*50
                                    print "\n"
                                    sql = "update bug set SOLUTION = '%s', SOLVED_ON = now() ,STATUS = 'SOLVED' where ASSIGNED_TO = %d and BID = %d"
                                    values = (sol, EID, BID)
                                    mycursor.execute(sql % values)
                                    sql1 = "select * from expert where EID = %d"
                                    mycursor.execute(sql1 % (EID))
                                    for i in mycursor:
                                        load = i[12]

                                    load = load - 1
                                    sql = "update expert set ELOAD = %d where EID = %d"
                                    values = (load, EID)
                                    mycursor.execute(sql % values)
                                    db.commit()
                                    print "PLEASE WAIT.........................."
                                    print "\n"
                                    sleep(2)
                                    print '-'*100
                                    print 'SOLUTION SAVED SUCCESSFULLY.....'
                                    print '-'*100
                                    sleep(1)
                                    print 'REDIRECTING TO MAIN MENU ....'
                                    print '-'*100
                                    sleep(2)
                                    expert_menu(EID)

                                else:
                                    print 'QUERY IS NOT VALID....'
                                    print '-'*100
                                    print 'PLEASE ENTER A VALID QUERY OR PRESS ENTER TO GO BACK TO MAIN MENU..'
                                    sleep(1)
                                    print "\n"
                                    print 'REDIRECTING BACK TO MAIN MENU...'
                                    print '-'*100
                                    sleep(2)
                                    expert_menu(EID)
def expert_menu(EID):
    print '-' * 100
    print "WELCOME TO EXPERT MAIN MENU"
    print '-' * 100
    print '\n'
    print '1---> VIEW SOLVED QUERIES'
    print '2---> VIEW ASSIGNED QUERIES'
    print '3---> PROVIDE SOLUTIONS'
    print '4---> LOG OUT'
    ch = input('ENTER THE CHOICE --->  ')

    if ch == 1:
        solved_query(EID)

    elif ch == 2:
        assigned_query(EID)

    elif ch == 3:
        provide_solution(EID)

    elif ch == 4:
        print "\n"
        print "!!!!!!!!YOU HAVE SUCCESSFULLY LOGGGED OFF !!!!!!!!"
        print "\n"
        CSignIn()

    else:
        print '-' * 100
        print 'PLEASE ENTER A VALID VALUE...'
        print '-' * 100
        print 'REDIRECTING TO MAIN MENU ....'
        time.sleep(1)
        expert_menu(EID)


def expertsignin():

                            mycursor = db.cursor()
                            user_name = raw_input('ENTER EXPERT NAME --->>  ')
                            passw = raw_input("ENTER PASSWORD --->>  ")
                            sql = "select * from expert where ELOGINNAME = '%s' and EPASSWORD = '%s' and ESTATUS = 'ACTIVATE '"
                            values = (user_name, passw)
                            mycursor.execute(sql % values)
                            if mycursor.rowcount > 0:
                                for i in mycursor:
                                    EID = i[0]

                                expert_menu(EID)

                            else:
                                print '-'*100
                                print "USER NAME OR PASSWORD IS WRONG ...."
                                print 'TRY AGAIN LATER'
                                print "-"*100
                                print 'REDIRECTING TO MAIN MENU ....'
                                print '-'*100
                                sleep(2)
                                CSignIn()










def CSignIn():
        mycursor = db.cursor()
        print"-"*50
        print "SIGN IN MODULE"
        print "-"*50
        print "1.--->ADMIN"
        print "2.--->EXPERT"
        print "3.--->CUSTOMER"
        print "4.--->QUIT SIGN IN MODULE"
        print "\n"
        ask=input("SELECT 1 FOR 'ADMIN', 2 FOR 'EXPERT', 3 FOR 'CUSTOMER' AND 4 TO 'QUIT' THE MODULE :--->")
        print "\n"
        print ".......................PLEASE WAIT............................"
        sleep(2)
        if ask == 1:
            admin()
        elif ask == 2:
            expertsignin()

        elif ask == 3:
            customer_signin()

        elif ask == 4:
            database()

        else:
            print "PLEASE ENTER A VALID ENTRY ...."
            CSignIn()


def report_bug(user_name, password):
    mycursor = db.cursor()
    print "-" * 100
    print "**********PRODUCTS AND THEIR IDs***********"
    print "-" * 100
    sleep(1)
    sql = "select * from products"
    mycursor.execute(sql)
    print "PID %-10s PNAME %-15s PDOMAIN " % (" ", " ")
    print "-" * 100
    for row in mycursor:
        print "%-10s %-23s %-15s" % (row[0], row[1], row[2])
    print "-"*100
    print "\n"

    mycursor = db.cursor()
    mycursor.execute("select * from customer where CLOGINNAME = '%s' and CPASSWORD = '%s' " % (user_name, password))
    print "-"*50
    product_id = input("ENTER PRODUCT ID-->>  ")
    print "-"*50
    print "\n"
    for i in mycursor:
        posted_by = i[0];
    print "-"*50
    bdomain = raw_input("ENTER BUG DOMAIN ---> ")
    print "-"*50
    print "\n"
    print "-"*50
    btitle = raw_input("ENTER BUG TITLE -->>  ")
    print "-"*50
    print "\n"
    print "-"*50
    bugdes = raw_input("BUG DESCRIPTION -->>  ")
    print "-"*50
    print "\n"

    try:

        values = (product_id, posted_by, btitle, bugdes, bdomain)
        sql = "insert into bug(PID, POSTED_BY, BTITLE,  BDESCRIPTION, DOMAIN,STATUS,POSTED_ON) values(%d, %d, '%s', '%s','%s','NEW',now())"
        mycursor.execute(sql % values)
        db.commit()

    except:
        print "PLEASE ENTER A VALID PRODUCT ID ...."

    else:
        print "..............PLEASE WAIT................................"
        sleep(2)
        print "\n"
        print "YOUR REPORT HAS BEEN REGISTERED......."
        sleep(2)
        print "\n"
        print 'WE WILL TRY TO SOLVE ASAP.........'
        sleep(1)
        print "\n"


def track_bug(user_name, password):
    mycursor = db.cursor()
    mycursor.execute("select * from customer where CLOGINNAME = '%s' and CPASSWORD = '%s' " % (user_name, password))
    for i in mycursor:
        cid = i[0]

    sql = "select * from bug where POSTED_BY = %d"
    mycursor.execute(sql % cid)
    print "-" * 200
    print "BID %-10s PID %-10s  POSTED_ON %-10s BTITLE %-15s BDESCRIPTION %-25s ASSIGNED_TO %-10s ASSIGNED_ON %-10s SOLVED_ON %-15s SOLUTION %-15s STATUS %-10s DOMAIN" % ( " ", " ", " ", " ", " ", " ", " ", " ", " ", " ")
    print "-" * 200
    for i in mycursor:

       print "%-15s %-15s %-15s %-20s %-26s %-45s %-15s %-23s %-25s %-18s %-15s " % (i[0], i[1], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11])
    print "-" * 200

    print "\n"
    sleep(1)
    ch = raw_input("PRESS ENTER TO RETURN BACK TO MENU ...")
    sleep(1)
    print "\n"

def customer_menu(user_name,password):
    print "-" * 100
    print '1---> REPORT BUG'
    print "2---> TRACK BUG"
    print '3---> LOG OUT'
    ch = input("ENTER THE CHOICE --->  ")
    if ch == 1:
        report_bug(user_name, password)
        cho = raw_input('PRESS ENTER TO GO BACK TO MAIN MENU...')
        customer_menu(user_name,password)

    elif ch == 2:
        track_bug(user_name, password)
        cho = raw_input("PRESS ENTER TO GO BACK TO MAIN MENU...")
        customer_menu(user_name,password)


    elif ch == 3:
        print '-' * 100
        print 'YOU HAVE BEEN SUCCESSFULLY LOGGED OUT....'
        print '-' * 100
        print 'REDIRECTING TO MAIN MENU....'
        print '-' * 100
        sleep(2)
        CSignIn()

def customer_signin():
    mycursor = db.cursor()
    print "-"*50
    user_name = raw_input("ENTER USER NAME -->>  ")
    password = raw_input("ENTER THE PASSWORD -->>  ")
    print"-"*50
    mycursor.execute("select * from customer where CLOGINNAME = '%s' and CPASSWORD = '%s' " % (user_name, password))

    if (mycursor.rowcount > 0):
            customer_menu(user_name,password)

    else:
        print '-'*100
        print "USER NAME OR PASSWORD DOES NOT MATCH..."
        print "-"*100
        print 'REDIRECTING TO SIGNIN MODULE....'
        print '-'*100
        sleep(2)
        CSignIn()







def database():
    print "*******************WELCOME TO BUGTRACKING SYSTEM********************"
    print "1.--->CUSTOMER SIGN UP"
    print "2.--->SIGN IN"
    print '3 ---> QUIT THE SYSTEM'
    print "\n"
    num=input("ENTER YOUR CHOICE :--->")
    mycursor=db.cursor()
    print "-"*50

    if num ==1:
        CSignUp()

    elif num == 2:
        CSignIn()

    elif num == 3:
        exit()

    else:
        print 'PLEASE ENTER A VALID OPTIION...'
        print '-'*100
        print 'REDIRECTING BACK TO MAIN MENU...'
        print '-'*100
        sleep(2)
        database()






database()


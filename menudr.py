import numpy as np
import datetime
import pymysql as sql
import tkinter as tkr
from tkinter import messagebox
import os
con1 = sql.connect("localhost","root","password","moviet")
c = con1.cursor()

f=open("movie_proj",'w+')
banker = tkr.Tk()
banker.title("ONLINE MOVIE TICKET BOOKING SYSTEM")
banker.configure(width=1200,height=600,bg='POWDER BLUE')
banker.mainloop()
var=-1

b1 = tkr.Button(banker,text="CREATE ACCOUNT", BG="ORANGE", font=("arial",20,"bold"), command=lambda : print("TOP"))
b2 = tkr.Button(banker,text="WITHDRAW AMOUNT", BG="ORANGE", font=("arial",20,"bold"), command=lambda : print("TOP"))
b3 = tkr.Button(banker,text="DEPOSIT AMOUNT", BG="ORANGE", font=("arial",20,"bold"), command=lambda : print("TOP"))
b4 = tkr.Button(banker,text="CHECK BALANCE", BG="ORANGE", font=("arial",20,"bold"), command=lambda : print("TOP"))
b5 = tkr.Button(banker,text="CHANGE PASSWORD", BG="ORANGE", font=("arial",20,"bold"), command=lambda : print("TOP"))
b6 = tkr.Button(banker,text="EXIT", BG="ORANGE", font=("arial",20,"bold"), command=lambda : print("TOP"))

l = []
l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
for i in range(1, 6):
        l1.append("AVA")
        l2.append("AVA")
        l3.append("AVA")
        l4.append("AVA")
        l5.append("AVA")
l.append(l1)
l.append(l2)
l.append(l3)
l.append(l4)
l.append(l5)
arr1 = np.array(l)
arr2 = np.array(l)
arr3 = np.array(l)


def acc():
    n = input("Enter name: ")
    a = int(input("Enter age: "))
    g = input("Enter gender: ")
    l = input("Enter address: ")
    p = input("Enter password: ")
    m = int(input("Enter mobile_no: "))
    qry = "insert into useracc(Name,age,gender,locality,password,mob_no) values('%s','%d','%s','%s','%s','%d')" % (n,int(a),g,l,p,int(m))
    r = c.execute(qry)
    if (r > 0):
        print("Account Created!")
    else:
        print("Account not Created!")
    con1.commit()

def spr(n):
    no = int(input("\nEnter no. of Ticket you want : "))
    print("------SEATS AVAILABLE------")
    print(arr1)
    d = input(datetime.date)
    s = input("Enter slots:\n1.Mrng\n2.Noon\n3.Eveng\n4.Night\n")
    q1 = "insert into ticketinfo (Name, Seatsbooked, Date, Slot, Movie) values ('%s','%d','%s','%s','%s')" % (n,int(no),d,s,"SPIDER-MAN")
    name = []
    for p in range(no):
        n = input("Enter name: ")
        name.append(n)
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        arr1[row,col] = "BK"
    r1 = c.execute(q1)
    if r1>0:
        print("BOOKING CONFIRMED!")
        print(arr1)
    else:
        print("BOOKING FAILED!")
    con1.commit()

def xman(n):
    no = int(input("\nEnter no. of Ticket you want : "))
    print("------SEATS AVAILABLE------")
    print(arr2)
    d = input(datetime.date)
    s = input("Enter slots:\n1.Mrng\n2.Noon\n3.Eveng\n4.Night\n")
    q2 = "insert into ticketinfo (Name, Seatsbooked, Date, Slot, Movie) values ('%s','%d','%s','%s','%s')" % (n, int(no), d, s, "X-MAN")
    name = []
    for p in range(no):
        n = input("Enter name: ")
        name.append(n)
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        arr2[row, col] = "BK"
    r2 = c.execute(q2)
    if r2 > 0:
        print("BOOKING CONFIRMED!")
        print(arr2)
    else:
        print("BOOKING FAILED!")
    con1.commit()

def fvf(n):
    no = int(input("\nEnter no. of Ticket you want : "))
    print("------SEATS AVAILABLE------")
    print(arr3)
    d = input(datetime.date)
    s = input("Enter slots:\n1.Mrng\n2.Noon\n3.Eveng\n4.Night\n")
    q3 = "insert into ticketinfo (Name, Seatsbooked, Date, Slot, Movie) values ('%s','%d','%s','%s','%s')" % (n, int(no), d, s, "FORDvsFERARI")
    name = []
    for p in range(no):
        n = input("Enter name: ")
        name.append(n)
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        arr3[row, col] = "BK"
    r3 = c.execute(q3)
    if r3 > 0:
        print("BOOKING CONFIRMED!")
        print(arr3)
    else:
        print("BOOKING FAILED!")
    con1.commit()

def bookt():
    n = input("Enter name: ")
    p = input("Enter password: ")
    qry = "select  Name, password from useracc where name='%s' and password='%s'" % (n,p)
    r = c.execute(qry)
    if r > 0:
        print("Login Successful")
        ch = int(input("Following movie at screen.\nCHOOSE\n\n1.SPIDER-MAN\n2.X-MAN\n3.FORDvsFERARI\n4.EXIT\nEnter your choice:\t"))

        if ch==1:
            spr(n)
        elif ch==2:
            xman(n)
        elif ch==3:
            fvf(n)
        else:
            print("\nTHANK YOU!\n")
    else:
        print("Login Fail")
        print("Please enter valid user_id and password to continue b")
    con1.commit()

def cancel():
    n = input("Enter name: ")
    p = input("Enter password: ")
    qry = "select  Name, password from useracc where name ='%s'and password ='%s'" % (n, p)
    r = c.execute(qry)
    if r > 0:
        print("Login Successful\nUpdate new details\n")
        a = int(input("Enter age: "))
        g = input("Enter gender: ")
        l = input("Enter address: ")
        p = input("Enter password: ")
        m = int(input("Enter mobile_no: "))
        q2 = "update useracc set age='%d',gender='%s',locality = '%s',password='%s',mob_no='%d' where Name = '%s'" % (
        int(a), g, l, p, int(m), n)
        r2 = c.execute(q2)
        if (r2 > 0):
            print("\nCancellation Successful!")
        else:
            print("\nCancellation Unsuccessful!")

    else:
        print("Login Fail")
        print("Please enter valid user_id and password to update account!")
    con1.commit()


def update():
    n = input("Enter name: ")
    p = input("Enter password: ")
    qry = "select  Name, password from useracc where name ='%s'and password ='%s'" % (n,p)
    r = c.execute(qry)
    if r > 0:
        print("Login Successful\nUpdate new details\n")
        a = int(input("Enter age: "))
        g = input("Enter gender: ")
        l = input("Enter address: ")
        p = input("Enter password: ")
        m = int(input("Enter mobile_no: "))
        q2 = "update useracc set age='%d',gender='%s',locality = '%s',password='%s',mob_no='%d' where Name = '%s'" %(int(a),g,l,p,int(m),n)
        r2 = c.execute(q2)
        if(r2>0):
            print("Account updated successfully!")
        else:
            print("Account updation failed!")

    else:
        print("Login Fail")
        print("Please enter valid user_id and password to update account!")
    con1.commit()


def main():
    while True:
        print("------CHOOSE------")
        choice = int(input("1.CREATE ACCOUNT\n2.BOOK_TICKET\n3.UPDATE ACCOUNT\n4.CANCEL TICKET\n5.EXIT\nEnter your choice:\t"))

        if choice==1:
            acc()
        elif choice==2:
            bookt()
        elif choice==3:
            update()
        elif choice==4:
            cancel()
        else:
            print("THANK YOU FOR YOUR TIME!")
        main()


main()
con1.close()

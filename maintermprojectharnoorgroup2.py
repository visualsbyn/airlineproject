import sqlite3
import random
import string
import datetime
from datetime import date

"Author - Harnoor Singh"
"Student id - 818658"
# Database Creation
connection = sqlite3.connect('airlinetickets')
cursor = connection.cursor()
# Creating Table
try:
    tablequery = 'create table passenger(tid text NOT NULL, firstname text , lastname text, email text, phonenumber text, Airline text, Date text, depart text, arrival text, class text, price int , bookedon text, cc int)'
    cursor.execute(tablequery)
    print("Table Up and Running ")
except:
    print("Table Fetched")


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def book():
    print("""
    Select Departing Airport From the List below:
    YYC - CALGARY
    YEG - EDMONTON
    YFC - FREDERICTON
    YQX - GANDER
    YHM - HAMILTON
    YHZ - HALIFAX
    YQM - MONCTON
    YUL - MONTREAL
    YOW - OTTAWA
    YQB - QUEBEC CITY
    YYT - ST.JOHN'S
    YYZ - TORONTO
    YVR - VANCOUVER
    YWG - WINNIPEG
    ORT - PRIVATE AIRPORT
    """)
    depintput = input("Enter Departing Airport: ")
    depair = str(depintput).lower()

    if depair == "calgary":
        depaartingairport = "YYC"
    elif depair == "edmonton":
        depaartingairport = "YEG"
    elif depair == "fredericton":
        depaartingairport = "YFC"
    elif depair == "gander":
        depaartingairport = "YGX"
    elif depair == "hamilton":
        depaartingairport = "YHM"
    elif depair == "halifax":
        depaartingairport = "yhz"
    elif depair == "moncton":
        depaartingairport = "YQM"
    elif depair == "montreal":
        depaartingairport = "YUL"
    elif depair == "ottawa":
        depaartingairport = "YOW"
    elif depair == "quebec city":
        depaartingairport = "YQB"
    elif depair == "st. john's":
        depaartingairport = "YYT"
    elif depair == "toronto":
        depaartingairport = "YYZ"
    elif depair == "vancouver":
        depaartingairport = "YYV"
    elif depair == "winnipeg":
        depaartingairport = "YWG"
    elif depair == "private airport":
        depaartingairport = "ORT"
    else:
        print("Select  A valid departing airport")
    depairport = depaartingairport

    print("""
        Select Arrival Airport From the List below:
        YYC - CALGARY
        YEG - EDMONTON
        YFC - FREDERICTON
        YQX - GANDER
        YHM - HAMILTON
        YHZ - HALIFAX
        YQM - MONCTON
        YUL - MONTREAL
        YOW - OTTAWA
        YQB - QUEBEC CITY
        YYT - ST.JOHN'S
        YYZ - TORONTO
        YVR - VANCOUVER
        YWG - WINNIPEG
        ORT - PRIVATE AIRPORT
        """)
    airvalin = input("Enter Arrival  Airport: ")
    arivalpair = str(airvalin).lower()

    if arivalpair != depaartingairport:
        if arivalpair == "calgary":
            arivalpairairport = "YYC"
        elif arivalpair == "edmonton":
            arivalpairairport = "YEG"
        elif arivalpair == "fredericton":
            arivalpairairport = "YFC"
        elif arivalpair == "gander":
            arivalpairairport = "YGX"
        elif arivalpair == "hamilton":
            arivalpairairport = "YHM"
        elif arivalpair == "halifax":
            arivalpairairport = "yhz"
        elif arivalpair == "moncton":
            arivalpairairport = "YQM"
        elif arivalpair == "montreal":
            arivalpairairport = "YUL"
        elif arivalpair == "ottawa":
            arivalpairairport = "YOW"
        elif arivalpair == "quebec city":
            arivalpairairport = "YQB"
        elif arivalpair == "st. john's":
            arivalpairairport = "YYT"
        elif arivalpair == "toronto":
            arivalpairairport = "YYZ"
        elif arivalpair == "vancouver":
            arivalpairairport = "YYV"
        elif arivalpair == "winnipeg":
            arivalpairairport = "YWG"
        elif arivalpair == "private airport":
            arivalpairairport = "ORT"
        else:
            print("Select  A valid Arrival airport")
    else:
        print("Arrival and deparing airport cant be the same")
    arribvalairport = arivalpairairport
    print("""
    Select Airline:
    (1) Air Canada
    (2) West Jet
    (3) Air Transat
    (4) Flair
    (5) Cath Pacific
    (6) Sunwing
    (7) Swoop
    (8) Charter Jet
    (9) Air Lynx
    (10) Delta 
    """)
    airint = int(input("Select Airline: "))

    match airint:
        case 1:
            airline = "Air Canada"
            baseprice = + 90
        case 2:
            airline = "Westjet"
            baseprice = + 80
        case 3:
            airline = "Air transat"
            baseprice = + 70
        case 4:
            airline = "Flair"
            baseprice = + 30
        case 5:
            airline = "Cath pacific"
            baseprice = + 70
        case 6:
            airline = "Sunwing"
            baseprice = + 35
        case 7:
            airline = "Swoop"
            baseprice = + 25
        case 8:
            airline = "Charter"
            baseprice = + 400
        case 9:
            airline = "Air lynx"
            baseprice = + 20
        case 10:
            airline = "Delta"
            baseprice = + 70
    print("""
    Please Select Traveling class:
    (1)Economy
    (2)Premium Economy
    (3)Business
    (4)First Class
    """)
    classint = int(input("Enter Your Selection: "))
    match classint:
        case 1:
            classtrav = "Economy"
            seatprice = + 40
        case 2:
            classtrav = "Premium Economy"
            seatprice = + 90
        case 3:
            classtrav = "Business"
            seatprice = + 120
        case 4:
            classtrav = "First Class"
            seatprice = + 180
    dayin = int(input("Enter Day(dd) You are travelling: "))
    daylog = str(dayin)
    if dayin <= 5:
        dayprice = 18
    elif dayin <= 10:
        dayprice = 22
    elif dayin <= 15:
        dayprice = 25
    elif dayin <= 23:
        dayprice = 30
    else:
        dayprice = 35
    monthin = input("Enter Travelling Month: ")
    month = str(monthin).lower()
    if month == "january":
        monthprice = + 80
    elif month == "february":
        monthprice = + 28
    elif month == "march":
        monthprice = + 50
    elif month == "april":
        monthprice = + 70
    elif month == "may":
        monthprice = + 90
    elif month == "june":
        monthprice = + 90
    elif month == "july":
        monthprice = + 30
    elif month == "august":
        monthprice = + 15
    elif month == "september":
        monthprice = + 55
    elif month == "october":
        monthprice = + 80
    elif month == "november":
        monthprice = + 60
    elif month == "december":
        monthprice = + 100
    else:
        print("Enter A valid month")
    totalprice = dayprice + seatprice + baseprice + monthprice
    price = str(totalprice)
    print("Total Price for your Ticket Would be: $" + price)
    print("------------------------------------------------")
    inoout = input("Would You continue to book(Y/N): ")
    inout = str(inoout).lower()
    if inout == "n":
        exit()
    else:
        "Log"
    dt_string = str(date.today())
    ticketid = get_random_string(6)
    id = str(ticketid)
    first_name = input("Enter Your First Name: ")
    last_name = input("Enter Your Last Name: ")
    email = input("Enter your Email: ")
    mobileno = input("Enter your Phone Number: ")
    cc = int(input("Enter your Credit Card Number: "))
    ccstr = str(cc)
    dateoo = str(daylog) + "/" + str(monthin)
    # inserting data into data base
    cursor.execute('insert into passenger(tid , firstname , lastname , email, phonenumber, Airline , Date , depart , arrival , class , price , bookedon, cc) values(?,?,?,?,?,?,?,?,?,?,?,?,?)',[id, first_name, last_name, email, mobileno, airline, dateoo, depaartingairport, arivalpairairport, classtrav,price, dt_string, cc])
    cursor.execute('select * from passenger where tid=?', [id])
    i = cursor.fetchone()
    tuplep = tuple(i)
    pticketid = str(tuplep[0])
    pfname = str(tuplep[1])
    planame = str(tuplep[2])
    pemail = str(tuplep[3])
    pmobile = str(tuplep[4])
    pdateo = str(tuplep[6])
    pdpa = str(tuplep[7])
    pariva = str(tuplep[8])
    pairlen = str(tuplep[5])
    pclass = str(tuplep[9])
    pdb = str(tuplep[11])
    print("Your Ticket has been genrated and emailed to you as well.")
    print("Here is your ticket as well:")
    print("-----------------------------")
    print("Booking Reference ID: " + pticketid)
    print("Passenger Name: " + pfname + " " + planame)
    print("Email: " + pemail)
    print("Date fo travel: " + pdateo)
    print("Date Of Booking: " + pdb)
    print("Departing Airport: " + pdpa)
    print("Arrival Airport: " + pariva)
    print("Airline: " + pairlen)
    print("Class: " + pclass)
    filename = str(first_name) + ".txt"
    line0 = "Booking Reference ID: " + id
    line1 = "Passenger Name: " + first_name + last_name
    line2 = "Email: " + email
    line3 = "Email: " + email
    line4 = "Date Of Travel: " + daylog + "/" + monthin
    line5 = "Departing Airport: " + depaartingairport
    line6 = "Arrival Airport: " + arivalpairairport
    linev = line5 + " " + line6
    line7 = "Airline: " + airline
    line8 = "Class: " + classtrav
    f = open(filename, "a")
    f.write(line0)
    f.write('\n' + line1)
    f.write('\n' + line2)
    f.write('\n' + line3)
    f.write('\n' + line4)
    f.write('\n' + linev)
    f.write('\n' + line7)
    f.write('\n' + line8)
    f.close()
    print('\n')
    print("""
    (1) Main Menu
    (2) Exit
    """)
    lstint = int(input("Enter Your Selection: "))
    match lstint:
        case 1:
            main()
        case 2:
            exit()


def manage():
    iid = input("Enter Booking Refernece")
    idforup = str(iid)
    print("""
    Select from the below mentioned list to continue:
    (1) Transfer Ticket
    (2) Change Airline
    (3) Change Dates 
    (4) Main Menu
    (5) Exit
    """)
    managef = int(input("Enter Your Selection: "))
    match managef:
        case 1:
            cursor.execute('select * from passenger where tid=?', [idforup])
            u = cursor.fetchone()  # will be fecthed in the form of list
            tuplep = tuple(u)
            pticketid = str(tuplep[0])
            pfname = str(tuplep[1])
            planame = str(tuplep[2])
            pemail = str(tuplep[3])
            pmobile = str(tuplep[4])
            pdateo = str(tuplep[6])
            pdpa = str(tuplep[7])
            pariva = str(tuplep[8])
            pairlen = str(tuplep[5])
            pclass = str(tuplep[9])
            pdb = str(tuplep[11])
            print("Here is the old Booking")
            print("Booking Reference ID: " + pticketid)
            print("Passenger Name: " + pfname + " " + planame)
            print("Email: " + pemail)
            print("Date fo travel: " + pdateo)
            print("Date Of Booking: " + pdb)
            print("Departing Airport: " + pdpa)
            print("Arrival Airport: " + pariva)
            print("Airline: " + pairlen)
            print("Class: " + pclass)
            print("---------------------------------")
            nfname = input("Enter New Passengers First Name: ")
            fup = str(nfname)
            nlname = input("Enter New Passengers First Name: ")
            lup = str(nlname)
            # (tid , firstname , lastname ,email text, phonenumber text Airline , Date , depart , arrival , class , price , bookedon, cc)
            cursor.execute('update passenger set firstname =? where tid=?', [fup, idforup])
            cursor.execute('update passenger set lastname =? where tid=?', [lup, idforup])
            cursor.execute('select *  from passenger where tid=? ', [idforup])
            p = cursor.fetchone()
            tuplepr = tuple(p)
            pticketid = str(tuplepr[0])
            pfname = str(tuplepr[1])
            planame = str(tuplepr[2])
            pemail = str(tuplepr[3])
            pmobile = str(tuplepr[4])
            pdateo = str(tuplepr[6])
            pdpa = str(tuplepr[7])
            pariva = str(tuplepr[8])
            pairlen = str(tuplepr[5])
            pclass = str(tuplepr[9])
            pdb = str(tuplepr[11])
            print("Here is the New Booking")
            print("Booking Reference ID: " + pticketid)
            print("Passenger Name: " + pfname + " " + planame)
            print("Email: " + pemail)
            print("Date fo travel: " + pdateo)
            print("Date Of Booking: " + pdb)
            print("Departing Airport: " + pdpa)
            print("Arrival Airport: " + pariva)
            print("Airline: " + pairlen)
            print("Class: " + pclass)
            print("""
                Select From the below options: 
                (1) Main Menu
                (2) Exit
                """)
            editinput12 = int(input("Enter your Selection: "))
            match editinput12:
                case 1:
                    main()
                case 2:
                    exit()
        case 2:
            cursor.execute('select * from passenger where tid=?', [idforup])
            u = cursor.fetchone()  # will be fecthed in the form of list
            tuplep = tuple(u)
            pticketid = str(tuplep[0])
            pfname = str(tuplep[1])
            planame = str(tuplep[2])
            pemail = str(tuplep[3])
            pmobile = str(tuplep[4])
            pdateo = str(tuplep[6])
            pdpa = str(tuplep[7])
            pariva = str(tuplep[8])
            pairlen = str(tuplep[5])
            pclass = str(tuplep[9])
            pdb = str(tuplep[11])
            print("Here is the old Booking")
            print("Booking Reference ID: " + pticketid)
            print("Passenger Name: " + pfname + " " + planame)
            print("Email: " + pemail)
            print("Date fo travel: " + pdateo)
            print("Date Of Booking: " + pdb)
            print("Departing Airport: " + pdpa)
            print("Arrival Airport: " + pariva)
            print("Airline: " + pairlen)
            print("Class: " + pclass)
            print("---------------------------------")
            print("Select new Airline And Class From Below: ")
            print("""
                Select Airline:
                (1) Air Canada
                (2) West Jet
                (3) Air Transat
                (4) Flair
                (5) Cath Pacific
                (6) Sunwing
                (7) Swoop
                (8) Charter Jet
                (9) Air Lynx
                (10) Delta 
                """)
            airint = int(input("Select Airline: "))

            match airint:
                case 1:
                    airline = "Air Canada"
                case 2:
                    airline = "Westjet"

                case 3:
                    airline = "Air transat"

                case 4:
                    airline = "Flair"

                case 5:
                    airline = "Cath pacific"

                case 6:
                    airline = "Sunwing"

                case 7:
                    airline = "Swoop"

                case 8:
                    airline = "Charter"

                case 9:
                    airline = "Air lynx"

                case 10:
                    airline = "Delta"

            print("""
                Please Select Traveling class:
                (1)Economy
                (2)Premium Economy
                (3)Business
                (4)First Class
                """)
            classint = int(input("Enter Your Selection: "))
            match classint:
                case 1:
                    classtrav = "Economy"
                case 2:
                    classtrav = "Premium Economy"
                case 3:
                    classtrav = "Business"
                case 4:
                    classtrav = "First Class"
            airlog = str(airline)
            classlog = str(classtrav)
            cursor.execute('update passenger set Airline =? where tid=?', [airlog, idforup])
            cursor.execute('update passenger set class =? where tid=?', [classlog, idforup])
            cursor.execute('select *  from passenger where tid=? ', [idforup])
            p = cursor.fetchone()
            tuplepr = tuple(p)
            pticketid = str(tuplepr[0])
            pfname = str(tuplepr[1])
            planame = str(tuplepr[2])
            pemail = str(tuplepr[3])
            pmobile = str(tuplepr[4])
            pdateo = str(tuplepr[6])
            pdpa = str(tuplepr[7])
            pariva = str(tuplepr[8])
            pairlen = str(tuplepr[5])
            pclass = str(tuplepr[9])
            pdb = str(tuplepr[11])
            print("Here is the New Booking")
            print("Booking Reference ID: " + pticketid)
            print("Passenger Name: " + pfname + " " + planame)
            print("Email: " + pemail)
            print("Date fo travel: " + pdateo)
            print("Date Of Booking: " + pdb)
            print("Departing Airport: " + pdpa)
            print("Arrival Airport: " + pariva)
            print("Airline: " + pairlen)
            print("Class: " + pclass)
            print("""
                            Select From the below options: 
                            (1) Main Menu
                            (2) Exit
                            """)
            editinput12 = int(input("Enter your Selection: "))
            match editinput12:
                case 1:
                    main()
                case 2:
                    exit()
            # (tid , firstname , lastname ,email text, phonenumber text Airline , Date , depart , arrival , class , price , bookedon, cc)
        case 3:
            cursor.execute('select * from passenger where tid=?', [idforup])
            u = cursor.fetchone()  # will be fecthed in the form of list
            tuplep = tuple(u)
            pticketid = str(tuplep[0])
            pfname = str(tuplep[1])
            planame = str(tuplep[2])
            pemail = str(tuplep[3])
            pmobile = str(tuplep[4])
            pdateo = str(tuplep[6])
            pdpa = str(tuplep[7])
            pariva = str(tuplep[8])
            pairlen = str(tuplep[5])
            pclass = str(tuplep[9])
            pdb = str(tuplep[11])
            print("Here is the old Booking")
            print("Booking Reference ID: " + pticketid)
            print("Passenger Name: " + pfname + " " + planame)
            print("Email: " + pemail)
            print("Date fo travel: " + pdateo)
            print("Date Of Booking: " + pdb)
            print("Departing Airport: " + pdpa)
            print("Arrival Airport: " + pariva)
            print("Airline: " + pairlen)
            print("Class: " + pclass)
            print("---------------------------------")
            print("Select dates from below to continue")
            dayin = int(input("Enter Day(dd) You are travelling: "))
            daylog = str(dayin)
            monthin = input("Enter Travelling Month: ")
            month = str(monthin).lower()
            dateoo = str(daylog) + "/" + str(month)
            cursor.execute('update passenger set Date =? where tid=?', [dateoo, idforup])
            cursor.execute('select *  from passengers where tid=? ', [idforup])
            p = cursor.fetchone()
            tuplepr = tuple(p)
            pticketid = str(tuplepr[0])
            pfname = str(tuplepr[1])
            planame = str(tuplepr[2])
            pemail = str(tuplepr[3])
            pmobile = str(tuplepr[4])
            pdateo = str(tuplepr[6])
            pdpa = str(tuplepr[7])
            pariva = str(tuplepr[8])
            pairlen = str(tuplepr[5])
            pclass = str(tuplepr[9])
            pdb = str(tuplepr[11])
            print("Here is the New Booking")
            print("Booking Reference ID: " + pticketid)
            print("Passenger Name: " + pfname + " " + planame)
            print("Email: " + pemail)
            print("Date fo travel: " + pdateo)
            print("Date Of Booking: " + pdb)
            print("Departing Airport: " + pdpa)
            print("Arrival Airport: " + pariva)
            print("Airline: " + pairlen)
            print("Class: " + pclass)
            print("""
                                        Select From the below options: 
                                        (1) Main Menu
                                        (2) Exit
                                        """)
            editinput12 = int(input("Enter your Selection: "))
            match editinput12:
                case 1:
                    main()
                case 2:
                    exit()
        case 4:
            main()
        case 5:
            exit()


def cancle(ticketidedit):
    iid = str(ticketidedit)
    cursor.execute('select * from passenger where tid=?', [iid])
    u = cursor.fetchone()  # will be fecthed in the form of list
    tuplep = tuple(u)
    pticketid = str(tuplep[0])
    pfname = str(tuplep[1])
    planame = str(tuplep[2])
    pemail = str(tuplep[3])
    pmobile = str(tuplep[4])
    pdateo = str(tuplep[6])
    pdpa = str(tuplep[7])
    pariva = str(tuplep[8])
    pairlen = str(tuplep[5])
    pclass = str(tuplep[9])
    pdb = str(tuplep[11])
    print("Booking Reference ID: " + pticketid)
    print("Passenger Name: " + pfname + " " + planame)
    print("Email: " + pemail)
    print("Date fo travel: " + pdateo)
    print("Date Of Booking: " + pdb)
    print("Departing Airport: " + pdpa)
    print("Arrival Airport: " + pariva)
    print("Airline: " + pairlen)
    print("Class: " + pclass)
    print("---------------------------------")
    print('\n')
    delint = input("Do you want to cancle this booking(y/n): ")
    if delint == "y":
        cursor.execute('delete from passenger where tid=?', [iid])
        print("Booking Canceled")
    else:
        edit()


def edit():
    ticketidedit = input("Enter Booking Id to Continue: ")
    print("""
    Select From the below options:
    (1) Manage a Booking
    (2) Cancel a Booking 
    (3) Main Menu
    (4) Exit
    """)
    editinput1 = int(input("Enter your Selection: "))
    match editinput1:
        case 1:
            manage()
        case 2:
            cancle(ticketidedit)
        case 3:
            main()
        case 4:
            exit()


def search():
    idsearch = input("Enter id To Search: ")
    cursor.execute('select *  from passenger where tid=? ', [idsearch])
    p = cursor.fetchone()
    tuplepr = tuple(p)
    pticketid = str(tuplepr[0])
    pfname = str(tuplepr[1])
    planame = str(tuplepr[2])
    pemail = str(tuplepr[3])
    pmobile = str(tuplepr[4])
    pdateo = str(tuplepr[6])
    pdpa = str(tuplepr[7])
    pariva = str(tuplepr[8])
    pairlen = str(tuplepr[5])
    pclass = str(tuplepr[9])
    pdb = str(tuplepr[11])
    print("Here is the New Booking")
    print("Booking Reference ID: " + pticketid)
    print("Passenger Name: " + pfname + " " + planame)
    print("Email: " + pemail)
    print("Date fo travel: " + pdateo)
    print("Date Of Booking: " + pdb)
    print("Departing Airport: " + pdpa)
    print("Arrival Airport: " + pariva)
    print("Airline: " + pairlen)
    print("Class: " + pclass)
    print("""
    Select From the below options: 
    (1) Search Another Booking
    (2) Main Menu
    (3) Exit
    """)
    editinput12 = int(input("Enter your Selection: "))
    match editinput12:
        case 1:
            search()
        case 2:
            main()
        case 3:
            exit()


def main():
    print("     Create By Group 6")
    print("Airline Ticket Booking Srvice")
    print("-----------------------------")
    print("""
    Select From List Below to continue: 
    (1) Book a Ticket
    (2) Edit a Booking
    (3) Search a Booking
    (4) Exit
    """)
    cursor.execute('select * from passenger')
    input1 = int(input("Enter your Selection: "))
    match input1:
        case 1:
            book()
        case 2:
            edit()
        case 3:
            search()
        case 4:
            exit()


main()
connection.commit()
connection.close()

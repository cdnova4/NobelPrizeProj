from Tkinter import *
import ttk
import tkMessageBox
import Tkinter
import sqlite3


# Win1 is the main Window of the application
def win1():
    top = Tkinter.Tk()
    top.configure(background='black')
    top.wm_title("Nobel Prize")
    frame = Frame(width="1000", height="1000")
    top.geometry("1000x1000")

    ###################################################
    # Search Criterias
    Label(top, text="Year of Prize", font=(None, 9), bg="black", fg="blue").grid(row=1, column=1)
    Label(top, text="Category of Prize", font=(None, 9), bg="black", fg="blue").grid(row=3, column=1)
    Label(top, text="ID# of Laureates", font=(None, 9), bg="black", fg="blue").grid(row=7, column=1)
    Label(top, text="First Name of Laureates", font=(None, 9), bg="black", fg="blue").grid(row=9, column=1)
    Label(top, text="Surname of Laureates", font=(None, 9), bg="black", fg="blue").grid(row=11, column=1)
    Label(top, text="DOB of Laureates", font=(None, 9), bg="black", fg="blue").grid(row=13, column=1)
    Label(top, text="DOD of Laureates", font=(None, 9), bg="black", fg="blue").grid(row=15, column=1)
    Label(top, text="Born Country of Laureates", font=(None, 9), bg="black", fg="blue").grid(row=17, column=1)
    Label(top, text="Born Country Code of Laureates", font=(None, 9), bg="black", fg="blue").grid(row=19, column=1)
    Label(top, text="Born City of Laureates", font=(None, 9), bg="black", fg="blue").grid(row=21, column=1)
    Label(top, text="Death Country of Laureates", font=(None, 9), bg="black", fg="blue").grid(row=23, column=1)
    Label(top, text="Death Country Code of Laureates", font=(None, 9), bg="black", fg="blue").grid(row=25, column=1)
    Label(top, text="Death City of Laureates", font=(None, 9), bg="black", fg="blue").grid(row=27, column=1)
    Label(top, text="Gender of Laureates", font=(None, 9), bg="black", fg="blue").grid(row=29, column=1)

    # Column Label
    Label(top, text="Search", bg="black", fg="blue").grid(row=0, column=1)

    #############################################################
    # Search Entry Variables
    ##############################################################
    sYear = StringVar()
    sCategory = StringVar()
    sID = StringVar()
    sFname = StringVar()
    sSname = StringVar()
    sDOB = StringVar()
    sDOD = StringVar()
    sBCountry = StringVar()
    sBCountryCode = StringVar()
    sBCity = StringVar()
    sDCountry = StringVar()
    sDCountryCode = StringVar()
    sDCity = StringVar()
    sGender = StringVar()

    # Entry components for User Input
    e2 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=sYear)
    e4 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=sCategory)
    e8 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=sID)
    e10 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=sFname)
    e12 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=sSname)
    e14 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=sDOB)
    e16 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=sDOD)
    e18 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=sBCountry)
    e20 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=sBCountryCode)
    e22 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=sBCity)
    e24 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=sDCountry)
    e26 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=sDCountryCode)
    e28 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=sDCity)
    e30 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=sGender)

    e2.grid(row=2, column=1)
    e4.grid(row=4, column=1)
    e8.grid(row=8, column=1)
    e10.grid(row=10, column=1)
    e12.grid(row=12, column=1)
    e14.grid(row=14, column=1)
    e16.grid(row=16, column=1)
    e18.grid(row=18, column=1)
    e20.grid(row=20, column=1)
    e22.grid(row=22, column=1)
    e24.grid(row=24, column=1)
    e26.grid(row=26, column=1)
    e28.grid(row=28, column=1)
    e30.grid(row=30, column=1)

    ###################################################
    # Add Criteria
    Label(top, text="Year of Prize", font=(None, 9), fg="green", bg="black").grid(row=1, column=2)
    Label(top, text="Category of Prize", font=(None, 9), fg="green", bg="black").grid(row=3, column=2)
    Label(top, text="First Name of Laureates", font=(None, 9), fg="green", bg="black").grid(row=9, column=2)
    Label(top, text="Surname of Laureates", font=(None, 9), fg="green", bg="black").grid(row=11, column=2)
    Label(top, text="DOB of Laureates", font=(None, 9), fg="green", bg="black").grid(row=13, column=2)
    Label(top, text="DOD of Laureates", font=(None, 9), fg="green", bg="black").grid(row=15, column=2)
    Label(top, text="Born Country of Laureates", font=(None, 9), fg="green", bg="black").grid(row=17, column=2)
    Label(top, text="Born City of Laureates", font=(None, 9), fg="green", bg="black").grid(row=21, column=2)
    Label(top, text="Death Country of Laureates", font=(None, 9), fg="green", bg="black").grid(row=23, column=2)
    Label(top, text="Death City of Laureates", font=(None, 9), fg="green", bg="black").grid(row=27, column=2)
    Label(top, text="Gender of Laureates", font=(None, 9), fg="green", bg="black").grid(row=29, column=2)

    # Add Column Label
    Label(top, text="Add", fg="green", bg="black").grid(row=0, column=2)

    #############################################################
    # Add Entry Variables
    ##############################################################
    aYear = StringVar()
    aCategory = StringVar()
    aFname = StringVar()
    aSname = StringVar()
    aDOB = StringVar()
    aDOD = StringVar()
    aBCountry = StringVar()
    aBCity = StringVar()
    aDCountry = StringVar()
    aDCity = StringVar()
    aGender = StringVar()

    e2 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=aYear)
    e4 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=aCategory)
    e10 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=aFname)
    e12 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=aSname)
    e14 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=aDOB)
    e16 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=aDOD)
    e18 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=aBCountry)
    e22 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=aBCity)
    e24 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=aDCountry)
    e28 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=aDCity)
    e30 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=aGender)

    e2.grid(row=2, column=2)
    e4.grid(row=4, column=2)
    e10.grid(row=10, column=2)
    e12.grid(row=12, column=2)
    e14.grid(row=14, column=2)
    e16.grid(row=16, column=2)
    e18.grid(row=18, column=2)
    e22.grid(row=22, column=2)
    e24.grid(row=24, column=2)
    e28.grid(row=28, column=2)
    e30.grid(row=30, column=2)

    ###################################################
    # Delete Criteria
    Label(top, text="Year of Prize", font=(None, 9), bg="black", fg="red").grid(row=1, column=3)
    Label(top, text="Category of Prize", font=(None, 9), bg="black", fg="red").grid(row=3, column=3)
    Label(top, text="ID# of Laureates", font=(None, 9), bg="black", fg="red").grid(row=7, column=3)
    Label(top, text="First Name of Laureates", font=(None, 9), bg="black", fg="red").grid(row=9, column=3)
    Label(top, text="Surname of Laureates", font=(None, 9), bg="black", fg="red").grid(row=11, column=3)
    Label(top, text="DOB of Laureates", font=(None, 9), bg="black", fg="red").grid(row=13, column=3)
    Label(top, text="DOD of Laureates", font=(None, 9), bg="black", fg="red").grid(row=15, column=3)
    Label(top, text="Born Country of Laureates", font=(None, 9), bg="black", fg="red").grid(row=17, column=3)
    Label(top, text="Born Country Code of Laureates", font=(None, 9), bg="black", fg="red").grid(row=19, column=3)
    Label(top, text="Born City of Laureates", font=(None, 9), bg="black", fg="red").grid(row=21, column=3)
    Label(top, text="Death Country of Laureates", font=(None, 9), bg="black", fg="red").grid(row=23, column=3)
    Label(top, text="Death Country Code of Laureates", font=(None, 9), bg="black", fg="red").grid(row=25, column=3)
    Label(top, text="Death City of Laureates", font=(None, 9), bg="black", fg="red").grid(row=27, column=3)
    Label(top, text="Gender of Laureates", font=(None, 9), bg="black", fg="red").grid(row=29, column=3)

    # Delete Label
    Label(top, text="Delete", bg="black", fg="red").grid(row=0, column=3)

    ###################################################
    # Delete Variables
    ###################################################
    dYear = StringVar()
    dCategory = StringVar()
    dID = StringVar()
    dFname = StringVar()
    dSname = StringVar()
    dDOB = StringVar()
    dDOD = StringVar()
    dBCountry = StringVar()
    dBCountryCode = StringVar()
    dBCity = StringVar()
    dDCountry = StringVar()
    dDCountryCode = StringVar()
    dDCity = StringVar()
    dGender = StringVar()

    e2 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=dYear)
    e4 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=dCategory)
    e8 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=dID)
    e10 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=dFname)
    e12 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=dSname)
    e14 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=dDOB)
    e16 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=dDOD)
    e18 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=dBCountry)
    e20 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=dBCountryCode)
    e22 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=dBCity)
    e24 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=dDCountry)
    e26 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=dDCountryCode)
    e28 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=dDCity)
    e30 = Entry(top, bg="grey", borderwidth="0", highlightcolor="Yellow", textvariable=dGender)

    e2.grid(row=2, column=3)
    e4.grid(row=4, column=3)
    e8.grid(row=8, column=3)
    e10.grid(row=10, column=3)
    e12.grid(row=12, column=3)
    e14.grid(row=14, column=3)
    e16.grid(row=16, column=3)
    e18.grid(row=18, column=3)
    e20.grid(row=20, column=3)
    e22.grid(row=22, column=3)
    e24.grid(row=24, column=3)
    e26.grid(row=26, column=3)
    e28.grid(row=28, column=3)
    e30.grid(row=30, column=3)

    #################################################

    #############
    # Function to obtain Search Entry Inputs
    ###############################################
    def searchParms():
        lst = {}  # List to obtain entry input
        temp = {}  # List to prepare query
        sentItems = []  # List to be sent out to win2()

        # Check each variable and see if there's an input and store it into a dictionary
        # if not, store the value as 'n/a'
        if (sYear.get() == ""):
            lst['year'] = 'n/a'
        else:
            lst['year'] = sYear.get()

        if (sCategory.get() == ""):
            lst['category'] = 'n/a'
        else:
            lst['category'] = sCategory.get()

        if (sID.get() == ""):
            lst['l_id'] = 'n/a'
        else:
            lst['l_id'] = sID.get()

        if (sFname.get() == ""):
            lst['firstname'] = 'n/a'
        else:
            lst['firstname'] = sFname.get()

        if (sSname.get() == ""):
            lst['surname'] = 'n/a'
        else:
            lst['surname'] = sSname.get()

        if (sDOB.get() == ""):
            lst['born'] = 'n/a'
        else:
            lst['born'] = sDOB.get()

        if (sDOD.get() == ""):
            lst['died'] = 'n/a'
        else:
            lst['died'] = sDOD.get()

        if (sBCountry.get() == ""):
            lst['bornCountry'] = 'n/a'
        else:
            lst['borncountry'] = sBCountry.get()

        if (sBCountryCode.get() == ""):
            lst['bornCountryCode'] = 'n/a'
        else:
            lst['bornCountryCode'] = sBCountryCode.get()

        if (sBCity.get() == ""):
            lst['bornCity'] = 'n/a'
        else:
            lst['bornCity'] = sBCity.get()

        if (sDCountry.get() == ""):
            lst['diedCountry'] = 'n/a'
        else:
            lst['diedCountry'] = sDCountry.get()

        if (sDCountryCode.get() == ""):
            lst['diedCountryCode'] = 'n/a'
        else:
            lst['diedCountryCode'] = sDCountryCode.get()

        if (sDCity.get() == ""):
            lst['diedCity'] = 'n/a'
        else:
            lst['diedCity'] = sDCity.get()

        if (sGender.get() == ""):
            lst['gender'] = 'n/a'
        else:
            lst['gender'] = sGender.get()

        # Starting point for the search query
        command_both = '''SELECT DISTINCT laureates.l_id, laureates.firstname, laureates.surname, laureates.born, laureates.died,
                                          laureates.bornCountryCode, laureates.bornCountry, laureates.bornCity, laureates.diedCountryCode,
                                          laureates.diedCountry, laureates.diedCity, laureates.gender, prizes.category, prizes.year
                                      FROM laureates, prizes
                                      WHERE laureates.l_id = prizes.l_id'''

        # Connect to the nobeldata DB and set the cursor
        conn = sqlite3.connect('nobeldata.sqlite')
        cur = conn.cursor()

        # Check if the key belongs to the prize table (year/category)
        # Build the existing query based on key.  Then add the value to the temporary dictionary
        for key, value in lst.items():
            if (key == "year" and value != "n/a"):
                command_both = command_both + " AND year like " + "'" + value + "'"
                temp[key] = value
            if (key == "category" and value != "n/a"):
                command_both = command_both + " AND category like " + "'" + value + "'"
                temp[key] = value
            else:
                if (value != "n/a" and (key != "year" and key != "category")):
                    command_both = command_both + " AND laureates." + key + " like " + "'" + value + "'"
                    temp[key] = value

        # Execute the command
        cur.execute(command_both)
        # Obtain the tuple and store it into an list to send to the display screen
        for tuple in cur:
            sentItems.append(tuple)
            print "GOT: " + tuple[0] + " " + tuple[1] + " " + tuple[2] + " " + tuple[3] + " " + tuple[4]

        # Close connection and open the results page
        conn.close()
        win2(sentItems)

    # Contains the 'About the App' message
    def aboutCallBack():
        tkMessageBox.showinfo("Developers: Christian DeGenova, Garry Dominique",
                              "This Application retrieves the Nobel Prize data dest from an online web service.  It has the ability to execute any CRUD operation.")

    B = Button(top, text="About", command=aboutCallBack).grid(row=1, column=6)

    # Displays confirmation for laureates being added
    def addConfirmCallBack():
        tkMessageBox.showinfo("Added ", "Laureate was added")

    # Display error for many laureates being found
    def deleteError(num):
        tkMessageBox.showinfo("Error",
                              "Too many laureates were found.  Be more specific.  # of Laureates found: " + str(num))

    ####################################
    # Functions to obtain user input to add laureates
    ###################################
    def addParms():
        lst = []  # List to obtain entry input

        if (aYear.get() == ""):
            lst.append('null')
        else:
            lst.append(aYear.get())

        if (aCategory.get() == ""):
            lst.append('null')
        else:
            lst.append(aCategory.get())

        if (aFname.get() == ""):
            lst.append('null')
        else:
            lst.append(aFname.get())

        if (aSname.get() == ""):
            lst.append('null')
        else:
            lst.append(aSname.get())

        if (aDOB.get() == ""):
            lst.append('null')
        else:
            lst.append(aDOB.get())

        if (aDOD.get() == ""):
            lst.append('null')
        else:
            lst.append(aDOD.get())

        if (aBCountry.get() == ""):
            lst.append('null')
        else:
            lst.append(aBCountry.get())

        if (aBCity.get() == ""):
            lst.append('null')
        else:
            lst.append(aBCity.get())

        if (aDCountry.get() == ""):
            lst.append('null')
        else:
            lst.append(aDCountry.get())

        if (aDCity.get() == ""):
            lst.append('null')
        else:
            lst.append(aDCity.get())

        if (aGender.get() == ""):
            lst.append('null')
        else:
            lst.append(aGender.get())
        # Send List to the insert Person method
        insertPerson(lst)

    ########
    # Function to obtain user input and delete laureate
    #########
    def deleteParm():
        lst = {}  # List to obtain entry input
        temp = {}  # List to prepare query
        sentItems = []  # List to be sent out to win2()

        if (dYear.get() == ""):
            lst['year'] = 'n/a'
        else:
            lst['year'] = dYear.get()

        if (dCategory.get() == ""):
            lst['category'] = 'n/a'
        else:
            lst['category'] = dCategory.get()

        if (dID.get() == ""):
            lst['l_id'] = 'n/a'
        else:
            lst['l_id'] = dID.get()

        if (dFname.get() == ""):
            lst['firstname'] = 'n/a'
        else:
            lst['firstname'] = dFname.get()

        if (dSname.get() == ""):
            lst['surname'] = 'n/a'
        else:
            lst['surname'] = dSname.get()

        if (dDOB.get() == ""):
            lst['born'] = 'n/a'
        else:
            lst['born'] = dDOB.get()

        if (dDOD.get() == ""):
            lst['died'] = 'n/a'
        else:
            lst['died'] = dDOD.get()

        if (dBCountry.get() == ""):
            lst['bornCountry'] = 'n/a'
        else:
            lst['borncountry'] = dBCountry.get()

        if (dBCountryCode.get() == ""):
            lst['bornCountryCode'] = 'n/a'
        else:
            lst['bornCountryCode'] = dBCountryCode.get()

        if (dBCity.get() == ""):
            lst['bornCity'] = 'n/a'
        else:
            lst['bornCity'] = dBCity.get()

        if (dDCountry.get() == ""):
            lst['diedCountry'] = 'n/a'
        else:
            lst['diedCountry'] = dDCountry.get()

        if (dDCountryCode.get() == ""):
            lst['diedCountryCode'] = 'n/a'
        else:
            lst['diedCountryCode'] = dDCountryCode.get()

        if (dDCity.get() == ""):
            lst['diedCity'] = 'n/a'
        else:
            lst['diedCity'] = dDCity.get()

        if (dGender.get() == ""):
            lst['gender'] = 'n/a'
        else:
            lst['gender'] = dGender.get()

        # Base query to count the number of laureate based on user input
        command_both = '''SELECT DISTINCT COUNT(*)
                                              FROM laureates, prizes
                                              WHERE laureates.l_id = prizes.l_id'''
        # Base query to select commands
        command_select = '''SELECT DISTINCT laureates.l_id, laureates.firstname, laureates.surname, laureates.born, laureates.died,
                                          laureates.bornCountryCode, laureates.bornCountry, laureates.bornCity, laureates.diedCountryCode,
                                          laureates.diedCountry, laureates.diedCity, laureates.gender, prizes.category, prizes.year
                                                      FROM laureates, prizes
                                                      WHERE laureates.l_id = prizes.l_id'''
        # Connect to DB and set up cursor
        conn = sqlite3.connect('nobeldata.sqlite')
        cur = conn.cursor()

        # Check if the key belongs to the prize table (year/category)
        # Build the existing query based on key.  Then add the value to the temporary dictionary
        for key, value in lst.items():
            if (key == "year" and value != "n/a"):
                command_both = command_both + " AND year like " + "'" + value + "'"
                command_select = command_select + " AND year like " + "'" + value + "'"
                temp[key] = value
            if (key == "category" and value != "n/a"):
                command_both = command_both + " AND category like " + "'" + value + "'"
                command_select = command_select + " AND category like " + "'" + value + "'"
                temp[key] = value
            else:
                if (value != "n/a" and (key != "year" and key != "category")):
                    command_both = command_both + " AND laureates." + key + " like " + "'" + value + "'"
                    command_select = command_select + " AND laureates." + key + " like " + "'" + value + "'"
                    temp[key] = value

        # Execute count query and set count to True
        cur.execute(command_both)
        count = True
        # Check the number of rows, if the number is bigger than 1
        # call an error and set count to false
        for tuple in cur:
            if (tuple[0] > 1):
                deleteError(tuple[0])
                count = False
        # If count remains true, execute SELECT query and add it to the
        # sentItems to send it to the delete window screen
        if (count == True):
            cur.execute(command_select)
            for tuple in cur:
                sentItems.append(tuple)
            conn.close()
            win3(sentItems)

    ####
    # Insert person into DB
    ####
    def insertPerson(lst):
        # Connect to sqlite
        conn = sqlite3.connect('nobeldata.sqlite')
        cur = conn.cursor()
        # Base queries for SELECT and Count
        codeCommand = '''SELECT code
                 FROM country
                 WHERE name like ? '''
        lenCommand = '''SELECT COUNT(*)
                        FROM laureates;'''

        # Execute lenCommand to generate an ID
        cur.execute(lenCommand)
        # Assign variables to list values
        pYear = lst[0]
        pCate = lst[1]
        for tuple in cur:
            pID = tuple[0]
        pID += 100
        print "NEW ID IS: " + str(pID)
        fname = lst[2]
        lname = lst[3]
        dob = lst[4]
        dod = lst[5]
        bcountry = lst[6]
        print bcountry
        # Obtain Country Code based on Country
        cur.execute(codeCommand, (bcountry,))
        for tuple in cur:
            bCode = tuple[0]
        print bCode
        print "Code Obtained"
        bCity = lst[7]
        dCountry = lst[8]
        # Obtain Country Code based on Country
        cur.execute(codeCommand, (dCountry,))
        for tuple in cur:
            dCode = tuple[0]
        print dCode
        print "Code Obtained"
        dCity = lst[9]
        gender = lst[10]
        conn.commit()
        print "INSERTING NEW PERSON"
        # Insert Data into laureates table
        cur.execute('''INSERT INTO laureates (l_id,firstname, surname, born,
        died,bornCountry,bornCountryCode,bornCity,diedCountry,diedCountryCode,diedCity,
        gender) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''', ((pID), (fname), (lname), (dob), (dod),
                                                      (bcountry), (bCode), (bCity), (dCountry),
                                                      (dCode), (dCity), (gender),))
        # Insert Data into prizes table
        cur.execute('''INSERT INTO prizes (l_id,firstname,surname,year,category,share,
        motivation,affiliation_name,affiliation_country,affiliation_city) VALUES (?,?,?,?,?,?,?,?,?,?)''',
                    ((pID), (fname),
                     (lname), (pYear), (pCate), ('null'), ('null'),
                     ('null'), ('null'), ('null'),))

        print fname + " Added"
        conn.commit()
        conn.close()
        addConfirmCallBack()

    # buttons
    button1 = Button(top, text="Search", bg="grey", fg="blue", command=searchParms).grid(row=33, column=1)
    button2 = Button(top, text="Add", bg="grey", fg="green", command=addParms).grid(row=33, column=2)
    button3 = Button(top, text="Delete", bg="grey", fg="red", command=deleteParm).grid(row=33, column=3)

    top.mainloop()


# Window For search results
def win2(lst):
    board = Tkinter.Tk()
    board.title("Window 2")

    tree = ttk.Treeview(board)
    tree["columns"] = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14")
    tree.column("0", width=90)
    tree.column("1", width=90)
    tree.column("2", width=90)
    tree.column("3", width=90)
    tree.column("4", width=90)
    tree.column("5", width=90)
    tree.column("6", width=90)
    tree.column("7", width=90)
    tree.column("8", width=90)
    tree.column("9", width=90)
    tree.column("10", width=90)
    tree.column("11", width=90)
    tree.column("12", width=90)
    tree.column("13", width=90)
    tree.column("14", width=90)

    tree.heading("0", text='ID')
    tree.heading("1", text="First Name")
    tree.heading("2", text="Sur Name")
    tree.heading("3", text="DOB")
    tree.heading("4", text="DOD")
    tree.heading("5", text="Code (Born)")
    tree.heading("6", text="Country Born")
    tree.heading("7", text="City")
    tree.heading("8", text="Code (Died)")
    tree.heading("9", text="Country Died")
    tree.heading("10", text="City")
    tree.heading("11", text="Gender")
    tree.heading("12", text="Prize Category")
    tree.heading("13", text="Prize Years")

    # Insert Data into tree for each person
    for item in lst:
        tree.insert('', 'end', values=(
        item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11],
        item[12], item[13]))

    # Display tree
    tree.pack()
    board.mainloop()


# Window for deleteing laureates
def win3(lst):
    root = Tkinter.Tk()
    root.title("Window 3")
    winLst = lst
    tree = ttk.Treeview(root)
    tree["columns"] = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14")
    tree.column("0", width=90)
    tree.column("1", width=90)
    tree.column("2", width=90)
    tree.column("3", width=90)
    tree.column("4", width=90)
    tree.column("5", width=90)
    tree.column("6", width=90)
    tree.column("7", width=90)
    tree.column("8", width=90)
    tree.column("9", width=90)
    tree.column("10", width=90)
    tree.column("11", width=90)
    tree.column("12", width=90)
    tree.column("13", width=90)
    tree.column("14", width=90)

    tree.heading("0", text='ID')
    tree.heading("1", text="First Name")
    tree.heading("2", text="Sur Name")
    tree.heading("3", text="DOB")
    tree.heading("4", text="DOD")
    tree.heading("5", text="Code (Born)")
    tree.heading("6", text="Country Born")
    tree.heading("7", text="City")
    tree.heading("8", text="Code (Died)")
    tree.heading("9", text="Country Died")
    tree.heading("10", text="City")
    tree.heading("11", text="Gender")
    tree.heading("12", text="Prize Category")
    tree.heading("13", text="Prize Years")

    # Insert data into tables and display
    for item in lst:
        tree.insert('', 'end', values=(
        item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11],
        item[12], item[13]))
    tree.pack()

    # Function to delete the laureate's data from laureate and prize tables based on query.
    def deleteLaureate():
        conn = sqlite3.connect('nobeldata.sqlite')
        cur = conn.cursor()
        command1 = '''DELETE FROM laureates'''
        command2 = '''DELETE FROM prizes'''
        for item in winLst:
            command1 = command1 + "  WHERE l_id like " + item[0] + " AND firstname like " + "'" + item[1] + "'"
            command2 = command2 + "  WHERE l_id like " + item[0] + " AND firstname like " + "'" + item[1] + "'"
        print command1
        cur.execute(command1)
        cur.execute(command2)
        conn.commit()
        conn.close()
        root.destroy()

    # Delete Button
    testButton = Button(root, text="Delete", bg="grey", fg="red", command=deleteLaureate)
    testButton.pack()
    root.mainloop()


# Display Main Window on startup
win1()

from tkinter import *
from temp import mainWindow
import sqlite3
from tkinter import  messagebox
from temp import loginOrSignUp2nd
import smtplib as s
from PIL import ImageTk,Image
from temp import sendFeedbackWindow
from temp import aboutDeveloperWindow

def clear(root):
    list = root.grid_slaves()
    for l in list:
        l.grid_forget()
        
def saveChanges(ID,autoLog,name,loc,password,email):
    conn=sqlite3.connect("temp/userDetails.db")
    c=conn.cursor()
    c.execute("""UPDATE details SET
        autoLogin= :autoLog,   
        name= :name,
        location= :loc,
        password= :password,
        email= :email
        WHERE oid= :oid""",
        {
            'autoLog' : autoLog,
            'name' : name,
            'loc' : loc,
            'password' : password,
            'email' : email,

            'oid' : ID
        })
    conn.commit()
    conn.close()

def aboutDeveloper(root,ID):
    aboutDeveloperWindow.main(root, ID)

def sendFeedback(root,ID):
    sendFeedbackWindow.main(root,ID)

def changePasswordSubmit(tempRoot,ID, oldPass, newPass):
    if len(newPass)!=0 and oldPass!=newPass:
        conn=sqlite3.connect("temp/userDetails.db")
        c=conn.cursor()
        c.execute("SELECT *, oid FROM details")
        records=c.fetchall()
        for record in records:
            if record[5]==int(ID):
                realOldPass=record[3]
                autoLog=record[0]
                name=record[1]
                loc=record[2]
                email=record[4]
                break
        if realOldPass==oldPass:
            saveChanges(ID,autoLog,name,loc,newPass,email)
            messagebox.showinfo("PASSWORD CHANGED!!!", "Password of your account has successfully changed!!!")
            tempRoot.destroy()
        else:
            messagebox.showerror("ERROR!!!", "Old password doesn't match!!!")
            tempRoot.destroy()
        conn.commit()
        conn.close()
    else:
        if len(newPass)==0:
            messagebox.showerror("ERROR!!!", "Enter a Valid New Password!!!")
            tempRoot.destroy()
        else:
            messagebox.showerror("ERROR!!!", "New Password can't be same as Old Password!!!")
            tempRoot.destroy()

def changePassword(root,ID):
    tempRoot=Tk()
    width=500
    height=365
    screen_width=tempRoot.winfo_screenwidth()
    screen_height=tempRoot.winfo_screenheight()
    x_coordinate=(screen_width/2)-(width/2)
    y_coordinate=(screen_height/2)-(height/2)-40
    tempRoot.geometry("%dx%d+%d+%d" % (width, height, x_coordinate, y_coordinate))
    tempRoot.minsize(width,height)
    tempRoot.maxsize(width,height)
    tempRoot.title("Change Password | Fight Against COVID-19")
    tempRoot.iconbitmap("temp/loginPageIcon.ico")
    tempRoot.configure(background='#000000')

    #old pass label
    oldL=Label(tempRoot,
                       text="Enter Your Old Password",
                       bg="black",
                       fg="white",
                       font=("Courier", 20))
    oldL.pack(pady=(30,0))

    #old pass entry
    oldE=Entry(tempRoot,
            font=("Courier", 18),
            cursor='target')
    oldE.focus_set()
    oldE.pack(pady=(20,0))

    #new pass label
    newL=Label(tempRoot,
                       text="Enter Your New Password",
                       bg="black",
                       fg="white",
                       font=("Courier", 20))
    newL.pack(pady=(30,0))

    #new pass entry
    newE=Entry(tempRoot,
            font=("Courier", 18),
            cursor='target')
    newE.pack(pady=(20,0))

    #submit button
    submit=Button(tempRoot,
                          text="Change Password!!!",
                          font=("Courier", 18),
                          bg="green",
                  command=lambda:changePasswordSubmit(
                      tempRoot,
                        ID,
                        oldE.get().strip(),
                        newE.get().strip()
                      )
                          )
    submit.pack(pady=(40,0))

    tempRoot.mainloop()

def forgetPassword(root,ID):
    try:
        ob=s.SMTP("smtp.gmail.com",587)
        ob.starttls()
        ob.login('loginemailconfirmation@gmail.com','*****')
        subject="Your Password Of 'Fight Against COVID-19 Application'"

        conn=sqlite3.connect("temp/userDetails.db")
        c=conn.cursor()
        c.execute("SELECT *, oid FROM details")
        records=c.fetchall()
        for record in records:
            if record[5]==int(ID):
                name=record[1]
                password=record[3]
                email=record[4]
                break
        body="Hi {},\nPassword Of Your Account Is: {}".format(name,password)
        message="Subject:{}\n\n{}".format(subject,body)
        listOfAddress=[email]

        ob.sendmail("loginemailconfirmation@gmail.com",listOfAddress,message)
        ob.quit()
        messagebox.showinfo("CHECK THE REGISTERED EMAIL!!!", "We have sent your password in your registered email, check it and then change the password by 'Change Password' section...")
        conn.commit()
        conn.close()
    except:
        messagebox.showerror("ERROR!!!", "Please check your internet connection!!!")
        root.destroy()
        
def logoutClicked(root,ID):
    conn=sqlite3.connect("temp/userDetails.db")
    c=conn.cursor()

    c.execute("SELECT * FROM details WHERE oid = "+ID)
    records=c.fetchall()

    for record in records:
        autoLog='NO'
        name=record[1]
        loc=record[2]
        password=record[3]
        email=record[4]

    saveChanges(ID,autoLog,name,loc,password,email)
    messagebox.showinfo("Successfully Logged Out!!!", "Hi {}, \nYou have successfully logged out from your account!!!".format(name))
    conn.commit()
    conn.close()
    loginOrSignUp2nd.main(root)

def main(root, ID):
    clear(root)
    width=600
    height=600
    screen_width=root.winfo_screenwidth()
    screen_height=root.winfo_screenheight()
    x_coordinate=(screen_width/2)-(width/2)
    y_coordinate=(screen_height/2)-(height/2)-40
    root.geometry("%dx%d+%d+%d" % (width, height, x_coordinate, y_coordinate))
    root.minsize(width,height)
    root.maxsize(width,height)
    root.configure(background='black')
    root.title("Manage Account | Fight Against COVID-19")
    root.iconbitmap("temp/manageAccIcon.ico")

    #back button
    b=Button(root,
             text="<< Back",
             font=("Courier", 15),
             bg="#49A",
             fg="white",
             command=lambda:mainWindow.main(root,ID))
    b.pack(pady=(15,0))

    #personal info
    frame=LabelFrame(root,
                text="Personal Informations",
                     font=("Courier b", 15),
                     bg='#dda2d5',
                     padx=10,pady=10)
    frame.pack(pady=(15,0))

    conn=sqlite3.connect("temp/userDetails.db")
    c=conn.cursor()
    c.execute("SELECT *, oid FROM details")
    records=c.fetchall()

    for record in records:
        if record[5]==int(ID):
            autoLogin=record[0]
            name=record[1]
            location=record[2]
            password=record[3]
            email=record[4]
            break

    #name
    nameL=Label(frame,
                text="Name : "+name,
                bg='#dda2d5',
                font=("Courier", 15)
                )
    nameL.pack()

    #location
    locL=Label(frame,
                text="Location : "+location,
                bg='#dda2d5',
                font=("Courier", 15)
                )
    locL.pack(padx=(0,58))

    #Email ID
    emailL=Label(frame,
                text="Email : "+email,
                bg='#dda2d5',
                font=("Courier", 13)
                )
    emailL.pack(padx=(107,0))

    #helpline
    if location[0]=='A':
        if location[1]=='n':
            if location[3]=='h':
                number="0866-2410978"
            else:
                number=="03192-232102"
        elif location[1]=='r':
            number="9436055743"
        else:
            number="6913347770"
    elif location[0]=='B':
        number="104"
    elif location[0]=='C':
        if location[2]=='h':
            number="104"
        else:
            number="9779558282"
    elif location[0]=='D':
        if location[1]=='a':
            number="104"
        else:
            number="011-22307145"
    elif location[0]=="G":
        number="104"
    elif location[0]=="H":
        if location[1]=='a':
            number="8558893911"
        else:
            number="104"
    elif location[0]=='J':
        if location[1]=='a':
            number="1912520982, 0194-2440283"
        else:
            number="104"
    elif location[0]=='K':
        if location[1]=='a':
            number="104"
        else:
            number="0471-2552056"
    elif location[0]=='M':
        if location[2]=='d':
            number="104"
        elif location[2]=='h':
            number="020-26127394"
        elif location[2]=='n':
            number="3852411668"
        elif location[2]=='g':
            number="108"
        else:
            number="102"
    elif location[0]=='N':
        number="7005539653"
    elif location[0]=='O':
        number="9439994859"
    elif location[0]=='L':
        if location[2]=='d':
            number="1982256462"
        else:
            number="104"
    elif location[0]=='P':
        number="104"
    elif location[0]=='R':
        number="0141-2225624"
    elif location[0]=='S':
        number="104"
    elif location[0]=='T':
        if location[1]=='a':
            number="044-29510500"
        elif location[1]=='e':
            number="104"
        else:
            number="0381-2315879"
    elif location[0]=="U":
        if location[6]=="k":
            number="104"
        else:
            number="18001805145"
    else:
        number="3323412600, 1800313444222"
            
    helpL=Label(frame,
                text="COVID-19 Helpline : "+number,
                font=("Courier", 15),
                bg='#dda2d5'
                )
    helpL.pack()

    #All over helpline frame
    frame2=LabelFrame(root,
                text="Helplines From Government Of India",
                     font=("Courier b", 15),
                     bg='#dda2d5',
                     padx=20,pady=10)
    frame2.pack(pady=(15,0))

    #help line
    allHelpL=Label(frame2,
                text="Indian Helpline : +91-11-23978046",
                font=("Courier", 15),
                bg='#dda2d5'
                )
    allHelpL.pack()
    
    #toll free
    tollF=Label(frame2,
                text="Toll Free Helpline : 1075",
                font=("Courier", 15),
                bg='#dda2d5'
                )
    tollF.pack(padx=(0,167))

    #whatsapp
    whatL=Label(frame2,
                text="WhatsApp Number : 9013151515",
                font=("Courier", 15),
                bg='#dda2d5'
                )
    whatL.pack(padx=(0,57))

    #Technical query
    techL=Label(frame2,
                text="Technical Query : technicalquery.covid19@gov.in",
                font=("Courier", 14),
                bg='#dda2d5'
                )
    techL.pack()

    #indian mail
    mailL=Label(frame2,
                text="Email ID : ncov2019@gov.in, ncov2019@gmail.com",
                font=("Courier", 14),
                bg='#dda2d5'
                )
    mailL.pack()

    #forget password
    forget=Button(root,
             text="Forget Password",
             font=("Courier b", 15),
             bg="green",
             fg="white",
                  padx=6,
                  command=lambda:forgetPassword(root,ID)
                  )
    forget.pack(pady=(15,0))

    #change pass
    change=Button(root,
             text="Change Password",
             font=("Courier b", 15),
             bg="#c7be09",
             fg="white",
                  command=lambda:changePassword(root,ID)
                  )
    change.pack(pady=(12,0))

    #send feedback
    send=Button(root,
             text="Send Feedback",
             font=("Courier b", 15),
             bg="blue",
             fg="white",
                command=lambda:sendFeedback(root,ID)
                  )
    send.pack(side=LEFT,padx=(30,0))

    #about developer
    developer=Button(root,
             text="About Developer",
             font=("Courier b", 15),
             bg="#f79004",
             fg="white",
                     padx=8,
                     command=lambda:aboutDeveloper(root,ID)
                  )
    developer.pack(side=LEFT,padx=(25,0))
    
    #logout
    logout=Button(root,
             text="LogOut",
             font=("Courier b", 15),
             bg="red",
             fg="white",
                  padx=35,
                  command=lambda:logoutClicked(root,ID)
                  )
    logout.pack( side=RIGHT,padx=(0,30))

    conn.commit()
    conn.close()

if __name__=="__main__":
    main(root,ID)

from tkinter import *
from temp import loginOrSignUp2nd
from tkinter import  messagebox
import ttk
import smtplib as s
import random
import sqlite3
from temp import mainWindow

def insertIntoDatabase(tempRoot,root,name, loc, password, email):
    conn=sqlite3.connect("temp/userDetails.db")
    c=conn.cursor()
    c.execute("INSERT INTO details VALUES (:autoLogin, :name, :location, :password, :email)",
                {
                'autoLogin':'YES',
                'name':name,
                'location':loc,
                'password':password,
                'email':email
                }
          )
    conn.commit()
    conn.close()
    messagebox.showinfo("CONGRATULATIONS!!!", "Hi {}, \nYour account has been created successfully!!!".format(name))
    tempRoot.destroy()

    conn=sqlite3.connect("temp/userDetails.db")
    c=conn.cursor()
    c.execute("SELECT *, oid FROM details")
    records=c.fetchall()

    for record in records:
        if name==str(record[1]) and loc==str(record[2]) and password==str(record[3]) and email==str(record[4]):
            uniqueID=record[5]
            mainWindow.main(root,uniqueID)

    conn.commit()
    conn.close()

def checkIfCodeMatchs(actualCode,code,tempRoot,root,name, loc, password, email):
    if actualCode==int(code):
        insertIntoDatabase(tempRoot,root,name, loc, password, email)
    else:
        messagebox.showerror("ERROR!!!", "Your code doesn't match!!!")
        tempRoot.destroy()
        main(root)

def query(email):
    conn=sqlite3.connect("temp/userDetails.db")
    c=conn.cursor()

    c.execute("SELECT *, oid FROM details")
    records=c.fetchall()
    
    if len(records)==0:
        return True
    else:
        for record in records:
            if email==str(record[4]):
                return False
                break
        else:
            return True
    conn.commit()
    conn.close()

def sendmail(root,name, loc, password, email):
    try:
        result=query(email)
        if result:
            videoLink="https://youtu.be/ZPAEU0tlUxk"
            
            ob=s.SMTP("smtp.gmail.com",587)
            ob.starttls()
            ob.login('loginemailconfirmation@gmail.com','*****')

            subject="Confirmation Code For 'Fight Against COVID-19'"
            rangeOfCode=list(range(100001,999999+1))
            code=random.choice(rangeOfCode)
            videoLine="Click the link to watch the full guide of 'Fight Against COVID-19' desktop application: "+videoLink
            body="Hi "+name+","+"\nThanks for selecting us ;)\nYour Confirmation Code: "+str(code)+"\n\n"+videoLine+"\n\nThank you.\n#stayhomefightagainstcorona"

            message="Subject:{}\n\n{}".format(subject,body)

            listOfAddress=[email]

            ob.sendmail("loginemailconfirmation@gmail.com",listOfAddress,message)
            ob.quit()

            #verification window
            tempRoot=Tk()
            width=400
            height=300
            screen_width=tempRoot.winfo_screenwidth()
            screen_height=tempRoot.winfo_screenheight()
            x_coordinate=(screen_width/2)-(width/2)
            y_coordinate=(screen_height/2)-(height/2)-40
            tempRoot.geometry("%dx%d+%d+%d" % (width, height, x_coordinate, y_coordinate))
            tempRoot.minsize(width,height)
            tempRoot.maxsize(width,height)
            tempRoot.title("Email Verification...")
            tempRoot.iconbitmap("temp/verificationIcon.ico")
            tempRoot.configure(background='#000000')
            
            #label
            varL=Label(tempRoot,
                       text="Enter The \nVerification Code\n(Please Check Email)",
                       bg="black",
                       fg="white",
                       font=("Courier", 20))
            varL.pack(pady=30)

            #code entry
            codeE=Entry(tempRoot,
                              font=("Courier", 18),
                              cursor='target')
            codeE.pack(pady=(0,40))
            codeE.focus_set()

            #submit button
            submit=Button(tempRoot,
                          text="Create Account!!!",
                          font=("Courier", 18),
                          bg="green",
                          command=lambda:checkIfCodeMatchs(
                              code,
                              codeE.get().strip(),
                              tempRoot,
                              root,name, loc, password, email
                              ))
            submit.pack()

            tempRoot.mainloop()
        else:
            messagebox.showerror("ERROR!!!", "The Email ID is already in use!!!")
            main(root)
    except:
        messagebox.showerror("ERROR!!!", "Please Check Your Internet Connection!!!\nOr, are your given informations corret??")
        root.destroy()


def submittion(root,name, loc, password, email):
    if len(name)!=0:
        if len(loc)!=0:
            if len(password)!=0:
                if len(email)!=0:
                    sendmail(root,name, loc, password, email)
                else:
                    messagebox.showwarning("WARNING!!!", "Please Enter Your Email ID!!!")
                    main(root)
            else:
                messagebox.showwarning("Warning!!!", "Please Enter Your Password!!!")
                main(root)
        else:
            messagebox.showwarning("Warning!!!", "Please Enter Your Location!!!")
            main(root)
    else:
        messagebox.showwarning("Warning!!!", "Please Enter Your Name!!!")
        main(root)

def clear(root):
    list = root.pack_slaves()
    for l in list:
        l.pack_forget()

def main(root):
    clear(root)
    root.title("New User | Sign Up | Fight Against COVID-19")
    root.iconbitmap("temp/newAccountPageIcon.ico")

    #back button
    b=Button(root,
             text="<< Back",
             font=("Courier", 18),
             bg="#49A",
             fg="white",
             command=lambda:loginOrSignUp2nd.main(root))
    b.pack(pady=(15,10))

    #mandatory
    mainT="User Have To Fill \nAll The Informations"
    mainL=Label(root,
                text=mainT,
                font=("Courier", 18),
                bg="black",
                 fg="red",)
    mainL.pack(pady=(0,20))
    
    #name
    nameL=Label(root,
                      text="Enter Name",
                      font=("Courier", 18),
                      bg="black",
                      fg="white")
    nameL.pack(pady=(0,10))
    
    nameE=Entry(root,
                      font=("Courier", 20),
                      cursor='target')
    nameE.focus_set()
    nameE.pack(pady=(0,20))
    
    #location
    listOfStates=["Andhra Pradesh",
                             "Arunachal Pradesh",
                             "Assam",
                             "Bihar",
                             "Chhattisgarh",
                             "Goa",
                             "Gujarat",
                             "Haryana",
                             "Himachal Pradesh",
                             "Jharkhand",
                             "Karnataka",
                             "Kerala",
                             "Madhya Pradesh",
                             "Maharashtra",
                             "Manipur",
                             "Meghalaya",
                             "Mizoram",
                             "Nagaland",
                             "Odisha",
                             "Punjab",
                             "Rajasthan",
                             "Sikkim",
                             "Tamil Nadu",
                             "Telangana",
                             "Tripura",
                             "Uttarakhand",
                             "Uttar Pradesh",
                             "West Bengal",
                             "Andaman and Nicobar Islands",
                             "Chandigarh",
                             "Dadra and Nagar Haveli and Daman & Diu",
                             "Delhi",
                             "Jammu & Kashmir",
                             "Ladakh",
                             "Lakshadweed",
                             "Puducherry"]
    l=Label(root,
                      text="Enter Your Location",
                      font=("Courier", 18),
                      bg="black",
                      fg="white")
    l.pack(pady=(0,10))
    
    variable = StringVar()
    w = ttk.Combobox(root,
                     state="readonly",
                     font=("Courier", 20),
                     textvariable=variable,
                     values=listOfStates,
                     width=19)
    w.pack(pady=(0,20))

    #password
    passL=Label(root,
                      text="Enter Password",
                      font=("Courier", 18),
                      bg="black",
                      fg="white")
    passL.pack(pady=(0,10))

    passE=Entry(root,
                      font=("Courier", 20),
                      cursor='target')
    passE.pack(pady=(0,20))

    #email
    emailL=Label(root,
                      text="Enter Your Email ID",
                      font=("Courier", 18),
                      bg="black",
                      fg="white")
    emailL.pack(pady=(0,10))

    emailE=Entry(root,
                      font=("Courier", 20),
                      cursor='target')
    emailE.pack(pady=(0,20))

    #submit
    submit=Button(root,
                  text="Submit",
                 font=("Courier", 18),
                 bg="green",
                 command=lambda:submittion(
                     root,
                     nameE.get().strip(),
                     variable.get(),
                     passE.get().strip(),
                     emailE.get().strip()
                     ))
    submit.pack()
    
if __name__=="__main__":
    main(root)

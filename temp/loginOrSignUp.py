from tkinter import *
from PIL import ImageTk,Image
from temp import signUp
import sqlite3
from tkinter import  messagebox
from temp import loginOrSignUp2nd
from temp import mainWindow

def query(root,email,password):
    conn=sqlite3.connect("temp/userDetails.db")
    c=conn.cursor()
    c.execute("SELECT *, oid FROM details")
    records=c.fetchall()
    if len(records)==0:
        return (False, False, False)
    else:
        for record in records:
            if email==str(record[4]) and password==str(record[3]):
                return (True, str(record[1]), str(record[5]))
                break
        else:
            return (False, False, False)
    conn.commit()
    conn.close()

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

def loginChecking(root,email,password):
    result,n,ID=query(root,email,password)
    if result:
        messagebox.showinfo("WELCOME BACK!!!", "Welcome back {},\nWish you a healthy day from 'Fight Against COVID-19'".format(n))
        respond=messagebox.askyesno("Getting Permission!!!", "Enable Auto Login Feature?")
        if respond==1:
            conn=sqlite3.connect("temp/userDetails.db")
            c=conn.cursor()

            c.execute("SELECT * FROM details WHERE oid = "+ID)
            records=c.fetchall()

            for record in records:
                autoLog='YES'
                name=record[1]
                loc=record[2]
                password=record[3]
                email=record[4]

            saveChanges(ID,autoLog,name,loc,password,email)
            conn.commit()
            conn.close()
            
        mainWindow.main(root,ID)
    else:
        messagebox.showerror("ERROR!!!", "Email ID or Password is wrong!!!")
        loginOrSignUp2nd.main(root)

def main(root):
    root.destroy()
    root = Tk()
    width=500
    height=600
    screen_width=root.winfo_screenwidth()
    screen_height=root.winfo_screenheight()
    x_coordinate=(screen_width/2)-(width/2)
    y_coordinate=(screen_height/2)-(height/2)-40
    root.geometry("%dx%d+%d+%d" % (width, height, x_coordinate, y_coordinate))
    root.minsize(width,height)
    root.maxsize(width,height)

    root.title("Login Or Sign Up | Fight Against COVID-19")
    root.iconbitmap("temp/loginPageIcon.ico")
    root.configure(background='#000000')

    #uper image
    my_img1=ImageTk.PhotoImage(Image.open("temp/1.png"))
    my_label=Label(image=my_img1)
    my_label.pack(pady=(15,20))

    #taking email id
    userIdlabel=Label(root,
                      text="Enter Email ID",
                      font=("Courier", 18),
                      bg="black",
                      fg="white")
    userIdlabel.pack(pady=(0,15))

    userIdEntry=Entry(root,
                      font=("Courier", 20),
                      cursor='target')
    userIdEntry.focus_set()
    userIdEntry.pack(pady=(0,20))

    #taking password
    label=Label(root,
                      text="Enter Password",
                      font=("Courier", 18),
                      bg="black",
                      fg="white")
    #  view="*"    ####
    label.pack(pady=15)
    
    entry=Entry(root,font=("Courier", 20),cursor="target")
    entry.pack(pady=(0,25))

    #login button
    b=Button(root,
             text="Login",
             font=("Courier", 12),
             bg="green",
             command=lambda:loginChecking(
                 root,
                userIdEntry.get().strip(),
                entry.get().strip()
                 ))
    b.pack(pady=(0,20))

    #signup button
    s=Button(root,
             text="New User? Sign Up Here!!!",
             font=("Courier", 12),
             bg="#49A",
             command=lambda:signUp.main(root))
    s.pack()

    root.mainloop()

if __name__=="__main__":
    main(root)

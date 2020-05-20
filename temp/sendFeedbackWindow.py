from tkinter import *
from temp import manageAccountWindow2nd
from PIL import ImageTk,Image
import smtplib as s
from tkinter import  messagebox
from temp import manageAccountWindow2nd
import sqlite3

def clear(root):
    list = root.pack_slaves()
    for l in list:
        l.pack_forget()

def sendmail(root, ID, feedBack):
    try:
        ob=s.SMTP("smtp.gmail.com",587)
        ob.starttls()
        ob.login('loginemailconfirmation@gmail.com','*****')

        conn=sqlite3.connect("temp/userDetails.db")
        c=conn.cursor()
        c.execute("SELECT *, oid FROM details")
        records=c.fetchall()

        for record in records:
            if record[5]==int(ID):
                name=record[1]
                location=record[2]
                password=record[3]
                email=record[4]
        conn.commit()
        conn.close()
        
        subject="Feedback From Of {}".format(name)
        body=feedBack
        message="Subject:{}\n\n{}".format(subject,body)

        listOfAddress=['collectingdata211@gmail.com']

        ob.sendmail("loginemailconfirmation@gmail.com",listOfAddress,message)
        ob.quit()
        return (True, name)
    except: 
        messagebox.showerror("ERROR!!!", "Please check your internet connection")
        return (False, False)

def submitClicked(root, ID, feedBack):
    result, tempName=sendmail(root, ID, feedBack)
    if result:
        messagebox.showinfo("Thanks!!!", "Thank you {} for your feedback!!!".format(tempName))
        manageAccountWindow2nd.main(root,ID)

def main(root,ID):
    clear(root)
    root.title("Feedback Us | Fight Against COVID-19")
    root.iconbitmap("temp/feedback.ico")
    
    #back button
    b=Button(root,
             text="<< Back",
             font=("Courier", 15),
             bg="#49A",
             fg="white",
             command=lambda:manageAccountWindow2nd.main(root,ID))
    b.pack(pady=(15,0))

    #heading img
    load=Image.open('temp/feedback.jpg')
    render=ImageTk.PhotoImage(load)
    img=Label(root, image=render)
    img.image = render
    img.pack(padx=10,pady=(17,0))

    #TEXT box
    textFrame=Frame(root, bg="black")
    scroll=Scrollbar(textFrame)
    scroll.pack(side=RIGHT, fill=Y, padx=(0,10))
    ans=Text(textFrame,
            padx=10, pady=10,
             font=("Courier", 12),
             height=10,
             yscrollcommand=scroll.set,
             wrap=WORD)
    scroll.config(command=ans.yview)
    ans.pack(padx=(10,0))
    ans.focus_set()
    textFrame.pack(pady=(20,0))

    #sumbit button
    submit=Button(root,
                  text="Submit Your Feedback",
                  font=("Courier", 15),
                  bg="green",
                  fg="white",
                  command=lambda:submitClicked(root, ID, ans.get("1.0","end").strip()))
    submit.pack(pady=(13,0))
    
if __name__=="__main__":
    main(root,ID)

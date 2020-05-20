from tkinter import *
from temp import mainWindow
from PIL import ImageTk,Image
import wikipedia
import webbrowser
from tkinter import  messagebox

def clear(root):
    list = root.grid_slaves()
    for l in list:
        l.grid_forget()

def WHO():
    try:
        webbrowser.open("https://www.who.int/emergencies/diseases/novel-coronavirus-2019?gclid=CjwKCAjw5Ij2BRBdEiwA0Frc9dL72MEHgVUShOlN3yxo--bIAa7rYDbR8J0z3GIU0BpDRqqRsKMTsBoCzsAQAvD_BwE")
    except:
        messagebox.showerror("ERROR!!!", "Please check your Internet Connection!!!")
        root.destroy()

def INDIA():
    try:
        webbrowser.open("https://www.mygov.in/covid-19")
    except:
        messagebox.showerror("ERROR!!!", "Please check your Internet Connection!!!")
        root.destroy()

def searchClicked(topic, ans):
    try:
        ans.config(state=NORMAL)
        answer=wikipedia.summary(topic)
        ans.delete("1.0", END)
        ans.insert(INSERT, answer)
    except:
        ans.config(state=NORMAL)
        ans.delete("1.0", END)
        ans.insert(INSERT, "Sorry!!! Page not found!!!")
    ans.config(state=DISABLED)

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
    root.title("Important Sites | Fight Against COVID-19")
    root.iconbitmap("temp/enableNotificationIcon.ico")

    #back button
    b=Button(root,
             text="<< Back",
             font=("Courier", 15),
             bg="#49A",
             fg="white",
             command=lambda:mainWindow.main(root,ID))
    b.pack(pady=(15,0))

    #upper frame
    upFrame=LabelFrame(root,
                text="Quick Search",
                     font=("Courier b", 15),
                       fg="white",
                     bg='black',
                     padx=25,pady=15)
    upFrame.pack(pady=(15,0))

    sE=Entry(upFrame,
             font=("Courier", 20),
             width=25)
    sE.pack(pady=(15,0))
    sE.focus_set()
    
    #middle Frame
    mFrame=LabelFrame(root,
                      text="Search Result",
                      font=("Courier b", 15),
                       fg="white",
                     bg='black',
                     padx=25,pady=15)
    mFrame.pack(pady=(15,0),padx=(15,15))

    textFrame=Frame(mFrame, bg="black")
    scroll=Scrollbar(textFrame)
    scroll.pack(side=RIGHT, fill=Y)
    ans=Text(textFrame,
            padx=10, pady=10,
             font=("Courier", 15),
             bg="#dda2d5",
             fg="black",
             height=7,
             yscrollcommand=scroll.set,
             wrap=WORD
             )
    scroll.config(command=ans.yview)
    ans.pack()
    ans.config(state=DISABLED)
    textFrame.pack()

    searchB=Button(upFrame,
             text="Search",
             font=("Courier", 15),
             bg="green",
             fg="black",
             command=lambda:searchClicked(sE.get().strip(),
                                          ans))
    searchB.pack(pady=(15,0))

    #lower portion
    who=Button(root,
               text="View WHO\nWebsite",
             font=("Courier b", 15),
             bg="blue",
             fg="white",
               command=WHO
             )
    who.pack(side=LEFT, padx=(150,0))

    ind=Button(root,
               text="View MyGov\nWebsite",
             font=("Courier b", 15),
             bg="orange",
             fg="white",
               command=INDIA
             )
    ind.pack(side=RIGHT, padx=(0,135))

if __name__=="__main__":
    main(root, ID)

from tkinter import *
from PIL import ImageTk,Image
from temp import manageAccountWindow
from temp import impSitesWindow
from temp import dataAnalysisWindow

def clear(root):
    list = root.pack_slaves()
    for l in list:
        l.pack_forget()

def main(root,ID):
    clear(root)
    width=352
    height=301
    screen_width=root.winfo_screenwidth()
    screen_height=root.winfo_screenheight()
    x_coordinate=(screen_width/2)-(width/2)
    y_coordinate=(screen_height/2)-(height/2)-40
    root.geometry("%dx%d+%d+%d" % (width, height, x_coordinate, y_coordinate))
    root.minsize(width,height)
    root.maxsize(width,height)
    
    root.title("Main Window")
    root.iconbitmap("temp/anotherIcon.ico")
    root.configure(background='#a29d72')
    

    #Data Analysis
    first=Button(root,
                 text="Data\nAnalysis",
                 font=("Courier", 20),
                 bg="#7bade5",
                 fg="black",
                 activeforeground="white",
                 activebackground="black",
                 bd=5,
                 command=lambda:dataAnalysisWindow.main(root,ID)
        )
    first.grid(row=0,column=0,
               padx=(10,0), pady=(7,0))

    #Important Sites
    second=Button(root,
                 text="Important\nSites",
                 font=("Courier", 20),
                 bg="#dda000",
                 fg="black",
                 activeforeground="white",
                 activebackground="black",
                  bd=5,
                  command=lambda:impSitesWindow.main(root,ID)
        )
    second.grid(row=1,column=1,columnspan=2,
                padx=(0,0),pady=(10,0))

    #manage account
    third=Button(root,
                 text="Manage\nAccount",
                 font=("Courier", 20),
                 bg="#00d177",
                 fg="black",
                 activeforeground="white",
                 activebackground="black",
                 bd=5,
                 command=lambda:manageAccountWindow.main(root,ID)
        )
    third.grid(row=2,column=0,
               padx=(10,0), pady=(10,0))

if __name__=="__main__":
    main(root,ID)

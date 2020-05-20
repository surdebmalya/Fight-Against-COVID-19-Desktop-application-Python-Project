from tkinter import *
from temp import manageAccountWindow2nd
from PIL import ImageTk,Image
import webbrowser
from tkinter import  messagebox

def clear(root):
    list = root.pack_slaves()
    for l in list:
        l.pack_forget()

def blogShow(root,ID):
    try:
        webbrowser.open("https://dsasanengineer.blogspot.com/")
    except:
        messagebox.showerror("ERROR!!!", "Please check your Internet Connection!!!")
        root.destroy()
    
def main(root, ID):
    clear(root)
    root.title("About Developer | Fight Against COVID-19")
    root.iconbitmap("temp/developerIcon.ico")

    #back button
    b=Button(root,
             text="<< Back",
             font=("Courier", 15),
             bg="#49A",
             fg="white",
             command=lambda:manageAccountWindow2nd.main(root, ID))
    b.pack(pady=(20,0))

    #heading img
    load=Image.open('temp/aboutDeveloperImg.jpg')
    render=ImageTk.PhotoImage(load)
    img=Label(root, image=render)
    img.image = render
    img.pack(pady=(25,0))

    #text box
    file=open("temp/author.txt", "r")
    about=file.read()
    textFrame=Frame(root, bg="black")
    scroll=Scrollbar(textFrame)
    scroll.pack(side=RIGHT, fill=Y,padx=(0,50))
    ans=Text(textFrame,
            padx=10, pady=10,
             font=("Courier", 15),
             bg="#66e07d",
             fg="black",
             height=8,
             yscrollcommand=scroll.set,
             wrap=WORD
             )
    scroll.config(command=ans.yview)
    ans.pack(padx=(72,0))
    textFrame.pack(pady=(20,0))
    ans.insert("1.0", about)
    ans.config(state=DISABLED)
    
    #blog button
    blog=Button(root,
             text="See My Blog",
             font=("Courier", 15),
             bg="#e47f05",
             fg="white",
             command=lambda:blogShow(root,ID)
             )
    blog.pack(pady=(25,0))

if __name__=="__main__":
    main(root, ID)

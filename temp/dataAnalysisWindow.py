from tkinter import *
from temp import mainWindow
from tkinter import  messagebox
from PIL import ImageTk,Image
import requests
from bs4 import BeautifulSoup
import codecs
import webbrowser
import os


def clear(root):
    list = root.grid_slaves()
    for l in list:
        l.grid_forget()

def htmlFileOpen():
    temp=requests.get("https://www.mygov.in/covid-19")
    myHtmlData=temp.text
    soup=BeautifulSoup(myHtmlData, 'html.parser')
    myData=soup.find_all("table", id="state-covid-data")
    strData=str(myData)
    strData=strData[1:-1]
    finalStr='<!DOCTYPE html><html lang="en">'+strData+"</html>"
    file=codecs.open("temp/htmlRaw.html", "w")
    file.write(finalStr)
    file.close()
    filename = 'file:///'+os.getcwd()+'/temp/' +"htmlRaw.html"
    webbrowser.open_new_tab(filename)
    
def main(root, ID):
    clear(root)
    width=600
    height=513
    screen_width=root.winfo_screenwidth()
    screen_height=root.winfo_screenheight()
    x_coordinate=(screen_width/2)-(width/2)
    y_coordinate=(screen_height/2)-(height/2)-40
    root.geometry("%dx%d+%d+%d" % (width, height, x_coordinate, y_coordinate))
    root.minsize(width,height)
    root.maxsize(width,height)
    root.configure(background='black')
    root.title("Data Analysis | Fight Against COVID-19")
    root.iconbitmap("temp/dataAnalysisIcon.ico")
    
    #upper world wide cases, deaths, recovered
    try:
        #back button
        b=Button(root,
                 text="<< Back",
                 font=("Courier", 15),
                 bg="#49A",
                 fg="white",
                 command=lambda:mainWindow.main(root,ID))
        b.pack(pady=(15,0))
        temp=requests.get("https://www.worldometers.info/coronavirus/")
        myHtmlData=temp.text
        soup=BeautifulSoup(myHtmlData, 'html.parser')

        myData=soup.find_all("div", class_="maincounter-number")
        cases=str(myData[0])
        deaths=str(myData[1])
        recovered=str(myData[2])

        l=['0','1','2','3','4','5','6','7','8','9']
        c1=cases[58:]
        finalCases=""
        for i in range(len(c1)):
            if c1[i] in l:
                finalCases+=c1[i]
            elif c1[i]==',':
                continue
            else:
                break
        d1=deaths[39:]
        finalDeaths=""
        for i in range(len(d1)):
            if d1[i] in l:
                finalDeaths+=d1[i]
            elif d1[i]==',':
                continue
            else:
                break
        r1=recovered[62:]
        finalRecovered=""
        for i in range(len(r1)):
            if r1[i] in l:
                finalRecovered+=r1[i]
            elif r1[i]==',':
                continue
            else:
                break

        #frame
        frame=LabelFrame(root,
                         text="World Wide COVID-19 Information",
                         font=("Courier", 20),
                         bg="#dda2d5",
                         fg="black")
        frame.pack(pady=(15,0))
        
        fCases=Label(frame,
                     text="Total Cases      "+finalCases,
                     font=("Courier", 18),
                     bg="#dda2d5",
                     fg="black")
        fCases.pack(pady=(15,0))

        fDeaths=Label(frame,
                     text="Total Deaths    "+finalDeaths,
                     font=("Courier", 18),
                     bg="#dda2d5",
                     fg="black")
        fDeaths.pack(pady=(15,0))

        fRecovs=Label(frame,
                     text="Total Recoveries  "+finalRecovered,
                     font=("Courier", 18),
                     bg="#dda2d5",
                     fg="black")
        fRecovs.pack(pady=(15,15))

        #See state update button
        iF=LabelFrame(root,
                         bg="#66e07d",
                      padx=25)
        iF.pack(pady=(20,0))
        
        label=Label(iF,
                    text="Click the button below to\nsee the updates of the Staes\nof India",
                    font=("Courier", 20),
                    bg="#66e07d",
                    fg="black")
        label.pack()

        button=Button(iF,
                      text="See Updates\nOf\nIndian States",
                      font=("Courier", 15),
                    bg="#25e4ee",
                    fg="black",
                      command=htmlFileOpen)
        button.pack(pady=(15,15))        

    except:
        messagebox.showerror("ERROR!!!", "Please check your internet connection!!!")
        root.destroy()

    
if __name__=="__main__":
    main(root, ID)

from tkinter import *
from ttk import Label
from PIL import Image, ImageTk
from temp import loginOrSignUp
from temp import autoLoginMainWindow
import sqlite3

count,N=1,200

def openWindow(root):
    conn=sqlite3.connect("temp/userDetails.db")
    c=conn.cursor()
    c.execute("SELECT *, oid FROM details")
    records=c.fetchall()
    
    for record in records:
        if record[0]=="YES":
            ID=str(record[5])
            autoLoginMainWindow.main(root,ID)
            break
    else:
        loginOrSignUp.main(root)

    conn.commit()
    conn.close()

class AnimatedGIF(Label, object):
    def __init__(self, master, path, forever=True):
        self._master = master
        self._loc = 0
        self._forever = forever
        self._is_running = False
        im = Image.open(path)
        self._frames = []
        i = 0
        try:
            while True:
                photoframe = ImageTk.PhotoImage(im.copy().convert('RGBA'))
                self._frames.append(photoframe)
                i += 1
                im.seek(i)
        except EOFError: pass
        self._last_index = len(self._frames) - 1
        try:
            self._delay = im.info['duration']
        except:
            self._delay = 100
        self._callback_id = None
        super(AnimatedGIF, self).__init__(master, image=self._frames[0])
    def start_animation(self, frame=None):
        global count
        global N
        if count==N:
            global root
            openWindow(root)
        else:
            count+=1
            if self._is_running: return
            if frame is not None:
                self._loc = 0
                self.configure(image=self._frames[frame])
            self._master.after(self._delay, self._animate_GIF)
            self._is_running = True
    def stop_animation(self):
        global count
        global N
        if count==N:
            global root
            openWindow(root)
        else:
            count+=1
            if not self._is_running: return
            if self._callback_id is not None:
                self.after_cancel(self._callback_id)
                self._callback_id = None
            self._is_running = False
    def _animate_GIF(self):
        global count
        global N
        if count==N:
            global root
            openWindow(root)
        else:
            count+=1
            self._loc += 1
            self.configure(image=self._frames[self._loc])
            if self._loc == self._last_index:
                if self._forever:
                    self._loc = 0
                    self._callback_id = self._master.after(self._delay, self._animate_GIF)
                else:
                    self._callback_id = None
                    self._is_running = False
            else:
                self._callback_id = self._master.after(self._delay, self._animate_GIF)
    def pack(self, start_animation=True, **kwargs):
        global count
        global N
        if count==N:
            global root
            openWindow(root)
        else:
            count+=1
            if start_animation:
                self.start_animation()
            super(AnimatedGIF, self).pack(**kwargs)
    def grid(self, start_animation=True, **kwargs):
        global count
        global N
        if count==N:
            global root
            openWindow(root)
        else:
            count+=1
            if start_animation:
                self.start_animation()
            super(AnimatedGIF, self).pack(**kwargs)
    def place(self, start_animation=True, **kwargs):
        global count
        global N
        if count==N:
            global root
            openWindow(root)
        else:
            count+=1
            if start_animation:
                self.start_animation()
            super(AnimatedGIF, self).pack(**kwargs)
    def pack_forget(self, **kwargs):
        global count
        global N
        if count==N:
            global root
            openWindow(root)
        else:
            count+=1
            self.stop_animation()
            super(AnimatedGIF, self).pack_forget(**kwargs)
    def grid_forget(self, **kwargs):
        global count
        global N
        if count==N:
            global root
            openWindow(root)
        else:
            count+=1
            self.stop_animation()
            super(AnimatedGIF, self).pack_forget(**kwargs)
    def place_forget(self, **kwargs):
        global count
        global N
        if count==N:
            global root
            openWindow(root)
        else:
            count+=1
            self.stop_animation()
            super(AnimatedGIF, self).pack_forget(**kwargs)

if __name__ == "__main__":
    
    conn=sqlite3.connect("temp/userDetails.db")
    c=conn.cursor()
    
    #It should be executed once to create the table
    '''
    c.execute("""CREATE TABLE details(
                autoLogin text,
                name text,
                location text,
                password text,
                email text
                )""")
    ''' 
    global root
    root = Tk()
    #Make the root in the middle
    width=448
    height=254
    screen_width=root.winfo_screenwidth()
    screen_height=root.winfo_screenheight()
    x_coordinate=(screen_width/2)-(width/2)
    y_coordinate=(screen_height/2)-(height/2)-40
    root.geometry("%dx%d+%d+%d" % (width, height, x_coordinate, y_coordinate))
    root.minsize(width,height)
    root.maxsize(width,height)
    
    root.title("Loading... | Fight Against COVID-19")
    root.iconbitmap("temp/mainIcon.ico")
    root.configure(background='#000000')
    l = AnimatedGIF(root, "temp/loadingGIF.gif")
    l.pack()
    
    conn.commit()
    conn.close()
    
    root.mainloop()

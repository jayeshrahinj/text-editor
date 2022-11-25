from threading import main_thread
from tkinter import*
from tkinter import*
from tkinter import ttk
from tkinter.filedialog import askopenfilename,asksaveasfile,asksaveasfilename
import os
from tkinter.messagebox import showinfo


def newFile():
    global file
    root.title("siddhesh-notepad")
    file=None
    #1.0 means first line and zeroth character
    TextArea.delete(1.0,END)

def OpenFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents",".txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+ "-Notepad")
        TextArea.delete(1.0,END)
        f=open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()
        
        
        
        
    

def savefile():
    global file
    if file == None:
        file=asksaveasfilename(initialfile='untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
            #save new file
           f=open(file,"w")
           f.write(TextArea.get(1.0,END))
           f.close()
           root.title(os.path.basename(file) + "-Notepad")
           print("file saved")
           
    else:
        f=open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()
        
        



    
def quitapp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def About():
    showinfo("siddhesh-Notepad","this notepad is created by siddhesh mankar")
     

def HelpMenu():
    pass





if __name__  == '__main__':
    #basic tkinter setup
    root=Tk()
    root.title("siddhesh-notepad")
    root.wm_iconbitmap("favicon.ico")
    root.geometry("720x880")
   
    
  
    
    
    
    #adddd textarea
    TextArea=Text(root,font="lucida 13")
    file=None
    TextArea.pack(expand=True,fill=BOTH)
    
    #menubar
    menuBar=Menu(root)
    FileMenu=Menu(menuBar,tearoff=0)
    
    #to open new file
    FileMenu.add_command(label="New",command=newFile)
    
    #to open existing file
    FileMenu.add_command(label="Open",command=OpenFile)
    
    #to save the file
    FileMenu.add_command(label="save",command=savefile)
    
  
    menuBar.add_command(label="Exit",command=quitapp)
    FileMenu.add_separator()
    
   #cascade will attach all file
    menuBar.add_cascade(label="File",menu=FileMenu)
    
    
    #edit menu
    editmenu=Menu(menuBar,tearoff=0)
    #cut ,copy paste feature
    editmenu.add_command(label="Cut",command=cut)
    editmenu.add_command(label="Copy",command=copy)
    editmenu.add_command(label="paste",command=paste)
    menuBar.add_cascade(label="edit",menu=editmenu)
    
    #help menu
    helpmenu=Menu(menuBar,tearoff=0)
    helpmenu.add_command(label="about-notpad",command=About)
    menuBar.add_cascade(label="help",menu=helpmenu)
    
    root.config(menu=menuBar)
    
    #adding scrollbar
    Scroll=Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=TextArea.yview)

    TextArea.config(yscrollcommand=Scroll.set)
    
    
    root.mainloop()
    
    
    
    
      
    
    
    
    
    
    
    
    


    
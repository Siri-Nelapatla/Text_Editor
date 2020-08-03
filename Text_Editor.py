from tkinter import *
from tkinter.filedialog  import*
from tkinter.messagebox import*

filename = 'Untitled'

def newFlie():
    global filename
    filename = 'Untitled'
    Text.delete(0.0,END)

def savefile():
    global filename
    t=Text.get(0.0,END)   
    f=open(filename,'w')
    f.write(t)
    f.close()
def saveAs():
    f= asksaveasfile(mode='w',defaultextension='.txt' ) 
    t=Text.get(0.0,END)
    try:
        f.write(t.rstrip())
    except :
        showerror(title='oops',message='unable to save file...')
def openFile():
    global filename
    f=askopenfile(mode='r')
    t=f.read()
    Text.delete(0.0,END)
    Text.insert(0.0,t)
    

root = Tk()
root.title('Siri Text Editor')   
root.text = Text(width = 60, height = 30)
root.text.pack(expand=YES, fill=BOTH) 



menubar = Menu(root)
filemenu= Menu(menubar)
filemenu.add_command(label='New',command = newFlie)
filemenu.add_command(label = 'Open', command = openFile)
filemenu.add_command(label = 'Save', command = savefile)
filemenu.add_command(label = 'SaveAs',command = saveAs)
filemenu.add_separator()
filemenu.add_command(label = 'Quit',command=root.quit)
menubar.add_cascade(label='File',menu=filemenu)
menubar.add_cascade(label = 'Edit' )
menubar.add_cascade(label = 'Format')
menubar.add_cascade(label = "View")
menubar.add_cascade(label = 'Help')
root.config(menu=menubar)
root.mainloop()
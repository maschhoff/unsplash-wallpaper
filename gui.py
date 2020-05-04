from tkinter import *
from PIL import ImageTk, Image
import os
import unsplash
import settings
import getpass


USER_NAME = getpass.getuser()
cron = {"on Startup" : 999999, "5 Minutes": 500, "30 Minutes": 3000, "60 Minutes": 60000, "3 Hours":180000}


def clickExitButton():
        print("clickExitButton")
        #print("\nvalue: "+str(c1var.get())+","+collections.get()+","+times.get()+","+str(cron.get(times.get())))

        #Change config
        config=settings.loadConfig()
        config["updatetime"]=cron.get(times.get())
        config["collection"]=collections.get()
        settings.writeConfig(config)
        
        if c1var.get()==1:
             add_to_startup()

        unsplash.del_image() 
        exit()

def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
        print("path: "+file_path)
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    print("bat: "+bat_path)
    #TODO startup?
    with open(bat_path + '\\' + "unsplashipy.bat", "w+") as bat_file:
        bat_file.write("cd "+file_path+"\npythonw ./unsplash_bg.pyw")

def clickRefresh():
        print("clickRefresh")
        global uimg
        uimg=unsplash.get_image(1)
        img = ImageTk.PhotoImage(Image.open(uimg).resize((950, 425), Image.ANTIALIAS))
        limg = Label(root, image = img)
        limg.grid(row=0,column=0,columnspan=5)  
        limg.configure(image = img)
        limg.image=img
                
        

def clicksetWP():
        unsplash.windows(uimg)
        print("clicksetWP")
        


config=settings.loadConfig() 

root = Tk()

global limg
clickRefresh()

refreshButton = Button(root, text="Next Image", command=clickRefresh)
refreshButton.grid(row = 1, column = 0, sticky = W, pady = 2)

setWPButton = Button(root, text="Set as Wallpaper", command=clicksetWP)
setWPButton.grid(row = 2, column = 0, sticky = W, pady = 2)


l1 = Label(root, text = "Refresh Time:") 
l2 = Label(root, text = "Collection:") 
  
l1.grid(row = 1, column = 1, sticky = E, pady = 2) 
l2.grid(row = 2, column = 1, sticky = E, pady = 2) 
  
times = StringVar(root)
times.set(list(cron.keys())[list(cron.values()).index(config["updatetime"])]) 
w = OptionMenu(root, times, *list(cron.keys()))
w.grid(row = 1, column = 2, pady = 2) 

collections = StringVar(root)
collections.set(config["collection"]) 
w = OptionMenu(root, collections, "wallpaper","nature", "travel", "animals","landscape")
w.grid(row = 2, column = 2, pady = 2) 
 
c1var = IntVar(root) 
c1 = Checkbutton(root, text='Install to Startup', onvalue=1, offvalue=0, variable=c1var)
c1.select()
c1.grid(row = 2, column = 3, sticky = E, pady = 2)

exitButton = Button(root, text="Save and Exit", command=clickExitButton)
exitButton.grid(row = 2, column = 4, sticky = S, pady = 2)


root.geometry("950x500+300+150")
root.resizable(width=False, height=False)
root.title('Unsplash Wallpaper (github.com/maschhoff)')
root.mainloop()


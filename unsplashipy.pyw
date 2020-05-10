from tkinter import *
from PIL import ImageTk, Image
import os
import unsplash
import settings
import time
import getpass
import platform
import sys


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
        
        if osvar == "Windows": 
                if c1var.get()==1:
                        add_to_startup()
                else:
                        del_from_startup()

        unsplash.del_image() 
        sys.exit(0)

def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
        print("path: "+file_path)
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    print("bat: "+bat_path)
    print("add_to_startup")
    #TODO startup?
    with open(bat_path + '\\' + "unsplashipy.bat", "w+") as bat_file:
        bat_file.write("start "+file_path+"\\unsplashipy.exe -bg\nexit")
        
def del_from_startup(file_path=""):
    print("del_from_startup")
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\unsplashipy.bat' % USER_NAME
    print("bat: "+bat_path)
    if os.path.isfile(bat_path):
                os.remove(bat_path)
    

def clickRefresh():
        print("clickRefresh")
        global uimg
        uimg=unsplash.get_image()
        img = ImageTk.PhotoImage(Image.open(uimg).resize((950, 425), Image.ANTIALIAS))
        limg = Label(root, image = img)
        limg.grid(row=0,column=0,columnspan=5)  
        limg.configure(image = img)
        limg.image=img
                
        

def clicksetWP():
        print("clicksetWP")
        if osvar == "Windows":
                unsplash.windows(uimg)
        elif osvar == "Linux":
                unsplash.linux(uimg)



def bg_task():

        while True:
                unsplash.main()
                time.sleep(config["updatetime"])
                unsplash.del_image()


osvar = platform.system()
config=settings.loadConfig() 

print(str(sys.argv)+"_:"+str(len(sys.argv)))

if len(sys.argv)>1:
        if sys.argv[1] == "-background" or sys.argv[1] == "-bg":
                print("run background task")
                bg_task()
else:
        print("start GUI")
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


        if osvar == "Windows": 
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
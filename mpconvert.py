from tkinter import *
from tkinter import filedialog
import moviepy.editor as mp
import time
import os

#Main Screen Init
master       = Tk()
master.title('Video to Audio')

#Icon
# photo = PhotoImage(file = "icon.png")
# master.iconphoto(False, photo)

#functions
def get_file():
    filename = filedialog.askopenfilename(initialdir='c:/',title='Please select a file',filetype=[('MP4 Files', '*.mp4')])
    try:
        with open(filename, 'rb') as fx:
            temp_file.set(fx.name)
        notif.config(fg='green', text = 'Selected ' + str(temp_file.get()) )
    except:
        notif.config(fg='red', text = 'No file Selected ')

def mp4_to_mp3(mp4, mp3):
    mp4_without_frames =mp.AudioFileClip(mp4)
    mp4_without_frames.write_audiofile(mp3,logger=None,verbose=False)
    mp4_without_frames.close()
    

def convert():
    try:
        a=temp_file.get()
        b=(temp_file.get()).split('/')
        l=b[-1].split('.')
        time.sleep(1)
        namef="Converted\\"+l[0]+'.mp3'
        mp4_to_mp3(a, namef)
        notif.config(fg='green', text = 'Successfully converted ' + str(temp_file.get()) )
        os.startfile(r".\Converted")
    except:
        notif.config(fg='red', text = "Can't Convert the file " + str(temp_file.get()) )

#pathcheck
outputpath = r'.\Converted' 
if not os.path.exists(outputpath):
    os.makedirs(outputpath)
    
#Labels
Label(master, text="Convert Video to Audio", font=('Calibri',15),foreground='blue').grid(row=0, sticky=N)
Label(master, text="Audio file folder opens after the convertion", font=('Calibri',11),foreground='blue').grid(row=1, sticky=W, padx=5 ,pady=10)
Label(master, text="Video File", font=('Calibri', 11),foreground='#c403ff').grid(row=2,sticky=W, padx=5)
notif = Label(master, text="Please check file path here", font=('Calibri', 11),fg="orange")
notif.grid(row=3,sticky=S)

#Storage
temp_file = StringVar()

#Buttons
Button(master, text = 'Select file', command = get_file,foreground='green').grid(row=2,column=0)
Button(master, text = 'Convert', command = convert,foreground='green').grid(row=4,column=0)

master.mainloop()

from tkinter import *
from tkinter import messagebox, filedialog
from customtkinter import *
from pytube import YouTube
import os
import threading

set_appearance_mode("System")
set_default_color_theme("blue")

def reset_function():
    title.configure(text="Insert a YouTube link", text_color="white")
    link.delete(0,END)
    Dl_messege.configure(text="")
    progPrecent.configure(text="0%")
    progBar.set(0)

def open_location_dialog():
    threading.Thread(target=location).start()

def location():
    global destination_to
    file_location = filedialog.askdirectory()
    destination_to = file_location

def start_Dl_Mp3():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=progress)
        music = ytObject.streams.get_audio_only()
        title.configure(text=ytObject.title, text_color="green")
        Dl_messege.configure(text="")
        source = music.download()
        Dl_messege.configure(text="Downlaod Complete")
        destination = os.path.join(destination_to, os.path.basename(source)) 

        if os.path.exists(destination):
            messagebox.showwarning("Warning", "File already exists")
        else:
            # change_to_mp3 = os.replace(source,destination)
            # base, ext = os.path.splitext(change_to_mp3)
            # new_file = base + ".mp3"
            os.rename(source,destination)
            messagebox.showinfo("File", "File was moved to " + destination_to )

        
    except:
        Dl_messege.configure(text="Downlaod Failed", text_color="red")
        
def start_Dl_Mp4_low_res():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=progress)
        music = ytObject.streams.get_lowest_resolution()
        title.configure(text=ytObject.title, text_color="green")
        Dl_messege.configure(text="")
        source = music.download()
        Dl_messege.configure(text="Downlaod Complete")
        destination = os.path.join(destination_to, os.path.basename(source)) 
        if os.path.exists(destination):
            messagebox.showwarning("Warning", "File already exists")
        else:
            
            os.replace(source,destination)
            messagebox.showinfo("File", "File was moved to " + destination_to )
    except:
        Dl_messege.configure(text="Downlaod Failed")
    
def start_Dl_Mp4_high_res():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=progress)
        music = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title, text_color="green")
        Dl_messege.configure(text="")
        source = music.download()
        Dl_messege.configure(text="Downlaod Complete")
        destination = os.path.join(destination_to, os.path.basename(source)) 
        if os.path.exists(destination):
            messagebox.showwarning("Warning", "File already exists")
        else:
            
            os.replace(source,destination)
            messagebox.showinfo("File", "File was moved to " + destination_to )
        Dl_messege.configure(text="Downlaod Complete")
    except:
        Dl_messege.configure(text="Downlaod Failed")

def progress(stream, chunks, bytes_reamining):
    total_size = stream.filesize
    bytes_Dl = total_size - bytes_reamining
    p_of_completion = bytes_Dl / total_size * 100
    per = str(int(p_of_completion))
    progPrecent.configure(text=per + "%")
    progPrecent.update()

    progBar.set(float(p_of_completion) / 100)


win = CTk()
win.geometry("720x420")
win.title("Youtube Downloader")


set_diretory_Btn = CTkButton(win, text="Set Location", font=("Serif", 15), command=open_location_dialog)
set_diretory_Btn.pack(padx=30, pady=30)

title = CTkLabel(win, text="Insert a YouTube link", font=("Serif", 25))
title.pack(padx=10, pady=5)

url_var = StringVar()
link = CTkEntry(win, width=420, height=50, textvariable=url_var)
link.pack(padx=10, pady=10)

Dl_messege = CTkLabel(win, text="", font=("Serif", 15))
Dl_messege.pack(padx=10, pady=10)

progPrecent = CTkLabel(win, text="0%", font=("Serif", 15))
progPrecent.pack(padx=10, pady=10)

progBar = CTkProgressBar(win, width=400)
progBar.set(0)
progBar.pack(padx=10, pady=10)

Btn_frame = CTkFrame(win)
Btn_frame.pack()

Dl_BtnMp3 = CTkButton(Btn_frame, font=("Serif", 15), text="Download Mp3", command=start_Dl_Mp3)
Dl_BtnMp4_low = CTkButton(Btn_frame, font=("Serif", 15), text="Download Mp4 Low Resolution",  command=start_Dl_Mp4_low_res)
Dl_BtnMp4_high = CTkButton(Btn_frame, font=("Serif", 15), text="Download Mp4 High Resolution",  command=start_Dl_Mp4_high_res)


Dl_BtnMp3.pack(side=LEFT,  padx=10, pady=5)
Dl_BtnMp4_low.pack(side=LEFT, padx=10, pady=5)
Dl_BtnMp4_high.pack(side=LEFT, padx=10, pady=5)

reset_Btn = CTkButton(win, text="Reset", font=("Serif", 15), command=reset_function)
reset_Btn.pack(side=BOTTOM, anchor=SE)

messagebox.showinfo(message="Please insert a file location first to download")
win.mainloop()
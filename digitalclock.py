#import tkinter as tk
from tkinter import Label 
import tkinter as tk    
import time

#Saat Tasarımı
app_windows=tk.Tk()
app_windows.title("Dijital Saat")
app_windows.geometry("300x300")
app_windows.resizable(1,1)
app_windows.configure(bg="black")

#Etiket Tasarımı
text_font=("Boulder",36,'bold')
background="black"
foreground="white"
border_widht=20 

#Saat Etiketi
label=Label(app_windows,font=("Boulder",18),bg=background,fg=foreground,borderwidth=border_widht)
label.grid(row=1,column=1,padx=10,pady=10) 

#Tarih Etiketi
date_label=Label(app_windows,font=("Boulder",18),bg=background,fg=foreground,borderwidth=border_widht)
date_label.grid(row=2,column=1,padx=10,pady=10)

def digital_clock():

    time_live=time.strftime("%H:%M:%S")
    label.config(text=time_live)
        #tarih etiketi
    date_live=time.strftime("%d  %B  %Y")
    date_label.config(text=date_live)
    label.after(200,digital_clock)

digital_clock()
app_windows.mainloop() 
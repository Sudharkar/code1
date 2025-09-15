from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")

def restart_time():
    os.system("shutdown /r /t 20")

def log_out():
    os.system("shutdown -l")

def shutdown():
    os.system("shutdown /s /t 1")



st=Tk()

st.title("SHUTDOWN APP")
st.geometry("500x500")
st.configure(bg="blue")

r_button=Button(st,text="RESTART",font=("Time New Roman",18,"bold"),
                relief=RAISED,cursor="plus",command=restart)
r_button.place(x=150,y=60,height=50,width=200)

rt_button=Button(st,text="RESTART TIME",font=("Time New Roman",18,
                "bold"),relief=RAISED,cursor="plus",command=restart_time)
rt_button.place(x=150,y=170,height=50,width=200)

lg_button=Button(st,text="LOG OUT",font=("Time New Roman",18,"bold")
                 ,relief=RAISED,cursor="plus",command=log_out)
lg_button.place(x=150,y=280,height=50,width=200)

sd_button=Button(st,text="SHUTDOWN",font=("Time New Roman",18,
                 "bold"),relief=RAISED,cursor="plus",command=shutdown)
sd_button.place(x=150,y=390,height=50,width=200)



st.mainloop()
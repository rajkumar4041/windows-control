from tkinter import *
import os


def restart():
    os.system("shutdown /r /t 1")

def restart_time():
    os.system("shutdown /r /t 1 10")
def log_out():
    os.system("shutdown -1")
def shut_doown():
    os.system("shutdown /s /t 1")


#use tk 
def startapp():
    st = Tk()
    st.title("shutdown App")
    st.geometry("500x500")
    st.config(bg="grey")

#creating button 
    r_button=Button(st,text="Restart",font=("Times New Rooman", 20,"bold"),relief=RAISED,cursor="plus",command=restart)
    r_button.place(x=150,y=60,height=50,width=200)

    rt_button=Button(st,text="Restart time",font=("Times New    Rooman",20,"bold"),relief=RAISED,cursor="plus",command=restart_time)
    rt_button.place(x=150,y=170,height=50,width=200)

    lg_button=Button(st,text="Log out",font=("Times New     Rooman",20,"bold"),relief=RAISED,cursor="plus",command=log_out)
    lg_button.place(x=150,y=270,height=50,width=200)

    st_button=Button(st,text="shutdown",font=("Times New    Rooman",20,"bold"),relief=RAISED,cursor="plus",command=shut_doown)
    st_button.place(x=150,y=370,height=50,width=200)


    st.mainloop()

startapp()
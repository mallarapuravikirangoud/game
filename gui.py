from tkinter import *
def register():
    screen=Toplevel(screen)
    screen.title("register")
    screen.geometry("300x250")

    username=stringvariable()
    username=stringvariable()

    Label(text="username * ").pack()
    entry(textvariable=username)
    Label(text="password * ").pack()
    entry(textvariable=username)

def login():
    print("login session started")

def main_screen():
    global screen
    screen=Tk()
    screen.geometry("300x250")
    screen.title("notes 1.0")
    Label(text="notes 1.0",bg="green",width="50",height="2",font=("calibari",13)).pack()
    Label(text="").pack()
    Button(text="login",height="2",width="30",command=login).pack()
    Label(text="").pack()
    Button(text="register",height="2",width="30",command=register).pack()

    screen.mainloop()
main_screen()
    
    

from tkinter import *
from scrap import *

main_screen=()
username_entry=()
password_entry=()
register_screen=()

def main_account_screen():
    global main_screen
    global username_entry
    global password_entry
    global register_screen
    main_screen = Tk()
    main_screen.geometry("300x400")
    main_screen.title("Account Login")
    main_screen.configure(bg="#F9F0EA")
    Label(text="Choose Account Type", bg="#F9CBCA", width="300", height="2", font=("Calibri", 20)).pack()
    Label(text="").pack()
    Button(text="Public", height="5",bg="#F9CBC6", width="50", command=public).pack()
    Label(text="").pack()
    Button(text="Private", height="5",bg="#F9CBFA", width="50", command=private).pack()
    main_screen.mainloop()


def private():
    global main_screen
    global username_entry
    global password_entry
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Private Account")
    register_screen.configure(bg="#F9EBEA")
    register_screen.geometry("300x250")
    username = StringVar()
    password = StringVar()
    Label(register_screen, text="Please enter details below", bg="#F9EBEA").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ",bg="#F9EBEA")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ",bg="#F9EBEA")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="#B9EBEA", command=funprivate).pack()


def public():
    global main_screen
    global username_entry
    global password_entry
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Public Account")
    register_screen.configure(bg="#F9EBEA")
    register_screen.geometry("300x250")
    username = StringVar()
    Label(register_screen, text="Please enter details below", bg="#F9EBEA").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ",bg="#F9EBEA")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Submit", width=10, height=1, bg="#D9EBEA" , command=funpublic).pack()

def funpublic():
    global username_entry
    username = username_entry.get()
    scrapping_public(username)

def funprivate():
    global username_entry
    global password_entry
    username=username_entry.get()
    password=password_entry.get()
    scrapping_private(username,password)
    #print(username)
    #print(password)



main_account_screen()

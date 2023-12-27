import tkinter
from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font


#Calculator window
def calculator():
    from VirtualCal import virtual_calculator
    cal=virtual_calculator()
    cal.mainloop()

#Exit window
def exitCal():
    home.withdraw()
    exit=Toplevel(home)
    exit.geometry("800x500+10+20")
    exit.title('Exit')
    exit.configure(bg='white')

    lblExit = Label(exit, text="Thank you for using Virtual Calculator!!", bg='white', fg='darkslategray',
                font=("GEEKSFORGEEKS", 30))
    lblExit.place(x=50, y=300)

    imgBye = ImageTk.PhotoImage(Image.open("goodbye.jpg"))
    imgByelbl = Label(exit, image=imgBye, bg='white')
    imgByelbl.place(x=230, y=10)

    exit.mainloop()

#Instructions Window
def instructions():

    #Go to the home window from instructions window
    def back():
        instruct.withdraw()
        home.deiconify()

    home.withdraw()
    instruct=Toplevel(home)
    instruct.geometry("800x500+10+20")
    instruct.title('Instructions')

    instruct.configure(bg='white')

    lblTitle = Label(instruct, text="Instructions to use the Virtual Calculator",bg ='white', fg='teal',
                font=("GEEKSFORGEEKS", 20))
    lblTitle.place(x=180, y=10)

    btnBack = Button(instruct, text="Back to home", fg='silver', bg='darkslategray', activebackground='gray',
                 width=25, height=1, command=back)
    btnBack.place(x=260, y=450)
    btnBack['font'] = font.Font(size=12)

    lblInst1 = Label(instruct, text="Use your index finger and middle finger of left or right hand to use the calculator.",
                 fg='darkslategray', bg='white', font=("GEEKSFORGEEKS", 12))
    lblInst1.place(x=12, y=60)

    lblInst2 = Label(instruct, text="Move your fingers closer to the button you want to click and take the tips of two fingers closer.",
                 fg='darkslategray', bg='white', font=("GEEKSFORGEEKS", 12))
    lblInst2.place(x=12, y=100)

    imgFingers1 = ImageTk.PhotoImage(Image.open("fingersNotclose.jpg"))
    imagelbl1 = Label(instruct, image=imgFingers1, bg='white')
    imagelbl1.place(x=100, y=130)

    imgFingers2 = ImageTk.PhotoImage(Image.open("fingersClose.jpg"))
    imagelbl2 = Label(instruct, image=imgFingers2, bg='white')
    imagelbl2.place(x=430, y=130)

    lblInst3 = Label(instruct,
                     text="Click 'c' on the keyboard to stop calculator and then close the window.",
                     fg='darkslategray', bg='white', font=("GEEKSFORGEEKS", 12))
    lblInst3.place(x=12, y=390)

    instruct.mainloop()

#Home window
home=Tk()
home.configure(bg='white')

imgCal = ImageTk.PhotoImage(Image.open("cal.jpg"))
imagelbl=Label(home, image=imgCal, bg='white')
imagelbl.place(x=0, y=60)

btnInst=Button(home, text="View Instructions", fg='silver', bg='darkslategray', activebackground='gray',
            width=25, height=1, command=instructions)
btnInst.place(x=470, y=150)
btnInst['font'] = font.Font(size=15)

btnGo=Button(home, text="Go to the Calculator", fg='silver', bg='darkslategray', activebackground='gray',
           width=25, height=1, command=calculator)
btnGo.place(x=470, y=250)
btnGo['font'] = font.Font(size=15)

btnExit=Button(home, text="Exit", fg='silver', bg='darkslategray', activebackground='gray',
           width=25, height=1, command=exitCal)
btnExit.place(x=470, y=350)
btnExit['font'] = font.Font(size=15)


lblWelcome=Label(home, text="Welcome to Virtual Calculator", fg='teal', bg='white', font=("GEEKSFORGEEKS", 30))
lblWelcome.place(x=150, y=15)

home.title('Virtual Calculator')
home.geometry("800x500+10+20")
home.mainloop()
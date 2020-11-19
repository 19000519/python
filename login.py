from tkinter import*
from PIL import ImageTk

class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")

        #====All images=====
        self.bg_icon=ImageTk.PhotoImage(file ="image\veco.jpg")
        self.user_icon=PhotoImage(file ="image\ppk.png")
        self.pass_icon=PhotoImage(file ="image\pk.png")

        title=Label(self.root, text ="Login System", font = ("times new roman", 40, "bold"))
        title.place(x=0,y=0,relwidth=1)

root = Tk()
obj = Login_System(root)
root.mainloop()